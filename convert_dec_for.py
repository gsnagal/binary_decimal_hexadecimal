
class DecFor:
    
    def __init__(self):
        self.para = []
        self.valor = ""
    
    def convert(self, value):   
        dec = int(input("Digite o número em decimal: "))
        self.dec = dec
        while dec >= value:
            resto = dec % value
            dec = dec // value
            self.para.append(str(resto))
        self.para.append(str(dec))
        self.para.reverse()

        return self.para


class DecForBin(DecFor):
    
    def calculate(self):
        bin = self.convert(2)
        for i, value in enumerate(bin):
            self.valor += bin[i]

        print(f"O valor de {self.dec} (decimal) em binário: {self.valor}")


class DecForHex(DecFor):
    
    def calculate(self):
        hex = self.convert(16)
        valor = self.transform(hex)
        print(f"O valor de {self.dec} (decimal) em binário: {valor}")

    def transform(self, hex):
        for i, value in enumerate(hex):
            if value == "10":
                hex[i] = "A"
            elif value == "11":
                hex[i] = "B"
            elif value == "12":
                hex[i] = "C"
            elif value == "13":
                hex[i] = "D"
            elif value == "14":
                hex[i] = "E"
            elif value == "15":
                hex[i] = "F"
            self.valor += hex[i]
        
        return self.valor