import sys, pygame, pymunk
from settings import *

def createObect(space, position, data):
	body = pymunk.Body(data['mass'], data['inertia'], body_type = data['body_type'])
	body.position = position
	shape = pymunk.Circle(body, data['hitbox'])
	
	space.add(body, shape)
	return shape

def drawObject(obj_list, data):
	for obj in obj_list:
		pos_x = int(obj.body.position.x)
		pos_y = int(obj.body.position.y)
		if data['path']:
			rect = apple_surface.get_rect(center = (pos_x,pos_y))
			screen.blit(apple_surface,rect)
		else:	
			pygame.draw.circle(screen, data['color'],(pos_x,pos_y), data['radius'])

def GameLoop():
	drawObject(apples, apple_data)
	drawObject(balls, ball_data)

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0,500)

apples = []
balls = []

apple_surface = pygame.transform.scale(pygame.image.load('apple.png'),(apple_data['radius']*2,apple_data['radius']*2))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				apples.append(createObect(space, event.pos, apple_data))
			
			elif pygame.mouse.get_pressed()[2]:
				balls.append(createObect(space, event.pos, ball_data))

	screen.fill((217,217,217))
	GameLoop()
	space.step(1/50)
	pygame.display.update()
	clock.tick(FPS)