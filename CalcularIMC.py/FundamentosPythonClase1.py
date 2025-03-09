def calcular_imc():
    try:
        peso = float(input("Ingrese su peso en kg:"))
        altura = float(input("Ingrese su altura en metros"))

        if peso <= 0 or altura <= 0:
            print("El peso y la altura deben ser valores positivos.")
            return
        imc = peso / (altura **2)

        print (f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Clasificación: Bajo peso")
        elif 18.5 <= imc < 24.9:
            print("Clasificación: Peso normal")
        elif 25 <= imc < 29.9:
            print("Clasificación: Sobrepeso")
        else:
            print("Clasificación: Obesidad")

    except ValueError:
        print("Error: Ingresa valores númericos válidos.")

calcular_imc()