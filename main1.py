import pygame

pygame.init()
Screen_Width , Screen_Height = 500 , 500

display_surface = pygame.display.set_mode((Screen_Width , Screen_Height))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transform.scale(pygame.image.load('image copy.png').convert() , (Screen_Height , Screen_Width))

penguin_image = pygame.transform.scale(pygame.image.load('imagee.png').convert_alpha() , (200,200))

penguin_rect = penguin_image.get_rect(center=(Screen_Width // 2, Screen_Height// 2 - 30))

text = pygame.font.Font(None , 36).render('Hello World' , True, pygame.Color('black'))

text_rect = text.get_rect(center=(Screen_Width // 2 , Screen_Height // 2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image , (0, 0))
        display_surface.blit(penguin_image , penguin_rect)
        display_surface.blit(text , text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
