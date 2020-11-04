import pygame
import os

#Constants
WIDTH = 800
HEIGHT = 600
FPS = 30

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 235)

#Asset Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

#Player Class
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder,"slime1.png")).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)
		self.y_speed = 5

	def update(self):
		keystate = pygame.key.get_pressed()

		if keystate [pygame.K_RIGHT]:
			self.rect.x += 5
		if keystate [pygame.K_LEFT]:
			self.rect.x += -5
		if keystate [pygame.K_UP]:
			self.rect.y += -5
		if keystate [pygame.K_DOWN]:
			self.rect.y += 5

#Initalize Variables
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('The Platformer')

clock = pygame.time.Clock()

#Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#Game Loop

#Process Events
running = True

while running:

	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

#Update
	all_sprites.update()

#Draw
	screen.fill(SKYBLUE)
	all_sprites.draw(screen)

#Flip
	pygame.display.flip()


pygame.quit()