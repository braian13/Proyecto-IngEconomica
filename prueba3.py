import math

def anualidad_general(pago, tasa, n_periodos):
    """Calcula el valor presente de una anualidad general."""
    if tasa == 0:
        return pago * n_periodos
    else:
        return pago * ((1 - (1 + tasa) ** -n_periodos) / tasa)

def anualidad_anticipada(pago, tasa, n_periodos):
    """Calcula el valor presente de una anualidad general anticipada."""
    return anualidad_general(pago, tasa, n_periodos) * (1 + tasa)

def anualidad_diferida(pago, tasa, n_periodos, n_diferidos):
    """Calcula el valor presente de una anualidad diferida."""
    return anualidad_general(pago, tasa, n_periodos) / ((1 + tasa) ** n_diferidos)

def anualidad_vencida_futura(pago, tasa, n_periodos):
    """Calcula el valor futuro de una anualidad vencida."""
    if tasa == 0:
        return pago * n_periodos
    else:
        return pago * (((1 + tasa) ** n_periodos - 1) / tasa)

def anualidad_futura_anticipada(pago, tasa, n_periodos):
    """Calcula el valor futuro de una anualidad futura anticipada."""
    return anualidad_vencida_futura(pago, tasa, n_periodos) * (1 + tasa)






def anualidad_generalC(pago, tasa, n_periodos):
    """Calcula el valor presente de una anualidad general."""
    if tasa == 0:
        return pago * n_periodos
    else:
        return pago / ((1 - (1 + tasa) ** -n_periodos) / tasa)

def anualidad_anticipadaC(pago, tasa, n_periodos):
    """Calcula el valor presente de una anualidad general anticipada."""
    return anualidad_generalC(pago, tasa, n_periodos) / (1 + tasa)

def anualidad_diferidaC(pago, tasa, n_periodos, n_diferidos):
    """Calcula el valor presente de una anualidad diferida."""
    return anualidad_generalC(pago, tasa, n_periodos) * ((1 + tasa) ** n_diferidos)

def anualidad_vencida_futuraC(pago, tasa, n_periodos):
    """Calcula el valor futuro de una anualidad vencida."""
    if tasa == 0:
        return pago * n_periodos
    else:
        return pago / ((((1 + tasa) ** n_periodos )-1) / tasa)

def anualidad_futura_anticipadaC(pago, tasa, n_periodos):
    """Calcula el valor futuro de una anualidad futura anticipada."""
    return anualidad_vencida_futuraC(pago, tasa, n_periodos) / (1 + tasa)
# Ejemplo de uso
pago = 400000 # Pago periódico
tasa = 0.1255  # Tasa de interés por periodo
n_periodos = 9  # Número de periodos
n_diferidos = 3  # Número de periodos diferidos

print("Anualidad General:", anualidad_general(pago, tasa, n_periodos))
print("C Anualidad General:", anualidad_generalC(pago, tasa, n_periodos))
print("\n")

print("Anualidad General Anticipada:", anualidad_anticipada(pago, tasa, n_periodos))
print("C Anualidad General Anticipada:", anualidad_anticipadaC(pago, tasa, n_periodos))
print("\n")


print("Anualidad Diferida:", anualidad_diferida(pago, tasa, n_periodos, n_diferidos))
print("C Anualidad Diferida:", anualidad_diferidaC(pago, tasa, n_periodos, n_diferidos))
print("\n")


print("Anualidad Futura:", anualidad_vencida_futura(pago, tasa, n_periodos))
print("C Anualidad Futura:", anualidad_vencida_futuraC(pago, tasa, n_periodos))
print("\n")

print("Anualidad Futura Anticipada:", anualidad_futura_anticipada(pago, tasa, n_periodos))
print("C Anualidad Futura Anticipada:", anualidad_futura_anticipadaC(pago, tasa, n_periodos))
print("\n")
