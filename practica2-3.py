from math import pi, tan

class Figura:
    
    def areaFig(ladoLargo, numLado):
        area = (1 / 4) * numLado * (ladoLargo ** 2) / tan(pi / numLado)
        return area

    def perimetroFig(ladoLargo, numLado):
        perimetro = ladoLargo * numLado
        return perimetro

numLado = int(input("ingresa la cantidad de lados en la figura: "))
ladoLargo = float(input("ingresa la medida del lado: "))

if numLado <= 2 or ladoLargo <=0:
    print("Figura no valida")
else:
    print(f"area de la figura: {Figura.areaFig(ladoLargo, numLado)}")
    print(f"perímetro de la figura: {Figura.perimetroFig(ladoLargo, numLado)}")

