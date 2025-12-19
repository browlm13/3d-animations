use std::fs;
use std::path::Path;

use cosmic_core::Node;

use crate::NodeMeta;

/// Export the physics tree to JSON so downstream tools can consume it.
pub fn write_core_json(path: impl AsRef<Path>, nodes: &[Node]) -> std::io::Result<()> {
    let json = serde_json::to_string_pretty(nodes).expect("serializing nodes");
    fs::write(path, json)
}

/// Export metadata alongside the physics tree.
pub fn write_meta_json(path: impl AsRef<Path>, meta: &[NodeMeta]) -> std::io::Result<()> {
    let json = serde_json::to_string_pretty(meta).expect("serializing metadata");
    fs::write(path, json)
}
