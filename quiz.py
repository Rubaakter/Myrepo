questions = ["Vilken funktion används för att skriva ut saker på skärmen?",
    "Hur tar man fram längden på listan i variabeln 'fruits'?",
    "Vad heter nyckelordet för att göra en loop i Python?"]

correct_answers = 0
for i in range(3):
    print(questions[i])
    answer = (input("Ditt svar: "))
    print(answer)
    if i==0:
        if answer == "print":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: print")
    if i==1:
        if answer == "len":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: len")
    if i==2:
        if answer == "for":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: for")

print("Du fick " + str(correct_answers) + " av 3 rätt.")

