# coding=utf-8
import pygame
import time 
import random
import time
from playsound import playsound
from pac import *
from maplvl1 import *
from ennemy import *

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
dark_red = (120, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
g70 = (70, 70, 70)
yellow = (255, 255, 102)
green = (0, 255, 0)
purple = (200, 0, 255)
cyan = (0, 120, 255)
gray = (50, 50, 50)
background=(20, 10, 95)

color = [red, white, yellow, green, purple]

dis_width = 1800
dis_height = 800
screen = pygame.display.set_mode((dis_width,dis_height), pygame.DOUBLEBUF)
pygame.display.set_caption('Pacman')

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
speed_font = pygame.font.SysFont("comicsansms", 21)

def Board(pac, best_score):
	value = score_font.render("Score : " + str(pac.score), True, yellow)
	screen.blit(value, [100, 740]) 
	value = score_font.render("Life : " + str(pac.life), True, red)
	screen.blit(value, [350, 740]) 
	value = score_font.render("Best Score : " + str(best_score), True, red)
	screen.blit(value, [500, 740]) 

def play_ready():
    playsound("./sound/pacman_beginning.wav")



def gameloop():

	game_over = False

	maplvl = MapLvl1()
	maplvl.create_gem()
	
	#Init player
	pac = Pacman()

	dghostb = 0
	dghostout = 0

	ghostb = Ennemy()
	ghostout = EnnemyA()
	ghostout.find_pac(maplvl, pac, 1)

	t1 = threading.Thread(target=play_ready)
	t1.start()

	freeze_game = 0
	restart_game = 0
	end_game= 0
	eat_all_gem = 0

	best_score = 0

	time_bonus = pygame.time.get_ticks()

	move_up= move_down=move_left = move_right = 0
	
	while not game_over:

		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				game_over = True

			elif event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_UP:
					if pac.start:
						pac.move_up = 1

					move_up = 1
					move_down= move_left = move_right = 0

					

					pac.start = 0
				elif event.key == pygame.K_DOWN:
					if pac.start:
						pac.move_down = 1

					move_down=1
					move_up=move_left = move_right = 0
			
					

					pac.start = 0
				elif event.key == pygame.K_LEFT:
					if pac.start:
						pac.move_left = 1

					move_left = 1
					move_up= move_down=move_right = 0

					
				
					pac.start = 0
				elif event.key == pygame.K_RIGHT:
					if pac.start:
						pac.move_right = 1

					
					move_right = 1
					move_up= move_down=move_left =0
								
					pac.start = 0

			elif event.type == pygame.KEYUP:	
				move_up= move_down=move_left = move_right = 0

				if event.key == pygame.K_SPACE:
					if freeze_game and not end_game:

						freeze_game = 0
						pac.death = 0
						restart_game = 1

						if dghostb:
							ghostb = Ennemy()

						if dghostout:
							ghostout = EnnemyA()
							ghostout.find_pac(maplvl, pac, 1)

						dghostb = 0
						dghostout = 0

					if end_game:
						tb = 10000 * (180000 / time_bonus) * eat_all_gem
						best_score = max(best_score, pac.score +  pac.life * 500 + tb)
						maplvl = MapLvl1()
						maplvl.create_gem()
	
						#Init player
						pac = Pacman()

						dghostb = 0
						dghostout = 0

						ghostb = Ennemy()
						ghostout = EnnemyA()
						ghostout.find_pac(maplvl, pac, 1)

						t1 = threading.Thread(target=play_ready)
						t1.start()

						freeze_game = 0
						restart_game = 0
						end_game= 0
						eat_all_gem = 0
						time_bonus = pygame.time.get_ticks()


		if not freeze_game:			
			if move_up:
				pac.change_dir(maplvl, 0)
			elif move_down:
				pac.change_dir(maplvl, 1)
			elif move_left:
				pac.change_dir(maplvl, 2)
			elif move_right:
				pac.change_dir(maplvl, 3)

		screen.fill(background)

		screen.blit(maplvl.get_display(), (0, 0))

		maplvl.draw_gem(screen)
		
		if not freeze_game:
			frz = 0
			if restart_game: frz = 1
			pac.update_pos(maplvl, frz)

		if maplvl.eat_gem(pac):
			end_game = 1
			freeze_game = 1
			eat_all_gem = 1

		pac.display(screen)

		if not freeze_game:
			frz = 0
			if restart_game: frz = 1
			ghostb.update_pos(maplvl, frz)
			if ghostb.death_pac(pac):
				dghostb = 1
		ghostb.draw(screen)
			
		ghostout.find_pac(maplvl, pac, 0)
		if not freeze_game:
			frz = 0
			if restart_game: frz = 1
			r = ghostout.update_pos(maplvl, frz)
			if r == -1:
				ghostout.find_pac(maplvl, pac, 1)
			if ghostout.death_pac(pac):
				dghostout = 1
		ghostout.draw(screen)

		if pac.death:
			freeze_game = 1
			if pac.life == 0:
				end_game = 1

		restart_game = 0

		Board(pac, best_score)

		pygame.display.flip()

		
	pygame.quit()
	quit()


gameloop()