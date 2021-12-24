import math
from settings import Settings
import random

class Asteroid:
	def __init__(self, ship_pos_x, ship_pos_y):
		self.radius = 50
		self.start_pos(ship_pos_x, ship_pos_y)

	def start_pos(self, ship_pos_x, ship_pos_y):
		self.pos_x = random.uniform(0,Settings.width)
		self.pos_y = random.uniform(0,Settings.height)
		self.ang = random.uniform(0,360)

	def upd_pos(self):
		self.pos_x += Settings.asteroid_vel * math.cos(math.radians(self.ang))
		self.pos_y += Settings.asteroid_vel * math.sin(math.radians(self.ang))


		if self.pos_x < 0.0:
			self.pos_x = Settings.width
		if self.pos_x > Settings.width:
			self.pos_x = 0.0
		if self.pos_y < 0.0:
			self.pos_y = Settings.height
		if self.pos_y > Settings.height:
			self.pos_y = 0.0

	def check_hit(self, x, y):
		if((x-self.pos_x)**2 + (y-self.pos_y)**2 < self.radius**2):
			return True
		return False
