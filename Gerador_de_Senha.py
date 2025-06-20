# importei as bibliotecas
import random
import string

#Função para gerar as senhas
def gerar_senhas(gerador):
# montanto quais caracteristicas vai aparecer nessa senha
    quais_Caracteres= string.ascii_letters + string.digits + string.punctuation
    
    senha= ''.join (random.choice(quais_Caracteres) for _ in range(gerador))
    return senha
quantidade = int(input('quantos caracteres você deseja na sua senha:'))
senha_gerada= gerar_senhas(quantidade)
print(f'Senha gerada com Sucesso:_______{senha_gerada}________')

    