print ("Bem-vindo ao PerX")
print()
print ("»Criador-Stefan Monteiro")
print ("»Whatssap-935461678«")
print ("»[Descenders]«")
print()
print ("[Soma] |1|")
print()
print ("[Subtração] |2|")
print()
print ("[Divisão] |3|")
print()
print ("[Multiplicação] |4|")
print()
boga = int(input("Qual operação voce deseja calcular ?\n"))


if (boga == 1):
    s = int(input ("Digite o primeiro numero:"))
    t = int(input ("Segundo o primeiro numero:"))
    torra = s + t
    print ("O resultado é:" ,torra)
    print ()
if (boga == 2):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y - p
    print("O resultado é:", bota)

if (boga == 3):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y / p
    print("O resultado é:", bota)

if (boga == 4):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y * p
    print("O resultado é:", bota)
