import pygame
import random
pygame.init()
WIDTH, HEIGHT = 700, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()
BG = pygame.transform.scale(pygame.image.load("placeholder.jpg"), (WIDTH, HEIGHT))
pygame.display.set_caption("Színözön2")

def draw():
    WINDOW.blit(BG, (0, 0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        FPS.tick(60)
        draw()
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
