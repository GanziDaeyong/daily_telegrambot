import requests


def get_coin_prices():
    solana_url = "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=KRW"
    matic_url = "https://min-api.cryptocompare.com/data/price?fsym=MATIC&tsyms=KRW"
    solana = (((requests.get(solana_url)).content).decode())[7:-1]
    matic = (((requests.get(matic_url)).content).decode())[7:-1]
    res = f"솔라나 {solana} / 폴리곤 {matic}"
    return res
