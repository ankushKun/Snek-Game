# Python Snek Game 
import pygame
import random
import time

#PYGAME VARIABLES
width=500
height=500

#COLORS
white=(255,255,255)
black=(0,0,0)
greeen=(0,255,0)
red=(255,0,0)

pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont('monospace',30)
score_font = pygame.font.SysFont('monospace',25)
pygame.display.update()

def rand_food_spawn():
    global food_x
    global food_y
    food_x=random.randrange(10,width-10,10)
    food_y=random.randrange(10,height-10,10)
    
def draw_snake(snake_Head,snake_body):
    for body in snake_body:
        pygame.draw.rect(window,white,[body[0],body[1],snake_Head,snake_Head])
        
def show_score():
    sco = score_font.render(f'LENGTH : {length_snake}',True,greeen)
    window.blit(sco,[0,0])
    
def Exit_Menu():
    sco = score_font.render(f'LENGTH : {length_snake}       GAME OVER',True,greeen)
    window.blit(sco,[0,0])
    pygame.display.update()
    time.sleep(2)
    _exit=True
    while _exit:
        window.fill(black)
        GO = font_style.render('  GAME OVER   ',True,greeen)
        T1 = font_style.render('PLAY AGAIN : P',True,greeen)
        T2 = font_style.render('   EXIT    : X',True,greeen)
        window.blit(GO,[110,180])
        window.blit(T1,[110,220])
        window.blit(T2,[110,260])
        # Pygame events
        for event in pygame.event.get():
            # Check for exit
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_game()
                elif event.key == pygame.K_x:
                    exit()
        pygame.display.update()
    
def play_game():
    # Food Variables
    global food_x
    global food_y
    
    food_x=random.randrange(10,width-10,10)
    food_y=random.randrange(10,height-10,10)
    
    #SNAKE VARIABLES
    direction='STOP'
    snake_head_size=10

    x_move=0
    y_move=0

    x_pos=width/2
    y_pos=height/2

    speed=10

    snake_body=[]
    global length_snake
    length_snake=1
    
    Running=True
    while Running:
        window.fill(black)
        
        # Pygame events
        for event in pygame.event.get():
            # Check for exit
            if event.type == pygame.QUIT:
                Exit_Menu()
            # Check for keypresses and move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direction!='RIGHT':
                    direction='LEFT'
                    x_move=-speed
                    y_move=0
                if event.key == pygame.K_d and direction!='LEFT':
                    direction='RIGHT'
                    x_move=speed
                    y_move=0
                if event.key == pygame.K_w and direction!='DOWN':
                    direction='UP'
                    y_move=-speed 
                    x_move=0
                if event.key == pygame.K_s and direction!='UP':
                    direction='DOWN'
                    y_move=speed
                    x_move=0
                    
        # Check if out of boundary
        if x_pos<=0 or x_pos>=500 or y_pos<=0 or y_pos>=500:
            Exit_Menu()
            print('>>> OUT OF BOUNDARY')
        
        # Check if head collided with food
        if x_pos == food_x and y_pos ==  food_y:
            print('>>> ATE FOOD')
            length_snake+=1
            rand_food_spawn()
            
        x_pos += x_move
        y_pos += y_move
        
        # Make the snake body
        snake_head=[]
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snake_body.append(snake_head)
        
        if len(snake_body) > length_snake:
            del snake_body[0]
            
        # Check collisions with the body
        for body in snake_body[:-1]:
            if body == snake_head :
                print('>>> ATE YOURSELF')
                Exit_Menu()
                
        draw_snake(10,snake_body)
        pygame.draw.rect(window,red,[food_x,food_y,10,10])#draws food
        show_score()# displays the score
        pygame.display.update()
        
        clock.tick(15)

play_game()
    
pygame.quit()
quit()
