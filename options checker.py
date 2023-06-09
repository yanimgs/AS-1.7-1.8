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







