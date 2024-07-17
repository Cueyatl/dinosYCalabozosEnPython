import os
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def navigate_menu(options):
    current_selection = 0

    while True:
        clear_screen()
        
        # Display the options
        for idx, option in enumerate(options):
            if idx == current_selection:
                print(f"> {option}")
            else:
                print(f"  {option}")

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up' and current_selection > 0:
                current_selection -= 1
            elif event.name == 'down' and current_selection < len(options) - 1:
                current_selection += 1
            elif event.name == 'enter':
                return options[current_selection]

# Example usage
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
selected_option = navigate_menu(options)
print(f"Selected option: {selected_option}")
def fname(arg):
    return alp