#Estadísticas del Covid-19 en Venezuela
import requests
import json
if __name__ == '__main__':
    url = 'https://covid19.patria.org.ve/api/v1/summary'
    response = requests.get(url)

    if response.status_code == 200:

        response_json = response.json() 
        Confirmed = response_json['Confirmed']
        print('Confirmados',Confirmed['Count'])
        
        ByGender = Confirmed['ByGender']
        ByState = Confirmed['ByState']
        print('Record Por Estado')
        suma=0
        for x in ByState:
            print(f'{x:>20}:', ByState[x])
            suma += ByState[x]
        print()
        print('Total hasta la fecha',suma)    
               
        Deaths = response_json['Deaths']
        print('Masculino',ByGender['male'])
        print('Femenino',ByGender['female'])
        print('Fallecidos',Deaths['Count'])