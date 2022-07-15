class numRom:
    def __init__(self,username,entero):
        self.name=username
        self.numero=entero

    def convert(self,entero):
        numero = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
        simbolo = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        x=12
        while entero:
            divisor=entero // numero[x]
            entero %= numero[x]

            while divisor:
                print(simbolo[x],end="")
                divisor -= 1
            x -= 1

    def convertNum(self,roma):
      dicc_roma={'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      x=12
      indice=dicc_roma[roma[0]]
      for x in range(1,len(roma)):
        if dicc_roma[roma[x-1]] < dicc_roma[roma[x]]:
            indice += (dicc_roma[roma[x]] - 2) * dicc_roma[roma[x-1]]
        else:
            indice += dicc_roma[roma[x]]
      return indice






Jorge=numRom("Jorge",1987)

print(Jorge.convertNum('MMM'))
