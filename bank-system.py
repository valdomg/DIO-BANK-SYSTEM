operacoes_lista = []
quantidade_saques = 0
begin_operations = True



#Laço para repetição de operações
while begin_operations:
    saldo = float(input('Informe o saldo da conta:'))

    if saldo < 0:
        print('Saldo negativo, informe novamente o valor!')

    else:
        operacoes_lista.append(f'Saldo inicial de R${saldo} em conta')
        opc = None
        while opc != 4:

            opc = int(input('''Informe a operação que deseja realizar

    [1] - SAQUE
    [2] - DEPÓSITO
    [3] - EXTRATO
    [4] - Sair

    : '''))
            print()
            
            if opc == 1:
                #parei
                continuar_saque = True

                if quantidade_saques == 3:
                    print('Máximo de saques diáiros realizados. \n')     

                else:
                    while (continuar_saque == True) and (quantidade_saques <= 2):
                        print('Informe a quantia para saque ou digite 0 para voltar ao menu')
                        saque = float(input('Digite: '))
                        
                        if saque < 0:
                            print('Valor inválido, por favor tente novamente... \n')
                            operacoes_lista.append('Tentativa de saque sem êxito')
                            
                        elif saque == 0:
                            break

                        elif saque >= 500:
                            print('Limite de saque atingido, tente novamente \n',)
                            
                        elif saque > saldo:
                            print('Saque maior que saldo em conta. Por favor tente novamente \n')
                            operacoes_lista.append('Tentativa de saque sem êxito')

                        elif saque <= saldo:
                            print(f'Saque de R${saque:.2f} realizado com sucesso \n')
                            saldo -= saque
                            operacoes_lista.append(f'Saque realizado com êxito de R${saque:.2f}. Saldo restante de R${saldo:.2f}')
                            quantidade_saques += 1
                            continuar_saque = False

                    
            elif opc == 2:
                continuar_deposito = True
                while (continuar_deposito == True):

                    print('Digite a quantia a ser depositada ou digite 0 para voltar ao menu')
                    deposito = float(input('Digite: '))

                    if deposito < 0:
                        print('Valor não depositável, tente novamente.\n')
                        
                    elif deposito == 0:
                        break

                    else:
                        saldo += deposito
                        print(f'Depósito de R${deposito:.2f} realizado com sucesso! \n')
                        operacoes_lista.append(f'Depósito de R${deposito:.2f} realizado. Saldo disponível R${saldo:.2f}')
                        continuar_deposito = False
       

            elif opc == 3:
                print()
                for operacoes in operacoes_lista:
                    print(operacoes)
                print()
                print(f'Saldo Atual: R${saldo:.2f}')
                print(f'Quantidade de saques realizados: {quantidade_saques} \n')

            elif opc == 4:
                    begin_operations = False
                    break
            
            else:
                print('Opçao inválida\n')

    
        
