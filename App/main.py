from cgitb import text
from string import whitespace
from turtle import back
import pygame
import sys
from textboxes import InputBox
from oureertree import *
from comparingDNA import *
from restrictionEnzyme import *
from analyzingDNA import *

pygame.init()
gameclock = pygame.time.Clock()
# screen setting
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ancestry")
# general fonts
font = pygame.font.SysFont(None, 30)
# general colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (13, 14, 46)
LIGHTGREY = (211, 211, 211)
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
    click = False
    running = True

    while running:
        screen.fill(LIGHTGREY)

        mx, my = pygame.mouse.get_pos()
        # button 1 is string comparator
        # button 2 is restriction enzymes
        # future button 3 is DNAstring
        stringcomparator = pygame.Rect((200, 400), (100, 50))
        restrictionenzyme = pygame.Rect((400, 400), (100, 50))
        dnastring = pygame.Rect((600, 400), (100, 50))
        if stringcomparator.collidepoint((mx, my)):
            if click:
                StringComparator()
        if restrictionenzyme.collidepoint((mx, my)):
            if click:
                RestrictionEnzymes()
        if dnastring.collidepoint((mx, my)):
            if click:
                DNAString()

        pygame.draw.rect(screen, (171, 219, 227), stringcomparator)
        pygame.draw.rect(screen, (171, 219, 227), restrictionenzyme)
        pygame.draw.rect(screen, (171, 219, 227), dnastring)
        # text for button_1
        draw_text("StringComparator", font, BLACK, screen, 200, 395)
        draw_text("RestrcitionEnzymes", font, BLACK, screen, 400, 395)
        draw_text("DNAString", font, BLACK, screen, 600, 395)

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


def StringComparator():
    comparatorclick = False
    comparatorrunning = True
    string1_box = InputBox(150, 125, 30, 30)
    string2_box = InputBox(480, 125, 30, 30)
    #country_box = InputBox(450, 95, 30, 30)
    #genome_box = InputBox(850, 95, 30, 30)
    # testcase displaybox adds int from namebox and country box and displays result
    # output boxes
    SimilarPal_box = InputBox(305, 255, 30, 30, editable=False)
    # which string is unstabler
    Stabler_box = InputBox(305, 305, 30, 30, editable=False)
    SimScore_box = InputBox(
        305, 355, 30, 30, editable=False)  # similarity score

    NewEntryInputBoxes = [string1_box, string2_box,
                          SimilarPal_box, Stabler_box, SimScore_box]

    while comparatorrunning:
        screen.fill(LIGHTGREY)
        #screen.blit(BACKGROUND, (0, 0))
        # back and compare buttons
        cmx, cmy = pygame.mouse.get_pos()

        backbutton = pygame.Rect((200, 400), (100, 50))
        comparebutton = pygame.Rect((400, 400), (100, 50))
        clearvalsbutton = pygame.Rect((600, 400), (100, 50))
        if backbutton.collidepoint((cmx, cmy)):
            if comparatorclick:
                main_menu()
        if clearvalsbutton.collidepoint((cmx, cmy)):
            if comparatorclick:
                StringComparator()

        pygame.draw.rect(screen, (171, 219, 227), backbutton)
        pygame.draw.rect(screen, (171, 219, 227), comparebutton)
        pygame.draw.rect(screen, (171, 219, 227), clearvalsbutton)
        draw_text("Back", font, BLACK, screen, 200, 395)
        draw_text("Compare", font, BLACK, screen, 400, 395)
        draw_text("Clear Values", font, BLACK, screen, 600, 395)
        # string comparator text
        draw_text('DNA Comparison', font, BLACK, screen, 330, 70)
        # input boxes
        draw_text('DNA A:', font, BLACK, screen, 70, 130)
        draw_text('DNA B:', font, BLACK, screen, 400, 130)
        # output boxes
        draw_text('Mutual Palindromes:', font, BLACK, screen, 100, 260)
        draw_text('More Unstable:', font, BLACK, screen, 100, 310)
        draw_text('Similarity Score:', font, BLACK, screen, 100, 360)
        comparatorclick = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    comparatorclick = True
            if event.type == pygame.QUIT:
                comparatorrunning = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    comparatorrunning = False

                if event.key == pygame.K_RETURN:
                    if len(string1_box.text) == 0 or len(string2_box.text) == 0:
                        print("Incomplete values")
                        # return
                    elif len(string1_box.text) > 0 and len(string2_box.text) > 0:
                        print("complete values")
                        #SimilarPal_box.text = string1_box.text+string2_box.text
                        # display_box.text = str(
                        #     int(name_box.text)+int(country_box.text))
                        # //Area for Aumaimas code for mutual pals,more unstable, similarityscore
                        eertree1 = Eertree()
                        eertree2 = Eertree()
                        eertree1.addStringToTree(string1_box.text)
                        eertree2.addStringToTree(string2_box.text)
                        lst1 = eertree1.getPalindromes()
                        lst2 = eertree2.getPalindromes()
                        SimilarPal_box.text = str(
                            similar_palindromes(lst1, lst2))
                        SimScore_box.text = str(similarity_score(
                            SimilarPal_box.text, lst1, lst2))
                        Stabler_box.text = instability_comparission(lst1, lst2)
            for box in NewEntryInputBoxes:
                box.handle_event(event)
        # # compare on button press
        if comparebutton.collidepoint((cmx, cmy)):
            if comparatorclick:
                if len(string1_box.text) != 0 and len(string2_box.text) != 0:
                    print("Aumaimas code for comparison")
                    eertree1 = Eertree()
                    eertree2 = Eertree()
                    eertree1.addStringToTree(string1_box.text)
                    eertree2.addStringToTree(string2_box.text)
                    lst1 = eertree1.getPalindromes()
                    lst2 = eertree2.getPalindromes()
                    SimilarPal_box.text = str(similar_palindromes(lst1, lst2))
                    SimScore_box.text = str(similarity_score(
                        SimilarPal_box.text, lst1, lst2))
                    Stabler_box.text = instability_comparission(lst1, lst2)

                else:
                    print("Incomplete values")
        # #
        for box in NewEntryInputBoxes:
            box.update()
        for box in NewEntryInputBoxes:
            box.draw(screen)

        pygame.display.update()
        gameclock.tick(60)


