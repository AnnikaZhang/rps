import pygame
from random import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 72)
smallfont=pygame.font.SysFont('Comic Sans MS', 20)
display_width = 800
display_height = 600
white=(255,255,255)
size=100
decided=False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rock, Paper, Scissors')

clock = pygame.time.Clock()

unknown_image=pygame.image.load('unknown.png')
unknown_image=pygame.transform.scale(unknown_image,(size,size))
rock_image=pygame.image.load('rock.png')
rock_image=pygame.transform.scale(rock_image, (size, size))
paper_image=pygame.image.load('paper.png')
paper_image=pygame.transform.scale(paper_image, (size, size))
scissor_image=pygame.image.load('scissor.png')
scissor_image=pygame.transform.scale(scissor_image, (size, size))
def rock(x,y):
    gameDisplay.blit(rock_image, (x,y))

def paper(x,y):
    gameDisplay.blit(paper_image, (x,y))

def scissor(x,y):
    gameDisplay.blit(scissor_image, (x,y))

def unknown(x,y):
    gameDisplay.blit(unknown_image,(x,y))

def move(num):
    if(num<1/3):
        rock(200,200)
    elif (num<2/3):
        paper(200,200)
    else:
        scissor(200,200)

def victory():
    textsurface = myfont.render('Victory  :)', False, (255, 0, 0))
    gameDisplay.blit(textsurface,(300,400))

def lost():
    textsurface = myfont.render('Lost  :(', False, (0, 0, 255))
    gameDisplay.blit(textsurface,(300,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYUP:
            num=random()
            gameDisplay.fill(white)
            text=smallfont.render("(My Move)",False, (0,0,0))
            gameDisplay.blit(text,(400,150))            
            if event.key==pygame.K_r:
                rock(400,200)
                move(num)
                if (num>=2/3):
                    victory()
                if (num>=1/3 and num<2/3):
                    lost()
            elif event.key==pygame.K_p:
                paper(400,200)
                move(num)
                if (num<1/3):
                    victory()
                if (num>=2/3):
                    lost()
            elif event.key==pygame.K_s:
                scissor(400,200)
                move(num)
                if (num<2/3 and num>=1/3):
                    victory()
                if (num<1/3):
                    lost()
            elif event.key==pygame.K_q:
                pygame.quit()
                quit()
            else:
                unknown(400,200)
                unknown(200,200)
                rock(700, 0)
                paper(700,200)
                scissor(700,400)
            pygame.display.update()
            clock.tick(60)
        else:
            gameDisplay.fill(white)
            rock(700, 0)
            paper(700,200)
            scissor(700,400)
            unknown(200,200)
            unknown(400,200)
            pygame.display.update()
            clock.tick(60)

pygame.quit()
quit()    



