import requests


def download_prize_data():
    """This function download the data as json for further use"""
    r = requests.get("http://api.nobelprize.org/2.1/nobelPrizes")
    r2 = r.json()
    return r2

HELP_STRING = """
Ange ett år och fält
Exempelvis:  1965 fysik
"""

category = {"fysik": "phy",
            "kemi": "che",
            "litteratur": "lit",
            "ekonomi": "eco",
            "fred": "pea",
            "medicin": "med"}


def find_winner_by_year_and_category():
    year = input(f"Year >")
    p_category = input(f"\033[96mPrize category > \n")
    c = category[p_category]
    c = {"nobelPrizeYear": int(year), "nobelPrizeCategory": c}

    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
    for p in res["nobelPrizes"]:
        pengar = p["prizeAmount"]
        print(f"\033[97m{p['categoryFullName']['se']} prissumma {pengar} SEK")

        winner = p["laureates"]
        for num, m in enumerate(winner, start=1):
            print(f"[{num}] Namnet på vinnaren är: {m['knownName']['en']}")
            print(f"\033[94mMotivation: \033[97m{m['motivation']['en']}")


def find_winners_prize():
    prize_data = download_prize_data()
    for data in prize_data["nobelPrizes"]:
        for f in data["laureates"]:
            portion = str(f["portion"])
            print(data["prizeAmount"]*portion)


def winners_by_year():
    year = input(f"Year >")
    c = {"nobelPrizeYear": int(year)}

    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
    prize = res["nobelPrizes"]
    for num, p in enumerate(prize, start=1):
        print(f"[{num}]  {p['category']}")
        pengar = p["prizeAmount"]
        print(f"\033[97m{p['categoryFullName']['se']} prissumma {pengar} SEK")
        for m in p["laureates"]:
            print(m['knownName']['en'])
            print(f"\033[94mMotivation: \033[97m{m['motivation']['en']}")


def main():
    print("""
     ---> MENU <---
            1) Name of the winner or winners based on year and prize category
            2) Amount of prize each winner received at a specific year and category
            3) Name of all winners in a certain years
            Q) Quit
    """)

    while True:
        print(HELP_STRING)
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
            print("Please choice a number from 1-4 or press 'Q'")


if __name__ == '__main__':
    main()
