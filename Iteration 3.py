frågor = {"Vilken symbol används för att starta en kommentar?" :{1: ["1. #", "2. &", "3. @"]},
             "Vad är nyckelordet för att definiera en funktion i python?" : {3:["1. Def", "2. define", "3. def"]},
             "Vilken funktion används för att skriva ut saker på skärmen?" : {2:["1. skriva", "2. print", "3. Print"]},
             "Hur tar man fram längden på listan i variabeln 'fruits'?" : {2:["1. length", "2. len", "3. Length"]},
             "Vad heter nyckelordet för att göra en loop i Python?" : {1:["1. for", "2. print", "3. def"]}}

#svar= [["1. #", "2. &", "3. @"],
#       ["1. Def", "2. define", "3. def"],
#       ["1. length", "2. len", "3. Length"],
#       ["1. for", "2. print", "3. def"]]

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

print("Du fick " + str(correct_answers) + " av 5 rätt.")