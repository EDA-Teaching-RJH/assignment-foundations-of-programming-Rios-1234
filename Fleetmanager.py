def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Cadet", "Lieutenant Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]
    return names, ranks, divs, ids

def display_menu(user):
    print(f"\n Fleet Manager (User: {user})")
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

    try:
        new_id = int(input("ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    if new_id not in ids:
        names.append(name)
        ranks.append(rank)
        divs.append(div)
        ids.append(new_id)
        print("Successfully added!")
    else:
        print("ID already exists!")

def remove_member(names, ranks, divs, ids):
    try:
        remove_id = int(input("ID to remove: "))
    except ValueError:
        print("Invalid ID!")
        return

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

def display_roster(name,rank,div,id):
   print("\n-roster-")
   for i in range(len(name)):
     print(f"{id[i]} | {name[i]} | {rank[i]} | {div[i]}")
     print()

def search_crew(name,rank,div,id):
   search=input("look for name: ").lower()
   print()
   for i in range(len(name)):
     if search in name [i].lower():
          print(f"{id[i]} | {name[i]} | {rank[i]} | {div[i]}")
   print()
  
def filter_by_diviision(name,div):
  div=input("science,commanda,operation")
  print()
  for name,division in zip(name,div):
    if division == div:
      print(name)
print()

def calculating_payroll(ranks):
    pay={
      "captin":1000,
      "cadet":500,
      "lieutenant comander":800,
      "lieutenant":750,
      "comander":900
    }
    return sum(pay.get(rank,0) for rank in ranks)

def counting_officers(ranks):
    return sum(rank in {"Captain", "Commander"} for rank in ranks)

def main():
    user = input("Enter your name: ")
    names, ranks, divs, ids = init_database()

    while True:
        choice = display_menu(user)

        if not choice.isdigit():
            print("Enter a number from 1–9.")
            continue

        choice = int(choice)

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
            print(f"Total payroll: {calculating_payroll(ranks)} credits\n")
        elif choice == 8:
            print(f"Senior officers: {counting_officers(ranks)}\n")
        elif choice == 9:
            print("Exit")
            break


main()
      
      




          
            

      
            
                        
