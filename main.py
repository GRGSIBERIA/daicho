
class Device:
    def __init__(self, price: int, tdp: int, btc_daily_income: float):
        self.price = price
        self.tdb = tdp
        self.btc_daily_income = btc_daily_income

if __name__ == "__main__":
    devices = {
        "a4000": Device(150000, 123, 0.00007629),
        "a5000": Device(281790, 222, 0.00013097)
    }
