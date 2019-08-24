import json
count=0
with open('2018-01-17-D3.json') as json_file:
    data = json.load(json_file)
    for p in data['acList']:
        print('Icao = '+str(p['Icao'])+' - Id = '+str(p['Id'])+' - Model = '+ p['Mdl']+' - Cou = '+ p['Cou']+' - Op = '+ p['Op']+' - From = '+ p['From']+' - To = '+ p['To'])
        count+=1
print('\nTotal Aircrafts = '+str(count))