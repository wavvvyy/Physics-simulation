import pymunk

FPS = 120
screen_size = (800,800)

apple_data = {
    'mass': 1, 
    'inertia': 100, 
    'body_type': pymunk.Body.DYNAMIC,
    'radius': 50,
    'color': (255,0,0)
}

ball_data = {
    'mass': 1, 
    'inertia': 100, 
    'body_type': pymunk.Body.STATIC,
    'radius': 30,
    'color': (130,130,130)
}