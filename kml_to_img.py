import geopandas as gpd
import matplotlib.pyplot as plt
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

 
# Filepath to KML file
fp = "./files/417-86-11687-19052021.kml"

polys = gpd.read_file(fp, driver='KML')



polys.plot("Name")

plt.savefig('./files/test.jpg')

polys.plot("Name",legend=True)

plt.savefig('./files/test2.jpg')