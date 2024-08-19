from tkinter import *
import tkinter.font as font
import random
import pygame
from tkinter import messagebox

# In-game sound files

pygame.mixer.init()
click_sound = pygame.mixer.Sound("./sounds/click-47609.mp3")
win_sound = pygame.mixer.Sound("./sounds/goodresult-82807.mp3")
lose_sound = pygame.mixer.Sound("./sounds/kids-laugh-45357.mp3")
brbr_sound = pygame.mixer.Sound("./sounds/back-tick-107822.mp3")

# Default values

player_score = 0
computer_score = 0
game_count = 0
player_wins = 0
computer_wins = 0
options = [('Rock', 0), ('Paper', 1), ('Scissors', 2)]
difficulty = 'Easy'


def play_sound(effect):
    effect.play()


def reset_game():
    global player_score, computer_score, game_count
    player_score = 0
    computer_score = 0
    game_count += 1
    winner_label.config(text="Choose an option to play...", fg='#e6e5e1')


# Resets the game

def reset_all():
    global player_score, computer_score, game_count, player_wins, computer_wins
    player_score = 0
    computer_score = 0
    game_count = 0
    player_wins = 0
    computer_wins = 0
    winner_label.config(text="Choose an option to play...", fg='#e6e5e1')
    player_score_label.config(text='Your Score: -')
    computer_score_label.config(text='Computer Score: -')
    player_choice_label.config(text='Your Choice: ---')
    computer_choice_label.config(text='Computer\'s Choice: ---')
    difficulty_label.config(text="Difficulty Level: X")

    play_sound(click_sound)


def player_choice(player_input):
    global player_score, computer_score, player_wins, computer_wins


