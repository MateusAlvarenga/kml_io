from pydantic import BaseModel

#@param {caminho_arquivo_kml} str
#@param {caminho_arquivo_kml} str
#@param {tamanho_fonte} Optional default = 16
class Requisicao_padrao(BaseModel):
    caminho_arquivo_kml: str
    caminho_arquivo_saida: str
    tamanho_fonte Optional[int] = 16