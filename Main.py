""""
========================== PIG LATIN =============================
Pig Latin é um jogo linguístico, em que você move a primeira letra
da palavra para o final e adiciona "ay".
Então, "Palavra" se torna "alavrapay".
==================================================================
"""

pyg = "ay"
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():    # nesse if verificamos se a palavra informada nao eh vazia e se nao contem numeros
    word = original.lower()                     # aqui mudamos as letras da palavra para minusculas
    first = word[0]                             # aqui armazenamos a primeira letra da palavra
    new_word = word[1:len(word)] + first + pyg  # aqui armazenamos o resultado final (palavra sem a primeira letra + primeira letra + "ay")
    print(new_word)
else:
    print("error")                              # nesse else avisamos que os valores informados estao errados