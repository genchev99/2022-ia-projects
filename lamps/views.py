from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.
import json

# from gpiozero import PWMLED 



from time import sleep 

# led = PWMLED(5)
# from tkinter import *

def home(request):
  state = request.POST.get('state')
  state_file_path: Path = Path('button_state.txt')  
  
  if not state_file_path.exists():
    # If the state file doesn't exists we set the led to be off
    state_from_file = False
  else:
    # Otherwiwser we read the file and check for the state
    with open('button_state.txt', 'r') as fd:
      state_from_file = fd.read().strip() == 'true' 
  
  print("state from file: ", state_from_file)
  if state_from_file:
    # If the state is true we light up the led 
    # led.value = 1
    print('Light is on')
  else:
    # If the state is false we stop the led
    # led.value = 0
    print('Light is off')

  return render(request,"home.html", {"button_state": state_from_file})

def toggle(request):
  state_file_path: Path = Path('button_state.txt')  
  state = request.POST["state"]

  # if the toggle button is switched we save the state to a file
  with open(state_file_path, 'w') as fd:
    fd.write(state)

  return HttpResponse('success')
