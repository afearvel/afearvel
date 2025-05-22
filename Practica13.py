import numpy as np

arreglo = np.array([1, 2, 3, "4", 5])
lista = [1, "hola", True, 3.2, 5]
tuplaNp = tuple(arreglo)
tuplaLista = tuple(lista)
conjuntoNp = set(arreglo)
conjuntoLista = set(lista)
diccionario = {"cadena": "Juan", 
               "entero": 24, 
               "Booleano": True,
               "decimal": 3.2,
               "entero": 1}
print(tuplaNp)
print(tuplaLista)
print(conjuntoNp)
print(conjuntoLista)
print(diccionario)

lista.append(32)
print(lista)
lista.insert(1,12)
print(lista)
lista.extend([2,"hola"])
print(lista)
lista.remove(2)
print(lista)
lista.count(2)
print(lista)
lista.pop(2)
print(lista)

dic = {"x": "equis", "y": "ye", "z": "zeta"}
print(dic)
dic = dict(x="equis", y="ye", z="zeta")
print(dic)
print(dic["x"])
print(dic.get("x"))
print(dic.get("a"))

dic["x"] = "equisde"
print(dic)
dic["a"] = "a"
print(dic)
del dic["a"]
print(dic)
x = dic.pop("x")
print(x)
print("y" in dic)
print(dic.values())
p = dic.items()
print(p)
print(dic.keys())
print(dic.update({"x": "equis"}))
print(dic.clear())

a = {1, 2, 3}
b = {3, 4, 5}

union = a.union(b)
print("Unión:", union)

interseccion = a.intersection(b)
print("Intersección:", interseccion)

diferencia = a.difference(b)
print("Diferencia:", diferencia)
diferenciaMenos = b-a
print("Diferencia menos:", diferenciaMenos)

diferenciaSimetrica = a.symmetric_difference(b)
print("Diferencia simétrica:", diferenciaSimetrica)
diferenciaExpresion = a ^ b
print("Diferencia simétrica expresion:", diferenciaExpresion)

a = {1,2,3}
b = {1,2,3,4,5}
c = {}
print(type(c))
subconjunto = a.issubset(b)
print("Subconjunto:", subconjunto)

superconjunto = b.issuperset(a)
print("Superconjunto:", superconjunto)

a= {1, 2, 3}
b= {4, 5, 6}
disjunto = a.isdisjoint(b)
print("Disjunto:", disjunto)

a = {1, 2, 3}
e = a.copy()
print("Copia de a:", e)

al = len(a)
print("Longitud de a:", al)
print(a.clear())



conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.add(6)  
conjunto.add(3)  
conjunto.remove(2)
conjunto.remove(8)
conjunto.discard(7)
print(conjunto)
print(3 in conjunto) 
print(7 in conjunto)
