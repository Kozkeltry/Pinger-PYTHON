import requests

try:
    r = requests.get(input("Введите сайт: "), headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
    if r.status_code == 200:
        print("Сайт активен")
    else:
        print(f"Сайт вернул ошибку: {r.status_code}")
except requests.exceptions.RequestException:
    print("Произошла ошибка!")