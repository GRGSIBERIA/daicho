
class 装置:
    def __init__(self, price: int, tdp: int, btc_daily_income: float):
        self.price = price
        self.tdb = tdp
        self.btc_daily_income = btc_daily_income

class 仕入台帳:
    def __init__(self):
        records = []
    
    def add(self, devices):
        pass

if __name__ == "__main__":
    devices = {
        "a4000": 装置(150000, 123, 0.00007629),
        "a5000": 装置(281790, 222, 0.00013097)
    }
