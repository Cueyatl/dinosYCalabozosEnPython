def Printer(prefix,fileName, is_option):
  # txtascii/alertaMuerte/alerta_muerte_1.txt')
  # Cases: alertas/menu,| armas,| enemigos/personalPy/dinosaurio, esqueleto, fantasma, grifo, hada, lobo, oso, peppa, zombie
  #objetos| pasillo
  
  match prefix:
    case 'alertas':
      file_path='ascii/alertas/'+fileName+'.txt'
      
    case 'armas':
      file_path='ascii/armas/'+fileName+'.txt'
    case 'enemigos':
      file_path='ascii/enemigos/'+fileName+'.txt'
    case 'objetos':
      file_path='ascii/objetos/'+fileName+'.txt'
    case 'pasillos':
      file_path='ascii/pasillos/'+fileName+'.txt'
  if is_option:
    return file_content
  else:
    try:
      with open(file_path, 'r') as file:
        # Read the content of the file
        # Print the content
        file_content = file.read()
        print(file_content)

    except FileNotFoundError:
      print(f"File '{file_path}' not found.")
    except Exception as e:
      print(f"An error occurred: {e}")




