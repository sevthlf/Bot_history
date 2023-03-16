from settings import token
import requests

base_url = 'https://api.telegram.org/bot'
base = requests.get(f'{base_url}{token}/getUpdates')
print(base.json())

message = base.json()['result'][-1]['message']['text']
print(message)
user_id = base.json()['result'][-1]['message']['chat']['id']
print(user_id)

# Here i'm using Telegram API for send message to user
requests.get(f'{base_url}{token}/sendMessage?chat_id={user_id}&text={message}')
