from Questions import frågor


def main():
    print("EXEMPELKÖRNING:    ")
    print("'''                      ")
    correct_answers = 0
    for i in frågor:
        print(i)
        answer = (input("Ditt svar (från 1/2/3): "))
        print(answer)
        if answer == frågor[i] :
            print("Rätt svar!")
            correct_answers += 1
        else:
            print("Fel svar")
            print(f"Rätt svar: {frågor[i]} ")
    print("                                      ")
    print(f"""**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av {str(len(frågor))}  möjliga.")


if __name__ == '__main__':
    main()