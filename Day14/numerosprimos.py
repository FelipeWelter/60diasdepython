numero = int(input("Digite o numero para verificar se ele e primo: "))
primo = True

if numero <= 1:
    primo = False
    
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        primo = False #nao e primo
        break #encerra o loop

if primo:
    print(f"{numero} E um numero Primo")
else:
    print(f"{numero} E não e um numero primo")