def RestrictionEnzymes():
    resenzrunning = True
    resenzclick = False
    dnaa_box = InputBox(150, 125, 30, 30)
    dnab_box = InputBox(480, 125, 30, 30)
    # output boxes
    ap1_box = InputBox(150, 215, 30, 30, editable=False)
    ap2_box = InputBox(480, 215, 30, 30, editable=False)
    bp1_box = InputBox(150, 255, 30, 30, editable=False)
    bp2_box = InputBox(480, 255, 30, 30, editable=False)
    resenzInputBoxes = [dnaa_box, dnab_box,
                        ap1_box, ap2_box, bp1_box, bp2_box]

    while resenzrunning:
        screen.fill(LIGHTGREY)
        #screen.blit(BACKGROUND, (0, 0))
        emx, emy = pygame.mouse.get_pos()
        back2button = pygame.Rect((200, 395), (100, 50))
        compare2button = pygame.Rect((400, 395), (100, 50))

        if back2button.collidepoint((emx, emy)):
            if resenzclick:
                main_menu()

        pygame.draw.rect(screen, (171, 219, 227), back2button)
        pygame.draw.rect(screen, (171, 219, 227), compare2button)
        draw_text("Back", font, BLACK, screen, 200, 395)
        draw_text("Compare", font, BLACK, screen, 400, 395)

        # string comparator text
        draw_text('Restriction Enzyme Detector', font, BLACK, screen, 250, 70)
        # input boxes
        draw_text('DNA A:', font, BLACK, screen, 70, 130)
        draw_text('DNA B:', font, BLACK, screen, 400, 130)
        # output boxes
        draw_text('aP1:', font, BLACK, screen, 100, 215)
        draw_text('bP1:', font, BLACK, screen, 100, 255)
        draw_text('aP2:', font, BLACK, screen, 430, 215)
        draw_text('bP2:', font, BLACK, screen, 430, 255)

        resenzclick = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    resenzclick = True
            if event.type == pygame.QUIT:
                resenzrunning = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    resenzrunning = False

                if event.key == pygame.K_RETURN:
                    if len(dnaa_box.text) == 0 or len(dnab_box.text) == 0:
                        print("Incomplete values")
                        # return
                    elif len(dnaa_box.text) > 0 and len(dnab_box.text) > 0:
                        print("complete values")
                        # display_box.text = str(
                        #     int(name_box.text)+int(country_box.text))
                        # //Area for Aumaimas code for mutual pals,more unstable, similarityscore
                        ap1_box.text, ap2_box.text, bp1_box.text, bp2_box.text = str(
                            restriction_enzyme_breakdown(dnaa_box.text, dnab_box.text))

            for box in resenzInputBoxes:
                box.handle_event(event)
        # # compare on button press
        if compare2button.collidepoint((emx, emy)):
            if resenzclick:
                if len(dnaa_box.text) != 0 and len(dnab_box.text) != 0:
                    print("Aumaimas code for comparison")
                    result = restriction_enzyme_breakdown(
                        dnaa_box.text, dnab_box.text)
                    if result != 'No Sequence recognized':
                        ap1_box.text, ap2_box.text, bp1_box.text, bp2_box.text = str(
                            restriction_enzyme_breakdown(dnaa_box.text, dnab_box.text))
                    else:
                        ap1_box.text = 'No Sequence recognized'
                        ap2_box.text = 'No Sequence recognized'
                        bp1_box.text = 'No Sequence recognized'
                        bp2_box.text = 'No Sequence recognized'
                else:
                    print("Incomplete values")

        for box in resenzInputBoxes:
            box.update()
        for box in resenzInputBoxes:
            box.draw(screen)

        pygame.display.update()
        gameclock.tick(60)


