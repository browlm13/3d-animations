# Wiki-First Universe Engine — Implementation Packet

This document captures the design summary for a wiki-first "Universe OS" that unifies lore editing with a shared ASTRA DSL for simulation. It is intended to be copy-pasted into a technical chat as a ready-made briefing for building file structures, schemas, editors, and simulator integrations.

---

## Goal

Build a **wiki-first universe engine**—akin to LegendKeeper or Memory Alpha—that directly drives a space simulator.

It must be:

- **Easy to edit** (AU, ly, Earth radii, natural language classifications)
- **Visually driven** (orbits drag-and-drop, concept art embedded)
- **Scientifically coherent** (tilted planes, eccentric orbits, trojans, belts)
- **RPG-friendly** (lore, factions, maps)
- **Hard-sci-fi flexible** (rogue planets, resonances, unusual orbits)
- **Bidirectional** (wiki ↔ sim share one data model)

The result is a unified **"Universe OS."**

---

## Top-Level Structure

### 1. Wiki Page = Entity

Every entity (galaxy, cluster, system, planet, moon, belt, faction, species…) is a **wiki page** with two layers:

- **Lore layer**: Rich text, images/concept art, cross-links, maps, timelines.
- **ASTRA block (physics layer)**: An embedded DSL block parsed by a compiler and fed into the simulation.

Example ASTRA snippet:

```astra
body Leviathan {
  class C
  kind super_earth
  orbit 1.6 AU
  size 1.9 Re
  mass 8.2 Me
  eccentricity 0.03
  plane tilt 15 deg, -5 deg
}
```

### 2. File Structure (Obsidian-Friendly)

```
universe/
  galaxies/
    milky_way.md
    perseus_arm.md
  clusters/
    ajhar.md
    tengri_cluster.md
  systems/
    tengri.md
    romulus_remus.md
  bodies/
    leviathan.md
    prosperity.md
    jade_belt.md
  factions/
    jade_covenant.md
  species/
    rorin.md
  art/
    leviathan_ultrawide.png
    tengri_concept.png
  templates/
    system_template.md
    body_template.md
  compiler/
    astra_parser.py
    astra_to_json.py
```

Each `.md` page: lore at the top; ASTRA block at the bottom.

Example page:

````markdown
# Leviathan

Jungle megabiome. Pirate fortress. Storm-wrapped super-Earth.

![concept](../art/leviathan_ultrawide.png)

```astra
body Leviathan {
  class C
  kind super_earth
  plane main
  orbit ellipse { a 1.6 AU; e 0.03; inc 2 deg }
  size 1.9 Re
  mass 8.2 Me
  trojans [Leviathan_L4, Leviathan_L5]
}
```
````

---

## ASTRA Language (DSL)

Readable like prose, powerful like a physics config.

- **Simple circular orbits:** `orbit 1.4 AU`
- **Elliptical orbits:**

  ```astra
  orbit ellipse { a 1.6 AU; e 0.03; inc 3 deg; node 40 deg }
  ```
- **Tilted planes:** per system or per body
- **Quaternions (optional):** `orbit tilt quaternion(w, x, y, z)`
- **Asteroid belts:**

  ```astra
  belt 2.1 AU .. 3.6 AU density high
  ```
- **Trojan bodies:**

  ```astra
  trojan_of Leviathan at L4
  ```
- **Rogue planets:** `orbit rogue`
- **Planet classes (fictional):** `class S/A/B/C/D/E/F/R/X`
- **Scientific kinds:** `kind super_earth`, `kind gas_giant`
- **Zones defined per star:**

  ```astra
  zones { inner < 0.7 AU; comfort 1-2 AU; outer >3.5 AU }
  ```

---

## Entity Hierarchy

- **Galaxy**: visual map coordinates; contains clusters
- **Cluster**: map coordinates; contains star systems
- **Star System**: stars (mass, radius, spectrum), system plane tilt, zones, bodies
- **Body**: type (planet/moon/belt/rogue), orbit details, size/mass/gravity, belts/rings/trojans, concept art

---

## Simulator Integration

- Simulator reads ASTRA blocks → normalized JSON.
- Simulator never edits wiki text directly; it edits via ASTRA updates.
- 2D/3D visualization of orbits with drag-to-edit orbits and plane rotations.
- Supports AU/ly/Earth radii/Earth masses.
- Handles multiple planes, eccentric orbits, resonances, belts, trojan geometry, rogue bodies, and optional custom ephemeris tracks.
- A universal compiler performs ASTRA → internal JSON → simulation.

---

## Desired Outputs from This Packet

- Directory structure
- ASTRA grammar definition
- ASTRA → JSON compiler
- JSON schema for the simulator
- Editor UI plans (basic and advanced)
- Frontend design for orbit dragging
- Cross-linking structure
- Concept art storage logic

This summary is intentionally compact and code-friendly so it can be handed off to build the technical foundation.
