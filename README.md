# PerX
[MEU PRIMEIRO PROJECTO] -Calculadora inufensiva, com 4 operações empregadas para testes...

print ("Bem-vindo ao PerX")
print()
print ("[Soma] |1|")
print ("[Subtra��o] |2|")
print ("[Divis�o] |3|")
print ("[Multiplica��o] |4|")
boga = int(input("Qual opera��o voce deseja calcular ?\n"))


if (boga == 1):
    s = int(input ("Digite o primeiro numero:"))
    t = int(input ("Segundo o primeiro numero:"))
    torra = s + t
    print ("O resultado �:" ,torra)
    print ()
if (boga == 2):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y - p
    print("O resultado �:", bota)

if (boga == 3):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y / p
    print("O resultado �:", bota)

if (boga == 4):
    y = int(input("Digite o primeiro numero:"))
    p = int(input("Segundo o primeiro numero:"))
    bota = y * p
    print("O resultado �:", bota)
