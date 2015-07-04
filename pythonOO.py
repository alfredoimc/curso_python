#Old-Style
class Pessoa(object):
    #atributo
    nome = ""
    idade = 0

    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print('A pessoa estar andando')
        
    #instancia
p=Pessoa('alfredo inacio')

p.idade = 26
print("nome :" ,p.nome, " idade:" ,p.idade)
p.andar()
