from convert_dec_for import DecForBin, DecForHex
from convert_for_dec import BinForDec, HexForDec



dic = {
    1: BinForDec(),
    2: DecForBin(),
    3: HexForDec(),
    4: DecForHex()
}

print("*"*50)
print("Escolhas uma das opções abaixo:")
print("-"*50)
print("""1: Binário para Decimal;
2: Decimal para Binário;
3: Hexadecimal para Decimal;
4: Decimal para Hexadecimal;""")
print("-"*50)

option = int(input("Opção escolhida: "))

dic[option].calculate()