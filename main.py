import asciiPrint as ascii
import dialogPrint as dlg
import interface as itf

"""
TODO: create and check ascii prints.
TODO: CnT interface with asciis
TODO: Restructure dialogs into a txt file.
TODO: Create a method for calling dialogs with  f.readline(), get the size and print each char one by one.
#and use f.read(n) so n+1 and cls while n<readline().size this is for a typewritter style of chars.
TODO: 

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

  ######### EXAMPLE OF A NESTED DICT.

"""
#ascii art
#options: alertas, armas, enemigos, objetos, pasillos
# personalPy\dinosYCalabozosEnPython\ascii\alertas\alerta_menu_juego_1.txt

# menu1=ascii.Printer('alertas', 'alerta_menu_juego_1', True)
# menu2=ascii.Printer('alertas', 'alerta_menu_juego_2', True)
# menu3=ascii.Printer('alertas', 'alerta_menu_juego_3', True)

# filename = 'personalPy/dinosYCalabozosEnPython/dialogs.txt'
# dlg.print_lines(filename, 10, 14)

#interface
options = ['ascii/alertas/alerta_menu_juego_1.txt','ascii/alertas/alerta_menu_juego_1.txt','ascii/alertas/alerta_menu_juego_1.txt']
""""""
selected_option = itf.navigate_menu(options)
print(f'Selected option: {selected_option}')