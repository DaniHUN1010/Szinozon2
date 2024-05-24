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
color = (200, 75, 75)
rect = (50, 50, 310, 130)
S_betu = FONT.render("S", 1, (0, 0, 0))
Z1_betu = FONT.render("Z", 1, (100, 20, 20))
I_betu = FONT.render("Í", 1, (200, 10, 10))
N1_betu = FONT.render("N", 1, (140, 123, 120))
Ö1_betu = FONT.render("Ö", 1, (130, 111, 200))
Z2_betu = FONT.render("Z", 1, (100, 21, 200))
Ö2_betu = FONT.render("Ö", 1, (100, 220, 110))
N2_betu = FONT.render("N", 1, (100, 2, 120))

def draw(elapsed_time):
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(S_betu, (10, 10))
    WINDOW.blit(Z1_betu, (30, 10))
    WINDOW.blit(I_betu, (50, 9))
    WINDOW.blit(N1_betu, (60, 10))
    WINDOW.blit(Ö1_betu, (82, 9))
    WINDOW.blit(Z2_betu, (105, 10))
    WINDOW.blit(Ö2_betu, (122, 9))
    WINDOW.blit(N2_betu, (145, 10))
    pygame.draw.rect(WINDOW, color, rect)  # Téglalap rajzolása
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
    
