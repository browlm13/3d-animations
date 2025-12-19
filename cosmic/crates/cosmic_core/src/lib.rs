//! Minimal physics core for the cosmic workspace.
//! 
//! The core keeps the schema small and focused on evaluating node positions
//! based on parent-relative orbits. Metadata and presentation concerns live
//! in higher layers such as `cosmic_gen` and `cosmic_web`.

pub mod math;
pub mod orbit;
pub mod tree;

pub use math::Vec2;
pub use orbit::Orbit2D;
pub use tree::{eval_positions, Node, TreeError};
