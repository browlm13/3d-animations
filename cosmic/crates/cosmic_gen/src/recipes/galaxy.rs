use rand::{rngs::StdRng, SeedableRng};

use cosmic_core::{orbit::Orbit2D, Node};

use crate::{distributions::sample_cluster_radius, GeneratorConfig, NodeMeta};

/// Build a simple galaxy tree with a root and orbiting clusters.
pub fn build_galaxy(seed: u64, cfg: &GeneratorConfig) -> (Vec<Node>, Vec<NodeMeta>) {
    let mut rng = StdRng::seed_from_u64(seed);
    let root_id = "galaxy_root".to_string();

    let mut nodes = Vec::with_capacity(cfg.cluster_count + 1);
    let mut meta = Vec::with_capacity(cfg.cluster_count + 1);

    nodes.push(Node::root(root_id.clone()));
    let mut root_meta = NodeMeta::new(root_id.clone());
    root_meta.display_name = Some("Galaxy".into());
    root_meta.kind = Some("galaxy".into());
    meta.push(root_meta);

    for cluster_idx in 0..cfg.cluster_count {
        let radius = sample_cluster_radius(&mut rng, cfg);
        let phase = rng.gen_range(0.0..std::f64::consts::TAU);
        let node_id = format!("cluster_{cluster_idx}");
        nodes.push(Node {
            id: node_id.clone(),
            parent: Some(root_id.clone()),
            orbit: Some(Orbit2D::RotationCurve {
                radius_kpc: radius,
                phase0_rad: phase,
                angular_speed: cfg.rotation_speed,
            }),
        });

        let mut m = NodeMeta::new(node_id.clone());
        m.display_name = Some(format!("Cluster {cluster_idx}"));
        m.kind = Some("cluster".into());
        m.color_hint = Some("#66ccff".into());
        m.tags = vec!["orbiting".into()];
        meta.push(m);
    }

    (nodes, meta)
}
