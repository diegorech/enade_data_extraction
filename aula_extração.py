#  Extração de dados do ENADE utilizando Python

import pandas as pandas
import numpy as numpy
import zipfile
import requests # Realizar request para o site do inep e realizar o download dos dados
from io import BytesIO # Configurar os inputs dos dados para trabalhar no ambiente python
import os


# Como os dados do Enade chegam em um zip com vários arquivos, precisamos armazena-los em uma pasta para depois trabalhar-mos com eles

os.makedirs('./enade2019', exist_ok=True)

'''
    exists_ok=True, para que se executarmo o código mais de 1 vez, não retorne um erro.
    Se a pasta já existir, nada acontecerá e o processo continuará em execução
'''

url_enade_2019 = "http://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2019.zip"

# Download do conteúdo
filebytes = BytesIO( # Possuí o retorno do request realizado
    requests.get(url_enade_2019).content
)

# Informando o Python de que o arquivo é um .zip
myzip = zipfile.ZipFile(filebytes)
# Extração dos dados
myzip.extractall('./enade2019')
