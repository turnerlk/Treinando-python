import requests

for id in range(1,51): # numero de ID a ser testado

    # url a ser testada
    url = f'http://nahamstore-2020-dev.nahamstore.thm/api/customers/?customer_id={id}' # id -> onde is id vão ser testados,
    
    r = requests.get(url)
    
    #if len(r.text) > 22:
    
    if r.status_code != 404: # vai ignorar os status 404.
        print(r.text)
