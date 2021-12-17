import requests


def download_prize_data():
    """This function download the data as json for further use"""
    r = requests.get("http://api.nobelprize.org/2.1/nobelPrizes")
    r2 = r.json()
    return r2


def category_prize():
    category = {"fysik": "phy",
                "kemi": "che",
                "litteratur": "lit",
                "ekonomi": "eco",
                "fred": "pea",
                "medicin": "med"}
    return category


def find_winner_by_year_and_category():
    category = category_prize()
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
            portion = f["portion"]
            print(data["prizeAmount"]*portion)


def winners_by_year():
    year = input(f"Year >")
    c = {"nobelPrizeYear": int(year)}

    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
    prize = res["nobelPrizes"]
    for num, p in enumerate(prize, start=1):
        print(f"[{num}]  {p['category']['en']}")
        pengar = p["prizeAmount"]
        print(f"\033[97m{p['categoryFullName']['se']} prissumma {pengar} SEK")
        for m in p["laureates"]:
            # print(m["knownName"])
            print(f"\033[94mMotivation: \033[97m{m['motivation']['en']}")