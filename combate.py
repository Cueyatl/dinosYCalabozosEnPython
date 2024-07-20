import asciiPrint as ascii
import interface as itf
import random
import time
import sys
import os
# def interface(options, ascii_route,aditional_info,is_ascii):

def combatiendo(enemigo):
    informacion='\nEspada vence a Magia (la corta). \nMagia vence a flecha (lo atraviesa).\nflecha vence a Espada (le dispara).'
    ascii.combatIntro(0.1)
    ascii.combatIntro(0.2)
    
    opciones = ["espada", "flecha", "magia"]
    
    puntaje_usuario = 0
    puntaje_maquina = 0
    actual_ascii=['enemigos',enemigo+'_espada_1']
    while puntaje_usuario < 2 and puntaje_maquina < 2:
        eleccion_maquina =  random.randint(0, 2)
        
        eleccion_usuario = itf.interface(opciones,actual_ascii,informacion,False)
        print(f"{enemigo} eligió: {eleccion_maquina}")
        
        match eleccion_usuario:
          case 0:
            actual_ascii[1]=enemigo+'_espada_1'
            
          
          case 1:
            actual_ascii[1]=enemigo+'_arco'
            
          case 2:
            actual_ascii[1]=enemigo+'_baston'
            
            
            # comment: 
        # end match
        if eleccion_usuario == eleccion_maquina:
            informacion='\nEspada vence a Magia (la corta). \nMagia vence a flecha (lo atraviesa).\nflecha vence a Espada (le dispara).'
            informacion="\n¡Es un empate!\n"+informacion
            
            
        elif (eleccion_usuario == 0 and eleccion_maquina == 2) or \
            (eleccion_usuario == 2 and eleccion_maquina == 1) or \
            (eleccion_usuario == 1 and eleccion_maquina == 0):
            informacion='Espada vence a Magia (la corta). \nMagia vence a flecha (lo atraviesa).\nflecha vence a Espada (le dispara).'
            informacion="\n¡Ganaste este turno!\n"+informacion
            puntaje_usuario += 1
        else:
            informacion='\nEspada vence a Magia (la corta). \nMagia vence a flecha (lo atraviesa).\nflecha vence a Espada (le dispara).'
            
            informacion=f"\n{enemigo} gana este turno.\n"+informacion
            puntaje_maquina += 1
            
        informacion+=f"\nPuntaje - Usuario: {puntaje_usuario}, Máquina: {puntaje_maquina}\n"
        

    if puntaje_usuario == 2:
        os.system('cls')
        return 1
    else:
      select_muerte=random.randint(0,2)
      ascii_fin_juego=['muerte1', 'muerte2', 'muerte3']
      itf.interface([ ascii_fin_juego[select_muerte]],["Fin del juego"],  "fin del juego, rawr..",True)
      os.system('cls')
      
      sys.exit()
