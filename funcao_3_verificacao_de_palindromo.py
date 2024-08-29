"""
Exercício: Verificação de Palíndromo

Escreva uma função chamada eh_palindromo que receba uma string como parâmetro e
retorne True se a string for um palíndromo, e False caso contrário. Um palíndromo é
uma palavra, frase ou número que é lido da mesma forma de trás para frente,
desconsiderando espaços, pontuação e diferenças entre maiúsculas e minúsculas.

Exemplos de palíndromos:

    "radar"
    "A man a plan a canal Panama"
    "12321"

Tarefas:

    Implemente a função eh_palindromo que verifique se uma string é um palíndromo.
    A função deve ignorar espaços, pontuação e diferenças entre maiúsculas e minúsculas.

Dicas:

    Você pode usar a função str.lower() para converter a string para minúsculas.
    Use str.replace() para remover espaços e pontuação.
    Uma maneira simples de verificar se uma string é um palíndromo é compará-la
    com sua versão invertida (usando slicing, por exemplo).

"""
# Import da biblioteca string
import string


# Criação da função eh_palindromo
def eh_palindromo(texto):
    # deixando todas as letras minusculas com .lower()
    texto = texto.lower()

    # Removendo pontuações
    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, '')

    # Invertendo o texto
    texto_invertido = texto[::-1]

    # Verifica se é palindromo ou não
    return texto == texto_invertido


# Executando a função
print(eh_palindromo('Radar'))
print(eh_palindromo('Python'))
print(eh_palindromo('LOL'))


