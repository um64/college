import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

coordinates = {'122.44.55.66': (35.6895, 139.6917),
               '111.444.55.6': (37.0902, -95.7129),
               '553.44.44.44': (20.5937, 78.9629)}


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())


ax.set_facecolor('#000000')  


ax.set_global()
ax.coastlines(color='white') 


dots = []
dot_alphas = []


for country, coords in coordinates.items():
    dot, = ax.plot(coords[1], coords[0], 'wo', markersize=0, transform=ccrs.PlateCarree()) 
    dots.append(dot)
    dot_alphas.append(0.0)  
    ax.text(coords[1], coords[0], country, color='lime', fontsize=12, transform=ccrs.PlateCarree()) 


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
        dot.set_color('lime')
    return dots


ani = FuncAnimation(fig, animate, frames=fade_duration * 2 + visible_duration, interval=100)


fig.set_facecolor('#000000')

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

ani.save('map_animation2.gif', writer='pillow', savefig_kwargs={'facecolor': '#000000', 'transparent': True}, dpi=300)
