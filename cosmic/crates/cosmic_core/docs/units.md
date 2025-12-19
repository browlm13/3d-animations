# Units

The core keeps units explicit to stay wiki-ready and to allow downstream
crates to overlay their own presentation. Distances are stored as `f64`
and expressed in kiloparsecs in the galaxy-scale recipes. Time is a
unitless parameter that can be mapped to any real-world cadence by the
viewer or simulator.
