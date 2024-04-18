import pygame
from src.NitzanimGameFoler.Constants_Buttons import *

pygame.init()
screen = pygame.display.set_mode((360, 640))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
fontAnswers = pygame.font.Font(None, 20)
fontQuestion = pygame.font.Font(None, FONT_SIZE_QUESTION)
fontStatus = pygame.font.Font(None, FONT_SIZE_STATUS)

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
		self.original_y_pos = pos[1]

		# top rectangle
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#1DAAFF'

		# bottom rectangle
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#007AC4'
		#text
		self.text_surf = fontAnswers.render(text, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self, screen):
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#0b5394'
			if pygame.mouse.get_pressed()[0]:
				self.pressed = True
				return True
		else:
			self.dynamic_elevation = self.elevation
			self.top_color = '#475F77'
			return False


class Surface:
	def __init__(self, text, width, height, pos, color, fontSize, fontColor):
		self.text = text
		self.width = width
		self.height = height
		self.pos = pos
		self.font = pygame.font.Font(None, fontSize)

		self.rect = pygame.Rect(pos, (width, height))
		self.color = color

		self.text_surf = self.font.render(text, True, fontColor)
		self.text_rect = self.text_surf.get_rect(center=self.rect.center)


	def draw(self):
		pygame.draw.rect(screen, self.color, self.rect, border_radius= 12)
		screen.blit(self.text_surf, self.text_rect)
