use serde::{Deserialize, Serialize};

use crate::math::Vec2;

/// Parent-relative orbit models.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum Orbit2D {
    /// Fixed offset in the parent's frame.
    Static { dx: f64, dy: f64 },

    /// Simple rotation curve defined by a radius, starting phase, and angular speed.
    RotationCurve {
        radius_kpc: f64,
        phase0_rad: f64,
        angular_speed: f64,
    },
}

impl Orbit2D {
    /// Evaluate the position offset for a given time parameter.
    pub fn offset(&self, time: f64) -> Vec2 {
        match self {
            Orbit2D::Static { dx, dy } => Vec2::new(*dx, *dy),
            Orbit2D::RotationCurve {
                radius_kpc,
                phase0_rad,
                angular_speed,
            } => {
                let angle = phase0_rad + angular_speed * time;
                Vec2::from_polar(*radius_kpc, angle)
            }
        }
    }
}
