"""
Juan José Salazar Cortés - A01642126
Mariana Esquivel Hernández - A01641244
Terminado el 31 de Marzo de 2022
"""
from cmath import log, sqrt
def formulas(a,b,c,x,y,M):
    print(" El valor de a es: ", a, "\n", "El valor de b es: ", b, "\n", "El valor de c es: ", c)
    valor_1 = 0
    valor_2 = 0
    Hz = 0
    print("El valor de altura del punto silla es: ", M)
    print("\nPrimera condición cumplida...")
    print('Valor 1: ' + str(((x**2)/(a**2))-((y**2)/(b**2))) + ' , 32/c = ' + str(32/c))
    if ((x**2)/(a**2))-((y**2)/(b**2)) == (32/c):
        print('Valor1 = True')
        valor_1 = True
    else:
         valor_1 = False
    print("\nSegunda condición cumplida...")
    print('Valor 2: ' + str(8 + (c*(y**2))/(4*(b**2))) + ', Valor 2 = ' + str(((c*(x**2))/(4*(a**2)))))
    valor_3 = 8 + (c*(y**2))/(4*(b**2))
    Hz = valor_3
    print("Hz es igual a: ", Hz)
    if (8 + (c*(y**2))/(4*(b**2))) == ((c*(x**2))/(4*(a**2))):
        print('Valor2 = True')
        valor_2 = True
    else: 
        valor_2 = False
    #if valor_1 and valor_2:

    M2 = 7.88

    vVault = ((4 * a * c) / b ** 3) * ((y / 4) * ((y ** 2 / 4) + (M * b ** 2 / c)) ** (3 / 2) +
                    ((3 * M * b ** 2 * y) / (8 * c)) * sqrt((y ** 2 / 4) + (M * b ** 2 / c)) +
                                 ((3 * (M ** 2) * (b ** 4)) / (8 * c ** 2)) * (log((sqrt(((y ** 2) / 4) +
                                     (M * b ** 2 / c)) + y / 2) / (sqrt(((y ** 2) / 4) + (M * b ** 2 / c)) - y / 2))))

    vVault2 = ((4 * a * c) / b ** 3) * ((y / 4) * ((y ** 2 / 4) + (M2 * b ** 2 / c)) ** (3 / 2) +
                    ((3 * M2 * b ** 2 * y) / (8 * c)) * sqrt((y ** 2 / 4) + (M2 * b ** 2 / c)) +
                                ((3 * (M2 ** 2) * (b ** 4)) / (8 * c ** 2)) * (log((sqrt(((y ** 2) / 4) +
                                    (M2 * b ** 2 / c)) + y / 2) / (sqrt(((y ** 2) / 4) + (M2 * b ** 2 / c)) - y / 2))))

    print("\nLa cantidad de volumen de la bóveda cuando M es igual a 8 es: ", vVault)
    print("La cantidad de volumen de la bóveda cuando M es igual a 7.88 es: ", vVault2)
    print("\nLa cantidad de cemento requerida para la bóveda es de: ", vVault-vVault2, "(m3) metros cúbicos de cemento")
    #else:
    # return(a,b,c,"Falso")
def main():
    m = 8
    lx = 16
    ly = 50
    a = 1
    b = 3.5
    c = 0.617
    formulas(a,b,c,lx,ly,m)
if __name__ == '__main__':
    main()
