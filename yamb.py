import pygame
import random

pygame.init()

WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('YAMB.KP')
font = pygame.font.Font('freesansbold.ttf', 17)
timer = pygame.time.Clock()
fps = 60

blue0 = (74, 85, 162)       # glavna boja
blue1 = (120, 149, 203)     # svjetlija plava
blue2 = (197, 223, 248)     # jos svjetlija plava
blue3 = (229, 242, 255)     # najsvjetlija plava
yellow = (245, 230, 0)      # zuta za oznacavanje stvari
white = (255, 255, 255)
black = (0, 0, 0)

values = [0, 0, 0, 0, 0]
roll = False
rolls_left = 3
downwards = 0
upwards = 27
selected_dice = [False, False, False, False, False]
selected_option = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False]
points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sums = [0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0]
final_score = 0
fields_done = 0
clicked_option = -1
possible_points = 0
selected_position = 123

class Dice:     # stvaranje kockica
    
    def __init__(self, x_pos, y_pos, value, key):
        global selected_dice
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value
        self.key = key
        self.die = ''
        self.selected = selected_dice[key]

    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)        # draw.rect --> crta se rectangle: na sta, boja, di, velicina, solid, rounded edges
        # pa crtamo "brojeve" na kockicama, jednu po jednu
        if self.value == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)               # + 50 --> centriranje u sredinu kockice, 10 --> radijus tockice
        elif self.value == 2:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        elif self.value == 3:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        elif self.value == 4:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
        elif self.value == 5:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        elif self.value == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.selected:
            self.die = pygame.draw.rect(screen, yellow, [self.x_pos, self.y_pos, 100, 100], 5, 5)

    def check_clicked(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected_dice[self.key]:
                selected_dice[self.key] = False     # ako kliknemo na oznacenu kockicu, odznacavamo je
            elif not selected_dice[self.key]:
                selected_dice[self.key] = True      # ako kliknemo na neoznacenu kockicu, oznacavamo je

class Table:     # stvaranje okvira tablice

    def __init__(self, x_pos, y_pos, option):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.option = option

    def draw(self):
        pygame.draw.rect(screen, (59, 70, 147), [self.x_pos, self.y_pos, 60, 30])
        pygame.draw.line(screen, blue2, (self.x_pos, self.y_pos), (self.x_pos + 60, self.y_pos), 2)
        pygame.draw.line(screen, blue2, (self.x_pos, self.y_pos + 30), (self.x_pos + 60, self.y_pos + 30), 2)
        pygame.draw.line(screen, blue2, (self.x_pos, self.y_pos), (self.x_pos, self.y_pos + 30), 2)
        pygame.draw.line(screen, blue2, (self.x_pos + 60, self.y_pos), (self.x_pos + 60, self.y_pos + 30), 2)
        option_text = font.render(str(self.option), True, blue2)
        screen.blit(option_text, (self.x_pos + 3, self.y_pos + 8))

class Choice:    # stvaranje tablice za upisivanje bodova

    def __init__(self, x_pos, y_pos, selected, possible, done, points):      # select --> je li opcija odabrana (oznacena), possible --> je li moguce upisati na to mjesto, done --> je li nesto upisano
        global selected_option
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.selected = selected
        self.possible = possible
        self.done = done
        self.points = points

    def draw(self):
        if self.possible:
            pygame.draw.rect(screen, (94, 105, 192), [self.x_pos, self.y_pos, 60, 30])
        if self.selected:
            pygame.draw.rect(screen, blue2, [self.x_pos, self.y_pos, 61, 31])
        if self.done:
            pygame.draw.rect(screen, blue0, [self.x_pos, self.y_pos, 60, 30])
            points_text = font.render(str(self.points), True, blue2)
            screen.blit(points_text, (self.x_pos + 23, self.y_pos + 9))
        pygame.draw.line(screen, blue1, (self.x_pos, self.y_pos), (self.x_pos + 60, self.y_pos), 2)                # gornja crta (koja razdvaja) neke opcije
        pygame.draw.line(screen, blue1, (self.x_pos, self.y_pos + 30), (self.x_pos + 60, self.y_pos + 30), 2)      # donja crta (koja razdvaja) neke opcije
        pygame.draw.line(screen, blue1, (self.x_pos, self.y_pos), (self.x_pos, self.y_pos + 30), 2)                # liva crta
        pygame.draw.line(screen, blue1, (self.x_pos + 60, self.y_pos), (self.x_pos + 60, self.y_pos + 30), 2)      # desna crta

def misc_stuff():

    if fields_done == 70:
        pygame.draw.rect(screen, blue2, [450, 250, 500, 300])
        game_over_txt = font.render('SCORE: ' + str(final_score), True, blue1)
        screen.blit(game_over_txt, (647, 392))

    roll_text = font.render('ROLL DICE', True, blue2)
    screen.blit(roll_text, (793, 467))
    accept_text = font.render('ACCEPT TURN', True, blue2)
    screen.blit(accept_text, (1016, 467))
    rolls_text = font.render('Rolls left this turn: ' + str(rolls_left), True, blue2)
    screen.blit(rolls_text, (670, 275))

def whats_possible(possibles_list, done_list):
    
    global selected_option
    selected_call = False

    if rolls_left <= 2:

        # prvo provjeravamo je li ista najavljeno
        for index2 in range(42, 56):
            if selected_option[index2] == True:
                for index3 in range(len(possibles_list)):
                    possibles_list[index3] = False
                possibles_list[index2] = True
                selected_call = True

        # ako nije nista najavljeno, provjeravamo druge opcije
        if selected_call == False:
            # stupci prema dolje i prema gore
            possibles_list[downwards] = True
            possibles_list[upwards] = True
            # stupac koji se moze ispunjavati bilo kada
            for index4 in range(28, 42):
                possibles_list[index4] = True
            # stupac najave
            for index in range(42, 56):
                if rolls_left == 2:
                    possibles_list[index] = True
                else:
                    possibles_list[index] = False
            # stupac rucnog bacanja
            if rolls_left == 2:
                for index5 in range(56, 70):
                    possibles_list[index5] = True
            else:
                for index6 in range(56, 70):
                    possibles_list[index6] = False
                    if selected_option[index6]:
                        selected_option[index6] = False
            # ako je negdje upisan rezultat, upis novih bodova nije moguc
            for index7 in range(len(possibles_list)):
                if done_list[index7] == True:
                    possibles_list[index7] == False

    return possibles_list

def select_option(selected, selected_option, done):

    global possible

    if possible[selected]:
        for index in range(len(selected_option)):
            selected_option[index] = False
        if done[selected] == False and possible[selected] == True:
            selected_option[selected] = True

    return selected_option

def calculate_points(selected_option, rolls_left, values):

    selected = 0
    values_counter = [0, 0, 0, 0, 0, 0]
    one_pair = False
    two_pairs = False
    tris = False
    little_straight_counter = 0
    large_straight_counter = 0
    little_straight = False
    large_straight = False
    poker = False
    yamb = False
    one_pair_pos = 123
    two_pairs_pos = 123
    tris_pos = 123
    poker_pos = 123
    yamb_pos = 123

    # brojimo koliko imamo jedinica, duja, (...), sestica kod trenutnih kockica
    for index in range(len(values)):
        values_counter[values[index]-1] += 1

    # provjera postoje li dva para, tris, skala (i koja), full, poker, ili yamb
    for index2 in range(0, 6):
        if values_counter[index2] == 2 and one_pair == False:
            one_pair = True
            one_pair_pos = index2 + 1
        if values_counter[index2] == 2 and one_pair == True:
            two_pairs = True
            two_pairs_pos = index2 + 1
        if values_counter[index2] == 3:
            tris = True
            tris_pos = index2 + 1
        if index2 < 4 and values_counter[index2] == 1 and values_counter[index2 + 1] == 1:
            little_straight_counter += 1
            if little_straight_counter == 4:
                little_straight = True
        if index2 != 0:
            if index2 < 5 and values_counter[index2] == 1 and values_counter[index2 + 1] == 1:
                large_straight_counter += 1
                if large_straight_counter == 4:
                    large_straight = True
        if values_counter[index2] == 4:
            poker = True
            poker_pos = index2 + 1
        if values_counter[index2] == 5:
            yamb = True
            yamb_pos = index2 + 1
        
    for index3 in range(len(selected_option)):
        if selected_option[index3] == True:
            selected = index3
    
    # dodjeljujemo bodove jedinicama, dujama, (...), sesticama
    if selected == 0 or selected == 14 or selected == 28 or selected == 42 or selected == 56:
        possible_points = values_counter[0] * 1
    elif selected == 1 or selected == 15 or selected == 29 or selected == 43 or selected == 57:
        possible_points = values_counter[1] * 2
    elif selected == 2 or selected == 16 or selected == 30 or selected == 44 or selected == 58:
        possible_points = values_counter[2] * 3
    elif selected == 3 or selected == 17 or selected == 31 or selected == 45 or selected == 59:
        possible_points = values_counter[3] * 4
    elif selected == 4 or selected == 18 or selected == 32 or selected == 46 or selected == 60:
        possible_points = values_counter[4] * 5
    elif selected == 5 or selected == 19 or selected == 33 or selected == 47 or selected == 61:
        possible_points = values_counter[5] * 6
    # dodjeljujemo bodove maksimumu i minimumu
    elif selected == 6 or selected == 20 or selected == 34 or selected == 48 or selected == 62:
        possible_points = sum(values)
    elif selected == 7 or selected == 21 or selected == 35 or selected == 49 or selected == 63:
        possible_points = sum(values)
    # dodjeljujemo bodove za dva para
    elif selected == 8 or selected == 22 or selected == 36 or selected == 50 or selected == 64:
        if two_pairs: possible_points = one_pair_pos * 2 + two_pairs_pos * 2 + 10
        else: possible_points = 0
    # dodjeljujemo bodove za tris
    elif selected == 9 or selected == 23 or selected == 37 or selected == 51 or selected == 65:
        if tris == True and one_pair == False: possible_points = tris_pos * 3 + 20
        else: possible_points = 0
    # dodjeljujemo bodove za skalu
    elif selected == 10 or selected == 24 or selected == 38 or selected == 52 or selected == 66:
        if little_straight: possible_points = 45
        elif large_straight: possible_points = 50
        else: possible_points = 0
    # dodjeljujemo bodove za full
    elif selected == 11 or selected == 25 or selected == 39 or selected == 53 or selected == 67:
        if one_pair and tris: possible_points = one_pair_pos * 2 + tris_pos * 3 + 40
        else: possible_points = 0
    # dodjeljujemo bodove za poker
    elif selected == 12 or selected == 26 or selected == 40 or selected == 54 or selected == 68:
        if poker: possible_points = poker_pos * 4 + 50
        else: possible_points = 0
    # dodjeljujemo bodove za yamb
    elif selected == 13 or selected == 27 or selected == 41 or selected == 55 or selected == 69:
        if yamb: possible_points = yamb_pos * 5 + 60
        else: possible_points = 0

    for index4 in range(56, 70):
        if selected_option[index4] and rolls_left < 2:
            possible_points = 0
    
    return possible_points

def calculate_sums(sums, points):

    # izracunavanje prvog reda suma
    sums[0] = points[0] + points[1] + points[2] + points[3] + points[4] + points[5]
    sums[1] = points[14] + points[15] + points[16] + points[17] + points[18] + points[19]
    sums[2] = points[28] + points[29] + points[30] + points[31] + points[32] + points[33]
    sums[3] = points[42] + points[43] + points[44] + points[45] + points[46] + points[47]
    sums[4] = points[56] + points[57] + points[58] + points[59] + points[60] + points[61]

    for index in range(0, 5):
        if sums[index] >= 60 and sums[index] < 90:
            sums[index] += 30

    # izracunavanje drugog reda suma
    if points[6] != 0 and points[7] != 0:
        sums[5] = (points[6] - points[7]) * points[0]
    if points[20] != 0 and points[21] != 0:
        sums[6] = (points[20] - points[21]) * points[14]
    if points[34] != 0 and points[35] != 0:
        sums[7] = (points[34] - points[35]) * points[28]
    if points[48] != 0 and points[49] != 0:
        sums[8] = (points[48] - points[49]) * points[42]
    if points[62] != 0 and points[63] != 0:
        sums[9] = (points[62] - points[63]) * points[56]

    # izracunavanje treceg reda suma
    sums[10] = points[8] + points[9] + points[10] + points[11] + points[12] + points[13]
    sums[11] = points[22] + points[23] + points[24] + points[25] + points[26] + points[27]
    sums[12] = points[36] + points[37] + points[38] + points[39] + points[40] + points[41]
    sums[13] = points[50] + points[51] + points[52] + points[53] + points[54] + points[55]
    sums[14] = points[64] + points[65] + points[66] + points[67] + points[68] + points[69]

    return sums

running = True

while running:

    timer.tick(fps)
    screen.fill(blue0)

    roll_button = pygame.draw.rect(screen, blue1, [740, 450, 200, 50], 0, 3)
    accept_button = pygame.draw.rect(screen, blue1, [980, 450, 200, 50], 0, 3)
    if fields_done == 70:
        final_score = sum(sums)

    # stvaranje kockica
    die1 = Dice(670, 300, values[0], 0)
    die2 = Dice(790, 300, values[1], 1)
    die3 = Dice(910, 300, values[2], 2)
    die4 = Dice(1030, 300, values[3], 3)
    die5 = Dice(1150, 300, values[4], 4)
    #stvaranje rubnog stupca
    ones = Table(150, 160, '   1s')
    twos = Table(150, 190, '   2s')
    threes = Table(150, 220, '   3s')
    fours = Table(150, 250, '   4s')
    fives = Table(150, 280, '   5s')
    sixes = Table(150, 310, '   6s')
    sums1 = Table(150, 340, '  SUM')
    max = Table(150, 370, '  MAX')
    min = Table(150, 400, '  MIN')
    sums2 = Table(150, 430, '  SUM')
    pairs = Table(150, 460, '  2x 2')
    tris = Table(150, 490, '   3x')
    straight = Table(150, 520, '  STR.')
    full = Table(150, 550, ' FULL')
    poker = Table(150, 580, '   4x')
    yamb = Table(150, 610, ' YAMB')
    sums3 = Table(150, 640, '  SUM')
    # stvaranje rubnog retka
    downward = Table(210, 130, 'DOWN')
    upward = Table(270, 130, '   UP')
    central = Table(330, 130, ' MAIN')
    call = Table(390, 130, ' CALL')
    hand = Table(450, 130, ' HAND')
    # stvaranje tablice za upisivanje bodova
    # prvi stupac
    one = Choice(210, 160, selected_option[0], possible[0], done[0], points[0])
    two = Choice(210, 190, selected_option[1], possible[1], done[1], points[1])
    three = Choice(210, 220, selected_option[2], possible[2], done[2], points[2])
    four = Choice(210, 250, selected_option[3], possible[3], done[3], points[3])
    five = Choice(210, 280, selected_option[4], possible[4], done[4], points[4])
    six = Choice(210, 310, selected_option[5], possible[5], done[5], points[5])
    sum1 = Table(210, 340, sums[0])
    seven = Choice(210, 370, selected_option[6], possible[6], done[6], points[6])
    eight = Choice(210, 400, selected_option[7], possible[7], done[7], points[7])
    sum6 = Table(210, 430, sums[5])
    nine = Choice(210, 460, selected_option[8], possible[8], done[8], points[8])
    one0 = Choice(210, 490, selected_option[9], possible[9], done[9], points[9])
    one1 = Choice(210, 520, selected_option[10], possible[10], done[10], points[10])
    one2 = Choice(210, 550, selected_option[11], possible[11], done[11], points[11])
    one3 = Choice(210, 580, selected_option[12], possible[12], done[12], points[12])
    one4 = Choice(210, 610, selected_option[13], possible[13], done[13], points[13])
    sum11 = Table(210, 640, sums[10])
    # drugi stupac
    one5 = Choice(270, 160, selected_option[14], possible[14], done[14], points[14])
    one6 = Choice(270, 190, selected_option[15], possible[15], done[15], points[15])
    one7 = Choice(270, 220, selected_option[16], possible[16], done[16], points[16])
    one8 = Choice(270, 250, selected_option[17], possible[17], done[17], points[17])
    one9 = Choice(270, 280, selected_option[18], possible[18], done[18], points[18])
    two0 = Choice(270, 310, selected_option[19], possible[19], done[19], points[19])
    sum2 = Table(270, 340, sums[1])
    two1 = Choice(270, 370, selected_option[20], possible[20], done[20], points[20])
    two2 = Choice(270, 400, selected_option[21], possible[21], done[21], points[21])
    sum7 = Table(270, 430, sums[6])
    two3 = Choice(270, 460, selected_option[22], possible[22], done[22], points[22])
    two4 = Choice(270, 490, selected_option[23], possible[23], done[23], points[23])
    two5 = Choice(270, 520, selected_option[24], possible[24], done[24], points[24])
    two6 = Choice(270, 550, selected_option[25], possible[25], done[25], points[25])
    two7 = Choice(270, 580, selected_option[26], possible[26], done[26], points[26])
    two8 = Choice(270, 610, selected_option[27], possible[27], done[27], points[27])
    sum12 = Table(270, 640, sums[11])
    # treci stupac
    two9 = Choice(330, 160, selected_option[28], possible[28], done[28], points[28])
    three0 = Choice(330, 190, selected_option[29], possible[29], done[29], points[29])
    three1 = Choice(330, 220, selected_option[30], possible[30], done[30], points[30])
    three2 = Choice(330, 250, selected_option[31], possible[31], done[31], points[31])
    three3 = Choice(330, 280, selected_option[32], possible[32], done[32], points[32])
    three4 = Choice(330, 310, selected_option[33], possible[33], done[33], points[33])
    sum3 = Table(330, 340, sums[2])
    three5 = Choice(330, 370, selected_option[34], possible[34], done[34], points[34])
    three6 = Choice(330, 400, selected_option[35], possible[35], done[35], points[35])
    sum8 = Table(330, 430, sums[7])
    three7 = Choice(330, 460, selected_option[36], possible[36], done[36], points[36])
    three8 = Choice(330, 490, selected_option[37], possible[37], done[37], points[37])
    three9 = Choice(330, 520, selected_option[38], possible[38], done[38], points[38])
    four0 = Choice(330, 550, selected_option[39], possible[39], done[39], points[39])
    four1 = Choice(330, 580, selected_option[40], possible[40], done[40], points[40])
    four2 = Choice(330, 610, selected_option[41], possible[41], done[41], points[41])
    sum13 = Table(330, 640, sums[12])
    # cetvrti stupac
    four3 = Choice(390, 160, selected_option[42], possible[42], done[42], points[42])
    four4 = Choice(390, 190, selected_option[43], possible[43], done[43], points[43])
    four5 = Choice(390, 220, selected_option[44], possible[44], done[44], points[44])
    four6 = Choice(390, 250, selected_option[45], possible[45], done[45], points[45])
    four7 = Choice(390, 280, selected_option[46], possible[46], done[46], points[46])
    four8 = Choice(390, 310, selected_option[47], possible[47], done[47], points[47])
    sum4 = Table(390, 340, sums[3])
    four9 = Choice(390, 370, selected_option[48], possible[48], done[48], points[48])
    five0 = Choice(390, 400, selected_option[49], possible[49], done[49], points[49])
    sum9 = Table(390, 430, sums[8])
    five1 = Choice(390, 460, selected_option[50], possible[50], done[50], points[50])
    five2 = Choice(390, 490, selected_option[51], possible[51], done[51], points[51])
    five3 = Choice(390, 520, selected_option[52], possible[52], done[52], points[52])
    five4 = Choice(390, 550, selected_option[53], possible[53], done[53], points[53])
    five5 = Choice(390, 580, selected_option[54], possible[54], done[54], points[54])
    five6 = Choice(390, 610, selected_option[55], possible[55], done[55], points[55])
    sum14 = Table(390, 640, sums[13])
    # peti stupac
    five7 = Choice(450, 160, selected_option[56], possible[56], done[56], points[56])
    five8 = Choice(450, 190, selected_option[57], possible[57], done[57], points[57])
    five9 = Choice(450, 220, selected_option[58], possible[58], done[58], points[58])
    six0 = Choice(450, 250, selected_option[59], possible[59], done[59], points[59])
    six1 = Choice(450, 280, selected_option[60], possible[60], done[60], points[60])
    six2 = Choice(450, 310, selected_option[61], possible[61], done[61], points[61])
    sum5 = Table(450, 340, sums[4])
    six3 = Choice(450, 370, selected_option[62], possible[62], done[62], points[62])
    six4 = Choice(450, 400, selected_option[63], possible[63], done[63], points[63])
    sum10 = Table(450, 430, sums[9])
    six5 = Choice(450, 460, selected_option[64], possible[64], done[64], points[64])
    six6 = Choice(450, 490, selected_option[65], possible[65], done[65], points[65])
    six7 = Choice(450, 520, selected_option[66], possible[66], done[66], points[66])
    six8 = Choice(450, 550, selected_option[67], possible[67], done[67], points[67])
    six9 = Choice(450, 580, selected_option[68], possible[68], done[68], points[68])
    seven0 = Choice(450, 610, selected_option[69], possible[69], done[69], points[69])
    sum15 = Table(450, 640, sums[14])

    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()

    one.draw()
    two.draw()
    three.draw()
    four.draw()
    five.draw()
    six.draw()
    seven.draw()
    eight.draw()
    nine.draw()
    one0.draw()
    one1.draw()
    one2.draw()
    one3.draw()
    one4.draw()
    one5.draw()
    one6.draw()
    one7.draw()
    one8.draw()
    one9.draw()
    two0.draw()
    two1.draw()
    two2.draw()
    two3.draw()
    two4.draw()
    two5.draw()
    two6.draw()
    two7.draw()
    two8.draw()
    two9.draw()
    three0.draw()
    three1.draw()
    three2.draw()
    three3.draw()
    three4.draw()
    three5.draw()
    three6.draw()
    three7.draw()
    three8.draw()
    three9.draw()
    four0.draw()
    four1.draw()
    four2.draw()
    four3.draw()
    four4.draw()
    four5.draw()
    four6.draw()
    four7.draw()
    four8.draw()
    four9.draw()
    five0.draw()
    five1.draw()
    five2.draw()
    five3.draw()
    five4.draw()
    five5.draw()
    five6.draw()
    five7.draw()
    five8.draw()
    five9.draw()
    six0.draw()
    six1.draw()
    six2.draw()
    six3.draw()
    six4.draw()
    six5.draw()
    six6.draw()
    six7.draw()
    six8.draw()
    six9.draw()
    seven0.draw()

    sum1.draw()
    sum2.draw()
    sum3.draw()
    sum4.draw()
    sum5.draw()
    sum6.draw()
    sum7.draw()
    sum8.draw()
    sum9.draw()
    sum10.draw()
    sum11.draw()
    sum12.draw()
    sum13.draw()
    sum14.draw()
    sum15.draw()

    ones.draw()
    twos.draw()
    threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    sums1.draw()
    max.draw()
    min.draw()
    sums2.draw()
    pairs.draw()
    tris.draw()
    straight.draw()
    full.draw()
    poker.draw()
    yamb.draw()
    sums3.draw()
    downward.draw()
    upward.draw()
    central.draw()
    call.draw()
    hand.draw()

    misc_stuff()

    possible = whats_possible(possible, done)
    possible_points = calculate_points(selected_option, rolls_left, values)
    for i in range(len(selected_option)):
        if selected_option[i] == True:
            selected_position = i

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False         # prekidamo igru
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            die1.check_clicked(event.pos)
            die2.check_clicked(event.pos)
            die3.check_clicked(event.pos)
            die4.check_clicked(event.pos)
            die5.check_clicked(event.pos)
            if roll_button.collidepoint(event.pos) and rolls_left > 0:
                roll_button = pygame.draw.rect(screen, blue2, [740, 450, 200, 50], 0, 3)
                roll = True
                rolls_left -= 1
            if 210 <= event.pos[0] < 270:
                if 160 <= event.pos[1] < 190:
                    clicked_option = 0
                elif 190 <= event.pos[1] < 220:
                    clicked_option = 1
                elif 220 <= event.pos[1] < 250:
                    clicked_option = 2
                elif 250 <= event.pos[1] < 280:
                    clicked_option = 3
                elif 280 <= event.pos[1] < 310:
                    clicked_option = 4
                elif 310 <= event.pos[1] < 340:
                    clicked_option = 5
                elif 370 <= event.pos[1] < 400:
                    clicked_option = 6
                elif 400 <= event.pos[1] < 430:
                    clicked_option = 7
                elif 460 <= event.pos[1] < 490:
                    clicked_option = 8
                elif 490 <= event.pos[1] < 520:
                    clicked_option = 9
                elif 520 <= event.pos[1] < 550:
                    clicked_option = 10
                elif 550 <= event.pos[1] < 580:
                    clicked_option = 11
                elif 580 <= event.pos[1] < 610:
                    clicked_option = 12
                elif 610 <= event.pos[1] < 640:
                    clicked_option = 13
                selected_option = select_option(clicked_option, selected_option, done)
            if 270 <= event.pos[0] < 330:
                if 160 <= event.pos[1] < 190:
                    clicked_option = 14
                elif 190 <= event.pos[1] < 220:
                    clicked_option = 15
                elif 220 <= event.pos[1] < 250:
                    clicked_option = 16
                elif 250 <= event.pos[1] < 280:
                    clicked_option = 17
                elif 280 <= event.pos[1] < 310:
                    clicked_option = 18
                elif 310 <= event.pos[1] < 340:
                    clicked_option = 19
                elif 370 <= event.pos[1] < 400:
                    clicked_option = 20
                elif 400 <= event.pos[1] < 430:
                    clicked_option = 21
                elif 460 <= event.pos[1] < 490:
                    clicked_option = 22
                elif 490 <= event.pos[1] < 520:
                    clicked_option = 23
                elif 520 <= event.pos[1] < 550:
                    clicked_option = 24
                elif 550 <= event.pos[1] < 580:
                    clicked_option = 25
                elif 580 <= event.pos[1] < 610:
                    clicked_option = 26
                elif 610 <= event.pos[1] < 640:
                    clicked_option = 27
                selected_option = select_option(clicked_option, selected_option, done)
            if 330 <= event.pos[0] < 390:
                if 160 <= event.pos[1] < 190:
                    clicked_option = 28
                elif 190 <= event.pos[1] < 220:
                    clicked_option = 29
                elif 220 <= event.pos[1] < 250:
                    clicked_option = 30
                elif 250 <= event.pos[1] < 280:
                    clicked_option = 31
                elif 280 <= event.pos[1] < 310:
                    clicked_option = 32
                elif 310 <= event.pos[1] < 340:
                    clicked_option = 33
                elif 370 <= event.pos[1] < 400:
                    clicked_option = 34
                elif 400 <= event.pos[1] < 430:
                    clicked_option = 35
                elif 460 <= event.pos[1] < 490:
                    clicked_option = 36
                elif 490 <= event.pos[1] < 520:
                    clicked_option = 37
                elif 520 <= event.pos[1] < 550:
                    clicked_option = 38
                elif 550 <= event.pos[1] < 580:
                    clicked_option = 39
                elif 580 <= event.pos[1] < 610:
                    clicked_option = 40
                elif 610 <= event.pos[1] < 640:
                    clicked_option = 41
                selected_option = select_option(clicked_option, selected_option, done)
            if 390 <= event.pos[0] < 450:
                if 160 <= event.pos[1] < 190:
                    clicked_option = 42
                elif 190 <= event.pos[1] < 220:
                    clicked_option = 43
                elif 220 <= event.pos[1] < 250:
                    clicked_option = 44
                elif 250 <= event.pos[1] < 280:
                    clicked_option = 45
                elif 280 <= event.pos[1] < 310:
                    clicked_option = 46
                elif 310 <= event.pos[1] < 340:
                    clicked_option = 47
                elif 370 <= event.pos[1] < 400:
                    clicked_option = 48
                elif 400 <= event.pos[1] < 430:
                    clicked_option = 49
                elif 460 <= event.pos[1] < 490:
                    clicked_option = 50
                elif 490 <= event.pos[1] < 520:
                    clicked_option = 51
                elif 520 <= event.pos[1] < 550:
                    clicked_option = 52
                elif 550 <= event.pos[1] < 580:
                    clicked_option = 53
                elif 580 <= event.pos[1] < 610:
                    clicked_option = 54
                elif 610 <= event.pos[1] < 640:
                    clicked_option = 55
                selected_option = select_option(clicked_option, selected_option, done)
            if 450 <= event.pos[0] <= 510:
                if 160 <= event.pos[1] < 190:
                    clicked_option = 56
                elif 190 <= event.pos[1] < 220:
                    clicked_option = 57
                elif 220 <= event.pos[1] < 250:
                    clicked_option = 58
                elif 250 <= event.pos[1] < 280:
                    clicked_option = 59
                elif 280 <= event.pos[1] < 310:
                    clicked_option = 60
                elif 310 <= event.pos[1] < 340:
                    clicked_option = 61
                elif 370 <= event.pos[1] < 400:
                    clicked_option = 62
                elif 400 <= event.pos[1] < 430:
                    clicked_option = 63
                elif 460 <= event.pos[1] < 490:
                    clicked_option = 64
                elif 490 <= event.pos[1] < 520:
                    clicked_option = 65
                elif 520 <= event.pos[1] < 550:
                    clicked_option = 66
                elif 550 <= event.pos[1] < 580:
                    clicked_option = 67
                elif 580 <= event.pos[1] < 610:
                    clicked_option = 68
                elif 610 <= event.pos[1] < 640:
                    clicked_option = 69
                selected_option = select_option(clicked_option, selected_option, done)
            if accept_button.collidepoint(event.pos) and selected_position != 123 and rolls_left < 3:
                accept_button = pygame.draw.rect(screen, blue2, [980, 450, 200, 50], 0, 3)
                points[selected_position] = possible_points
                selected_option[selected_position] = False
                done[selected_position] = True
                for index in range(len(selected_dice)):
                    selected_dice[index] = False
                if selected_position >= 0 and selected_position <= 12:
                    downwards += 1
                if selected_position <= 27 and selected_position >= 15:
                    upwards -= 1
                values = [0, 0, 0, 0, 0]
                selected_position = 123
                rolls_left = 3
                fields_done += 1
                sums = calculate_sums(sums, points)

    if roll:
        for value in range(len(values)):
            if not selected_dice[value]:
                values[value] = random.randint(1, 6)    # dodjeljujemo vrijednosti neoznacenim kockicama
        roll = False

    pygame.display.flip()

pygame.quit()