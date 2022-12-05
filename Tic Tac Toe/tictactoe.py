import pygame
pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic Tac Toe (. .)")
block_size = 200

move_left = False
move_right = False
move_up = False
move_down = False

# define colors 
white = (255,255,255)
green = (100,255,100)
red_lower = (255,100,100)

# turns 
turn = 0
x = 0
y = 0

def Drawing_Grids():
    for i in range(1,3):
        pygame.draw.line(screen,white,(0,block_size*i),(screen_width,block_size*i),2)
        pygame.draw.line(screen,white,(block_size*i,0),(block_size*i,screen_height),2)

def Draw_shapes(x,y,turn):
    if turn == 0:
        # drawing circle 
        pygame.draw.circle(screen, green, (x,y), 50,10)
        turn = 1
    
    elif turn == 1:
        # drawing cross 
        pygame.draw.line(screen,red_lower,(x-50,y-50),(x+50,y+50),10)
        pygame.draw.line(screen,white,(x+50,y-50),(x-50,y+50),10)

        turn = 0
    
    
    return turn


run = True
while run:
    Drawing_Grids()
    pos = pygame.mouse.get_pos()

    if pos[0] < 200:
        x = 100
    elif pos[0] < 400 and pos[0] > 200:
        x = 300
    elif pos[0] < 600 and pos[0] > 400:
        x = 500
    
    if pos[1] < 200:
        y = 100
    elif pos[1] < 400 and pos[1] > 200:
        y = 300
    elif pos[1] < 600 and pos[1] > 400:
        y = 500
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            turn = Draw_shapes(x, y,turn)
            
    pygame.display.update()

pygame.quit()