#3d model
from ursina import *
from pynput import keyboard
import speech_recognition as sr
import random

random_generator = random.Random()      # Create a random number generator
app = Ursina()

truman = Entity(model = 'model.dae', color = color.white, scale=(2,2,2))

window.color = color.gray
window.fullscreen = False
window.exit_button.visible = True
window.borderless = False
CAMERA_SPEED = 5
def update():
    truman.rotation_x += time.dt * 20    
    truman.rotation_y += time.dt * 20             
    if held_keys['w']:                                          # If q is pressed
        camera.position += (0, time.dt * CAMERA_SPEED, 0)       # move camera up
    if held_keys['s']:                                          # If a is pressed
        camera.position -= (0, time.dt * CAMERA_SPEED, 0)       # move camera down
    if held_keys['d']:                                          # If d is pressed
        camera.position += (time.dt * CAMERA_SPEED, 0, 0)       # move camera right
    if held_keys['a']:                                          # If a is pressed
        camera.position -= (time.dt * CAMERA_SPEED, 0, 0)       # move camera left
    if held_keys['q']:                                          # If d is pressed
        camera.position += (0, 0, time.dt * CAMERA_SPEED)       # move camera right
    if held_keys['e']:                                          # If a is pressed
        camera.position -= (0, 0, time.dt * CAMERA_SPEED)       # move camera left
def input(key):
    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        truman.color = color.rgb(red, green, blue)
    if key =='control':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        window.color = color.rgb(red, green, blue)
    if key == '`':
        exit()
    if key == '/':
        val = (input("Enter Your Command"))
        print (val)

descr = dedent('''
      <scale:1.5><orange>Controls:<default><scale:1>
      Pressing Control Will Change The Background Color
      Pressing Space Will Change The Object Color
      Pressing / Will Have You Manually Enter The Command
      WASD To Move Camera Angle
      Q To Enlarge and E to Shrink''').strip()
Text.default_resolution = 1080 * Text.size
test = Text(text=descr, origin=(0,0), background=True)
test.x = 0.0
test.y = 0.4

app.run()