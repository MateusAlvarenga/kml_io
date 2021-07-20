import geopandas as gpd
import matplotlib.pyplot as plt
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


# Filepath to KML file
fp = "history.kml"

polys = gpd.read_file(fp, driver='KML')
print(polys)
polys.plot()
plt.savefig('test.jpg')