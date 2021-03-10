import requests

ngrok_url = 'http://9938085ae0b4.ngrok.io'
end_point = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(end_point, json={})
print(r.text)