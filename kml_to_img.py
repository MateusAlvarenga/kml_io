import geopandas as gpd
import matplotlib.pyplot as plt
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


# Filepath to KML file
fp = "./files/417-94-11688-19052021.kml"

polys = gpd.read_file(fp, driver='KML')
print(polys)
polys.plot()
plt.savefig('./files/test2.jpg')