# Plays a sound when the button is pressed

    play_sound(click_sound)

    computer_input = get_computer_choice()

    player_choice_label.config(text='Your Choice: ' + player_input[0])
    computer_choice_label.config(text='Computer\'s Choice: ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text="It's a Tie!", fg="#a87c3e", font=('Helvetica', 26, 'bold'))
        play_sound(brbr_sound)
    elif (player_input[1] - computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Win!", fg="#598a34", font=('Helvetica', 26, 'bold'))
        player_score_label.config(text='Your Score: ' + str(player_score))
        play_sound(win_sound)
    else:
        computer_score += 1
        winner_label.config(text="Computer Wins!", fg="#962929", font=('Helvetica', 26, 'bold'))
        computer_score_label.config(text='Computer\'s Score: ' + str(computer_score))
        play_sound(lose_sound)

    if player_score == 3 or computer_score == 3:
        if player_score == 3:
            player_wins += 1
            messagebox.showinfo("Game Over", "Congratulations, you won the game!")
        else:
            computer_wins += 1
            messagebox.showinfo("Game Over", "Sorry, the computer won the game!")

        ask_play_again()


# Ask to play again when the game ends

def ask_play_again():
    global player_wins, computer_wins, game_count
    play_again = messagebox.askyesno("Play Again", "Do you want to play another game?")
    computer_response = random.choice([True, False])
    if computer_response:
        messagebox.showinfo("Computer's Response", "Computer: Yes, let's play another game!")
    else:
        messagebox.showinfo("Computer's Response", "Computer: No, that's enough!")

    # If both sides want to continue, reset the game
    if play_again and computer_response:
        reset_game()
    else:
        messagebox.showinfo("Game Over", "The game is over!")
        game_window.quit()


# Computer's choice strategies

def get_computer_choice():
    # The difficulty increases as the probability of a smart choice decreases
    if difficulty == 'Easy':  # Makes choices completely randomly
        return random.choice(options)

    elif difficulty == 'Medium':
        if random.random() > 0.5:  # 50%
            if player_choice_label['text'] == 'Your Choice: Rock':
                return options[1]  # Paper
            elif player_choice_label['text'] == 'Your Choice: Paper':
                return options[2]  # Scissors
            elif player_choice_label['text'] == 'Your Choice: Scissors':
                return options[0]  # Rock
        else:
            return random.choice(options)

    elif difficulty == 'Hard':
        if random.random() > 0.3:  # 70%
            if player_choice_label['text'] == 'Your Choice: Rock':
                return options[1]  # Paper
            elif player_choice_label['text'] == 'Your Choice: Paper':
                return options[2]  # Scissors
            elif player_choice_label['text'] == 'Your Choice: Scissors':
                return options[0]  # Rock
        else:
            return random.choice(options)

    elif difficulty == 'Impossible':
        # Always wins 
        if player_choice_label['text'] == 'Your Choice: Rock':
            return options[1]  # Paper
        elif player_choice_label['text'] == 'Your Choice: Paper':
            return options[2]  # Scissors
        elif player_choice_label['text'] == 'Your Choice: Scissors':
            return options[0]  # Rock


def set_difficulty(level):
    global difficulty
    difficulty = level
    difficulty_label.config(text="Difficulty Level: " + difficulty)
    play_sound(click_sound)

game_window = Tk()
game_window.title("rock-paper-scissors")
game_window.configure(bg='#2e2e2e')
app_font = font.Font(family='Helvetica', size=25, weight='bold')
game_title = Label(game_window, text='Rock paper scissors', font=font.Font(family='Helvetica', size=35), fg='#9ab5a1', bg='#2e2e2e')
game_title.pack()


# Difficulty level selection

difficulty_frame = Frame(game_window, bg='#2e2e2e')
difficulty_frame.pack(pady=10)
difficulty_label = Label(difficulty_frame, text="Difficulty Level: NO SELECTION", font=app_font, fg='#cf5353', bg='#2e2e2e')
difficulty_label.grid(row=0, column=0, pady=8)
easy_btn = Button(difficulty_frame, text='EASY', width=10, command=lambda: set_difficulty('Easy'),
                  font=app_font, fg='#80a883')
easy_btn.grid(row=0, column=1, padx=8)
medium_btn = Button(difficulty_frame, text='MEDIUM', width=10, command=lambda: set_difficulty('Medium'),
                    font=app_font, fg='#a8a880')
medium_btn.grid(row=0, column=2, padx=8)
hard_btn = Button(difficulty_frame, text='HARD', width=10, command=lambda: set_difficulty('Hard'),
                  font=app_font, fg='#a88080')
hard_btn.grid(row=0, column=3, padx=8)
impossible_btn = Button(difficulty_frame, text='IMPOSSIBLE', width=10, command=lambda: set_difficulty('Impossible'),
                        font=app_font, fg='#9180a8')
impossible_btn.grid(row=0, column=4, padx=8)
winner_label = Label(game_window, text="Choose an option to play...", fg='#e6e5e1', font=('Helvetica', 26, 'bold'),
                     pady=8, bg='#2e2e2e')
winner_label.pack()

input_frame = Frame(game_window, bg='#2e2e2e')
input_frame.pack()

# Options

player_options = Label(input_frame, text="Your Options: ", font=app_font, fg='#b5ad81', bg='#2e2e2e')
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(input_frame, text='🪨 Rock ', width=10, bd=0, bg='pink', pady=5,
                  command=lambda: player_choice(options[0]),
                  font=app_font)
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='📄 Paper ', width=10, bd=0, bg='silver', pady=5,
                   command=lambda: player_choice(options[1]),
                   font=app_font)
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='✂️ Scissors ', width=10, bd=0, bg='light blue', pady=5,
                      command=lambda: player_choice(options[2]),
                      font=app_font)
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

# Displaying reports

score_label = Label(input_frame, text='Score:', font=app_font, fg='#e6e5e1', bg='#2e2e2e')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Your Choice: ---', font=app_font, fg='#858fa8', bg='#2e2e2e')
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Your Score: -', font=app_font, fg='#858fa8', bg='#2e2e2e')
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Computer\'s Choice: ---', font=app_font, fg='#e6e5e1', bg='#2e2e2e')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Computer\'s Score: -', font=app_font, fg='#e6e5e1', bg='#2e2e2e')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

# Reset button

reset_btn = Button(game_window, text="Reset", command=reset_all, font=app_font, fg='#2b2b2b', bg='lightgrey')
reset_btn.pack(pady=20)

game_window.geometry('1200x500')  # Game window size
game_window.mainloop()
