#@author Mateus Alarenga Pereira - github.com/MateusAlvarenga

from pydantic import BaseModel
from typing import Optional

#@param {caminho_arquivo_kml} str
#@param {caminho_arquivo_kml} str
#@param {tamanho_fonte} Optional default = 16
class Requisicao_padrao(BaseModel):
    caminho_arquivo_kml: str
    caminho_arquivo_saida: str
    tamanho_fonte: Optional[int] = 8
    altura: Optional[int] = 7
    largura: Optional[int] = 15

class Requisicao_Diretorio(BaseModel):
    caminho_diretorio: str
    caminho_diretorio_saida: str