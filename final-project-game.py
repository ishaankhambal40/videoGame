# Creating a baseball game 
# Make a one inning game with different results on what the player can do


#importing libraries
import sys
import random
import time

#giving the option to play in the game 
playing = 'y'

#option to agree to play the game or too not continue to play the game
yes = ('y','yes')
no = ('n', 'no')

#Setting the final results of the game loss tie and win
loses = 0
ties = 0

# Pitching and defensive settings
strikes = 0
balls = 0
fouls = True

# Only one type of pitch with is the fastball
pitches = 0
