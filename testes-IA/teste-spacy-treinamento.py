import spacy
import random
from spacy.training import Example

# Carregar o modelo de linguagem em português
nlp = spacy.blank("pt")

# Adicionar categorias personalizadas ao modelo
categorias = ["AGENTE_ENVOLVIDO", "ARMA_UTILIZADA", "LOCAL_INCIDENTE"]
for categoria in categorias:
    nlp.add_label(categoria)

# Definir o conjunto de dados anotado (substitua isso com seus próprios dados anotados)
dados_anotados = [
    ("No dia 10 de março de 2024, ocorreu um incidente na rua principal. Os agentes Silva e Souza foram envolvidos. Foi utilizada uma pistola no incidente.", 
     {"entities": [(42, 47, "AGENTE_ENVOLVIDO"), (48, 53, "AGENTE_ENVOLVIDO"), (116, 123, "ARMA_UTILIZADA"), (66, 79, "LOCAL_INCIDENTE")]}),
    # Adicione mais exemplos anotados aqui
]

# Função para treinar o modelo
def treinar_modelo(dados_anotados, n_iter=10):
    # Inicializar o otimizador
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    # Adicionar as categorias personalizadas ao ner
    for categoria in categorias:
        ner.add_label(categoria)

    # Preparar os dados de treinamento
    exemplos = []
    for texto, anotacoes in dados_anotados:
        exemplo = Example.from_dict(nlp.make_doc(texto), anotacoes)
        exemplos.append(exemplo)

    # Treinar o modelo
    for _ in range(n_iter):
        random.shuffle(exemplos)
        losses = {}
        for batch in spacy.util.minibatch(exemplos, size=2):
            nlp.update(batch, losses=losses)
        print("Losses:", losses)

# Treinar o modelo
treinar_modelo(dados_anotados)
