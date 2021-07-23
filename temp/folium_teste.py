import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import re

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

fp = "/workspace/kml_io/temp/files/teste2.kml"
polys = gpd.read_file(fp)

geometria = str(polys["geometry"][0])
posicionamento = geometria.split(",")[2].split(" ")
print(posicionamento)
latitude = posicionamento[1]
longitude = posicionamento[2]

print('latitude:', latitude)
print('logintude:', longitude)


plt.tight_layout()
plt.rcParams.update({'font.size': 6}) 
 
#lg = plt.legend(list(polys["Name"]),bbox_to_anchor=(1.05, 1.0), loc='upper left')
fig = polys.plot(legend=False,)


fmap = folium.Map(location=[longitude, latitude],zoom_start=15)


#fmap = folium.Map()
fmap_geojson = folium.features.GeoJson(polys)
fmap.add_child(fmap_geojson)


fmap_geojson.save("/workspace/kml_io/temp/files/index.html")