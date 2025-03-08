#busquedas lineales  -----  cuanod no conocemos el arreglo ---en se basan en los indices
informacion = [
    #0,1,2,3,4
    [1,2,3,4,5], #0
    [6,7,8,9,10],#1
    [11,12,13,14,15],#2
    [16,17,18,19,20],#3
    ["uno", "dos","tres","cuatro"],#4
    [1.1,1.2,1.3,1.4,1.5] #5
]

valor = input("ingrese un  valor: ")
for fila in range(len(informacion)):
    for columna in range(len(informacion[fila])):
        if informacion[fila][columna] == valor:
            print(f"filas {fila} - - columnas {columna} -- valor {informacion[fila][columna]}")




#busquedas binarias  --cuando conozco la informacion -- buscar por valores
lista_cliente = [
    [  #clientes 2024
        ["1803435", "xxxxx",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"],
        ["1803435", "eeeeee",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"],
        ["1803435", "ttttt",    "Llerena",    "Ambato",    "123",    "correo@gmail.com"]
    ],
    
    [ #clientes 2025
        ["1803435", "rrrrrr",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"],
        ["1803435", "wwwwww",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"],
        ["1803435", "nnnnnn",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"],
        ["1803435", "mmmmmm",    "Llerena",    "Ambato",    "0987654321",    "correo@gmail.com"]
    ]
]


encuentra = 0
for cliente in lista_cliente:
    for atributos in cliente:
        if atributos == valor:
            print("Se encontro------------")
            encuentra = 1
            break
       
    if encuentra == 1:
        break


dto = [[2,5,3,1],[1,2,3,4]]


dto.sort()

print(dto)




