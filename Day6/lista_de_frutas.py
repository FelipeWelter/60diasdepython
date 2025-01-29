frutas = ["banana", "maça", "uva", "pera", "manga"]

for fruta in frutas:
    print(fruta)
    

#utilizado input para criar lista de frutas

frutas = []
while True:
    fruta = input("Digite o nome da fruta: ")
    if fruta == "sair":
        break
    frutas.append(fruta)
    
print(frutas)