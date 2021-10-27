import requests


class BeelineAPI():

    @staticmethod
    def get_token(phone_number: str, password: str) -> str:
        r = requests.get(f'https://my.beeline.ru/api/1.0/auth?login={phone_number}&password={password}')
        if r.ok:
            return r.json()['token']

    @staticmethod
    def get_balance(phone_number: str, token: str) -> float:
        r = requests.get(f'https://my.beeline.ru/api/1.0/info/prepaidBalance?ctn={phone_number}&token={token}')
        if r.ok:
            return r.json()['balance']
