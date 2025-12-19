# Clocks (future)

Time remains a unitless parameter for now. When clocks are added, each node
can carry a simple affine transform from global time into local time
(e.g. `tau(T) = alpha * T + beta`). This keeps the schema forward compatible
without forcing the web viewer to change.
