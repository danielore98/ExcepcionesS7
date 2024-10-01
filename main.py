def leer_numero_natural():
    while True:
        try:
            # Solicitamos el ingreso de un número natural
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                raise ValueError("El número debe ser natural (mayor que 0).")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Inténtelo de nuevo.")

def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def principal():
    numero = leer_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    principal()
