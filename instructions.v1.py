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
    print("\n**** How To Play ****")
    print("This is a quiz about testing your Maori knowledge, this quiz has multiple choices.")
    print("\n**** The rules of the quiz will go here ****")
    print("The example of the format:\n "\
            "\n(A) Right Answer\n(B) Wrong Answer"\
            "\n(C) Wrong Answer\n(C) Wrong Answer\n"\
            "\nChoose one for each option. Good Luck.\n")
    print("Game starts")
    print()

# Main routines go here
played_before = yes_no("Have you played this game before? ")
if played_before.lower() == "no":
    instructions()
else:
    print("Game starts")
