use rand::prelude::*;
use rand_distr::{Distribution, Normal};

use crate::GeneratorConfig;

/// Sample a cluster radius from a normal distribution centered on the
/// configured radius with the provided spread (standard deviation).
pub fn sample_cluster_radius<R: Rng + ?Sized>(
    rng: &mut R,
    cfg: &GeneratorConfig,
) -> f64 {
    let normal = Normal::new(cfg.cluster_radius_kpc, cfg.cluster_spread_kpc.max(0.001))
        .expect("positive standard deviation");
    normal.sample(rng).max(0.0)
}
