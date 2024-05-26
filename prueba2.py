def menu():
    print("Seleccione la conversión de tasa de interés que desea realizar:")
    print("1. Convertir tasa nominal (J) a tasa efectiva (i)")
    print("2. Convertir tasa efectiva (i) a tasa nominal (J)")
    choice = int(input("Ingrese el número correspondiente: "))
    
    if choice == 1:
        print("Convertir tasa nominal (J) a tasa efectiva (i):")
        return 'J_to_i'
    elif choice == 2:
        print("Convertir tasa efectiva (i) a tasa nominal (J):")
        return 'i_to_J'
    else:
        raise ValueError("Opción no válida")

def seleccionar_periodo(tipo):
    print(f"Seleccione el periodo de la tasa {tipo}:")
    print("1. Mensual")
    print("2. Bimestral")
    print("3. Trimestral")
    print("4. Cuatrimestral")
    print("5. Semestral")
    periodo = int(input("Ingrese el número correspondiente: "))
    
    if periodo == 1:
        return 12  # Mensual
    elif periodo == 2:
        return 6  # Bimestral
    elif periodo == 3:
        return 4  # Trimestral
    elif periodo == 4:
        return 3  # Cuatrimestral
    elif periodo == 5:
        return 2  # Semestral
    else:
        raise ValueError("Opción de periodo no válida")

def seleccionar_tipo_tasa():
    print("Seleccione el tipo de tasa efectiva:")
    print("1. Normal")
    print("2. Anticipada")
    tipo = int(input("Ingrese el número correspondiente: "))
    
    if tipo == 1:
        return 'normal'
    elif tipo == 2:
        return 'anticipada'
    else:
        raise ValueError("Opción de tipo de tasa no válida")

def convertir_J_a_i(J, n_J, n_i, tipo_i):
    if tipo_i == 'normal':
        i_anual = (1 + J / n_J) ** n_J - 1
        i_convertida = (1 + i_anual) ** (1 / n_i) - 1
    elif tipo_i == 'anticipada':
        i_anual = (1 + J / n_J) ** n_J - 1
        i_convertida = ((1 + i_anual) ** (1 / n_i) - 1) / (1 + ((1 + i_anual) ** (1 / n_i) - 1))
    return i_convertida

def convertir_i_a_J(i, n_i, n_J):
    i_anual = (1 + i) ** n_i - 1
    J_convertida = n_J * ((1 + i_anual) ** (1 / n_J) - 1)
    return J_convertida

def periodo_nombre(n):
    if n == 12:
        return "mensual"
    elif n == 6:
        return "bimestral"
    elif n == 4:
        return "trimestral"
    elif n == 3:
        return "cuatrimestral"
    elif n == 2:
        return "semestral"
    else:
        return f"de {12/n} periodos anuales"

def menu_interes_compuesto():
    print("Seleccione el tipo de cálculo de interés compuesto que desea realizar:")
    print("1. Calcular monto futuro (S)")
    print("2. Calcular valor presente (P)")
    print("3. Calcular tasa de interés (i)")
    print("4. Calcular número de periodos (n)")
    choice = int(input("Ingrese el número correspondiente: "))
    
    return choice

def calcular_interes_compuesto(choice, P=None, S=None, i=None, n=None):
    if choice == 1:
        if P is None or i is None or n is None:
            raise ValueError("Faltan datos para calcular el monto futuro (S)")
        S = P * (1 + i) ** n
        print(f"El monto futuro (S) es: {S:.2f}")
    elif choice == 2:
        if S is None or i is None or n is None:
            raise ValueError("Faltan datos para calcular el valor presente (P)")
        P = S / (1 + i) ** n
        print(f"El valor presente (P) es: {P:.2f}")
    elif choice == 3:
        if P is None or S is None or n is None:
            raise ValueError("Faltan datos para calcular la tasa de interés (i)")
        i = (S / P) ** (1 / n) - 1
        print(f"La tasa de interés (i) es: {i * 100:.2f}%")
    elif choice == 4:
        if P is None or S is None or i is None:
            raise ValueError("Faltan datos para calcular el número de periodos (n)")
        import math
        n = math.log(S / P) / math.log(1 + i)
        print(f"El número de periodos (n) es: {n:.2f}")
    else:
        raise ValueError("Opción no válida")

def main():
    conversion = menu()
    if conversion == 'J_to_i':
        J = float(input("Ingrese la tasa nominal (J) como decimal (por ejemplo, 0.08 para 8%): "))
        n_J = seleccionar_periodo("nominal (J)")
        n_i = seleccionar_periodo("efectiva (i)")
        tipo_i = seleccionar_tipo_tasa()
        i = convertir_J_a_i(J, n_J, n_i, tipo_i)
        print(f"La tasa efectiva {tipo_i} {periodo_nombre(n_i)} es: {i * 100:.2f}%")
    elif conversion == 'i_to_J':
        i = float(input("Ingrese la tasa efectiva (i) como decimal (por ejemplo, 0.08 para 8%): "))
        n_i = seleccionar_periodo("efectiva (i)")
        n_J = seleccionar_periodo("nominal (J)")
        J = convertir_i_a_J(i, n_i, n_J)
        print(f"La tasa nominal {periodo_nombre(n_J)} es: {J * 100:.2f}%")
    
    opcion_interes_compuesto = menu_interes_compuesto()
    if opcion_interes_compuesto == 1:
        P = float(input("Ingrese el valor presente (P): "))
        n = int(input("Ingrese el número de periodos (n): "))
        calcular_interes_compuesto(opcion_interes_compuesto, P=P, i=i, n=n)
    elif opcion_interes_compuesto == 2:
        S = float(input("Ingrese el monto futuro (S): "))
        n = int(input("Ingrese el número de periodos (n): "))
        calcular_interes_compuesto(opcion_interes_compuesto, S=S, i=i, n=n)
    elif opcion_interes_compuesto == 3:
        P = float(input("Ingrese el valor presente (P): "))
        S = float(input("Ingrese el monto futuro (S): "))
        n = int(input("Ingrese el número de periodos (n): "))
        calcular_interes_compuesto(opcion_interes_compuesto, P=P, S=S, n=n)
    elif opcion_interes_compuesto == 4:
        P = float(input("Ingrese el valor presente (P): "))
        S = float(input("Ingrese el monto futuro (S): "))
        calcular_interes_compuesto(opcion_interes_compuesto, P=P, S=S, i=i)

if __name__ == "__main__":
    main()