import geopandas as gpd
import fiona

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
df = gpd.read_file("./files/417-86-11687-19052021.kml", driver='KML')


type(df)

print(df)