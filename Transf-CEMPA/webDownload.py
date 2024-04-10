import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Função para baixar arquivos
def download_file(url, local_path):
    with open(local_path, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

# URL da página que contém os links dos arquivos
url = 'https://tatu.cempa.ufg.br/BRAMS-dataout/2024040200/'

# Pasta local para salvar os arquivos
local_folder = 'd:\\temp\\CEMPA-UFG'

# Certifique-se de que a pasta local existe
if not os.path.exists(local_folder):
    os.makedirs(local_folder)

# Fazer a requisição para a página
response = requests.get(url)

# Analisar o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os links com extensão .ctl e .gra
links = soup.find_all('a', href=True)
for link in links:
    href = link['href']
    if href.endswith('.ctl') or href.endswith('.gra'):
        # Construir o URL completo
        file_url = urljoin(url, href)
        # Nome do arquivo
        filename = os.path.join(local_folder, href.split('/')[-1])
        # Baixar o arquivo
        download_file(file_url, filename)
        print(f"Arquivo {filename} baixado com sucesso!")
