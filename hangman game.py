import pygame
import math
from words import words_list
from random import randint


# setup display
# necessary step to avoid errors
pygame.init()
# width and height in pixels
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
pygame_icon = pygame.image.load('hangman6.png')
pygame.display.set_icon(pygame_icon)


# guess a word
i = randint(0, len(words_list))
random_word = words_list[i]
guessed_word = []
print(random_word)

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP*2 + ((RADIUS * 2 + GAP)*(i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A+i), True])


# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)


# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# game variables
hangman_status = 0


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw():
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH/2-text.get_width()/2,20))

    # draw letters
    display_word = ""
    for letter in random_word:
        if letter in guessed_word:
            display_word += (letter + " ")
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (350, 200))


    # draw buttons
    for letter in letters:
        x, y, l, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(l, 1, BLACK)
            win.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

    win.blit(images[hangman_status], (100, 100))
    pygame.display.update()


def display_message(message1, message2):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text1 = WORD_FONT.render(message1, 1, BLACK)
    text2 = LETTER_FONT.render(message2, 1, BLACK)
    win.blit(text1, (WIDTH /2 - text1.get_width() / 2, HEIGHT*0.33 - text1.get_height() / 2))
    win.blit(text2, (WIDTH/2 - text2.get_width() / 2, HEIGHT*0.66 - text2.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


#frames per second tells how many times images appear per sec like here 60 times images/frames appear per sec
def main():
    global hangman_status
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, l, visible = letter
                    if visible:
                        dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed_word.append(l)
                            print(l)
                            if l not in random_word:
                                hangman_status += 1
        draw()
        won = True
        for letter in random_word:
            if letter not in guessed_word:
                won = False
                break

        if won:
            display_message("YOU WON!", f"The word is {random_word}")
            break

        if hangman_status == 6:
            display_message("You Lose!", f"The corrct word is {random_word}")
            break


#problem statement
# 1) make a page which asks do you like to play the game, play button
# 2) start pygame
# 3) weather i lose or win this game
# 4) would you like to play again
# 5) I can even display how many times i played and what is my current score,(optional)

# def drawButtons():
#     x, y = WIDTH/2, HEIGHT/2
#     pygame.draw.rect(win, BLACK, (x, y, 140, 40))
#     text = LETTER_FONT.render("PLAY", 1, BLACK)
#     win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

# def mainMenu():
#     FPS = 60
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = pygame.mouse.get_pos()
#                 #playquit

main()
pygame.quit()
