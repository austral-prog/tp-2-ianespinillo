def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    print('Vuelto')
    print (f"Pesos: {vuelto}")
    print (f"Centavos: .{str(vuelto).split('.')[1]}")
