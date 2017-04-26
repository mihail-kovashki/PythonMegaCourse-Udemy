def convert(celsius):
    if celsius<-273.15 :
        return "Input lower than minimum"
    else:
        fahrenheit = celsius*9/5+32
        return fahrenheit

temperatures = [10, -20, -289, 100]

for t in temperatures:
    print(convert(t)) 