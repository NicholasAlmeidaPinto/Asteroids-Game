from settings import Settings
import pygame
import math

class Ship:
	def __init__(self):
		self.vel_x = 0.0
		self.vel_y = 0.0
		self.ang = 90

		self.pos_x = Settings.width/2.0
		self.pos_y = Settings.height/2.0

		self.image = pygame.image.load('..//fig//ship.bmp')
		self.image = pygame.transform.scale(self.image, (40,40))
		self.rotated_image_rect = self.image.get_rect()

	def rotate_left(self):
		self.ang += Settings.ship_acceleration_angle

	def rotate_right(self):
		self.ang -= Settings.ship_acceleration_angle

	def img(self):
		self.newPos()
		image_rect = self.image.get_rect(topleft = (self.pos_x-20, self.pos_y-20))
		offset_center_to_pivot = pygame.math.Vector2((self.pos_x, self.pos_y)) - image_rect.center

		# roatated offset from pivot to center
		rotated_offset = offset_center_to_pivot.rotate(self.ang-90)

		# roatetd image center
		rotated_image_center = (self.pos_x - rotated_offset.x, self.pos_y - rotated_offset.y)

		img = pygame.transform.rotate(self.image, self.ang-90)

		self.rotated_image_rect = img.get_rect(center = rotated_image_center)

		return img, self.rotated_image_rect

	def accelerate(self):
		self.vel_x += Settings.ship_acceleration * math.cos(math.radians(self.ang))
		self.vel_y -= Settings.ship_acceleration * math.sin(math.radians(self.ang))
		if abs(self.vel_x) > Settings.ship_max_vel:
			self.vel_x = Settings.ship_max_vel * self.vel_x / abs(self.vel_x)
		if abs(self.vel_y) > Settings.ship_max_vel:
			self.vel_y = Settings.ship_max_vel * self.vel_y / abs(self.vel_y)


	def newPos(self):
		self.pos_x += self.vel_x
		self.pos_y += self.vel_y

		if self.pos_x < 0.0:
			self.pos_x = Settings.width
		if self.pos_x > Settings.width:
			self.pos_x = 0.0
		if self.pos_y < 0.0:
			self.pos_y = Settings.height
		if self.pos_y > Settings.height:
			self.pos_y = 0.0

