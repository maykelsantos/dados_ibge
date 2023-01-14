import requests
import pandas as pd
import plotly.express as px
    

url = 'https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020/variaveis/9808|93|9812?localidades=N1[all]'
requisicao = requests.get(url)
dados = requisicao.json()

display(dados)

