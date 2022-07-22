

valorCapital=float(400000)
valorInteres=float(0.03)
valorCuotas=float(360)
valorInteres_A=float(0.06)

calculo_uno= valorCapital * valorInteres * (1+valorInteres)*valorCuotas/((1+valorInteres)*valorCuotas-1)
calculo_dos= valorCapital * valorInteres_A * (1+valorInteres_A)*valorCuotas/((1+valorInteres_A)*valorCuotas-1)



print('Pago Mensual con tasa de 3% -> ', calculo_uno)
print('Pago Mensual con tasa de 6% -> ', calculo_dos)

