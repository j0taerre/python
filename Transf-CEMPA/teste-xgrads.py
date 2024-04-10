#from xgrads import open_CtlDataset
import os 
import xgrads
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np



# Caminho para os arquivos
path = os.getcwd()
os.chdir("d:\\temp\\")
path = os.getcwd()

##ctl_file = 'd:\\temp\\Go5km-A-2023-04-15-000000-g1.ctl'
ctl_file = "Go5km-A-2023-04-15-000000-g1.ctl"

#print(ctl_file)

## load the data into xarray.Dataset
#dset = open_CtlDataset(ctl_file)

#dset['dat'].plot()

# Carregar o conjunto de dados CTL usando xgrads
dataset = xgrads.open_mfdataset(ctl_file)

# Ler os dados do conjunto de dados
data = dataset.to_dict()

print(data['coords'].keys())

# Imprimir todas as chaves disponíveis
#print(data['data_vars'].keys())
#print(data['data_vars']['TEMPC'].keys())
#print(data['data_vars']['TEMPC']['data'])
#print(data['data_vars']['TEMPC']['data'].keys())

# Exemplo de como acessar os dados
# Supondo que você queira acessar a variável "TEMPC" (temperatura)
#temperatura = data['TEMPC']
temperatura = data['data_vars']['TEMPC'].values#['data']


# Agora você pode processar e analisar os dados conforme necessário

# Coletar as coordenadas de latitude e longitude
##lons = data['dims']['x']
##lats = data['dims']['y']

# Acessar as coordenadas de latitude e longitude
lats = data['coords']['lat']
lons = data['coords']['lon']

# Criar uma grade de coordenadas
#lon, lat = np.meshgrid(lons, lats)
lon, lat = np.meshgrid(lons.values, lats.values)

# Criar a figura e os eixos
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plotar os dados de temperatura
plt.contourf(lon, lat, temperatura, 20, transform=ccrs.PlateCarree(), cmap='coolwarm')

# Adicionar limites do mapa
ax.coastlines()

# Adicionar grade de latitude e longitude
ax.gridlines()

# Adicionar título
plt.title('Mapa de Temperatura')

# Mostrar o plot
plt.show()