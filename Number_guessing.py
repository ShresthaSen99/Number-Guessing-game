import random

print ("Welcome to the number guessing game.")
print ("I'm thinking of a number between 1-100.")

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

comp_choosen_number= (random.choice (numbers))
# print (comp_choosen_number)

level = (input("Choose a difficulty level. Type 'easy' or 'hard'.\n"))


def easy_py():
    print ("You have 10 attempts to complete this challenge!")
#easy level
    attempts_e = 10
    attempts_there_e = True

    while attempts_there_e:
        def easy ():
            guess_e= int(input("Guess a number:\n"))
            if guess_e == comp_choosen_number:
                return "bingo"
            elif guess_e != comp_choosen_number:
                if guess_e> comp_choosen_number:
                    print ("Your guess is too High")
                else:
                    print ("Your guess is too Low")
            return attempts_e-1
        
        attempts_e = easy()
        if attempts_e !="bingo":
            result_e = (f"Attempts left {attempts_e}")
        else:
            result_e = (attempts_e)
        print (result_e)


        if result_e == "bingo":
            attempts_there_e = False
            print (f"You got it. The number is {comp_choosen_number}.")

        elif attempts_e == 0:
            print ("Game over")
            attempts_there_e = False



#hard level
def hard_py():
    print ("You have 5 attempts to complete this challenge!")
    attempt_there = True
    attemps = 5

    while attempt_there:
        def hard():
            """ hard level's function"""
            guess = int(input("Guess a number:\n"))
            if guess == comp_choosen_number:
                return "bingo"
            elif guess != comp_choosen_number:
                if guess> comp_choosen_number:
                    print ("Your guess is too High")
                else:
                    print ("Your guess is too Low")
            return attemps-1

        attemps = hard()
        if attemps !="bingo":
            result = (f"Attempts left {attemps}")
        else:
            result = (attemps)
        print (result)

        if result =="bingo":
            attempt_there = False
            print (f"You got it. The number is {comp_choosen_number}.")


        elif attemps == 0:
            print ("Game over")
            attempt_there = False
  

#condition to choose hard or easy method
if level=="easy":
    easy_py()
elif level=="hard":
    hard_py()