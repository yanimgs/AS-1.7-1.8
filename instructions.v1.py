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
