from Questions import frågor

correct_answers = 0
i = 0
for i in frågor:
    print(i)
    answer = (input("Ditt svar: ").lower())
    print(answer)
    if answer == frågor[i] :
        print ("Rätt svar!")
        correct_answers += 1
    else:
        print("Fel svar")
        print(f"Rätt svar: {frågor[i]} ")

print("Du fick " + str(correct_answers) + " poäng av 10 möjliga.")

