"""
Generate an Obsidian-friendly Universe OS directory scaffold with example
lore + ASTRA pages spanning galaxies → clusters → systems → bodies → factions
→ species.

Usage:
    python build_universe_scaffold.py [--base ./universe] [--force]

The script is intentionally self-contained and idempotent; re-running without
--force will leave existing files untouched. Use --force to overwrite.
"""

from argparse import ArgumentParser
from pathlib import Path
from textwrap import dedent


BASE_TREE = [
    "_templates",
    "galaxies",
    "clusters",
    "systems",
    "bodies",
    "factions",
    "species",
    "maps",
    "art",
    "attachments",
    "compiler",
]


def get_sample_entities():
    """Return sample entity definitions spanning the hierarchy."""
    return {
        "galaxies": [
            {
                "filename": "asterion.md",
                "title": "Asterion",
                "lore": (
                    "A young barred-spiral galaxy rich with dust lanes and fast-forming arms.\n"
                    "Home to the Tengri Cluster and a beacon for early explorers."
                ),
                "astra": dedent(
                    """
                    galaxy Asterion {
                      clusters [Tengri_Cluster]
                      notes "Anchor galaxy for the expeditionary atlas"
                    }
                    """
                ).strip(),
            }
        ],
        "clusters": [
            {
                "filename": "tengri_cluster.md",
                "title": "Tengri Cluster",
                "lore": (
                    "Sparse open cluster orbiting the Asterion bar.\n"
                    "Features resonant star pairs and a high incidence of trojans."
                ),
                "astra": dedent(
                    """
                    cluster Tengri_Cluster {
                      galaxy Asterion
                      systems [Tengri, Romulus_Remus]
                    }
                    """
                ).strip(),
            }
        ],
        "systems": [
            {
                "filename": "tengri.md",
                "title": "Tengri",
                "lore": (
                    "Golden dwarf system known for its stable habitable zone and vivid auroras.\n"
                    "Trade convoys refuel at the Jade Covenant's orbital stations."
                ),
                "astra": dedent(
                    """
                    system Tengri {
                      star primary {
                        mass 0.92 Ms
                        radius 0.93 Rs
                        spectrum G3V
                      }
                      plane main tilt 4 deg
                      zones { inner < 0.7 AU; comfort 0.9-1.6 AU; outer >3.5 AU }
                      bodies [Leviathan, Prosperity, Jade_Belt]
                    }
                    """
                ).strip(),
            },
            {
                "filename": "romulus_remus.md",
                "title": "Romulus-Remus",
                "lore": (
                    "Binary-star system with braided asteroid streams at each Lagrange point.\n"
                    "Pilgrims prize its eclipses for ritual skywriting displays."
                ),
                "astra": dedent(
                    """
                    system Romulus_Remus {
                      star Romulus { mass 0.71 Ms; spectrum K5V }
                      star Remus   { mass 0.68 Ms; spectrum K7V }
                      plane binary tilt 12 deg
                      bodies [Janus, Delphi]
                    }
                    """
                ).strip(),
            },
        ],
        "bodies": [
            {
                "filename": "leviathan.md",
                "title": "Leviathan",
                "lore": (
                    "Storm-wrapped super-Earth fortress world with a thriving pirate underbelly.\n"
                    "Orbital elevators tie into the Jade Belt shipping lanes."
                ),
                "astra": dedent(
                    """
                    body Leviathan {
                      class C
                      kind super_earth
                      plane main
                      orbit ellipse { a 1.6 AU; e 0.03; inc 2 deg }
                      size 1.9 Re
                      mass 8.2 Me
                      moons [Remora]
                      trojans [Leviathan_L4, Leviathan_L5]
                    }
                    """
                ).strip(),
            },
            {
                "filename": "remora.md",
                "title": "Remora",
                "lore": "Tidal-locked moon supporting research vaults and blacksite labs.",
                "astra": dedent(
                    """
                    body Remora {
                      class D
                      kind rocky_moon
                      orbit 320000 km
                      parent Leviathan
                      period 2.6 days
                      size 0.3 Re
                      mass 0.05 Me
                    }
                    """
                ).strip(),
            },
            {
                "filename": "prosperity.md",
                "title": "Prosperity",
                "lore": (
                    "Temperate ocean world with archipelagos that seed towering cloud spires.\n"
                    "Capital of the Jade Covenant and homeworld of the Rorin."
                ),
                "astra": dedent(
                    """
                    body Prosperity {
                      class B
                      kind ocean_world
                      plane main
                      orbit 1.14 AU
                      size 1.05 Re
                      mass 1.08 Me
                      atmosphere breathable
                      residents [Rorin]
                    }
                    """
                ).strip(),
            },
            {
                "filename": "jade_belt.md",
                "title": "Jade Belt",
                "lore": "Emerald-tinged asteroid belt mined for volatiles and rare silicates.",
                "astra": dedent(
                    """
                    belt Jade_Belt {
                      plane main
                      belt 2.1 AU .. 3.6 AU density high
                      parent Tengri
                    }
                    """
                ).strip(),
            },
            {
                "filename": "janus.md",
                "title": "Janus",
                "lore": (
                    "Resonant planet weaving between the binary stars, with alternating day lengths."
                ),
                "astra": dedent(
                    """
                    body Janus {
                      class R
                      kind rogue_captured
                      plane binary
                      orbit ellipse { a 0.9 AU; e 0.21; inc 7 deg }
                      size 1.4 Re
                      mass 2.3 Me
                      resonances [Delphi 3:2]
                    }
                    """
                ).strip(),
            },
            {
                "filename": "delphi.md",
                "title": "Delphi",
                "lore": "Icy world with luminous ring arcs, prized for neutrino observatories.",
                "astra": dedent(
                    """
                    body Delphi {
                      class E
                      kind ice_giant
                      plane binary
                      orbit ellipse { a 1.6 AU; e 0.08; inc 5 deg }
                      size 3.7 Re
                      mass 16.0 Me
                      rings translucent
                    }
                    """
                ).strip(),
            },
        ],
        "factions": [
            {
                "filename": "jade_covenant.md",
                "title": "Jade Covenant",
                "lore": (
                    "Merchant league overseeing the Tengri trade corridor and arbitration pacts.\n"
                    "Operates sky-barges above Leviathan and Prosperity."
                ),
                "astra": dedent(
                    """
                    faction Jade_Covenant {
                      scope Tengri_Cluster
                      seats [Prosperity, Leviathan]
                      fleets 3
                    }
                    """
                ).strip(),
            }
        ],
        "species": [
            {
                "filename": "rorin.md",
                "title": "Rorin",
                "lore": (
                    "Aquatic-adapted sophonts with bioluminescent cartilage.\n"
                    "They engineer coral databanks and favor ocean world migrations."
                ),
                "astra": dedent(
                    """
                    species Rorin {
                      origin Prosperity
                      physiology amphibiotic
                      tech_level interstellar
                    }
                    """
                ).strip(),
            }
        ],
    }


