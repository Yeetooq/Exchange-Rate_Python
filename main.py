import currencyapicom
from datetime import datetime

client = currencyapicom.Client('токен с сайта https://currencyapi.com/')
result = client.latest()

# Парсим строку времени в объект datetime
last_updated = datetime.fromisoformat(result['meta']['last_updated_at'])

# Форматируем объект datetime в нужный формат
formatted_time = last_updated.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_time)
valyuta = input('Введите валюту:')
print(result['data'][valyuta]['value'])

