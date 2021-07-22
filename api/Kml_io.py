import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os
import contextily as ctx
import kml2geojson
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image
from fastapi import HTTPException


gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
 
class Kml_io:
    
    # @param {caminho_arquivo} string - caminho do arquivo kml a ser convertido
    # @param {caminho_saida} strinh - caminho da pasta onde o arquivo convertido será salvo
    # !!!! O arquivo será salvo em {caminho_saida} + nome original do arquivo + jpg
    # @param {tamanho_fonte} Number - Tamanho da fonte, Valor default = 16
    # @param {altura} Number - altura da imagem, Valor default = 20
    # @param {largura} Number - largura da imagem, Valor default = 20
    # @return - retorna 200 se o arquivo foi salvo
    def Converte(
                    self, 
                    caminho_arquivo_kml,
                    caminho_saida,
                    tamanho_fonte = 16,
                    altura = 20,
                    largura = 20
    ):


        # #Leitura do arquivo kml
        fp = caminho_arquivo_kml
        try:
            polys = gpd.read_file(fp)
        except:
           raise HTTPException(status_code=500, detail="Erro ao encontrar o arquivo")
        
        novo_nome = os.path.splitext(os.path.basename(caminho_arquivo_kml))[0]

        #Fonte e espaçamento
        plt.tight_layout()
        plt.rcParams.update({'font.size': 6}) 
        
        #Plota o gráfico
        fig = polys.plot(
                            "Name",
                            legend=True,
                            facecolor="white",
                            figsize=(altura, largura),
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
            response = plt.savefig(caminho_saida + novo_nome + '.jpg')
        except expression as identifier:
            raise HTTPException(status_code=500, detail="Erro ao salvar")
        else:
            return 200

        