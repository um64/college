import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

# Coordinates for markers
coordinates = {'122.44.55.66': (35.6895, 139.6917),
               '111.444.55.6': (37.0902, -95.7129),
               '553.44.44.44': (20.5937, 78.9629)}

# Create figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

# Set map background color to dark blue
ax.set_facecolor('#000000')  

# Draw coastlines with a different color
ax.set_global()
ax.coastlines(color='white') 

# Initialize lists to store dots and alphas
dots = []
dot_alphas = []

# Plot markers and texts for each country
for country, coords in coordinates.items():
    dot, = ax.plot(coords[1], coords[0], 'wo', markersize=0, transform=ccrs.PlateCarree())  # Change marker color to white
    dots.append(dot)
    dot_alphas.append(0.0)  
    ax.text(coords[1], coords[0], country, color='white', fontsize=12, transform=ccrs.PlateCarree())  # Change text color to white

# Define animation parameters and logic
fade_duration = 3 
visible_duration = 10  

def animate(frame):
    for i, dot in enumerate(dots):
        if frame < fade_duration:
            dot_alphas[i] = frame / fade_duration
        elif frame < fade_duration + visible_duration:
            dot_alphas[i] = 1.0
        else:
            dot_alphas[i] = max(0.0, 1 - (frame - fade_duration - visible_duration) / fade_duration)
        
        dot.set_markersize(8)  
        dot.set_alpha(dot_alphas[i])  
    return dots

# Create the animation
ani = FuncAnimation(fig, animate, frames=fade_duration * 2 + visible_duration, interval=100)

# Set the face color of the figure to match the map background color
fig.set_facecolor('#000000')

# Adjust figure size and remove padding
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the animation as a GIF file with transparent background and adjusted boundaries
ani.save('map_animation2.gif', writer='pillow', savefig_kwargs={'facecolor': '#000000', 'transparent': True}, dpi=300)
