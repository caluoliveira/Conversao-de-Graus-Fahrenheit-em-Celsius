#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre em graus Celsius.
#Fórumula = (C-32)/1.8
temperatura_f=float(input("Informe a temperatura em FAHRENHEIT: \n")) #Em se tratando de temperatura, é preciso usar a conversão do input (strint) para float.
temperatura_c=(temperatura_f-32)/1.8
print("A temperatura", temperatura_f, "FAHRENHEIT equivale a " "%.2f" % temperatura_c, "graus CELSIUS")
