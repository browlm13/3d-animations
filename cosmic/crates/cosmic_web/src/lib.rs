//! Thin wrapper that ties the generator and core together for a future WASM viewer.
//! The crate stays free of rendering code so the web layer can be swapped without
//! disturbing the physics core or the generator recipes.

pub mod draw;

use cosmic_core::{eval_positions, Node, Vec2};
use cosmic_gen::{generate_galaxy, GeneratorConfig, NodeMeta};

#[derive(Debug, Clone)]
pub struct SceneSnapshot {
    pub nodes: Vec<Node>,
    pub meta: Vec<NodeMeta>,
    pub positions: Vec<(String, Vec2)>,
}

/// Build a ready-to-render scene. The caller can handle camera transforms
/// and UI while the positions remain tied to stable node IDs.
pub fn build_scene(seed: u64, cfg: &GeneratorConfig) -> SceneSnapshot {
    let generated = generate_galaxy(seed, cfg);
    let positions = eval_positions(&generated.nodes, 0.0)
        .expect("generator builds consistent tree")
        .into_iter()
        .collect();

    SceneSnapshot {
        nodes: generated.nodes,
        meta: generated.meta,
        positions,
    }
}
