import math

def anualidad_general(pago, tasa, n_periodos, opcion):
    """Calcula el valor presente o futuro de una anualidad general."""
    if opcion.lower() == 's':
        if tasa == 0:
            return pago * n_periodos
        else:
            return pago * (((1 + tasa) ** n_periodos - 1) / tasa)
    elif opcion.lower() == 'a':
        if tasa == 0:
            return pago * n_periodos
        else:
            return pago * ((1 - (1 + tasa) ** -n_periodos) / tasa)
    else:
        return "Opción no válida."

def anualidad_anticipada(pago, tasa, n_periodos, opcion):
    """Calcula el valor presente o futuro de una anualidad general anticipada."""
    return anualidad_general(pago, tasa, n_periodos, opcion) * (1 + tasa)

def anualidad_diferida(pago, tasa, n_periodos, n_diferidos, opcion):
    """Calcula el valor presente o futuro de una anualidad diferida."""
    return anualidad_general(pago, tasa, n_periodos, opcion) / ((1 + tasa) ** n_diferidos)

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione la opción:")
    print("S - Calcular Valor Futuro")
    print("A - Calcular Cuota")

# Ejemplo de uso
pago = 400000  # Pago periódico
tasa = 0.1255  # Tasa de interés por periodo
n_periodos = 9  # Número de periodos
n_diferidos = 3  # Número de periodos diferidos

mostrar_menu()
opcion = input("Opción: ")

if opcion.lower() in ['s', 'a']:
    print("Anualidad General:", anualidad_general(pago, tasa, n_periodos, opcion))
    print("Anualidad General Anticipada:", anualidad_anticipada(pago, tasa, n_periodos, opcion))
    print("Anualidad Diferida:", anualidad_diferida(pago, tasa, n_periodos, n_diferidos, opcion))
else:
    print("Opción no válida.")