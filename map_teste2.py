import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

  
# #Leitura do arquivo kml
fp = "./files/teste.kml"
polys = gpd.read_file(fp, driver='KML')

plt.tight_layout()
plt.rcParams.update({'font.size': 6}) 
 
#lg = plt.legend(list(polys["Name"]),bbox_to_anchor=(1.05, 1.0), loc='upper left')


fig = polys.plot("Name",legend=True, figsize=(12, 5),facecolor="white", edgecolor="black",cmap="tab20",legend_kwds={'bbox_to_anchor': (1, 1)}) 



plt.axis('off') 
plt.savefig('./files/legenda.jpg')
