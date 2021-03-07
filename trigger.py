import requests

ngrok_url = ' http://e96375db0785.ngrok.io'
end_point = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(end_point, json={})
print(r.text)