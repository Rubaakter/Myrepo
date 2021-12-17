from tentamen.tenta_functions import find_winner_by_year_and_category, find_winners_prize, winners_by_year


def main():
    print("""
     ---> MENU <---
            1) Name of the winner or winners based on year and prize category
            2) Amount of prize each winner received at a specific year and category
            3) Name of all winners in a certain years
            Q) Quit
    """)

    while True:
        user_choice = input("Which of the above list do you want? ").upper().strip()
        if user_choice == '1':
            find_winner_by_year_and_category()
        elif user_choice == '2':
            find_winners_prize()
        elif user_choice == '3':
            winners_by_year()
        elif user_choice.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return
        else:
            print("Please choice a number from 1-3 or press 'Q'")


if __name__ == '__main__':
    main()
