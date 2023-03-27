print("Welcome To Terminal_Quiz")
print("Are Sure To want To Play?", )
a = input().lower()
print("Let's Play" if a == 'yes' else quit())

Score = 0
# Question (1)
print("What is the sum of 2+5? ")
answer = input().lower()
if answer == '7':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (2)
print("What is the sum of 22+5? ")
answer = input().lower()
if answer == '27':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (3)
print("What is the sum of 22+55? ")
answer = input().lower()
if answer == '77':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (4)
print("Who is the cm of odisha? ")
answer = input().lower()
if answer == 'nabin':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (5)
print("What is the sum 2x and 3x ")
answer = input().lower()
if answer == '5x':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (6)
print("What is the Fullform of CPU ")
answer = input().lower()
if answer == 'central processing unit':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')

# Question (7)
print("What is the Fullform of ups ")
answer = input().lower()
if answer == 'uniterputted power supply':
    print("Correct")
    Score = Score + 1
else:
    print('Incorrect')



print('Your Score is ' + str(Score))
print('pass' if Score > 3 else 'fail')
if Score >= 5:
    print('Brilliant')
else:
    print('Avg')
