import pygame
from settings import Settings
from ship import Ship
from shot import Shot
from asteroid import Asteroid
import time



def check_hits(asteroids, shots):
	idxs_ast = []
	idxs_sht = []
	count = 0
	for idx_shts, shot in enumerate(shots):
		for idx_atr, asteroid in enumerate(asteroids):
			if(asteroid.check_hit(shot.pos_x, shot.pos_y)):
				asteroids.pop(idx_atr)
				shots.pop(idx_shts)
				count += 1

	return asteroids, shots, count

def check_game_over(asteroids, ship):
	rect = ship.rotated_image_rect
	for asteroid in asteroids:
		if (asteroid.check_hit(rect.topleft[0], rect.topleft[1])):
			return True
		if (asteroid.check_hit(rect.topright[0], rect.topright[1])):
			return True
		if (asteroid.check_hit(rect.bottomleft[0], rect.bottomleft[1])):
			return True
		if (asteroid.check_hit(rect.bottomright[0], rect.bottomright[1])):
			return True

	return False


def game():
	score = 0
	pygame.init()

	ship = Ship()

	screen = pygame.display.set_mode((Settings.width,Settings.height))
	clock = pygame.time.Clock()

	shots = []
	asteroids = []
	last_shot = 0

	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 20)

	while(True):
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				raise SystemExit

		pressed_key = pygame.key.get_pressed()
		if pressed_key[pygame.K_LEFT]: 
		    ship.rotate_left()         
		if pressed_key[pygame.K_RIGHT]:
		    ship.rotate_right()
		if pressed_key[pygame.K_UP]:
		    ship.accelerate()
		if pressed_key[pygame.K_SPACE]:
			if(time.time()-last_shot > Settings.shot_delay):
				shots.append(Shot(ship.ang, ship.pos_x, ship.pos_y))
				last_shot = time.time()


		# bullets
		for index, sht in enumerate(shots):
			if not sht.check_border():
				shots.pop(index)


		for sht in shots:
			pygame.draw.circle(screen, (255,255,255), (sht.pos_x, sht.pos_y), 5)

		if (len(asteroids) < 10):
			asteroids.append(Asteroid(ship.pos_x, ship.pos_y))

		for ast in asteroids:
			ast.upd_pos()
			pygame.draw.circle(screen, (255,255,255), (ast.pos_x, ast.pos_y), ast.radius)

		asteroids, shots, new_score = check_hits(asteroids, shots)
		score += new_score
		textSurface = myfont.render('Pontuacao: ' + str(score), False, (0,255,0))
		if check_game_over(asteroids, ship):
			print('GAME OVER!')
			print('Pontuacao: ' + str(score) + ' asteroides!')
			break
		img, pos = ship.img()
		screen.blit(textSurface, (0,0))
		screen.blit(img, pos)

		pygame.display.flip()
		clock.tick(60)


if __name__ == '__main__':
	game()
