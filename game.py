import pygame
import config
import os

pygame.init()

info = pygame.display.Info() 
screen_width, screen_height = info.current_w, info.current_h

class vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

with open(config.NAMEFILENAME,'r') as n:
    if n.read() == '':
        config.HASNAME = True
    else:
        config.HASNAME = False
    n.close()

RUNNING = True
clock = pygame.time.Clock()
FPS = config.GMAXFPS

if open(str(config.NAMEFILENAME),'r').read() == '':
    cmdstr = 'python '+str(config.NINFILENAME)
    os.system(cmdstr)

x = 200
y = 200

speed = 10

ds = pygame.display.set_mode((screen_width, screen_height))

alpha = pygame.image.load('textures/alpha.png').convert_alpha()
alpha_rect = alpha.get_rect(width=screen_width, height=screen_height)

bg_new = pygame.transform.scale(pygame.image.load('textures/shit_map.png').convert(), (screen_width, screen_height))
bg_new_r = bg_new.get_rect(x=0, y=0)

car_main = pygame.transform.scale(pygame.image.load('textures/preview.jpg').convert_alpha(), (125//2, 250//2,)).convert()
car_main.set_colorkey("#fffaaa")
car_left = pygame.transform.rotate(car_main, 90)
car_right = pygame.transform.rotate(car_main, -90)
car_down = pygame.transform.rotate(car_main, 180)
car_rect = car_main.get_rect(x=x,y=y)
car_vector = vector()
car = car_main
font = pygame.font.SysFont("Anime Ace v3", 18)

def toPreInt(num: float, coef: float, minimal: float):
    if abs(num - num * coef) <=minimal:
        return 0
    return num - num * coef

def costrator(num, t=3):
    if str(num).find('.')==-1:
        return num
    return float(str(num)[:str(num).find('.')+t-1])
def speedCheck(v:vector, maxspeed):
    if v.x > maxspeed:
        v.x = maxspeed

    if v.x < -maxspeed:
        v.x = -maxspeed
    
    if v.y > maxspeed:
        v.y = maxspeed

    if v.y < -maxspeed:
        v.y = -maxspeed
def additionalKeysTrapper(keys, speed, FPS):
    state = True
    if keys[pygame.K_LSHIFT]:
            speed += 1
    elif keys[pygame.K_LCTRL]:
            speed -= 1
    elif keys[pygame.K_UP]:
        FPS += 1
    elif keys[pygame.K_DOWN]:
        FPS -= 1
    if keys[pygame.K_g] or keys[pygame.K_ESCAPE]:
        state = False
    return speed, FPS, state
def moveKeyTrapper(keys, car, car_vector, speed=1, speedCoeff=0.5):
    keyWasPressed = False
    if keys[pygame.K_w] and y > 0:
        car = car_main
        car_vector.y -= speed * speedCoeff
        keyWasPressed = True
    if keys[pygame.K_s] and y < screen_height:
        car = car_down
        car_vector.y += speed * speedCoeff
        keyWasPressed = True
    if keys[pygame.K_d]  and x < screen_width :
        car = car_right
        car_vector.x += speed * speedCoeff
        keyWasPressed = True
    if keys[pygame.K_a] and x > 9:
        car = car_left
        car_vector.x -= speed * speedCoeff
        keyWasPressed = True
    return car, keyWasPressed
x = 100
y = 100
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    keyWasPressed = False
    position = str("X: "+ str(x)+ ", Y: "+ str(y))
    framespersec = str('fps: '+str(int(clock.get_fps()))+', max fps: '+str(FPS))

    pos = font.render(position, False, '#ffffff','#000000')
    pos_rect = pos.get_rect(x=0, y=0)

    fps = font.render(framespersec, False, '#ffffff','#000000')
    fps_rect = fps.get_rect(x=0, y=18)

    car, keyWasPressed = moveKeyTrapper(pygame.key.get_pressed(), car, car_vector, speed, 0.3)
    speed, FPS, RUNNING = additionalKeysTrapper(pygame.key.get_pressed(), speed, FPS)
    speedCheck(car_vector, speed)
    
    print(car_vector.x, car_vector.y,sep='    ')
    
    if keyWasPressed:
        car_vector.x = toPreInt(costrator(car_vector.x), 0.05, 0.32)
        car_vector.y = toPreInt(costrator(car_vector.y), 0.05, 0.32)
    if x + car_vector.x > 20 and x + car_vector.x < screen_width:
        x += car_vector.x
    if y + car_vector.y > 60  and y + car_vector.y < screen_height:
        y += car_vector.y

    x = costrator(x)
    y = costrator(y)

    car_rect.centerx = x
    car_rect.centery = y

    ds.blit(car, car_rect)
    ds.blit(bg_new, bg_new_r)
    ds.blit(pos, pos_rect)
    ds.blit(fps, fps_rect)
    ds.blit(car, car_rect)
    pygame.display.update()
    ds.blit(car, car_rect)

    clock.tick(FPS)