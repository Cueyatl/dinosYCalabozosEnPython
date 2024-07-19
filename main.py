import asciiPrint as ascii
import interface as itf

import time
import sys
import os
def print_lines( start_line, end_line, delay, ascii_path):
  ascii.Printer(ascii_path[0], ascii_path[1], False)
  with open('dialogs.txt', 'r',) as file:
    lines = file.readlines()
    for i in range(start_line - 1, end_line):
      time.sleep(0.2)
      for c in lines[i]:
        lines[i].strip()
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
  time.sleep(delay)
  os.system('cls')

#Historia

#DIALOGS
peppa_ascii=['enemigos', 'peppa_espada_1']
oso_ascii=['enemigos','oso_espada_1']
optionsInteraction=['Conversar', 'Atacar']
print_lines( 2,6,4,['objetos', 'dino'])
#DIALOGS
print_lines( 8,9,4,peppa_ascii)
#DIALOGS
print_lines( 11,17,4,peppa_ascii)
#DIALOGS
print_lines( 20,23,4,peppa_ascii)       
#DIALOGS

print_lines( 26,27,4,peppa_ascii)
ascii.printPasillo()

selected_menu=itf.interface(optionsInteraction,oso_ascii, 'Elige una de las dos opciones, usa las flechas arriba y abajo, selecciona con Enter.', False)
print_lines( 30,48,4,oso_ascii) #si conversar con oso
#DIALOGS
print_lines( 51,55,4,oso_ascii)       
print_lines( 57,69,4,oso_ascii) #si conversar con Lorenzo
#DIALOGS
print_lines( 72,74,4,oso_ascii)       
print_lines( 77,98,4,oso_ascii) #si conversar con Dani el dinosaurio
#DIALOGS
print_lines( 101,102,4)         
print_lines( 103,116,4) #si conversar con Lucero el Hada
#DIALOGS
print_lines( 120,124,4)         
print_lines( 126,138,4) #si conversar con Lucero el Hada
#DIALOGS
print_lines( 141,144,4)         
print_lines( 146,152,4) #si conversar con Pedro el Lobo
#DIALOGS
print_lines( 155,159,4)         
print_lines( 161,171,4) #si conversar con Huesos
#DIALOGS
print_lines( 173,175,4)         
print_lines( 176,188,4) #si conversar con Vincent el fantasma
#DIALOGS
print_lines( 191,196,4)         
print_lines( 197,203,4) #Conversacion con peppa
#se pelea con peppa
print_lines( 205,215,4) 





















