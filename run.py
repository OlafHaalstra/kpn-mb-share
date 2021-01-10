import requests
from decouple import config, Csv

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
NUMBER = config("NUMBER")
SC_SERVICE_TOKEN = config("SC_SERVICE_TOKEN")

MBS = config("MBS", cast=Csv(int))
NUMBERS = config("NUMBERS", cast=Csv(str))

print("Sending MBs")

session = requests.Session()

url = "https://account.kpn.com/api/cigateway/v1/login"

payload = 'username={}&password={}&grant_type=password&response_type=token'.format(EMAIL, PASSWORD)
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = session.request("POST", url, headers=headers, data = payload)

csrf = response.headers['Csrf-session-key']
cookie = response.headers['Set-cookie']

url = "https://mijn.kpn.com/api/v5/?method=kpn.account.dataTransfer&sc_service_token={}".format(SC_SERVICE_TOKEN)

for n,m in zip(NUMBERS, MBS):
    payload = 'number={}&memberId={}&productId={}'.format(NUMBER, n, m)
    headers = {
    'CSRF-Session-Key': csrf,
    'Cookie': cookie,
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = session.request("POST", url, headers=headers, data = payload)

print("MBs sent, see you next month.")