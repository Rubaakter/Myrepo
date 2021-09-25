questions = ["Vilken symbol används för att starta en kommentar?",
             "Vad är nyckelordet för att definiera en funktion i python?",
             "Vilken funktion används för att skriva ut saker på skärmen?",
             "Hur tar man fram längden på listan i variabeln 'fruits'?",
             "Vad heter nyckelordet för att göra en loop i Python?"]

correct_answers = 0
for i in range(5):
    print(questions[i])
    answer = (input("Ditt svar: "))
    print(answer)
    if i == 0:
        if answer == "#":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: #")
    if i == 1:
        if answer == "def":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: def")
    if i == 2:
        if answer == "print":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: print")
    if i == 3:
        if answer == "len":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: len")
    if i == 4:
        if answer == "for":
            print("Rätt!")
            correct_answers += 1
        else:
            print("Fel!")
            print("Rätt svar: for")

print("Du fick " + str(correct_answers) + " av 5 rätt.")