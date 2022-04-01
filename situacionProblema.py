""" Bienvenida Mary --- Ponte a Trabajar"""
from cmath import log, sqrt
def formulas(a,b,c,x,y,M):
    print(a,b,c)
    valor_1 = 0
    valor_2 = 0
    Hz = 0
    if ((x**2)/(a**2))-((y**2)/(b**2)) == (32/c):
        print('Valor2 = True')
        valor_1 = True
    else:
         valor_1 = False
    valor_3 = 8 + (c*(y^2))/(4*(b^2))
    if 8 + (c*(y^2))/(4*(b^2)) == ((c*(x^2))/(4*(a^2))):
        print('Valor2 = True')
        Hz = valor_3
        print(Hz)
        valor_2 = True
    else: 
        valor_2 = False
    if valor_1 and valor_2:
        vVault = ((4*a*c)/b^3)*[(y/4)*((y^2/4)+(M*b^2/c))^(3/2)] + ((3*M*b^2*y)/(8*c))*sqrt((y^2/4)+(M*b^2/c)) + ((3*M^2*b^4)/(8*c^2)) * (log(sqrt(((y^2)/4)+(M*b^2))))
    else:
        return(a,b,c,"Falso")
def main():
    m = 8
    lx = 16
    ly = 50
    a = 1
    b = 2
    c = 3
    print('Culo')
    print(formulas(a,b,c,lx,ly,m))
if __name__ == '__main__':
    main()
"""vVault = ((4*a*c)/b^3)*[(ly/4)*((ly^2/4)+(M*b^2/c))^(3/2)] + ((3*M*b^2*ly)/(8*c))*sqrt((ly^2/4)+(M*b^2/c)) + ((3*M^2*b^4)/(8*c^2)) * log(sqrt((ly^2/4)+(M*b^2)))
"""