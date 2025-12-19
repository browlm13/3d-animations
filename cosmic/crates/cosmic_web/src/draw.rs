use cosmic_core::Vec2;

/// Convert world coordinates into screen coordinates with a simple scale.
pub fn world_to_screen(pos: Vec2, scale: f64) -> (f64, f64) {
    (pos.x * scale, pos.y * scale)
}

/// Placeholder render hook. Future WASM code can call into this with a canvas
/// context and paint each node according to its metadata.
pub fn describe_point(id: &str, pos: Vec2) -> String {
    format!("{} @ ({:.2}, {:.2})", id, pos.x, pos.y)
}
