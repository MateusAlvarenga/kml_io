import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

 
#Leitura do arquivo kml
fp = "./files/417-86-11687-19052021.kml"
polys = gpd.read_file(fp, driver='KML')
#print(polys)
#Plota o mapa
fig = polys.plot("Name", facecolor="white", edgecolor="black")
plt.axis('off')
fig.set_title("Titulo")
plt.savefig('./files/mapa.jpg')

#Plota a legenda
plt.rcParams.update({'font.size': 7})
 
plt.box(False)
ax = polys.plot("Name",legend=True,label='_nolegend_')
plt.axis('off') 
plt.rcParams.update({'font.size': 10})

plt.savefig('./files/legenda.jpg')


#Junta a imagem com a legenda
image1 = Image.open('./files/mapa.jpg')
image2 = Image.open('./files/legenda.jpg')
#Ajuste de tamanho das imagens
image1 = image1.resize((600, 400))

image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image2_size[0], image2_size[1]), (250,250,250))
new_image.paste(image1,(-10,-10))
new_image.paste(image2,(image2_size[0] -10 ,0))
new_image.save("./files/output.jpg","JPEG")