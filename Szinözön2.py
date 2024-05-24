import pygame
import random
import time
pygame.font.init()
pygame.init()
WIDTH, HEIGHT = 700, 850
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = pygame.time.Clock()
BG = pygame.transform.scale(pygame.image.load("hatterkep.png"), (WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Calibri", 30, bold = True)
start_time = time.time()
elapsed_time = 0
pygame.display.set_caption("Színözön2")
color = (186, 56, 56)
rect_1 = (195, 440, 310, 130)  #középső gomb
rect_2=(195, 270, 310, 130)    #felső gomb
rect_3=(195, 610, 310, 130)    #alsó gomb

def draw(elapsed_time):
    WINDOW.blit(BG, (0, 0))
    pygame.draw.rect(WINDOW, color, rect_1)  # Téglalap rajzolása
    pygame.draw.rect(WINDOW, color, rect_2)  # Téglalap rajzolása
    pygame.draw.rect(WINDOW, color, rect_3)  # Téglalap rajzolása
    pygame.display.update()
    time_text = FONT.render(f"Idő: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))
# Ha nyert vagy vesztett, akkor írja ki az időt! 
def main():
    run = True
    while run:
        FPS.tick(60)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(elapsed_time)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
