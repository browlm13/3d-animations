# Galaxy recipe

The initial generator builds a single galaxy root with a handful of orbiting
clusters. The layout is deterministic for a given `(seed, config)` pair so the
viewer and future wiki overlays can refer to stable node IDs.

Parameters:

- `cluster_count`: number of clusters to spawn
- `cluster_radius_kpc`: mean radius for cluster orbits
- `cluster_spread_kpc`: standard deviation around the mean radius
- `rotation_speed`: angular speed applied to every cluster (simplified model)
