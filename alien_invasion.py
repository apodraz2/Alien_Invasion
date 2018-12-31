import sys

import pygame

import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

def run_game():
	# Initialize pygame, settings and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	
	# Make an alien.
	alien = Alien(ai_settings, screen)
	
	# Start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		bullets.update()
		gf.update_bullets(bullets)
		ship.update()
		gf.update_screen(ai_settings, screen, ship, alien bullets)	
		

run_game()
