import requests

LOGIN = "lyudamilasmirnova7777@gmail.com"
PASSWORD = "HHVtsS89V!5Juqy"
COMPANY_ID = "c98a5fcf-8b22-4acd-8cc1-8e145d17ab9c"

url = "https://yougile.com"
body = {
    "login": LOGIN,
    "password": PASSWORD,
    "companyId": COMPANY_ID
}

response = requests.post(url, json=body)
print("СТАТУС ОТВЕТА:", response.status_code)
print("ОТВЕТ СЕРВЕРА:", response.text)
