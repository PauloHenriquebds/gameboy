class Pessoa:
    def _init_(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self):
        if self.comendo == True:
            print(f"{self.nome} já esta comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode comer pois esta falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pois esta dormindo")
        else:
            comida = input(f"O que {self.nome} vai comer?: ")
            print(f"{self.nome} começou a comer {comida}")
            self.comendo = True
    def falar(self):
        if self.falando == True:
            print(f"{self.nome} já esta falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois esta comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois esta dormindo")
        else:
            print(f"{self.nome} começou a falar")
            self.falando = True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} já esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir pois esta falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir pois esta comendo")
        else:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
    def apresentar(self):
        print(f"Olá meu nome é: {self.nome} "
              f"Tenho {self.idade} anos "
              f"e peso {self.peso}")
    def parardormir(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} já acordou")
    def pararcomer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} já parou de comer")
    def pararfalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
            self.falando = False
        else:
            print(f"{self.nome} não esta falando")