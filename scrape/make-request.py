import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
}

res = requests.get(
    'https://sports.coral.co.uk/competitions/football/football-england/premier-league',
    headers=headers)

print(res.status_code)
