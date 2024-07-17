import curses

def navigate_menu(options):
    def main(stdscr):
        # Clear screen
        stdscr.clear()

        current_selection = 0

        while True:
            stdscr.clear()
            
            # Display the options
            for idx, option in enumerate(options):
                if idx == current_selection:
                    stdscr.addstr(idx, 0, option, curses.A_REVERSE)
                else:
                    stdscr.addstr(idx, 0,option)

            key = stdscr.getch()

            if key == curses.KEY_UP:
                if current_selection<=0:
                    current_selection=len(options)-1
                else:
                    current_selection-=1

            elif key == curses.KEY_DOWN:
                #  opcion >= comandos.size() ? opcion = 1 : opcion += 1;
                if current_selection>=len(options)-1:
                    current_selection=0
                else:    
                    current_selection += 1
                
            elif key == ord('\n'):
                stdscr.addstr(len(options) + 1, 0, f"You selected: {options[current_selection]}")
                stdscr.refresh()
                stdscr.getch()
                return options[current_selection]

            stdscr.refresh()

    return curses.wrapper(main)
    

