#Estadísticas del Covid-19 en Venezuela Summary
import requests
import json
if __name__ == '__main__':
    url = 'https://covid19.patria.org.ve/api/v1/summary'
    response = requests.get(url)

    if response.status_code == 200:

        response_json = response.json() 
        Confirmed = response_json['Confirmed']
        print('Cocid-19 en Venezuela')       
        print()
        
        print('Casos Positivos',Confirmed['Count'])       
        
        ByGender = Confirmed['ByGender']
        print('Masculino',ByGender['male'])
        print('Femenino',ByGender['female'])
        
        Active = response_json['Active']
        print('Activos',Active['Count'])
        
        Recovered = response_json['Recovered']
        print('Recuperados',Recovered['Count'])
        
        Deaths = response_json['Deaths']
        print('Fallecidos',Deaths['Count'])