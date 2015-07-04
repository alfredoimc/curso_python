class area(object):
    a = 0.0
    c = 0.0
    np = 0.0
    

    def __init__(self, a):

        self.a = a
        

a = input('digite a area do lugar \n')
c = input('digite a quantos metros quadrados deseja para cada pessoa \n')
np = a/c
print('O numero maximo de pessoas eh de ', np)
