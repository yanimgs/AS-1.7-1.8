print("Welcome to the Maori knowledge quiz")


# intstruction checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        #if they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")

# Function to display instructions
def instructions():
    print("\nThis is a quiz about testing your Maori knowledge on days of the week. This quiz has multiple choices.")
    print("\n**** How to Play ****")
    print("The example of the format:\n "\
            "\n(A) Right Answer\n(B) Wrong Answer"\
            "\n(C) Wrong Answer\n(C) Wrong Answer\n"\
            "\nPlease choose one for each option. Good Luck.\n")
    print("You will be tested on the days of the week in Maori.")
    print()

# Main routines go here
played_before = yes_no("Do you want to skip the instructions? ")
if played_before.lower() == "no":
    instructions()
else:
    print("You will be tested on the days of the week in Maori.")

import random

def maori_days_quiz():
    days_of_week = {
        'Monday': 'Rāhina',
        'Tuesday': 'Rātū',
        'Wednesday': 'Rāapa',
        'Thursday': 'Rāpare',
        'Friday': 'Rāmere',
        'Saturday': 'Rāhoroi',
        'Sunday': 'Rātapu'
    }

    rounds = 7  # Seven rounds for each question

    score = 0

    for i in range(1, rounds + 1):
        day = random.choice(list(days_of_week.keys()))
        maori_translation = days_of_week[day]

        options = random.sample(list(days_of_week.values()), 4)

        print(f"Question {i}: What is the Maori translation for {day}?")
        print("A. " + options[0])
        print("B. " + options[1])
        print("C. " + options[2])
        print("D. " + options[3])

        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == 'A':
            user_choice = options[0]
        elif user_answer == 'B':
            user_choice = options[1]
        elif user_answer == 'C':
            user_choice = options[2]
        elif user_answer == 'D':
            user_choice = options[3]
        else:
            print("Invalid input. Please enter A, B, C, or D.")
            continue

        if user_choice == maori_translation:
            score += 1

    print("Quiz completed!")
    print(f"Score: {score}/{rounds}")

# Run the quiz
maori_days_quiz()









