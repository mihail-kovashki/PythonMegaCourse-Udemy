def convert(celsius):
    if celsius<-273.15 :
        print("Input lower than minimum")
    else:
        fahrenheit = celsius*9/5+32
        file.write(str(fahrenheit)+"\n")

temperatures = [10, -20, -289, 100]

with open("exercise5.txt", "w") as file:
    for t in temperatures:
        convert(t)