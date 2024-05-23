import pygame
import random
pygame.init()
WIDTH, HEIGHT = 700, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Színözön2")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
