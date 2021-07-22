from pydantic import BaseModel

class Requisicao_padrao(BaseModel):
    caminho_arquivo_kml: str
    caminho_arquivo_saida: str
    tamanho_fonte Optional[int] = 16