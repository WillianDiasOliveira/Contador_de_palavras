from contador import contar_palavras

frase = input("Digite uma frase: ").strip() #remove os espaços na frase.
if not frase:
    print("Error: Nenhuma frase foi digitada.") #Caso coloque uma frase invalida. como: só espaços ou caracteres. mostra a mensagem de erro.
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de Palavras: ")
        for palavra, quantidade in resultado.items():
            print(f"{palavra} : {quantidade}")
        else:
            print(f"Nenhuma palavra válida foi encontrada.")

# Código Aprimorado













#from contador import contar_palavras

#frase = input('Digite uma frase: ')
#quantidade = contar_palavras(frase) 
#print(f'A frase tem {quantidade} palavras.')

# código principal