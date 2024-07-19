
import interface as itf
import time
import os
"""
  
  TODO: create a method for a for i in range(n of events.): if else interact/attack at the end drop item.
  TODO: Create two classes of heroes, with four attacks and two classes of evil-doers with four attacks, 
  
        add to their inventory 3 items, give em an if else sentience for selecting if attack or heal themselves.  
  TODO: create combat system.
  dialogs
  
--STRUCTURE:
main menu
  main():
  list: start, credits, exit
  if credits show ascii two, option: return
  if start: execute game.add(element)
  if/else: speak/attack
    if atack if/else: select attack/use Inventory
      if select attack: options-> attack
      if inventory:  options-> inventory
    
    if speak: options: speak/attack
    
  narrativa parte 1 y peppa dino
  narrativa p2
  if narrativa 1  - encunetro 2
  
  narrativa p3
  narrativa p4

  if narrativa 2  -encuentro 3
  narrativa p5
  if narrativa 3 -encuetntro 4
  narrativa p6
  if narrativa 4 -encuetntro 5
  narrativa p7

  
Options must be shown always.
"""
#ascii art
#options: alertas, armas, enemigos, objetos, pasillos
# personalPy\dinosYCalabozosEnPython\ascii\alertas\alerta_menu_juego_1.txt

# dlg.print_lines(filename, 10, 14)

#interface
"""
Example of interface
options=['a','b','c','d'] #0, 1,2
aditional_info="lorem  ipsum"

"""

ascci_route=['', '']
optionsMenu=['menu1','menu2','menu3']
additional_info="no info"
selected_menu=0
while selected_menu != 2:
  selected_menu=itf.interface(optionsMenu,ascci_route, additional_info, True)
  print(selected_menu)
  
  if selected_menu==0:
    os.system('cls')
    print("TEST:play game")
    time.sleep(3)
  if selected_menu==1:
    os.system('cls')
    out_bounds=itf.interface(["creditos"], ['alertas', 'creditos'], "Hecho",True)
    
    
print("TEST:exited game")

