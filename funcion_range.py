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