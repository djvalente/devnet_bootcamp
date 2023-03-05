import requests

# Exemplo de chamada API (get) que retorna dados no formato JSON
get_url = 'https://swapi.dev/api/people/1'
get_headers = {"content-type": "application/json"}

r = requests.get(get_url,headers=get_headers)
json_data = r.json()
print(json_data)