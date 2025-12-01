# 3d-animations

A tiny demo for generating and saving a 3D surface animation with Matplotlib.
The default animation renders a damped circular wave and writes it to an MP4
(or GIF if ffmpeg is unavailable).

## Usage

```bash
python 3d_animation.py --help
```

Example rendering with defaults:

```bash
python 3d_animation.py
```

Customize the wave or output:

```bash
python 3d_animation.py \
  --output custom_wave.mp4 \
  --frames 300 \
  --grid-size 80 \
  --amplitude 1.2 \
  --speed 0.06 \
  --decay 0.004
```

If ffmpeg is installed it will produce an MP4; otherwise the script falls back
to Pillow and writes a GIF.
