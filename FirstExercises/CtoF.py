#exercise 3


def convert(celsius):
    if celsius<-273.15 :
        return "Input lower than minimum"
    else:
        fahrenheit = celsius*9/5+32
        return fahrenheit

print(convert(-300))