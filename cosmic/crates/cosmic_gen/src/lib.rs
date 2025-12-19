//! Deterministic tree generator layered on top of `cosmic_core`.

pub mod distributions;
pub mod export;
pub mod recipes;

use serde::{Deserialize, Serialize};

use cosmic_core::{eval_positions, Node, Vec2};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct NodeMeta {
    pub id: String,
    pub display_name: Option<String>,
    pub kind: Option<String>,
    pub color_hint: Option<String>,
    pub tags: Vec<String>,
}

impl NodeMeta {
    pub fn new(id: impl Into<String>) -> Self {
        Self {
            id: id.into(),
            display_name: None,
            kind: None,
            color_hint: None,
            tags: Vec::new(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GeneratorConfig {
    pub cluster_count: usize,
    pub cluster_radius_kpc: f64,
    pub cluster_spread_kpc: f64,
    pub rotation_speed: f64,
}

impl Default for GeneratorConfig {
    fn default() -> Self {
        Self {
            cluster_count: 8,
            cluster_radius_kpc: 15.0,
            cluster_spread_kpc: 4.0,
            rotation_speed: 0.02,
        }
    }
}

#[derive(Debug, Clone)]
pub struct GeneratedGalaxy {
    pub nodes: Vec<Node>,
    pub meta: Vec<NodeMeta>,
    pub positions: Vec<(String, Vec2)>,
}

/// Create a galaxy tree with deterministic positions for a given seed.
pub fn generate_galaxy(seed: u64, cfg: &GeneratorConfig) -> GeneratedGalaxy {
    let (nodes, meta) = recipes::galaxy::build_galaxy(seed, cfg);
    let positions_map = eval_positions(&nodes, 0.0).expect("generator builds consistent tree");
    let positions = positions_map
        .into_iter()
        .map(|(id, pos)| (id, pos))
        .collect();

    GeneratedGalaxy {
        nodes,
        meta,
        positions,
    }
}
