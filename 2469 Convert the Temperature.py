def convertTemperature(celsius: float) -> list[float]:
    f=celsius*1.8+32.00
    k=celsius+273.15
    return [k,f]