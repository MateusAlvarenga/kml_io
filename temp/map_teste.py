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
fp = "/workspace/kml_io/temp/files/teste3.kml"
polys = gpd.read_file(fp)
 
#Fonte e espaçamento
plt.tight_layout()
plt.rcParams.update({'font.size': 6}) 
 
 #Plota o gráfico
fig = polys.plot(

                    "Name",
                    legend=True,
                    facecolor="white",
                    figsize=(20, 20),
                    edgecolor="black",
                    cmap="tab20",
                    legend_kwds={'bbox_to_anchor': (1, 1)},                    
                    alpha=0.5
                   
                ) 

#Supostamente adicionaria o mapa ao gráfico
ctx.add_basemap(fig, zoom=4,crs='EPSG:900913', source=ctx.providers.CartoDB.Voyager)

#remove as referencias de eixo
plt.axis('off') 

#salva o arquivo
response = plt.savefig('./files/legenda3333.jpg')

print(response == None)


