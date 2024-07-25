# Day : 27 Exercise 3 : Kaun Banega Crorepati (KBC): Solution : By Me

# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

questions = [
    [
        "1. Who developed Python Programming Language?", "a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom", 3
    ],
    [
        "2. Which type of Programming does Python support?", "a) object-oriented programming", "b) structured programming", "c) functional programming", "d) all of the mentioned", 4
    ],
    [
        "3. Is Python case sensitive when dealing with identifiers?", "a) no", "b) yes", "c) machine dependent", "d) none of the mentioned", 2
    ],
    [
        "4. Which of the following is the correct extension of the Python file?", "a) .python", "b) .pl", "c) .py", "d) .p", 3
    ],
    [
        "5. Is Python code compiled or interpreted?", "a) Python code is both compiled and interpreted", "b) Python code is neither compiled nor interpreted", "c) Python code is only compiled", "d) Python code is only interpreted", 1
    ],
    [
        "6. All keywords in Python are in _________", "a) Capitalized", "b) lower case", "c) UPPER CASE", "d) None of the mentioned", 4
    ],
    [
        "7. What will be the value of the following Python expression? -->> 4 + 3 % 5", "a) 7", "b) 2", "c) 4", "d) 1", 1
    ],
     [
        "8. Which of the following is used to define a block of code in Python language?", "a) Indentation", "b) Key", "c) Brackets", "d) All of the mentioned", 1
    ],
    [
        "9. Which keyword is used for function in Python language?", "a) Function", "b) def", "c) Fun", "d) Define", 2
    ],
    [
        "10. Which of the following character is used to give single-line comments in Python??", "a) //", "b) #", "c) !", "d) /*", 2
    ],
    [
        "11. Which of the following functions can help us to find the version of python that we are currently working on?", "a) sys.version(1)", "b) sys.version(0)", "c) sys.version()", "d) sys.version", 4
    ],
    [
        "12. Python supports the creation of anonymous functions at runtime, using a construct called __________", "a) pi", "b) anonymous", "c) lambda", "d) none of the mentioned", 3
    ],
    [
        "13. What is the order of precedence in python?", "a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction", "c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition", "d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction", 4
    ],
    [
        "14. What will be the output of the following Python code snippet if x=1?? : x<<2", "a) 4", "b) 2", "c) 1", "d) 8", 1
    ],
    [
        "15. What does pip stand for python?", "a) Pip Installs Python", "b) Pip Installs Packages", "c) Preferred Installer Program", "d) All of the mentioned", 3
    ],
    [
        "16. Which of the following is true for variable names in Python?", "a) underscore and ampersand are the only two special characters allowed", "b) unlimited length", "c) all private members must have leading and trailing underscores", "d) none of the mentioned", 2
    ]
]

positions = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
Paisa = 0


for i in range(0, len(questions)):
    question = questions[i]

    print(f"{question[0]} for {positions[i]} Rupees")
    print(f"{question[1]}         {question[2]}")
    print(f"{question[3]}         {question[4]}")

    answer = int(input("Enter your answer: bet [1-4]\n"))
    if (answer == 0):
    Paisa = positions[i-1]
    break

    if(answer == question[-1]):
        print(f"Congrats, Your answer is absolutely Right. Now, You won {positions[i]} Rupees")
        if(i == 4):
            Paisa = 10000
        elif(i == 9):
            Paisa == 320000
        elif(i == 14):
            money = 10000000
        elif(i == 15):
            Paisa = 70000000
    else:
        print("Sorry, Your answer is wrong.")
        break

print(f"Your final won rupees is {Paisa}")










































