class Animal: 
    def __init__(self,nome,dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print('Nhom Nhom', self.nome)

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        super().__init__(nome,dono)
        self.raca = raca

    def miar(self):
        print('Miauuuu')

class Cachorro(Animal):
    def latir(self, **kwagrs):
        print('Auu auuuu')

gato =Gato('Harry','Lorrany','seila')
cachorro =Cachorro('Rex','Barbara')
animal =Animal('Max','Gabriel')
cachorro.latir()
