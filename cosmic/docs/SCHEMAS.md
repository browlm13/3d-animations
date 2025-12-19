# Schema overview

## Core (physics)

```rust
struct Node {
    id: String,
    parent: Option<String>,
    orbit: Option<Orbit2D>,
}

enum Orbit2D {
    Static { dx: f64, dy: f64 },
    RotationCurve { radius_kpc: f64, phase0_rad: f64, angular_speed: f64 },
}
```

Roots have `parent = None`. Children inherit their parent position and apply
their orbit offset at the requested time.

## Metadata (viewer/wiki friendly)

```rust
struct NodeMeta {
    id: String,
    display_name: Option<String>,
    kind: Option<String>,
    color_hint: Option<String>,
    tags: Vec<String>,
}
```

Metadata is intentionally stored separately so the core can stay focused on
physics. Stable IDs allow future wiki overrides to attach without rewriting the
viewer.
