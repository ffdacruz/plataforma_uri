soma_nota = 0 
quantidade_valores = 0
opcao = 1

while opcao != 2:
    nota = float(input())
  
    if nota >= 0.0 and nota <= 10:
        soma_nota += nota
        quantidade_valores += 1 

        if quantidade_valores == 2:
      
            print('media = {0:.2f}'.format(soma_nota/2))
            quantidade_valores = 0 
            soma_nota = 0

            while opcao != 2:
                print('novo calculo (1-sim 2-nao)')
                opcao = int(input())
                if opcao == 2:
                    break
                elif opcao == 1:
                    break  
    else:
        print('nota invalida')