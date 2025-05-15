# Ivan N. presenting....
# Snake in Trinket
# Todo:
# Death screen
# Restart after death
# Score counter?
# Speed up as time goes on?

# Setup:
import turtle # Turtle library
import random # Random number library
import math # Maths operations library
tommy = turtle.Turtle() # Define turtle tommy
tommy.speed(10000) # Turtle speed
screen = turtle.Screen() # Initialize screen for keyboardIn
drawncells = [] # Create list storing snake body locations
border = [] # Create list storing border locations
startlength = 4 # Snakes length
looprunning = True # Needed for main loop to run, used for stopping game
applepos = None # Initialize tuple holding apple position

# Functions:
def cell(): # Define function draw cell
  tommy.forward(5)
  tommy.right(90)
  tommy.backward(5) # Move from arbitrary center to corner
  tommy.begin_fill() # Color start
  for i in range(4): # For loop repeating 4 times
    tommy.forward(10) # 1 Wall of a cell
    tommy.right(90) # 1 Corner of a cell
  tommy.end_fill()
  tommy.penup() # Color stop
  tommy.forward(5)
  tommy.left(90)
  tommy.backward(5) # Move back from corner to center
  
def delcell(): # Define function delete cell
  tommy.forward(6)
  tommy.right(90)
  tommy.backward(6) # Move from arbitrary center to corner but 1 further to erase all
  tommy.begin_fill() # EColor start
  for i in range(4): # For loop repeating 4 times
    tommy.forward(12) # 1 Wall of a cell
    tommy.right(90) # 1 Corner of a cell
  tommy.end_fill()
  tommy.penup() # Color stop
  tommy.forward(6)
  tommy.left(90)
  tommy.backward(6) # Move back from corner to center
  
def gameover(): # Define game over function
  global looprunning # Fetch boolean looprunning defined in setup
  looprunning = False # Disallow loop from executing next time
  
def trim(currentpos): # Define function trimming worm tail, currentpos set in main loop
  if len(drawncells) > startlength: # If snake body is longer than snake length
    oldest_pos = next(iter(drawncells)) # Get first cords of drawncells, place in tuple oldest_pos
    tommy.goto(oldest_pos) # Go to first position from drawncells which is snake tail
    tommy.fillcolor("white") # Set color to white for erasing
    delcell() # Call function delete cell
    tommy.fillcolor("black") # Set color back to black
    tommy.goto(currentpos) # Go back to current head position set in main loop
    oldest_pos = drawncells.pop(0) # Remove first position from drawncells list

def apple(): # Define apple function
  global applepos # Fetch tuple applepos, currently empty
  currentpos = (round(tommy.xcor()), round(tommy.ycor())) # set currentpos again so turtle can go back after apple
  while True: # While true loop generates apple positions until valid is found
      applepos = (random.randint(-19, 19)*10, random.randint(-19, 19)*10) # Set random x,y value from -190 to 190 rounded to 10
      if applepos not in drawncells and applepos not in border: # Check if apple spawned in player or border
        break # If apple reachable, break out of while true loop
  tommy.goto(applepos) # Go to just defined apple position
  tommy.fillcolor("red") # Set color to red for apple
  tommy.right(90)
  tommy.forward(5)
  tommy.left(90) # Move to side so circle is on center
  tommy.begin_fill() # Color start
  tommy.circle(5) # Draw apple
  tommy.end_fill() # Color stop
  tommy.right(90)
  tommy.backward(5)
  tommy.left(90) # Move back to center
  tommy.fillcolor("black") # Set color back to black
  tommy.goto(currentpos) # Go back to current head position
  
def distance(pos1, pos2): # Define function for finding distance to apple
  return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) # Calculate distance to apple
  
# Keypresses:
def w(): # Define function called when uparrow is hit
  if tommy.heading() == 0 or tommy.heading() == 180: # If facing opposite way
    tommy.setheading(90) # Turn up
def a(): # Define function called when leftarrow is hit
  if tommy.heading() == 90 or tommy.heading() == 270: # If facing opposite way
    tommy.setheading(180) # Turn left
def s(): # Define function called when downarrow is hit
  if tommy.heading() == 180 or tommy.heading() == 0: # If facing opposite way
    tommy.setheading(270) # Turn down
def d(): # Define function called when rightarrow is hit
  if tommy.heading() == 270 or tommy.heading() == 90: # If facing opposite way
    tommy.setheading(0) # Turn right

# Loop
def loop(): # Define main loop function gets called in last line of main loop
  global looprunning, applepos, startlength # Fetch variables & tuples used in main loop
  if looprunning is True: # Only enters the meat of the main loop when looprunning is true
    tommy.forward(10) # Main forward move
    # Apple Eat:
    currentpos = (round(tommy.xcor()), round(tommy.ycor())) # Update currentpos to compare to applepos
    if distance(currentpos, applepos) <= 6: # If distance to apple less than 6 (cell radius +1 tolerance)
      apple() # Call apple function to generate new apple, snake paints over old one
      startlength += 1 # Give length for apple
      
    # Deathcheck:
    if currentpos not in drawncells and currentpos not in border: # If snake not inside itsself or border
      cell() # Draw next snake cell
      drawncells.append(currentpos) # Append new head position to drawncells list
      trim(currentpos) # Call trim function to remove last cell
    else: gameover() # Call gameover function of snake is inside itsself or border
    
    screen.listen() # Listen for keypresses
    screen.ontimer(loop, 600) # Restart loop with delay of 1s --> gamespeed

#    loop() # Call main loop function for starting game
    turtle.mainloop() # Keep window open to listen for keypresses

def reset():
  global drawncells, startlength, looprunning, applepos # Fetch variables & tuples used
  looprunning = False # Stop loop in case game gets reset manually
  drawncells = [] # Reset list storing snake body locations
  startlength = 4 # Snakes length reset
  tommy.setheading(0) # Reset heading in case reset was called mid draw
  tommy.goto(-196,-196) # Go to bottom left inside border
  tommy.fillcolor("white") # Set color white for background, normal is off white, snake left trace
  tommy.begin_fill() # Color start
  for i in range (4): # For loop for drawing square background
    tommy.forward(392) # 1 Wall of background
    tommy.left(90) # 1 Corner of background
  tommy.end_fill() # Color stop
  tommy.goto(0,0) # Move to center for starting game
  applepos = None # Reset tuple holding apple position
  apple() # Call apple function manually to generate first apple position
  tommy.fillcolor("black") # Set color back to black
  looprunning = True # Set looprunning to true for starting game
  loop() # Call main loop function for starting game

# Keypresses:
screen.onkey(w, "Up") # Call w function if uparrow detected
screen.onkey(a, "Left") # Call a function if leftarrow detected
screen.onkey(s, "Down") # Call s function if downarrow detected
screen.onkey(d, "Right") # Call d function if rightarrow detected
screen.onkey(reset, "r")
  
# Draw Background & Border:
tommy.penup() # Color stop
tommy.goto(-200,-200) # Go to bottom left
tommy.fillcolor("black") # Set color black
for i in range (4): # For loop repeats the line 4 times
  for i in range (40): # For loop makes line of 40 cells 
    currentpos = (round(tommy.xcor()), round(tommy.ycor())) # Capture border position for deathcheck
    cell() # Draw cell as border
    border.append(currentpos) # Append just captured border position to list for deathcheck
    tommy.forward(10) # Move forward between border cells
  tommy.left(90) # 1 Corner of border
reset() # Call reset function to start game

# Code by Ivan N.
