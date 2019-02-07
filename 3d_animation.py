#
# Animate
#

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

#
# settings
#

OUTPUT_ANIMATION_FNAME = 'shallow_water_animation_6.mp4'

INTERVAL = 20
INC = 1 #2500
MIN_H, MAX_H = -1, 1

FRAMES = H_history.shape[0] - 1 #int((H_history.shape[0]-1)/INC)-1

#
# Create animation
#


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(xs, ys)

counter = 0
def animate(i):
    
    global counter
    
    # update plot
    ax.clear()
 
    if counter % 10 ==0:
        print(counter)

    ax.set_title('Shallow Water Wave');
    ax.plot_surface(X, Y, H_history[counter,:,:])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('height(time)');
    
    # update counter
    counter += INC

shallow_water_animation = animation.FuncAnimation( fig, animate, frames=FRAMES, interval=INTERVAL )

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=42, metadata=dict(artist='Me'), bitrate=1800)
shallow_water_animation.save(OUTPUT_ANIMATION_FNAME, writer=writer)
