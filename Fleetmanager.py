def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Cadet", "Lieutenant Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]
    return names, ranks, divs, ids


def display_menu(user):
    print(f"\n Fleet Manager (User: {user})") #using \n keeps it nice and tidy by creating a new line.
    print("1 Add crew member")
    print("2 Remove crew member")
    print("3 Update rank")
    print("4 Display roster")
    print("5 Search crew")
    print("6 Filter by division")
    print("7 Calculate payroll")
    print("8 Count officers")
    print("9 Exit")
    return input("Choice: ")


def add_a_crew_member(names, ranks, divs, ids):
    name = input("Name: ")
    rank = input("Rank: ")
    div = input("Division: ")

    user_input = input("ID: ")

    # Check if the ID is a valid integer
    if not user_input.isdigit():
        print("Invalid ID!")
        return

    new_id = int(user_input) # making sure its a number input

    if new_id not in ids:
        names.append(name)
        ranks.append(rank)
        divs.append(div)
        ids.append(new_id)
        print("Successfully added!")
    else:
        print("ID already exists!")


def remove_member(names, ranks, divs, ids):
    remove_id_str = input("ID to remove: ")

    if not remove_id_str.isdigit(): # isdigit() ensures the input contains only numeric characters.

        print("Invalid ID!")
        return

    remove_id = int(remove_id_str)

    if remove_id in ids:
        index = ids.index(remove_id)
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("Removed!")
    else:
        print("ID not found!")



def update_ranks(name,rank,id):
  search_id = int(input("Id update: "))
  if search_id in id:
    index = id.index(search_id)
    rank[index] = input ("New Rank")
    print(" New rank Updated")
  else:
    print("Id not found")


def display_roster(names, ranks, divs, ids):
    print("\nRoster ")
    for i in range(len(names)):
        print(f"{ids[i]} | {names[i]} | {ranks[i]} | {divs[i]}")
    print()


def search_crew(names, ranks, divs, ids):
    search = input("Look for name: ").lower()
    print()
    for i in range(len(names)):
        if search in names[i].lower():
            print(f"{ids[i]} | {names[i]} | {ranks[i]} | {divs[i]}")
    print()


def filter_by_division(names, divs):
    division = input("Enter division (Command / Operations / Sciences): ").strip().lower()
    print()

    if division == "command":
        target = "Command"
    elif division == "operations":
        target = "Operations"
    elif division == "sciences":
        target = "Sciences"
    else:
        print("Invalid division.")
        return

    for name, div in zip(names, divs): # zip is a good way to cleaning up the code as its good for lopping over two things at the same time
        if div == target:
            print(name)

    print()



def calculating_payroll(ranks):
    pay = {
        "Captain": 1000,
        "Cadet": 500,
        "Lieutenant Commander": 800,
        "Lieutenant": 750,
        "Commander": 900
    }
    return sum(pay.get(rank, 0) for rank in ranks)


def counting_officers(ranks):
    return sum(rank in {"Captain", "Commander"} for rank in ranks)


def main():
    user = input("Enter your name: ")
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu(user)

        if not choice.isdigit():# isdigit keeps it the correct format e.g a number.
            print("Enter a number from 1–9.")
            continue

        choice = int(choice) # this means it has to be a number choice for it to work.

        if choice == 1:
            add_a_crew_member(names, ranks, divs, ids)
        elif choice == 2:
            remove_member(names, ranks, divs, ids)
        elif choice == 3:
            update_ranks(names, ranks, ids)
        elif choice == 4:
            display_roster(names, ranks, divs, ids)
        elif choice == 5:
            search_crew(names, ranks, divs, ids)
        elif choice == 6:
            filter_by_division(names, divs)
        elif choice == 7:
            print(f"Total payroll: {calculating_payroll(ranks)} britsh pounds\n")
        elif choice == 8:
            print(f"Senior officers: {counting_officers(ranks)}\n")
        elif choice == 9:
            print("Exit")
            break


main()
      
      




          
            

      
            
                        
