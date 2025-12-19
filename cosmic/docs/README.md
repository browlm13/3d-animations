# Cosmic workspace

This workspace splits the project into three crates:

- `cosmic_core`: minimal physics and schema definitions.
- `cosmic_gen`: deterministic tree generator that depends on the core.
- `cosmic_web`: thin glue for the web viewer that depends on the generator and core.

Run a quick health check from the workspace root:

```bash
cargo check --workspace
```

Explore the schemas in `docs/SCHEMAS.md` and the crate-level docs for more detail.
