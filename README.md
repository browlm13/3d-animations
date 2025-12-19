# 3d-animations

This repo now hosts the `cosmic` Rust workspace described in the project
proposal. The workspace is organized to keep the physics core small while
supporting a deterministic generator and a web-friendly viewer layer.

```
cosmic/
  Cargo.toml          # workspace definition
  crates/
    cosmic_core/      # minimal physics + schema
    cosmic_gen/       # deterministic generator built on the core
    cosmic_web/       # thin viewer glue (WASM-ready stub)
  data/               # configs, builds, and example exports
  docs/               # onboarding and schema notes
```

From `cosmic/` run `cargo check --workspace` to verify the crates build
together. The data examples include `tiny.core.json` and `tiny.meta.json`
showing the split between physics and metadata.
