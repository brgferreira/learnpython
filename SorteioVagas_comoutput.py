
#%%
#Created by @Bruno Gabriel -
# Github: https://github.com/brgferreira Linkedin https://www.linkedin.com/in/bruno-gabriel-ferreira-barros-31039423/

import random
import sys

leitura_arquivo_aps = open("lista_unidades.txt","r")
lista_aps = leitura_arquivo_aps.read().splitlines()
leitura_arquivo_aps.close()

leitura_arquivo_vagas = open("lista_numero-de-vagas.txt","r")
lista_vagas = leitura_arquivo_vagas.read().splitlines()
leitura_arquivo_vagas.close()

text_file = open('Resultado_Sorteio-de-Vagas.txt', 'w')

for ap_escolhido in lista_aps:
    
    vaga_escolhida = random.choice(lista_vagas)
    text_file.write("\nApartamento -> {} <-- Vaga --> {}.".format(ap_escolhido, vaga_escolhida))
lista_vagas.remove(vaga_escolhida)

text_file.write('\n    Sorteio Finalizado!')


# %%
