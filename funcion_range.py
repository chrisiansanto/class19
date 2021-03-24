print("Ejercicio 1")
for x in range(10):
    print(x,end=" ")
print("Ejercicio 2")
for x in range (100,200):
    print(x,end=" ")
print("Ejercicio 3")
for x in range(5,23,3):
    print(x,end=" ")
print("Ejercicio 4")
n=int(input("Numero: "))
for x in range(n, n*2):
    print(x, end=" ")
print("Ejercicio 5")
c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
   numero=int(input("Número: "))
   total+=numero
print("Total de la suma:", total, end=" ")
print("Ejercicio 6")
frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x, end=" ")
print("Ejercicio 7")
S = 0
for x in range(0, 101, 1):
    S += x
    print(x,end=" ")
print("La sumatoria total es ", S, end=" ")
print("Ejercicio 8")
total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total, end=" ")
print("Ejercicio 9")
total=0
for i in range(101):
    if i %3 == 0:
        total=total+i
print("Sumatoria de los múltiplos de 3:", total, end=" ")
print("Ejercicio 10")
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f, end=" ")