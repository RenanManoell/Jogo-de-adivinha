print('============================================================')
print("Bem vindo ao jogo maligno.")
print('============================================================')
print("")

Palavras = ['kiwi',
            'Tangerina',
            'Pitaia']
Letras = ['4','9','6']
Dicas = ['Fruto comestível, Actinidia deliciosa, com polpa verde, cuja pele marrom é coberta por uma pilosidade sedosa.',
         'Fruto de cor laranja e sabor cítrico, cuja casca desprende-se com facilidade dos gomos',
         'Fruto dessas plantas, geralmente comestível, de casca escamosa avermelhada, rosada ou amarelada e polpa esbranquiçada ou avermelhada, com pequenas sementes',
            ]
List_1 = list(Palavras)
List_2 = list(Letras)
List_3 = list(Dicas)


while True:
    print("")
    Resposta = input("Escolha entre 1, 2 ou 3, Boa sorte!: ")
    if str(Resposta) =='1' or str(Resposta) =='2' or str(Resposta) =='3':
        Resposta = int(Resposta)-1
        print("")
        print('============================================================')
        print('')
        print(f'A palavra secreta tem {List_2[Resposta]} letras.')
        print('E a dica secre é:')
        print(List_3[Resposta])
        print('')
        print('============================================================')
        print('')
        print("E você tem 6 chances para escrever a palavra.")
        print('')
        print('============================================================')
        print('')

        chanceusadas = 0
        palavra_secreta = List_1[Resposta]
        letra_acertada = ''
        letra_adivinhada = ''
        palavra_adivinhada = len(palavra_secreta)*"*"


        while int(chanceusadas) < 6:
            
            letra_digitada = input("Qual letra deseja colocar: ")
            if len(letra_digitada) >1:
                print("Digite apenas uma letra.")
                continue
            acertou = 0
            
            print('')

            if letra_digitada in palavra_secreta:
                letra_acertada += letra_digitada
                palavra_adivinhada = ""
                
                for letras in palavra_secreta:
                    if letras in letra_acertada:
                        palavra_adivinhada = palavra_adivinhada+letras
                    else:
                        palavra_adivinhada = palavra_adivinhada+"*"

                print(f'Parabens você acertou digitando "{letra_digitada}".')
                print (palavra_adivinhada)
                print('')
            else:
                print (palavra_adivinhada)
                print('Poxa... infelizmente essa letra não esta na palavra secreta.')
                print('Tente novamente.')
                print('')
                chanceusadas = chanceusadas+1

            if "*" in palavra_adivinhada:

                print(f'Ja se foram utilizadas {chanceusadas} chance, resta apenas {6-chanceusadas}.')
                
                print('')
                print('============================================================')
                print('')
            else:
                print("PARABENS VOCÊ CONSEGUIU ADIVINHAR A PALAVRA SECRETA.")
                print(f'"{palavra_adivinhada}" Era a palavra secreta, você é bom nisso.')
                print("Até a proxima.")
                exit()
    else:
        print("Digite entre '1,2 ou 3'.")
        continue






    



