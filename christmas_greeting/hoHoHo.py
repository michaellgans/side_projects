"""
Plays a holiday themed .mp3
Prints the days until Christmas!
"""

from datetime import datetime
import pygame
import time

current_date_time = datetime.now()
current_date = current_date_time.strftime("%d")

print()
print("----------------------------------")
print()

print("Initializing Pygame")
pygame.mixer.init()

print("Loading MP3 file")
pygame.mixer.music.load("./chimes.mp3")

print("Playing MP3 file")
pygame.mixer.music.play()

""" Display for User """
print()
print("----------------------------------")
print()

print(f"Today is December {current_date}!\n")
time.sleep(3)
print("You know what that means?\n")
time.sleep(3)

days = (25 - int(current_date))

print(f"There are {days} days until Christmas!!")

time.sleep(3)

print("Hope you were good ;)")

# Wait for the music to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

print()
print("----------------------------------")
print()

print("Quitting Pygame!\nGoodbye!")
pygame.mixer.quit()
pygame.quit()
