import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import contextily as ctx
import kml2geojson
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
 
class Kml_io:
    
    # @param {caminho_arquivo} string - caminho do arquivo kml a ser convertido
    # @param {caminho_saida} strinh - caminho onde o arquivo convertido será salvo
    # @param {tamanho_fonte} Number - Tamanho da fonte, Valor default = 16
    # @return - retorna 200 se o arquivo foi salvo
    def Converte(caminho_arquivo_kml,caminho_saida, tamanho_fonte = 16 ):
        # #Leitura do arquivo kml
        fp = caminho_arquivo_kml
        try:
            polys = gpd.read_file(fp)
        except:
            return 400
        
        
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

  

        try:
            #salva o arquivo - savefig retorna None caso nao ocorra erros
            response = plt.savefig(caminho_saida)
        except expression as identifier:
            return 400
        else:
            return 200

        