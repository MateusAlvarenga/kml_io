import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
import contextily as ctx
import kml2geojson
 
 
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

 
# #Leitura do arquivo kml
fp = "./files/teste.kml"

kml2geojson.main.convert(fp, './json_files/')
fp = './json_files/teste.geojson'
 
#polys = gpd.read_file(fp, driver='KML')
polys = gpd.read_file(fp)
 

polys = polys.to_crs(epsg=900913)
plt.tight_layout()
plt.rcParams.update({'font.size': 6}) 
 
#lg = plt.legend(list(polys["Name"]),bbox_to_anchor=(1.05, 1.0), loc='upper left')


fig = polys.plot(legend=True, facecolor="white", edgecolor="black",cmap="tab20",legend_kwds={'bbox_to_anchor': (1, 1)}) 

ctx.add_basemap(fig, zoom=15,crs='EPSG:900913', source=ctx.providers.CartoDB.Voyager)

plt.axis('off') 
plt.savefig('./files/legenda.jpg')
