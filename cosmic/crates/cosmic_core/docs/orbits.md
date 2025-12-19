# Orbit models

Orbit models are intentionally minimal and stable. Each node carries an
`Orbit2D` that expresses its motion relative to its parent.

## Static

A fixed offset in the parent's frame. Use this for roots or bodies that
should move in lockstep with the parent.

## RotationCurve

A circular motion defined by a radius (in kpc), a starting phase (radians),
and an angular speed. The offset at time `T` is
`Vec2::from_polar(radius, phase0 + angular_speed * T)`.

Future orbit types can add more expressive models (Keplerian, precession)
without altering the existing schema.
