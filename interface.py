from msvcrt import getch
import asciiPrint as asc
import os

"""Method for printing the interface and ascii art on top.
Args: 
    options: a string list that shows the options for the menu.
    ascii_route: as a string, the route to the ascii art that wants to be displayed,
    is_ascii: boolean, if true, then instead of showing the menu it shows ascii art as options.(useful for main menu and death screens).
    aditiona_info: print information for the inventory, stats, and others.
    """
def interface(options, ascii_route,aditional_info,is_ascii):
  c_value=0
  
  
  #ads a double space so its centered when the the actual value has a "->" signaling it is the current selected option.
  if not is_ascii:
    options=restoreOptions(options, c_value)

  while True:
    os.system('cls') #Clear screen
    if not is_ascii: #Meaning it shows text options instead of ascci art as options.
      asc.Printer(ascii_route[0], ascii_route[1], False) #Method for printing the required ascii art that goes above the text options.
      """This code restores the selected option from "->option" to "  "option """
      options=restoreOptions(options, c_value)
    
      print(aditional_info)
    else:
      asc.Printer('alertas', options[c_value], False) #Prints the ascii as an option.
    key = ord(getch()) #instruction used for identifying the key's ascii code.
    if key == 27: #ESC
      break
    elif key == 13: #Enter
      options=restoreOptions(options, c_value)
      return c_value
      
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
      key = ord(getch())
      if key == 80: #Down arrow
        #this ternary permits to keep pressing the down arrow key without exiting the list bounds. Applies the same to the up arrow.
        c_value=0 if c_value>=len(options)-1 else c_value+1
      
      elif key == 72: #Up arrow
        c_value=len(options)-1 if c_value<=0  else c_value-1

"Private method"
def restoreOptions(options, c_value):


  for i in range (len(options)):
    options[i]=options[i].strip()
    
    if options[i][0]!='-':
      options[i]='  '+options[i]
    if options[i][0]=='-':
      options[i]=options[i].replace('->','  ')
      options[i]=options[i].strip()
      options[i]='  '+options[i]
    
      
        
  options[c_value]=options[c_value].replace('->','')
  options[c_value]=options[c_value].strip()
  options[c_value]='->'+options[c_value]
  for i in range (len(options)):
    print(options[i])
  return options