def DNAString():
    dnaclick = False
    dnarunning = True
    string_box = InputBox(150, 95, 30, 30)
    thresholdbox = InputBox(500, 95, 30, 30)
    subpalinbox = InputBox(275, 195, 30, 30)
    longpalinbox = InputBox(275, 325, 30, 30)
    instabscorebox = InputBox(275, 455, 30, 30)
    NewEntryInputBoxes = [string_box, thresholdbox,
                          subpalinbox, longpalinbox, instabscorebox]

    while dnarunning:
        dmx, dmy = pygame.mouse.get_pos()

        backbutton = pygame.Rect((200, 600), (100, 50))
        computebutton = pygame.Rect((400, 600), (100, 50))
        clearvalsbutton = pygame.Rect((600, 600), (100, 50))
        if backbutton.collidepoint((dmx, dmy)):
            if dnaclick:
                main_menu()
        if clearvalsbutton.collidepoint((dmx, dmy)):
            if dnaclick:
                DNAString()

        pygame.draw.rect(screen, (171, 219, 227), backbutton)
        pygame.draw.rect(screen, (171, 219, 227), computebutton)
        pygame.draw.rect(screen, (171, 219, 227), clearvalsbutton)
        draw_text("Back", font, BLACK, screen, 200, 395)
        draw_text("Compare", font, BLACK, screen, 400, 395)
        draw_text("Clear Values", font, BLACK, screen, 600, 395)

        screen.fill(LIGHTGREY)
        draw_text('Enter String:', font, BLACK, screen, 50, 20)
        draw_text('String:', font, BLACK, screen, 80, 100)
        draw_text("Threshold:", font, BLACK, screen, 390, 100)
        draw_text('SubPalimdromes:', font, BLACK, screen, 70, 200)
        draw_text('Longest Palindrome:', font, BLACK, screen, 70, 330)
        draw_text('Instability Score:', font, BLACK, screen, 70, 460)
        dnaclick = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dnaclick = True
            if event.type == pygame.QUIT:
                dnarunning = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dnarunning = False
                if event.key == pygame.K_RETURN:
                    if len(string_box.text) == 0:
                        print("Incomplete values")
                        # return
                    elif len(string_box.text) > 0 and len(thresholdbox.text) > 0:
                        print("complete values")
                        subpalinbox.text = str(
                            get_subpalindromes(string_box.text))
                        palsresult = get_subpalindromes(string_box.text)
                        longpalinbox.text = longest_pal(palsresult)
                        instabscorebox.text = str(instability_rate(
                            palsresult, int(thresholdbox.text)))

            for box in NewEntryInputBoxes:
                box.handle_event(event)
        for box in NewEntryInputBoxes:
            box.update()
        for box in NewEntryInputBoxes:
            box.draw(screen)

        pygame.display.update()
        gameclock.tick(60)


main_menu()
