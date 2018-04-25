#!/usr/bin/python

op=str()
print()
date = str(input('Entre com a data (dd/MM/yyyy HH24:mi): '))
print()
while op!=str("+") and op!=str("-"):
    op = str(input('Entre com a operação desejada (+ ou -): '))    
    if op!=str("+") and op!=str("-"):
        print()
        print('Erro: Favor digitar um sinal válido (+ ou -)')
        print()
print()
value = int(input('Entre com a quantidade de minutos: '))
print()

def change_date(date,op,value):
    #Aqui eu separo a data em partes, dia, mes, ano, horas e minutos.
    day=int(date[0:2])
    month=int(date[3:5])
    year=int(date[6:10])
    hour=int(date[11:13])
    minute=int(date[14:16])

    #Aqui eu descubro quantos dias, horas e minutos precisam ser incrementados ou decrementados.
    years = int(value/365/1440)
    months = int(value/30/1440)
    days = int(value/1440)
    hours = int(value%1440/60)
    minutes = int(value%60)

    #Aqui exibe a quantidade de tempo que precisa ser incrementada ou decrementada.
    print('Esta é a quantidade de dias, horas e minutos que será somada ou subtraida da data informada inicialmente, dependendo da opção que você escolheu')
    print (days,'Dias',hours,'Horas',minutes,'Minutos')

    #Aqui eu defino qual a quantidade máxima de dias que o mês inicial possui.
    #Em seguida vou controlando a quantidade de dias a ser decrementada pela variavel days_left.
    #Vou somando os dias na variavel day e verificando se o mês tem 28, 30 ou 31 dias.
    #Quando a variavel day alcança o limite da variavel max_month_days é incrementado em 1 a variavel month.
    #Mas se a variavel month já tiver o valor 12, então a variável month recebe o valor 1 e então incrementa a variavel year em 1.
    max_month_days=month
    days_left=days
    while days_left>0:
        if month==1:
            max_month_days_before=31
            max_month_days=31
        elif month==2:
            max_month_days_before=31
            max_month_days=28
        elif month==3:
            max_month_days_before=28
            max_month_days=31
        elif month==4:
            max_month_days_before=31
            max_month_days=30
        elif month==5:
            max_month_days_before=30
            max_month_days=31
        elif month==6:
            max_month_days_before=31
            max_month_days=30
        elif month==7:
            max_month_days_before=30
            max_month_days=31
        elif month==8:
            max_month_days_before=31
            max_month_days=31
        elif month==9:
            max_month_days_before=31
            max_month_days=30
        elif month==10:
            max_month_days_before=30
            max_month_days=31
        elif month==11:
            max_month_days_before=31
            max_month_days=30
        elif month==12:
            max_month_days_before=30
            max_month_days=31
            break
        else:
            print('erro')
            
        if op==str('+'):
            if day<max_month_days:
                day+=1
                days_left-=1
            else:
                day=1
                days_left-=1
                if month<12:
                    month+=1
                else:
                    month=1
                    year+=1
            #Neste ponto ajusta-se as horas e minutos.
            if (hour+hours)>24 and days_left==0:
                hour=(hour+hours)%24
                day+=1

#Aqui inicia o calculo para decrementar dias, horas e minutos.
        if op==str('-'):
            if day<=max_month_days and day>1:
                day-=1
                days_left-=1
            else:
                day=max_month_days_before              
                days_left-=1
                if month>1:
                    month-=1
                else:
                    month=12
                    year-=1

    #Neste ponto ajusta-se as horas e minutos.
            if (hour-hours)>0 and days_left==0:
                hour=(hour-hours)
                if minutes>0:
                    hour-=1
                    minutes=60-minutes

    print()
    #Aqui é exibido o resultado da data inicial + ou - a quantidade em minutos, dependendo da opção escolhida (+ ou -).
    #Mostrando qual data será após a quantidade de minutos informada.
    print('Data atualizada:',day,'/',month,'/',year,hour,':',minutes)
    print()

    return('Data atualizada:',day,'/',month,'/',year,hour,':',minutes)    

change_date(date,op,value)   





    