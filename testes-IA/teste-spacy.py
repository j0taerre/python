import spacy

# Carregar o modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

# Função para extrair informações de um BO
def extrair_informacoes_bo(texto):
    # Processar o texto usando o modelo de linguagem
    doc = nlp(texto)
    
    # Lista para armazenar as informações extraídas
    informacoes = {
        "agentes_envolvidos": [],
        "armas_utilizadas": [],
        "local_incidente": ""
    }
    
    # Iterar sobre as entidades nomeadas no documento
    for entidade in doc.ents:
        # Verificar se a entidade é um agente envolvido
        if entidade.label_ == "AGENTE_ENVOLVIDO":
            informacoes["agentes_envolvidos"].append(entidade.text)
        # Verificar se a entidade é uma arma utilizada
        elif entidade.label_ == "ARMA_UTILIZADA":
            informacoes["armas_utilizadas"].append(entidade.text)
        # Verificar se a entidade é o local do incidente
        elif entidade.label_ == "LOCAL_INCIDENTE":
            informacoes["local_incidente"] = entidade.text
    
    return informacoes

# Exemplo de uso
texto_bo = """
No dia 10 de março de 2024, ocorreu um incidente na rua principal. 
Os agentes Silva e Souza foram envolvidos. Foi utilizada uma pistola no incidente.
"""

informacoes_extraidas = extrair_informacoes_bo(texto_bo)
print("Agentes envolvidos:", informacoes_extraidas["agentes_envolvidos"])
print("Armas utilizadas:", informacoes_extraidas["armas_utilizadas"])
print("Local do incidente:", informacoes_extraidas["local_incidente"])
