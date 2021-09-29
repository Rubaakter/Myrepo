f1 ="""Vilken symbol används för att starta en kommentar?
    1. #
    2. &
    3. %"""
f2 ="""Vad är nyckelordet för att definiera en funktion i python?
    1. define
    2. Def
    3. def"""
f3 = """Vilken funktion används för att skriva ut saker på skärmen?
    1. print
    2. skriva
    3. P"""
f4 = """Hur tar man fram längden på listan i variabeln 'fruits'?
     1. length
     2. Leng
     3. len"""
f5 = """ Vad heter nyckelordet för att göra en loop i Python?
    1. loop
    2. for
    3. if"""
f6 = """Hur får man tillgång till ett enskilt objekt på listan?
     1. len
     2. key
     3. index"""
f7 = """Vilken operatör returnerar heltalets återstod (modulo) av divisionen?
     1. %
     2. /
     3. //"""
f8 = """Hur kan du kontrollera objektets typ?
    1. index()
    2. type()
    3. typ()"""
f9 = """Vad heter behållare för lagring av datavärden?
     1. variabel
     2. lagring
     3. minne"""
f10 = """Hur skriver man datatypen för ett helt tal?
    1. float
    2. int
    3. str"""
svar = {f1: "1", f2: "3", f3: "1", f4:"3", f5:"2", f6: "3", f7: "1", f8: "2", f9: "1", f10: "2"}

correct_answers = 0
i = 0
for i in svar:
    print(i)
    answer = (input("Ditt svar (från 1/2/3): "))
    print(answer)
    if answer == svar[i] :
        print("Rätt svar!")
        correct_answers += 1
    else:
        print("Fel svar")
        print(f"Rätt svar: {svar[i]} ")

print("Du fick " + str(correct_answers) + " poäng av 10 möjliga.")