use std::collections::{HashMap, HashSet};

use serde::{Deserialize, Serialize};
use thiserror::Error;

use crate::{orbit::Orbit2D, Vec2};

/// Minimal node schema for the physics tree.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct Node {
    pub id: String,
    pub parent: Option<String>,
    pub orbit: Option<Orbit2D>,
}

impl Node {
    pub fn root(id: impl Into<String>) -> Self {
        Self {
            id: id.into(),
            parent: None,
            orbit: None,
        }
    }
}

#[derive(Debug, Error, PartialEq)]
pub enum TreeError {
    #[error("missing parent `{0}` for node")] 
    MissingParent(String),
    #[error("duplicate node id `{0}`")]
    DuplicateId(String),
    #[error("cycle detected at node `{0}`")]
    Cycle(String),
}

/// Evaluate absolute positions for every node at a given time parameter.
///
/// Roots are placed at the origin unless they carry their own orbit offset.
/// Child nodes inherit the evaluated position of their parent and apply their
/// orbit offset at the requested time.
pub fn eval_positions(nodes: &[Node], time: f64) -> Result<HashMap<String, Vec2>, TreeError> {
    let mut lookup: HashMap<&str, &Node> = HashMap::new();
    for node in nodes {
        if lookup.insert(node.id.as_str(), node).is_some() {
            return Err(TreeError::DuplicateId(node.id.clone()));
        }
    }

    let mut positions: HashMap<String, Vec2> = HashMap::new();
    let mut stack: HashSet<String> = HashSet::new();

    for node in nodes {
        compute_position(node.id.as_str(), time, &lookup, &mut positions, &mut stack)?;
    }

    Ok(positions)
}

fn compute_position(
    id: &str,
    time: f64,
    nodes: &HashMap<&str, &Node>,
    positions: &mut HashMap<String, Vec2>,
    stack: &mut HashSet<String>,
) -> Result<Vec2, TreeError> {
    if let Some(pos) = positions.get(id) {
        return Ok(*pos);
    }

    if !stack.insert(id.to_string()) {
        return Err(TreeError::Cycle(id.to_string()));
    }

    let node = nodes.get(id).expect("node looked up after map population");
    let base = if let Some(parent_id) = &node.parent {
        let parent = nodes
            .get(parent_id.as_str())
            .ok_or_else(|| TreeError::MissingParent(parent_id.clone()))?;
        let parent_pos = compute_position(parent.id.as_str(), time, nodes, positions, stack)?;
        let offset = node.orbit.as_ref().map(|orbit| orbit.offset(time)).unwrap_or(Vec2::zero());
        parent_pos + offset
    } else {
        node.orbit
            .as_ref()
            .map(|orbit| orbit.offset(time))
            .unwrap_or(Vec2::zero())
    };

    stack.remove(id);
    positions.insert(id.to_string(), base);
    Ok(base)
}
