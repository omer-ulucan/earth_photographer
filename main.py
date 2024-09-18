import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Specify a location using latitude and longitude
latitude = 30
longitude = 20

# Generate a world map
fig = plt.figure(figsize=(12, 8))
m = Basemap(
    projection='ortho',  # Orthographic projection
    lat_0=latitude,      # Center latitude
    lon_0=longitude,     # Center longitude
    resolution='l'       # Low resolution
    )

# Draw continents and oceans using the Bluemarble satellite image
m.bluemarble()  # High-quality satellite image

# Save the map as an image
plt.savefig("realistic_world.png", dpi=600)  # Save with 600 DPI resolution
plt.show()  # Display the map
