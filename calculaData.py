#!/usr/bin/python

date = str(input('Entre com a data (dd/MM/yyyy HH24:mi): '))
op = str(input('Entre com a operação desejada (+ ou -): '))
value = int(input('Entre com a quantidade de minutos: '))

days_jan = 31
days_fev = 28
days_mar = 31
days_apr = 30
days_may = 31
days_jun = 30
days_jul = 31
days_aug = 31
days_sep = 30
days_oct = 31
days_nov = 30
days_dec = 31

def change_date(date,op,value):
    #Aqui eu separo a data em partes, dia, mes, ano, horas e minutos
    day=int(date[0:2])
    month=int(date[3:5])
    year=int(date[6:10])
    hour=int(date[11:13])
    minute=int(date[14:16])

    #Aqui eu descubro quantos anos, meses, dias, horas e minutos precisam ser incrementados ou decrementados
    years = int(value/365/1440)
    months = int(value/30/1440)
    days = int(value/1440)
    hours = int(value%1440/60)
    minutes = int(value%60)
    #Aqui exibe a quantidade de tempo que precisa ser incrementada ou decrementada
    print (days,'Dias',hours,'Horas',minutes,'Minutos')

    days_left=days
    while days_left>0:
        if day<30:
            day+=1
            days_left-=1
        else:
            day=1
            days_left-=1
            month+=1

    print('mes',month)



    print('Data atualizada:',day,'/',month,'/',year,hour,':',minute)

change_date(date,op,value)   





    #while minutes>0:
    #    minute+=minutes  
    #    minutes=0        
    #    if hour < 23:
    #        hour+=1
    #    else:
    #        hour=0
    #        day+=1
    #     
    #    #print('resultado do minute',minute)
    #
    #    while hours>0:
    #        hour+=hours
    #        if hour>=23:
    #            hour=hour%24              
    #            hours=0
    #            if day<30:
    #                day+=1
    #            else:
    #                day=1
    #                month+=1
    #    #print('resultado do hours',hour)

        #while days>0:
        #    day+=days
        #    print('resultado day+=days',day)
        #    if day>=30:
        #        day=day%30
        #        month+=1
        #        days=0
        #days=0
                
        #print('resultado do days',day)

        #while months>0:
        #    month+=months
        #    if month>=12:
        #        month=months%12
        #        months=0
        #        year+=1
        #print('resultado do months',month)