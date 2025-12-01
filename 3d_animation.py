"""Generate a simple 3D surface animation and save it to disk.

This script procedurally generates a damped circular wave field and renders
it as an MP4 animation. Defaults can be customized with command-line
arguments; run ``python 3d_animation.py --help`` for details.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3  # noqa: F401  # imported for 3D projection
import numpy as np


DEFAULT_OUTPUT = Path("shallow_water_animation.mp4")
DEFAULT_FRAMES = 240
DEFAULT_GRID_SIZE = 60
DEFAULT_INTERVAL_MS = 20
DEFAULT_FPS = 30
DEFAULT_AMPLITUDE = 1.0
DEFAULT_SPEED = 0.04
DEFAULT_DECAY = 0.003


def generate_wave(
    frames: int,
    grid_size: int,
    amplitude: float,
    wave_speed: float,
    decay: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate a damped circular wave dataset.

    Returns arrays representing the X and Y grids and a history of height
    values over time shaped ``(frames, grid_size, grid_size)``.
    """

    xs = np.linspace(-np.pi, np.pi, grid_size)
    ys = np.linspace(-np.pi, np.pi, grid_size)
    X, Y = np.meshgrid(xs, ys)
    radius = np.sqrt(X**2 + Y**2)

    times = np.linspace(0, frames * wave_speed, frames)
    H_history = []
    for t in times:
        height = amplitude * np.sin(radius - t) * np.exp(-decay * radius**2)
        H_history.append(height)

    return X, Y, np.stack(H_history, axis=0)


def build_animation(
    X: np.ndarray,
    Y: np.ndarray,
    H_history: np.ndarray,
    output_path: Path,
    interval_ms: int,
    fps: int,
    bitrate: int = 2000,
) -> None:
    """Create and save the animation to ``output_path``."""

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    frames = H_history.shape[0]
    z_min, z_max = H_history.min(), H_history.max()

    def animate(frame_idx: int) -> None:
        ax.clear()
        ax.set_title("Shallow Water Wave")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("height")
        ax.set_zlim(z_min, z_max)
        ax.plot_surface(X, Y, H_history[frame_idx, :, :], cmap="viridis")

    writer_name = "ffmpeg" if "ffmpeg" in animation.writers.list() else "pillow"
    writer_cls = animation.writers[writer_name]
    writer = writer_cls(fps=fps, metadata=dict(artist="space_sim"), bitrate=bitrate)

    shallow_water_animation = animation.FuncAnimation(
        fig, animate, frames=frames, interval=interval_ms, blit=False
    )
    shallow_water_animation.save(output_path, writer=writer)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output filename for the animation (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--frames",
        type=int,
        default=DEFAULT_FRAMES,
        help="Number of frames to render",
    )
    parser.add_argument(
        "--grid-size",
        type=int,
        default=DEFAULT_GRID_SIZE,
        help="Number of grid points per dimension",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=DEFAULT_INTERVAL_MS,
        help="Delay between frames in milliseconds",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=DEFAULT_FPS,
        help="Frames per second in the output video",
    )
    parser.add_argument(
        "--amplitude",
        type=float,
        default=DEFAULT_AMPLITUDE,
        help="Initial wave amplitude",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=DEFAULT_SPEED,
        help="Phase speed multiplier controlling how fast the wave evolves",
    )
    parser.add_argument(
        "--decay",
        type=float,
        default=DEFAULT_DECAY,
        help="Damping factor; higher values attenuate the wave more quickly",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    X, Y, H_history = generate_wave(
        frames=args.frames,
        grid_size=args.grid_size,
        amplitude=args.amplitude,
        wave_speed=args.speed,
        decay=args.decay,
    )

    build_animation(
        X,
        Y,
        H_history,
        output_path=args.output,
        interval_ms=args.interval,
        fps=args.fps,
    )


if __name__ == "__main__":
    main()
