from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from Kml_io import Kml_io
from Requisicao import Requisicao_padrao, Requisicao_Diretorio


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def Links():
    return """
    <html>
        <head>
            <title>KML_IO</title>
        </head>
        <body>
            <ul>
                <li><a href='/docs'>Swagger teste a api</a></li>
                <li><a href='/redoc'>ReDoc</a></li>
            </ul>
        </body>
    </html>
    """


#@param {caminho_arquivo_kml} str
#@param {caminho_arquivo_kml} str
#@param {tamanho_fonte} Optional default = 16
@app.post("/api/Converte/")
async def Converte(Requisicao: Requisicao_padrao):
     
    Kml_io_provider = Kml_io()
    
  
    response = Kml_io_provider.Converte(
                    Requisicao.caminho_arquivo_kml,
                    Requisicao.caminho_arquivo_saida,
                    Requisicao.tamanho_fonte,
                    Requisicao.altura,
                    Requisicao.largura                                
                                
    )

    return response


@app.post("/api/Converte_Diretorio/")
async def Converte_Diretorio(Requisicao: Requisicao_Diretorio):
    Kml_io_provider = Kml_io()
    return Kml_io_provider.Converte_Diretorio(
                                                Requisicao.caminho_diretorio,
                                                 Requisicao.caminho_diretorio_saida
    )
    