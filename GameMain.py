# Word Quest
import random
import time
import pygame
from colorama import init, Fore
import enchant

# To print game score
init()


def printHighScore(scores):
    print("-" * 75, "\nOverall Scores and Time:")
    Game = 1

    for score, gameTime in scores:
        formattedTime = "{:.2f}".format(gameTime)
        print("Game:", Game, "Time:", formattedTime, "Score:", score)
        Game += 1

    maxScore = max(scores)
    print("-" * 75, Fore.LIGHTMAGENTA_EX + "\nHighest score..... ", maxScore[0])
    print(Fore.RESET + "-" * 75)


# Games default words list and music list
myWordsList = ["tams", "idiot", "crazy", "tamil", "tans"]
musicList = [
    "D:\python\CaseStudy\MiniProject\Sneaky-Snitch.mp3",
    "D:\python\CaseStudy\MiniProject\Fluffing-a-Duck.mp3",
    "D:\python\CaseStudy\MiniProject\Kevin-MacLeod-Investigations.mp3",
]
highScores = []
pygame.init()

while True:  # Game loop
    word = random.choice(myWordsList).upper()
    List = [word]
    life, count = 3, 0
    start_time = time.time()  # Game starting time

    # Code to start music
    musics = random.choice(musicList)

    try:
        pygame.mixer.music.load(musics)
        pygame.mixer.music.play(-1)
    
    except pygame.error:
        print("Error: Failed to load or play the music...")

    while True:  # Words loop
        last = word[-1]
        print(Fore.YELLOW + word,Fore.BLUE + "Enter word starts with...",Fore.YELLOW + last)
        print(Fore.CYAN + last, "...", end="")

        wordCheck = enchant.Dict("en_US")  # Dictionary check

        try:
            player1 = input(Fore.LIGHTMAGENTA_EX).upper()

        except KeyboardInterrupt:
            print("Game interrupted by user...")
            pygame.mixer.music.stop()
            exit()
        
        wordCheckResult = wordCheck.check(player1)

        if life != 0:
            if player1[0] == last and wordCheckResult == True:
                if player1 not in List:
                    List.append(player1)
                    word = player1
                    count += 1
                else:
                    life -= 1
                    if life == 0:
                        print(Fore.RED + "Three attempts finished.")
                        break
                    print(Fore.RED+ "Entered Word already exists.....Remaining attempts:",Fore.GREEN + str(life))
            else:
                life -= 1
                if life == 0:
                    print(Fore.RED + "Three attempts finished.")
                    break
                print(Fore.RED+ "Enter the word based on last letter or Word does not exist.....Remaining attempts:",Fore.GREEN + str(life))

    pygame.mixer.music.stop()  # To stop the music
    gameDuration = time.time() - start_time  # Overall game duration
    highScores.append([count, gameDuration])

    # To print list of words and total count
    print(Fore.RESET + "Word List:", List)
    print("Your total score is:", count)
    print("-" * 75)

    playAgain = input("Do you want to play again? Choose (yes or no): ").lower()
    if playAgain != "yes":
        break

printHighScore(highScores)  # To print highest score from n number of games