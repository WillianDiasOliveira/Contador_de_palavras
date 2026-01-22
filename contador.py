def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ".,!?:;\"'()[]{}" # todos os caracteres que não queremos ser considerados nesse momento.
    for char in caracteres:
        texto = texto.replace(char, "") 
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():       # Remove os espaços na frase.
        return {}               # se tiver uma palavra invalida, vai adicionar nesse dicionário.
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1 # feito para ver se existe mais de uma palavra com o mesmo nome.
    return contagem
# Código aprimorado 





#frase = input('Digite uma frase: ')
#palavras = frase.split()
#print(len(palavras))                
#print(palavras)

# código principal 
