from string import whitespace
import pygame
import sys
from textboxes import InputBox

pygame.init()
gameclock = pygame.time.Clock()
# screen setting
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ancestry")
# general fonts
font = pygame.font.SysFont(None, 30)
# general colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (13, 14, 46)
# textbox colors
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    running = True

    while running:
        screen.fill(BACKGROUND)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect((480, 540), (100, 50))
        button_2 = pygame.Rect((780, 540), (100, 50))
        if button_1.collidepoint((mx, my)):
            if click:
                GenomeSequencer()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, (171, 219, 227), button_1)
        pygame.draw.rect(screen, (171, 219, 227), button_2)
        # text for button_1
        draw_text("PLAY", font, (255, 255, 255), screen, 500, 555)
        draw_text("OPTIONS", font, (255, 255, 255), screen, 780, 555)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        gameclock.tick(60)


def GenomeSequencer():
    running = True
    name_box = InputBox(120, 95, 30, 30)
    country_box = InputBox(450, 95, 30, 30)
    genome_box = InputBox(850, 95, 30, 30)
    # testcase displaybox adds int from namebox and country box and displays result
    display_box = InputBox(640, 500, 30, 30)
    NewEntryInputBoxes = [name_box, country_box, genome_box, display_box]
    while running:
        screen.fill('#0d0e2e')
        #screen.blit(BACKGROUND, (0, 0))
        draw_text('Enter your data:', font, WHITE, screen, 20, 20)
        # name text and textbox
        draw_text('Name:', font, WHITE, screen, 50, 100)
        draw_text('Country:', font, WHITE, screen, 350, 100)
        draw_text('Genome Sequence:', font, WHITE, screen, 660, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_RETURN:
                    if len(name_box.text) == 0 or len(country_box.text) == 0 or len(genome_box.text) == 0:
                        print("Incomplete values")
                        # return
                    else:
                        print("complete values")
                        display_box.text = str(
                            int(name_box.text)+int(country_box.text))

            for box in NewEntryInputBoxes:
                box.handle_event(event)

        for box in NewEntryInputBoxes:
            box.update()
        for box in NewEntryInputBoxes:
            box.draw(screen)

        pygame.display.flip()
        gameclock.tick(60)


def options():
    running = True
    while running:
        screen.fill('#0d0e2e')
        #screen.blit(BACKGROUND, (0, 0))
        draw_text('options', font, WHITE, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        gameclock.tick(60)


main_menu()
