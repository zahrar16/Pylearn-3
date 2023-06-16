
import random

word_bank = ["zahra" , "fateme" , "sara" , "nazi" , "pari" , "hadis"]
user_mistakes = 0

good_chars = []
bad_chars = []

x = random.randint(0,len(word_bank)-1)
word = word_bank[x]

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end="")
        else:
            print("- ", end="")

    if len(word) == len(good_chars):
        print("  you win :)")
        break

    user_char = input("please enter your guess : ")
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("yes")
        else:
            bad_chars.append(user_char)
            user_mistakes += 1
            print("no")
    else:
        print("yek harf vared kon :")

if user_mistakes == 6:
    print("game over  :|")

    