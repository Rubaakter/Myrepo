frågor = {"Vilken symbol används för att starta en kommentar?" : "#",
             "Vad är nyckelordet för att definiera en funktion i python?" : "def",
             "Vilken funktion används för att skriva ut saker på skärmen?" : "print",
             "Hur tar man fram längden på listan i variabeln 'fruits'?" : "len",
             "Vad heter nyckelordet för att göra en loop i Python?" : "for"}

correct_answers = 0
i = 0
for i in frågor:
    print(i)
    answer = (input("Ditt svar: "))
    print(answer)
    if answer == frågor[i] :
        print ("Rätt svar!")
        correct_answers += 1
    else:
        print("Fel svar")
        print(f"Rätt svar: {frågor[i]} ")

print("Du fick " + str(correct_answers) + " av 5 rätt.")


# correct_answers = 0
# for i in range(5):
#     print(frågor[i])
#     answer = (input("Ditt svar: "))
#     print(answer)
#     if i == 0:
#         if answer == "#":
#             print("Rätt!")
#             correct_answers += 1
#         else:
#             print("Fel!")
#             print("Rätt svar: #")
#     if i == 1:
#         if answer == "def":
#             print("Rätt!")
#             correct_answers += 1
#         else:
#             print("Fel!")
#             print("Rätt svar: def")
#     if i == 2:
#         if answer == "print":
#             print("Rätt!")
#             correct_answers += 1
#         else:
#             print("Fel!")
#             print("Rätt svar: print")
#     if i == 3:
#         if answer == "len":
#             print("Rätt!")
#             correct_answers += 1
#         else:
#             print("Fel!")
#             print("Rätt svar: len")
#     if i == 4:
#         if answer == "for":
#             print("Rätt!")
#             correct_answers += 1
#         else:
#             print("Fel!")
#             print("Rätt svar: for")
#
# print("Du fick " + str(correct_answers) + " av 5 rätt.")