def render_markdown(title: str, lore: str, astra_block: str) -> str:
    """Combine lore and ASTRA into a markdown page."""
    return dedent(
        f"""
        # {title}

        {lore}

        ```astra
        {astra_block}
        ```
        """
    ).strip() + "\n"


def render_templates(base: Path):
    """Create starter templates that mirror the Obsidian guide."""
    templates = {
        "galaxy.md": """---\ntitle: <galaxy name>\nentity: galaxy\n---\n\n# <galaxy name>\n\nLore here.\n\n```astra\ngalaxy <galaxy> {\n  clusters [<cluster_a>, <cluster_b>]\n}\n```\n""",
        "cluster.md": """---\ntitle: <cluster name>\nentity: cluster\n---\n\n# <cluster name>\n\nLore here.\n\n```astra\ncluster <cluster> {\n  galaxy <parent_galaxy>\n  systems [<system_a>, <system_b>]\n}\n```\n""",
        "system.md": """---\ntitle: <system name>\nentity: system\n---\n\n# <system name>\n\nLore here.\n\n```astra\nsystem <system> {\n  star primary { mass 1.0 Ms; spectrum G2V }\n  plane main\n  zones { inner < 0.7 AU; comfort 0.9-1.5 AU; outer >3 AU }\n  bodies [<body_a>, <body_b>]\n}\n```\n""",
        "body.md": """---\ntitle: <body name>\nentity: body\n---\n\n# <body name>\n\nLore here.\n\n```astra\nbody <body> {\n  class C\n  kind super_earth\n  plane main\n  orbit 1.2 AU\n  size 1.8 Re\n  mass 7 Me\n}\n```\n""",
        "faction.md": """---\ntitle: <faction name>\nentity: faction\n---\n\n# <faction name>\n\nLore here.\n\n```astra\nfaction <faction> {\n  scope <cluster_or_region>\n  seats [<world_a>, <world_b>]\n}\n```\n""",
        "species.md": """---\ntitle: <species name>\nentity: species\n---\n\n# <species name>\n\nLore here.\n\n```astra\nspecies <species> {\n  origin <homeworld>\n  physiology <notable_traits>\n  tech_level <tier>\n}\n```\n""",
    }

    for filename, content in templates.items():
        path = base / "_templates" / filename
        if not path.exists():
            path.write_text(content.strip() + "\n", encoding="utf-8")


def ensure_tree(base: Path):
    for folder in BASE_TREE:
        (base / folder).mkdir(parents=True, exist_ok=True)


def write_entities(base: Path, entities: dict, force: bool):
    for category, pages in entities.items():
        for page in pages:
            path = base / category / page["filename"]
            if path.exists() and not force:
                continue
            content = render_markdown(page["title"], page["lore"], page["astra"])
            path.write_text(content, encoding="utf-8")


def write_compiler_stub(base: Path, force: bool):
    content = dedent(
        """
        # ASTRA Compiler Stub

        This folder is reserved for the ASTRA parser and JSON emitter. Add your
        implementation here and point the Obsidian vault or simulator watcher to
        these scripts.
        """
    ).strip() + "\n"
    path = base / "compiler" / "README.md"
    if not path.exists() or force:
        path.write_text(content, encoding="utf-8")


def main():
    parser = ArgumentParser(description="Build a Universe OS wiki scaffold")
    parser.add_argument(
        "--base",
        default="universe",
        help="Root directory to create (default: ./universe)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files with the sample content",
    )
    args = parser.parse_args()

    base = Path(args.base).expanduser().resolve()
    ensure_tree(base)
    render_templates(base)
    write_entities(base, get_sample_entities(), force=args.force)
    write_compiler_stub(base, force=args.force)
    print(f"Universe scaffold created at: {base}")


if __name__ == "__main__":
    main()
