""" Bienvenida Mary --- Ponte a Trabajar"""
def formulas(a,b,c,x,y):
    valor_1 = 0
    valor_2 = 0
    Hz = 0
    if x^2/a^2-y^2/b^2 == 32/c:
        print('Valor2 = True')
        valor_1 == True
    else:
         valor_1 == False
    valor_3 = 8 + c*y^2/4*b^2 
    if 8 + c*y^2/4*b^2 == c*x^2/4*a^2:
        print('Valor2 = True')
        Hz = valor_3
        print(Hz)
        valor_2 == True
    else: 
        valor_2 == False
    if valor_1 and valor_2:
        '''Formula Juan'''
    else:
        return(a,b,c,"Falso")
def main():
    lx = 16
    ly = 50
    a = 1
    b = 2
    c = 3
    if __name__ == '__main__':
        print(formulas(a,b,c,lx,ly))

