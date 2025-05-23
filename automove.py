import keyboard
import time
import mouse

# Variable de contrôle pour arrêter le programme
stop_program = False
delay = 2

delay = float(input("Enter the delay in seconds : "))

print(f"The delay is {delay} seconds.")

def on_key_event(event):
    global stop_program
    if event.name == 'f2':
        stop_program = True


keyboard.on_press(on_key_event)

print("Press F1 to start the program, and F2 to stop.")
keyboard.wait('f1')
print("Start.")

while not stop_program:
    mouse.move(25,25, absolute=False, duration=1)
    mouse.move(-25,-25, absolute=False, duration=1)
    time.sleep(delay)

print("Stop.")
