def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    
    final_1 = saldo + ingresos - egresos - (cheques * 13)
    final_2 = final_1 - (final_1 * .075)

    print("El saldo final de la cuenta es:", final_2)

if __name__ == '__main__':
    main()
