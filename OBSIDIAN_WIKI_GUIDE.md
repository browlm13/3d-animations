# Obsidian Wiki Structuring Guide

This guide gives you an Obsidian-first layout for the "Universe OS" wiki and includes NLP-friendly patterns so you can write AU, ly, meters, or natural language phrases and still compile them via the ASTRA DSL.

## Vault layout (ready to copy)
```
universe/
  _templates/
    galaxy.md
    cluster.md
    system.md
    body.md
    faction.md
    species.md
  galaxies/
  clusters/
  systems/
  bodies/
  factions/
  species/
  maps/
  art/
  attachments/
  compiler/
```

**Notes**
- `_templates` holds starter pages you can duplicate in Obsidian.
- `attachments` is a catch-all drop folder Obsidian can auto-use for pasted images.
- Keep lore + ASTRA in the same file per entity; Obsidian backlinks make navigation trivial.

## Page template (markdown + ASTRA block)
````markdown
---
title: Leviathan
entity: body
class: C
kind: super_earth
tags: [system/tengri, body/super_earth]
links:
  parent: [[tengri]]
  art: [[leviathan_ultrawide.png]]
  factions: [[jade_covenant]]
---

# Leviathan

Jungle megabiome. Pirate fortress. Storm-wrapped super-Earth.

![concept](../art/leviathan_ultrawide.png)

```astra
body Leviathan {
  class C
  kind super_earth
  plane main
  orbit ellipse { a 1.6 AU; e 0.03; inc 2 deg }
  size about 2 Earth radii
  mass ~8 Earth masses
  trojans [Leviathan_L4, Leviathan_L5]
}
```
````

**Tips**
- YAML frontmatter stays lore-facing; the ASTRA block is the compiler-facing portion.
- Lore can reference concept art with relative links so Obsidian previews work offline.

## Naming conventions
- **Files**: snake_case for filenames (`leviathan.md`, `tengri_cluster.md`).
- **Headings**: H1 matches filename/entity name; ASTRA `body`/`system` identifiers should match.
- **Tags**: use hierarchical tags for filters (`system/<name>`, `class/C`, `kind/super_earth`).
- **Attachments**: prefer descriptive names (`leviathan_ultrawide.png`).

## Cross-linking patterns
- Use Obsidian wikilinks for relationships (`[[tengri]]` parent system, `[[jade_covenant]]` faction).
- For location hierarchy, keep `parent` in frontmatter plus backlinks from child → parent.
- Maintain collections via tags (`kind/gas_giant`) and dataview queries if you use that plugin.

## NLP-friendly unit handling in ASTRA
Write naturally; the compiler normalizes. Suggested patterns:

### Supported distance units (input examples → canonical output)
- `1.2 AU`, `1.2 astronomical units`, `1.2 au` → meters (AU canonical)
- `4.3 ly`, `4.3 light years`, `4.3 ly away` → meters (light-year canonical)
- `700 million km`, `700e6 m` → meters
- `orbital radius fifty thousand km` → meters (extract number + unit)

### Size and mass
- `size 1.9 Re`, `size 1.9 Earth radii`, `radius about 2 Earth radii`
- `mass 8.2 Me`, `mass ~8 Earth masses`, `mass around 8x Earth`
- Gas giants: `radius 11 Rj`, `mass 318 Mj` (Jupiter units)

### Angles and time
- Inclination: `inc 5 deg`, `inclination five degrees`
- Node/argument: `node 120 deg`, `ascending node ~120°`
- Periods: `period 32 days`, `period ~1 yr`, `period 10 hours`

### Belts and ranges
- `belt 2.1 AU .. 3.6 AU density high`
- `belt from 2 to 3 AU low density`

### Rogue / special cases
- `orbit rogue`
- `trojan_of Leviathan at L4`

**Parsing guidance**
- Accept numbers with commas, decimals, scientific notation (`1e6`).
- Allow soft words like `about`, `~`, `approximately`, `around`, `roughly` before numbers.
- Strip stopwords (`at`, `around`, `about`, `roughly`, `away`) before normalization.
- Normalize to canonical units: meters for distance, kilograms for mass, radians/degrees stored explicitly, seconds for time.
- Preserve the written form (for round-tripping) but store canonical values alongside.

## Minimal compiler checklist
- **Tokenizer** tolerates units spelled out or abbreviated (AU/au, ly/light year, km/kilometer, m/meters, Re/Earth radii, Me/Earth masses, Rj/Mj).
- **Unit mapper** folds synonyms → canonical units and adds scaling factors.
- **Number extractor** handles numerals and simple words (`one`, `two`, `five`) when adjacent to units.
- **Range parser** detects `..` or `to` for belts and zone definitions.
- **Error messaging** points to the exact line in the ASTRA block when a unit is unrecognized.

## Quick-start workflow in Obsidian
1) Duplicate a template from `_templates`.  
2) Fill lore and cross-links first.  
3) Append the ASTRA block using natural wording for units.  
4) Run the compiler (or a watcher) to validate; fix reported unit issues inline.  
5) Drag orbit/plane in the sim → let it rewrite only the ASTRA block, keeping lore intact.

## Why Obsidian works here
- Local-first, markdown-native, and cross-platform.
- Wikilinks + backlinks give you instant graph views of systems and factions.
- Templates and snippets make ASTRA blocks consistent while keeping lore free-form.
- The vault mirrors the simulator's data model, so syncing is straightforward.
