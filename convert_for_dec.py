

class BinForDec:
    
    def calculate(self):
        bin = input("Digite o número em binário: ")
        dec = []
        final = 0
        for value in bin:
            if int(value) > 1:
                raise ValueError("Somente digitar 1 ou 0")
            dec.append(value)
                
        dec.reverse()        
        for i, value in enumerate(dec):
            value_int = int(value)
            final += value_int*2**i

        print(f"O valor binário {bin} em decimal fica: {final}")
        



class HexForDec:
    
    def calculate(self):
        hex = input("Digite o número em hexadecimal: ")
        dec = []
        final = 0
        for value in hex:
            if value == "A" or value == "a":
                dec.append("10")
            elif value == "B" or value == "b":
                dec.append("11")
            elif value == "C" or value == "c":
                dec.append("12")
            elif value == "D" or value == "d":
                dec.append("13")
            elif value == "E" or value == "e":
                dec.append("14")
            elif value == "F" or value == "f":
                dec.append("15")
            else:
                dec.append(value)
                
        dec.reverse()
        for i, value in enumerate(dec):
            final += int(value)*16**i

        print(f"O valor hexadecimal {hex} em decimal fica: {final}")