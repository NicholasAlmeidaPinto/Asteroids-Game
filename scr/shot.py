import math
from settings import Settings

class Shot:
	def __init__(self, angle, pos_x, pos_y):
		self.ang = -angle
		self.pos_x = pos_x
		self.pos_y = pos_y

	def check_border(self):
		self.new_pos()
		if self.pos_x < 0.0:
			return False
		if self.pos_x > Settings.width:
			return False
		if self.pos_y < 0.0:
			return False
		if self.pos_y > Settings.height:
			return False
		return True

	def new_pos(self):
		self.pos_x += Settings.shot_vel * math.cos(math.radians(self.ang))
		self.pos_y += Settings.shot_vel * math.sin(math.radians(self.ang))


