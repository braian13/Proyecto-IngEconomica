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

def convertir_J_a_i(J, n_J, n_i):
    i_anual = (1 + J / n_J) ** n_J - 1
    i_convertida = (1 + i_anual) ** (1 / n_i) - 1
    return i_convertida

def convertir_i_a_J(i, n_i, n_J):
    i_anual = (1 + i) ** n_i - 1
    J_convertida = n_J * ((1 + i_anual) ** (1 / n_J) - 1)
    return J_convertida

def main():
    conversion = menu()
    if conversion == 'J_to_i':
        J = float(input("Ingrese la tasa nominal (J) como decimal (por ejemplo, 0.08 para 8%): "))
        n_J = seleccionar_periodo("nominal (J)")
        n_i = seleccionar_periodo("efectiva (i)")
        i = convertir_J_a_i(J, n_J, n_i)
        print(f"La tasa efectiva {periodo_nombre(n_i)} es: {i * 100:.2f}%")
    elif conversion == 'i_to_J':
        i = float(input("Ingrese la tasa efectiva (i) como decimal (por ejemplo, 0.08 para 8%): "))
        n_i = seleccionar_periodo("efectiva (i)")
        n_J = seleccionar_periodo("nominal (J)")
        J = convertir_i_a_J(i, n_i, n_J)
        print(f"La tasa nominal {periodo_nombre(n_J)} es: {J * 100:.2f}%")

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

if __name__ == "__main__":
    main()