# Hangman Game
import random #random module for random choice selection
words=["python","java","hangman","robot","blockchain"] #I take the 5 words for the random se;ection
word=random.choice(words) #using the random keyword to select any word from the list
display=["_"]*len(word) #creating the display of _ according to the length of randomly selected word from 5 words which are provided to the list
lives=6 #these are the 6 lives for users to complete or guess the correct word to win the game
print("WELCOME TO THE HANGMAN GAME") #this massage is for welcoming the user in the game
print(f"YOU HAVE {lives} LIVES") #this massage shows the remenaing or current lives which are available for the user
print(" ".join(display)) #displaying _ according to the length of word
while "_" in display and lives>0: #loop will run until all the letters are guess or lives become 0
    guess=input("Guess a Letter:").lower() #its take the input from the user and convert them to the lowercase using lower() function
    if guess in display: #cheking condition if letter is already guess
        print("YOU ALREADY ENTERED THIS LATTER.")
        continue #this statement can skip the rest of the loop and start next iteration here
    if guess in word: #check condition if guessed letter in the word
        for i in range(len(word)): #loop through each latter in the word
            if word[i]==guess: #check condition if guess latter is as same as letter in word
                display[i]=guess #update display using index i to correct position of latter
        print("CORRECT GUESS!") 
    else: #if guess letter is not in the word
        lives -= 1 #decrement lives by 1 if user guess the wrong letter
        print("SORRY WRONG GUESS! YOU LOST ONE LIFE") 
    print(" ".join(display))
    print("LIVES LEFT",lives)

if "_" not in display: #check condition if user guessed all letters correctly
    print("CONGRATULATION YOU GUESS THE CORRECT WORD!")
else: #if user loose all lives
    print("SORRY THE GAME IS OVER AND THE WORD IS:",word)