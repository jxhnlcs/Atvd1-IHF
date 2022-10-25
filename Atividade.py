### Desenvolvimento de Sistemas - SENAI
### Professor Jefté Goes
### Grupo: John Lucas, Carla Saionara, João Neri e Micael Cunha.

print('''
DDD   | Destination
---------------------
61    | Brasilia
71    | Salvador
11    | São Paulo
21    | Rio de Janeiro
32    | Juiz de Fora
19    | Campinas
27    | Vitória
31    | Belo Horizonte
      ''')
x = 1
while x != 0:
    ddd = int(input("Digite o DDD da sua cidade:\n"))
    if ddd == 61:
        print("Seu DDD corresponde à Brasilia.")
    elif ddd == 71:
        print("Seu DDD corresponde à Salvador.")
    elif ddd == 11:
        print("Seu DDD corresponde à São Paulo.")
    elif ddd == 21:
        print("Seu DDD corresponde à Rio de Janeiro.")
    elif ddd == 32:
        print("Seu DDD corresponde à Juiz de Fora.")
    elif ddd == 19:
        print("Seu DDD corresponde à Campinas.")
    elif ddd == 27:
        print("Seu DDD corresponde à Vitória.")
    elif ddd == 31:
        print("Seu DDD corresponde à Belo Horizonte.")
        
        ### Validação
        
    else:
        print(f"Seu DDD {ddd} não está cadastrado.")
    x = int(input("Deseja continuar? \nSIM = Qualquer número | NÃO = 0 \n"))