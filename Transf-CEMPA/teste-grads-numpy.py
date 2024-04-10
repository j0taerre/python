import numpy as np
import os 

def read_ctl_file(ctl_file):
    ctl_info = {}
    with open(ctl_file, 'r') as file:
        lines = file.readlines()
        idx = 0 
        linha_lida = 0

        for line in lines:
            if linha_lida == idx:
                if line.strip():
                    if line.startswith('dset'):
                        ctl_info['data_file'] = line.split()[1]
                    elif line.startswith('undef'):
                        ctl_info['undef'] = float(line.split()[1])
                    elif line.startswith('title'):
                        ctl_info['title'] = line[1:]#line.split()[1:]
                    elif line.startswith('xdef'):
                        ctl_info['xdef'] = [float(val) for val in line.split()[3:]]
                    elif line.startswith('ydef'):
                        ctl_info['ydef'] = [float(val) for val in line.split()[3:]]
                    elif line.startswith('zdef'):
                        ctl_info['zdef'] = [float(val) for val in line.split()[3:]]
                    # Se os valores de zdef estiverem em uma linha diferente
                        next_line = lines[idx + 1]
                        ctl_info['zdef'].extend([float(val) for val in next_line.split()])
                        idx += 1  # Incrementando idx
                    elif line.startswith('tdef'):
                        ctl_info['tdef'] = line.split()[2:]
                    elif line.startswith('vars'):
                        num_vars = int(line.split()[1])
                        ctl_info['vars'] = {}
                        for _ in range(num_vars):
                            next_line = lines[idx + 1]
                            var_info = next_line.split()  #next_line.pop(0).split()
                            var_name = var_info[0]
                            var_levels = int(var_info[1])
                            var_missing_val = float(var_info[2])
                            var_desc = " ".join(var_info[3:])
                            ctl_info['vars'][var_name] = {
                                'levels': var_levels,
                                'missing_val': var_missing_val,
                                'description': var_desc
                            }
                            idx += 1  # Incrementando idx
                idx += 1  # Incrementando idx
                linha_lida += 1
            else:
                linha_lida += 1
    return ctl_info

def read_gra_file(data_file, undef, num_x, num_y, num_z, num_t):
    with open(data_file, 'rb') as file:
        # Lê os dados binários como uma matriz numpy
        data = np.fromfile(file, dtype=np.float32)
        
        # Substitui valores indefinidos
        data[data == undef] = np.nan
        
        # Verifica se o número de elementos é compatível com as dimensões fornecidas
        expected_num_elements = num_t * num_z * num_y * num_x
        if data.size != expected_num_elements:
            raise ValueError(f"O número de elementos nos dados ({data.size}) não corresponde ao esperado ({expected_num_elements})")
        
        # Ajusta o formato da matriz de acordo com as dimensões
        data = data.reshape(num_t, num_z, num_y, num_x)

    return data

# Caminho para os arquivos
path = os.getcwd()
os.chdir("d:\\temp\\")
path = os.getcwd()

# .ctl
#ctl_file = 'd:\\temp\\Go5km-A-2023-04-15-000000-g1.ctl'
ctl_file = path + "\\" + "Go5km-A-2023-04-15-000000-g1.ctl"


# Lê as informações do arquivo .ctl
ctl_info = read_ctl_file(ctl_file)

# Extrai as informações relevantes do arquivo .ctl
data_file = ctl_info['data_file']
undef_val = ctl_info['undef']
num_x = len(ctl_info['xdef'])
num_y = len(ctl_info['ydef'])
num_z = len(ctl_info['zdef'])
num_t = len(ctl_info['tdef'])

# Lê o arquivo .gra
if data_file[0] == '^': 
    data_file = path + "\\" +  data_file[1:]
else:
    data_file = path + "\\" +  data_file

data = read_gra_file(data_file, undef_val, num_x, num_y, num_z, num_t)

# Exemplo de como acessar os dados
# Supondo que você queira acessar a variável "TEMPC" (temperatura)
temperatura = data[:, :, :, :]

# Agora você pode processar e analisar os dados conforme necessário
