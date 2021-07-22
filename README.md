

##>Criando um virtualenv:   
```
    virtualenv kml_io_virtualenv
```

##>ativando virtualenv criado:   
```
    source kml_io_virtualenv/bin/activate
```

##>instalando dependencias:   
```
    pip install -r requirements.txt
```


##>Iniciando API:
(Obs: No diretorio /api)
```
    uvicorn main:app --port=9090 --reload
```

##>Acessar Documentação da API:
```
    host:porta/redoc
```
___
##>desativando virtualenv:
```
    deactive
```

##>listar dependencias: 
```
    pip freeze
```

##>Configuração Para instalar dependencias virtualenv no gitpod:
```
export PIP_USER=false
```