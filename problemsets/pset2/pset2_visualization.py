import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Read back geocoded file
ga_jobs = pd.read_csv("geocoded_jobs.csv")

# Create GeoDataFrame
ga_jobs = ga_jobs.dropna(subset=['lat', 'lon'])
geometry = [Point(xy) for xy in zip(ga_jobs.lon, ga_jobs.lat)]
geo_jobs = gpd.GeoDataFrame(ga_jobs, geometry=geometry, crs="EPSG:4326")

# Load Georgia state boundaries
usa = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
georgia = usa[(usa.name == "United States")]
georgia = georgia.to_crs("EPSG:4326")  # Match CRS

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
georgia.boundary.plot(ax=ax, color='black')
geo_jobs.plot(ax=ax, markersize=10, color='red', alpha=0.5)
plt.title("H-2A Employer Job Locations in Georgia")
plt.axis('off')
plt.show()
