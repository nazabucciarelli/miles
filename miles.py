from os import system
from random import randint
import sys

def input_numero():
    contador =0
    num = input()
    verificado = False
    while verificado == False:
        for i in range(len(num)):
            numero = num[i]
            for j in range(len(num)):
                if numero == num[j]:
                    contador +=1
        if num.isalpha():
            print('No haz ingresado un numero...')
            num = input()
        elif contador > 4:
            verificado= False
            contador = 0
            print('Recuerda: El numero no debe superar los 4 caracteres y sus digitos no se deben repetir.')
            num = input()
        else:
            verificado = True
            return num

def ranking():
    system("cls")
    print("---RANKING-10-MEJORES---")
    txt_ranking = open("players_database.txt","r+",encoding="UTF-8")
    lista = txt_ranking.readlines()
    mayor_puntuacion = 2
    for i in range(len(lista)):
        lista_linea = lista[i].split("-")
        if int(lista_linea[1]) < mayor_puntuacion:
            mayor_puntuacion = int(lista_linea[1])
    cantidad_ranking = 10
    while cantidad_ranking >0:
        for j in range(len(lista)):
            lista_linea = lista[j].split("-")
            if int(lista_linea[1]) == mayor_puntuacion:
                print("-".join(lista_linea).replace("\n",""))
                cantidad_ranking -=1
            else:
                pass
        mayor_puntuacion += 1

def game():
    system("cls")
    print("¡Que comience el juego!")
    lista_numero_maquina = list(str(randint(1000,10000)))
    contador = 0
    verificado = False

    while verificado == False:
        for i in range(len(lista_numero_maquina)):
            numero = lista_numero_maquina[i]
            for j in range(len(lista_numero_maquina)):
                if numero == lista_numero_maquina[j]:
                    contador +=1
        if contador > 4:
            verificado= False
            contador = 0
            lista_numero_maquina = list(str(randint(1000,10000)))
        else:
            verificado = True

    numero_maquina = "".join(lista_numero_maquina)
    game_over = False
    intentos = 1
    while game_over == False:
        numero_insertado = input_numero()
        numero_insertado = list(numero_insertado)
        contador_bien = 0
        contador_regular = 0
        for i in range(len(numero_insertado)):
            if numero_insertado == lista_numero_maquina:
                game_over = True
                print(f"¡Terminaste el juego! El numero pensado por la computadora era {''.join(lista_numero_maquina)} y tus intentos fueron {intentos}.")
                respuesta = input('¿Desea almacenar su puntuacion en el historial?(Si/No): ').upper()
                if respuesta == 'SI':
                    name = input('Ingrese su nombre:')
                    txt = open('players_database.txt','r+',encoding='UTF-8')
                    txt.read()
                    txt.write('\n'+ name  + '-' +str(intentos))
                    txt.close()
                    print(f'¡Listo {name}, se guardo tu puntuacion en el ranking!')
                    input("Presione enter para volver al menu")
                    menu()
                    verif = False
                    while verif == False:
                        menu_number = input()
                        if menu_number == '1':
                            verif = True
                            menu()                          
                        else:
                            print('Ingrese una opcion valida')
                else:
                    input("Presione enter para volver al menu")
                    menu()
            if numero_insertado[i] == numero_maquina[i]:
                contador_bien += 1
            elif numero_insertado[i] in numero_maquina:
                contador_regular +=1
        intentos += 1
        if game_over == False:
            print(f'{contador_bien}B {contador_regular}R')
        
def menu():
    system("cls")
    print("MILES")
    print("Instrucciones: Inserte un numero de 4 cifras cifras cuyos digitos no se repitan para intentar adivinar en cuál esta pensando nuestro poderoso computador... La máquina le devolvera pistas por cada número que ingrese (REGULAR: (R) El dígito está en el número pero no en la posicion correcta. BIEN: (B) El digito está en su posicion correcta.) Mientras menos intentos realices, mejor será para tu posicion en el ranking.")
    print("1) Jugar \n2) Ranking \n3) Salir")
    opcion = input()
    while opcion.isalpha():
        print("Opcion de menú incorrecta, escoja entre 1,2 y 3.")
        opcion = input()
    while int(opcion) > 3 or int(opcion) < 0:
        print("Opcion de menú incorrecta, escoja entre 1,2 y 3.")
        opcion = input()
    if opcion == "1":
        game()
    elif opcion == "2":
        ranking()
        input("Presione enter para volver al menu")
        menu()
    elif opcion == "3":
        input("¡Gracias por jugar! Presione enter para salir")
        sys.exit()
  
menu()

