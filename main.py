import asciiPrint as ascii
import interface as itf
import combate as cbt
import time
import sys
import os
def print_lines( start_line, end_line, delay, ascii_path):
  os.system('cls')
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

#Historiaj
def gameOn():
  #DIALOGS
  peppa_ascii=['enemigos', 'peppa_espada_1']
  oso_ascii=['enemigos','oso_espada_1']
  grifo_ascii=['enemigos','grifo_espada_1']
  dino_ascii=['enemigos', 'dinosaurio_espada_1']
  hada_ascii=['enemigos', 'hada_espada_1']
  zombie_ascii=['enemigos', 'zombie_espada_1']
  lobo_ascii=['enemigos', 'lobo_espada_1']
  huesos_ascii=['enemigos', 'esqueleto_espada_1']
  fantasma_ascii=['enemigos', 'fantasma_espada_1']

  ops_interact=['Conversar', 'Atacar']

  print_lines( 2,6,4,['objetos', 'dino'])

  # DIALOGS
  print_lines( 8,9,2,peppa_ascii)
  # DIALOGS
  print_lines( 11,17,4,peppa_ascii)
  #DIALOGS
  print_lines( 20,23,4,peppa_ascii)       
  #DIALOGS

  # print_lines( 26,27,4,peppa_ascii)
  ascii.printPasillo()
  #OSO
  scene1=itf.interface(ops_interact,oso_ascii, 'selecciona con enter', False)  
  if scene1==0:
    print_lines( 30,52,4,oso_ascii) #si conversar con oso
  else:
    cbt.combatiendo('oso')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  print_lines( 53,55,4,grifo_ascii)     #continue storys

  #GRIFO
  scene2=itf.interface(ops_interact,grifo_ascii, 'selecciona con enter', False)  
  if scene2==0:
    print_lines( 57,69,4,grifo_ascii) #si conversar con Lorenzo
  else:
    cbt.combatiendo('grifo')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  print_lines( 72,74,4,grifo_ascii)  #continue story

  #DINOSAURIO
  scene3=itf.interface(ops_interact,dino_ascii, 'selecciona con enter', False)  
  if scene3==0:
    print_lines( 77,98,4,dino_ascii) #si conversar con Dani el dinosaurio
  else:
    cbt.combatiendo('dinosaurio')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  print_lines( 101,102,3, hada_ascii) #continue story
  #HADA
  scene4=itf.interface(ops_interact,hada_ascii, 'selecciona con enter', False)  
  if scene4==0:
    print_lines( 103,116,4, hada_ascii) #si conversar con Lucero el Hada
  else:
    cbt.combatiendo('hada')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  ascii.printPasillo()
  print_lines( 120,124,4,['objetos','hallway2'] ) 


  #ZOMBIE
  scene5=itf.interface(ops_interact,zombie_ascii, 'selecciona con enter', False)  
  if scene5==0:
    print_lines( 126,138,4, zombie_ascii) #si conversar con Roberto el zombie
  else:
    cbt.combatiendo('zombie')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  print_lines( 141,144,4,['objetos', 'hallway'])         

  print_lines( 145,146,4,lobo_ascii) #Intro Pedro el lobo.
  #LOBO
  scene6=itf.interface(ops_interact,lobo_ascii, 'selecciona con enter', False)  
  if scene6==0:
    print_lines( 147,152,4, lobo_ascii) #si conversar con Pedro el Lobo
    print_lines( 155,159,4, lobo_ascii)         
  else:
    cbt.combatiendo('lobo')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  print_lines( 155,159,4, huesos_ascii) #intro huesos
  #HUESOS
  scene7=itf.interface(ops_interact,huesos_ascii, 'selecciona con enter', False)  
  if scene7==0:
    print_lines( 162,173,4, huesos_ascii) #si conversar con Huesos  
  else:
    cbt.combatiendo('esqueleto')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  print_lines( 175,176,4,['objetos','hallway2'])


  scene8=itf.interface(ops_interact,fantasma_ascii, 'selecciona con enter', False)  
  if scene8==0:
    print_lines( 177,189,4,fantasma_ascii) #si conversar con Vincent el fantasma
    print_lines( 192,193,4,['objetos', 'hallway'])
  else:
    cbt.combatiendo('fantasma')
    ascii.Printer('alertas','ganaste',False)
    time.sleep(3)
  #DIALOGS
  ascii.printPasillo()

  print_lines( 194,194,2,['objetos', 'gate'])


  print_lines( 195,204,4,peppa_ascii) #Conversacion con peppa
  #se pelea con peppa
  cbt.combatiendo('peppa')
  print_lines( 205,217,4.['objetos','castillo']) 
  print('FIN DEL JUEGO')
  # TODO: cambiar al fantasma



















