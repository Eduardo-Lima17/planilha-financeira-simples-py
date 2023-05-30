from time import sleep

import datetime

#Inicialização de variáveis

saldoInicial = 0
salario = 0
aluguel = 0
horas_extras = 0
decimo_terceiro = 0
ferias = 0
ticket = 0

despesas = 0
saldoFinal = 0

hora_atual = datetime.datetime.now()

pergunta = 'S'

while True:
    # Entrada de dados
    try:
        print('\nP R E E N C H I M E N T O  D E  R E C E I T A S  E  D E S P E S A S')
        print('-'*68)

        saldoInicial = float(input('\nSaldo Inicial...... R$ '))
        salario = float(input('Salário...... R$ '))
        aluguel = float(input('Aluguel...... R$ '))
        horas_extras = float(input('Horas Extras...... R$ '))
        decimo_terceiro = float(input('Décimo 13° Salário...... R$ '))
        ferias = float(input('Férias...... R$ '))
        ticket = float(input('Ticket...... R$ '))
        despesas = float(input('Despesas...... R$ '))

        # Cálculo

        saldoFinal = saldoInicial + salario + aluguel + horas_extras + decimo_terceiro + ferias + ticket - despesas

        # Saída de resultados
        print('\nI N F O R M A Ç Õ E S  G E R A I S')
        print('-'*48)

        print('\nSaldo Inicial R$ ', saldoInicial)
        print('Salário...... R$ ', salario)
        print('Aluguel...... R$ ', aluguel)
        print('Horas Extras...... R$ ', horas_extras)
        print('Décimo 13º Salário...... R$ ', decimo_terceiro)
        print('Férias...... R$ ', ferias)
        print('Ticket...... R$ ', ticket)
        print('Despesas...... R$ ', despesas)
        print('\nSaldo Final R$ ', saldoFinal)
        print('\nÚltimo acesso', hora_atual)

        pergunta = str(input('\nDeseja continuar? [S/N]: ')).upper()

        if pergunta == 'S':
            print('\nCONTINUE COM O PREENCHIMENTO')

        else:
            print('Saindo...')
            sleep(2)
            print('\nPlanilha finalizada! Até mais.\n')
            break
    except:
        print('\nInforme a informação correta! Tente de novo.')
    sleep(2)
