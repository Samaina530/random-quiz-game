print("----------Welcome to the quiz game----------")
answer=input('Do you wanna play? ').lower()
if answer!='yes':
    print('Bye bye!')
    quit()

print("let's start playing! ")
score=0

playing=True
while playing:
    answer=input('Who is the author of Harry Potter? ').lower()

    if answer!='jk rowling':
        print("Incorrect answer")

        ans=input("do you wanna try until you get it correct?(q to quit and move to next question) ").lower()
        if ans=='q':
                playing=False
        else:
                playing=True
    else:
        print("Correct answer!")
        score += 1
        playing=False

playing=True
while playing:
    answer=input('Who is the author of Metamorphosis? ').lower()

    if answer!='franz kafka':
        print("Incorrect answer")

        ans = input("do you wanna try until you get it correct?(q to quit and move to next question) ").lower()
        if ans == 'q':
            playing = False
        else:
            playing = True

    else:
        print("Correct answer!")
        score += 1
        playing = False
playing = True
while playing:

    answer=input('Who is the author of Sherlock Holmes? ').lower()

    if answer!='sir arthur conan doyle':
        print("Incorrect answer")

        ans = input("do you wanna try until you get it correct?(q to quit and end the game) ").lower()
        if ans == 'q':
            playing = False
        else:
            playing = True
    else:
        print("Correct answer!")
        score += 1
        playing = False

print(f'You scored {score} ')

#print("You got "+str(score/3*100)+"% answers correctly")
#but I can't get two digits after point as an output in this way

percentage=float(score/3*100)

print(f"You got {percentage:.2f}% answers correctly") #This is something I know

#print(f"You got {score/3*100:.2f}% answers correctly")


input("Press Enter to close the game...")


