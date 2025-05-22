from enum import Enum

class Dias(Enum):
    Lunes = "Lunes"
    Martes = "Martes"
    Miercoles = "Miércoles"
    Jueves = "Jueves"
    Viernes = "Viernes"
    Sabado = "Sábado"
    Domingo = "Domingo"


def verificar_dia(dia):
    try:
        if not isinstance(dia, str):
            raise TypeError("Se esperaba un valor de tipo string")

        dia = dia.capitalize()

        if dia in [d.value for d in Dias]:
            print(f"Día válido: {dia}")
        else:
            raise ValueError("El día ingresado no es válido. Debe ser un día de la semana.")

    except TypeError as e:
        print(f"Error de tipo: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Ejecución finalizada.")

verificar_dia("Lunes")
verificar_dia("domingo")
verificar_dia("Feriado")
verificar_dia(123)
