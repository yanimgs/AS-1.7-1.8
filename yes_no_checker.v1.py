def yes_no_checker():
    while True:
        response = input("Yes or no checker: ").lower()

        if response == 'yes' or response == 'y':
            print("You entered 'yes'.")
        elif response == 'no' or response == 'n':
            print("You entered 'no'.")
        else:
            print("Please enter 'yes' or 'no'")
            continue
yes_no_checker()










