class User:
    def __init__(self,username,usermail):
        self.name=username
        self.mail=usermail
        self.saldo=0
    def deposito(self,monto):
        self.saldo += monto 
    def giro(self,monto):
        self.saldo -= monto
    def balance(self):
        return "Nombre:%s -> Saldo:%s" % (self.name, self.saldo)
    def transfer(self,usuarioTransfer,monto):
        self.giro(monto)
        usuarioTransfer.deposito(monto)
        return "Nombre:%s -> Saldo:%s | Nombre:%s -> Saldo:%s" % (self.name, self.saldo, usuarioTransfer.name,usuarioTransfer.saldo)


Ariel=User('Ariel Calderon G','arielcalderon@google.com')
Esteban=User('Esteban Abarzua E','estebanabarzua@clic.com')
Monica=User('Monica Lewensky S','monicale@cat.com')


Ariel.deposito(1000)
Ariel.deposito(4000)
Ariel.deposito(10000)
Ariel.giro(100)
print(Ariel.balance())
##############################################################
Esteban.deposito(1500)
Esteban.deposito(43400)
Esteban.giro(11200)
Esteban.giro(10800)
print(Esteban.balance())
###############################################################
Monica.deposito(43400)
Monica.giro(1100)
Monica.giro(8001)
Monica.giro(123)
print(Monica.balance())
##############################################################
print(Ariel.transfer(Monica,200))