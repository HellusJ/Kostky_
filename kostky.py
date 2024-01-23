import random 
import time as t


print("\nVítejte ve hře kostky, kde budete soupeřit proti Vaškovi")
print("Kdo jako první získá 5000 bodů, tak vyhrává")
input("Zmáčkněte enter pro pokračování: ")

players_points = 0
vasek_points = 0

while True: 

    print("\nNyní jste na řadě, doporučuji si otevřít v přiloženém souboru pravidla kostek")
    input("zmáčkněte enter pro hození kostek: ")
    print("*kostky vrženy*")
    t.sleep(2.2)

    players_numbers = []
    vasek_numbers = []

    if players_points >= 5000:
        print("Gratuluji k výhře, dokázal jste jako první získat 5000 bodů")
        break

    if vasek_points >= 5000:
        print("Prohrál jste, Vašek získal 5000 ale nevadí, můžete to klidně zkusit znovu")
        break

    #-------HRACUV TAH-------
    for x in range(6):
        number = random.randint(1,6)
        players_numbers.append(number)

    #postupka
    postupka = set([1,2,3,4,5,6])
    new_numbers = set(players_numbers)

    if new_numbers == postupka:
        print("padla vám tzv. postupka, gratuluji získáváte 1500 bodů")
        players_numbers += 1500
        t.sleep(2)

    #dále
    players_numbers = ''.join(map(str, players_numbers))
    print(f"\nVaše čísla: {players_numbers}")

    pocet_jednicek = players_numbers.count("1")
    pocet_dvojek = players_numbers.count("2")
    pocet_trojek = players_numbers.count("3")
    pocet_ctverek = players_numbers.count("4")
    pocet_petek = players_numbers.count("5")
    pocet_sestek = players_numbers.count("6")

    #jednicky
    if pocet_jednicek == 1:
        players_points += 100
    if pocet_jednicek == 2:
        players_points += 200
    if pocet_jednicek == 3:
        players_points += 1000
    if pocet_jednicek == 4:
        players_points += 2000
    if pocet_jednicek == 5:
        players_points += 4000
    if pocet_jednicek == 6:
        players_points += 8000
    
    #dvojky
    if pocet_dvojek == 3:
        players_points = players_points + (2 * 100)
    if pocet_dvojek == 4:
        players_points = players_points + (2 * 200)
    if pocet_dvojek == 5:
        players_points = players_points + (2 * 300)
    if pocet_dvojek == 6:
        players_points = players_points + (2 * 500)   
    
    #trojky
    if pocet_trojek == 3:
        players_points = players_points + (3 * 100)
    if pocet_trojek == 4:
        players_points = players_points + (3 * 200)
    if pocet_trojek == 5:
        players_points = players_points + (3 * 300)
    if pocet_trojek == 6:
        players_points = players_points + (3 * 500)

    #ctverky
    if pocet_ctverek == 3:
        players_points = players_points + (4 * 100)
    if pocet_ctverek == 4:
        players_points = players_points + (4 * 200)
    if pocet_ctverek == 5:
        players_points = players_points + (4 * 300)
    if pocet_ctverek == 6:
        players_points = players_points + (4 * 500)

    #petky
    if pocet_petek == 1:
        players_points += 50
    if pocet_petek == 2:
        players_points += 100
    if pocet_petek == 3:
        players_points = players_points + (5 * 100)
    if pocet_petek == 5:
        players_points = players_points + (5 * 200)
    if pocet_petek == 5:
        players_points = players_points + (5 * 300)
    if pocet_petek == 6:
        players_points = players_points + (5 * 500) 

    #sestky
    if pocet_sestek == 3:
        players_points = players_points + (6 * 100)
    if pocet_sestek == 5:
        players_points = players_points + (6 * 200)
    if pocet_sestek == 5:
        players_points = players_points + (6 * 300)
    if pocet_sestek == 6:
        players_points = players_points + (6 * 500) 

    #3_dvojice

    #vyhodnoceni hrace
    print(f"Hodil jste {pocet_jednicek}krát číslo 1")
    print(f"Hodil jste {pocet_dvojek}krát číslo 2")
    print(f"Hodil jste {pocet_trojek}krát číslo 3")
    print(f"Hodil jste {pocet_ctverek}krát číslo 4")
    print(f"Hodil jste {pocet_petek}krát číslo 5")
    print(f"Hodil jste {pocet_sestek}krát číslo 6")
    print("*Počítám body*")
    t.sleep(3.1)
    print(f"\nVáš momentální počet bodů: {players_points}")
    t.sleep(2)

    #vyhra/prohra
    if vasek_points > players_points:
        prohra = (vasek_points - players_points)
        print(f"Vašek vede o {prohra}")

    elif vasek_points < players_points:
        vyhra = (players_points - vasek_points)
        print(f"vedete o {vyhra}")

    else:
        print("Oba máte stejný počet bodů")

    #-------VASKUV TAH-------
    print("\nNyní je na řadě Vašek")
    input("Zmáčkněte enter pro pokračování: ")

    print("*Vašek háže*")
    t.sleep(2)

    for y in range(6):
        number2 = random.randint(1,6)
        vasek_numbers.append(number2)

    #postupka
    postupka2 = set([1,2,3,4,5,6])
    new_numbers2 = set(vasek_numbers)

    if new_numbers2 == postupka2:
        print("Vaškovi padla tzv. postupka a získává tím 1500 bodů")
        vasek_points += 1500
    t.sleep(2)

    vasek_numbers = ''.join(map(str, vasek_numbers))
    print(f"\nVaškovi čísla: {vasek_numbers}")

    pocet_jednicek = vasek_numbers.count("1")
    pocet_dvojek = vasek_numbers.count("2")
    pocet_trojek = vasek_numbers.count("3")
    pocet_ctverek = vasek_numbers.count("4")
    pocet_petek = vasek_numbers.count("5")
    pocet_sestek = vasek_numbers.count("6")

    #jednicky
    if pocet_jednicek == 1:
        vasek_points += 100
    if pocet_jednicek == 2:
        vasek_points += 200
    if pocet_jednicek == 3:
        vasek_points += 1000
    if pocet_jednicek == 4:
        vasek_points += 2000
    if pocet_jednicek == 5:
        vasek_points += 4000
    if pocet_jednicek == 6:
        vasek_points += 8000
    
    #dvojky
    if pocet_dvojek == 3:
        vasek_points = vasek_points + (2 * 100)
    if pocet_dvojek == 4:
        vasek_points = vasek_points + (2 * 200)
    if pocet_dvojek == 5:
        vasek_points = vasek_points + (2 * 300)
    if pocet_dvojek == 6:
        vasek_points = vasek_points + (2 * 500)   
    
    #trojky
    if pocet_trojek == 3:
        vasek_points = vasek_points + (3 * 100)
    if pocet_trojek == 4:
        vasek_points = vasek_points + (3 * 200)
    if pocet_trojek == 5:
        vasek_points = vasek_points + (3 * 300)
    if pocet_trojek == 6:
        vasek_points = vasek_points + (3 * 500)

    #ctverky
    if pocet_ctverek == 3:
        vasek_points = vasek_points + (4 * 100)
    if pocet_ctverek == 4:
        vasek_points = vasek_points + (4 * 200)
    if pocet_ctverek == 5:
        vasek_points = vasek_points + (4 * 300)
    if pocet_ctverek == 6:
        vasek_points = vasek_points + (4 * 500)

    #petky
    if pocet_petek == 1:
        vasek_points += 50
    if pocet_petek == 2:
        vasek_points += 100
    if pocet_petek == 3:
        vasek_points = vasek_points + (5 * 100)
    if pocet_petek == 5:
        vasek_points = vasek_points + (5 * 200)
    if pocet_petek == 5:
        vasek_points = vasek_points + (5 * 300)
    if pocet_petek == 6:
        vasek_points = vasek_points + (5 * 500)

        #sestky
    if pocet_sestek == 3:
        vasek_points = vasek_points + (6 * 100)
    if pocet_sestek == 5:
        vasek_points = vasek_points + (6 * 200)
    if pocet_sestek == 5:
        vasek_points = vasek_points + (6 * 300)
    if pocet_sestek == 6:
        vasek_points = vasek_points + (6 * 500) 

    #3_dvojice

    #vyhodnoceni vaška
    print(f"Vašek hodil {pocet_jednicek}krát číslo 1")
    print(f"Vašek hodil {pocet_dvojek}krát číslo 2")
    print(f"Vašek hodil {pocet_trojek}krát číslo 3")
    print(f"Vašek hodil {pocet_ctverek}krát číslo 4")
    print(f"Vašek hodil {pocet_petek}krát číslo 5")
    print(f"Vašek hodil {pocet_sestek}krát číslo 6")
    print("*Počítám body*")
    t.sleep(3.1)
    print(f"\nVaškův momentální počet bodů: {vasek_points}")
    t.sleep(2)

    #vyhra/prohra
    if vasek_points > players_points:
        prohra = (vasek_points - players_points)
        print(f"Vašek vede o {prohra}")

    elif vasek_points < players_points:
        vyhra = (players_points - vasek_points)
        print(f"vedete o {vyhra}")

    else:
        print("Oba máte stejný počet bodů")

    input("Zmáčkněte enter pro pokračování: ")

exit()
