import sys

import pygame

import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
	# Initialize pygame, settings and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Make an alien.
	alien = Alien(ai_settings, screen)
	
	stats = GameStats(ai_settings)
	
	# Start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)	
		

run_game()
