import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game=False
word_list=["reaper","destroyer","butcher"]
chosen_word=random.choice(word_list)
print(f"the chosen word is {chosen_word}")
lives=6
display=[]
# for letter in range(len(chosen_word)):
for letter in chosen_word:
    display+="_"
print(display)

while not end_of_game:
    guess=input("guess the letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you loose")
    
    print(display)

    if "-" not in display:
        end_of_game=True
        print("you win")
    print(stages[lives])



