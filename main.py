from typing import List
from datetime import date

class Device:
    def __init__(self, name: str, price: int, tdp: int, btc_daily_income: float):
        self.name = name
        self.price = price
        self.tdp = tdp
        self.btc_daily_income = btc_daily_income

class PurchasingLedger:
    """仕入台帳
    """
    def __init__(self):
        self.records = []
    
    def add(self, buy_date: date, compositions: List[Device]):
        rec = {
            "date": buy_date,
            "price": sum([device.price for device in compositions]),
            "tdp": sum([device.tdp for device in compositions]),
            "btc_income": sum([device.btc_daily_income for device in compositions])
        }
        self.records.append(rec)

class DeviceList:
    def __init__(self):
        self.devices = {}
    
    def add(self, device_name):
        if not (device_name in self.devices):
            self.devices[device_name] = 0
        self.devices[device_name] += 1

if __name__ == "__main__":
    devices = {
        "a4000": Device("a4000", 150000, 123, 0.00007629),
        "a5000": Device("a5000", 281790, 222, 0.00013097),
        "base": Device("base", 0, 100, 0),
    }

    purchasing_ledger = PurchasingLedger()
    purchasing_ledger.add(date(2022,1,1), [devices["a5000"]] * 3 + [devices["base"]])
    
    print(purchasing_ledger.records)
