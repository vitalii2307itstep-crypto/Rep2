import requests


class CurrencyConverter: #зберігає курс та проводить конверцію
    def __init__(self, rate):
        self.rate = rate

    def convert_to_usd(self, uah):
        return uah / self.rate


url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json" # сайт НБУ

response = requests.get(url) #надсилає запит та отримує відповідь від сервера
data = response.json() #перевіряє запити на мопилки

usd_rate = data[0]["rate"]

converter = CurrencyConverter(usd_rate)

uah = float(input("Enter the amount in hryvnias: "))

usd = converter.convert_to_usd(uah)

print(f"{uah} грн = {usd:.2f} USD")