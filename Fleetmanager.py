def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Cadet", "Lieutenant Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]
    return names, ranks, divs, ids

def display_menu(user):
  print(f"\n Fleet Manager (User: {user})")
  print("1 Add crew memeber")
  print("2 remove crew member")
  print("3 update rank")
  print("4 Dispay roster")
  print("5 search crew")
  print("6 Filter by division")
  print("7 calculate pay roll")
  print("8 count officers")
  print("9 exit")
  return input("choice: ")
 
def add_a_crew_member(name,rank,div,id):
 name = input("name: ")
 rank = input("rank: ") 
 div = input("division: ")
 new_id = int(input("ID: "))

 if new_ID not in ids:
  names.append(name)
  rank.append(rank)
  div.append(div)
  id.appends(new_id)
  print("added")
 else:
  print("Id already exsists")

def remove_member(names, ranks, divs, ids):
    remove_id = int(input("ID to remove: "))
    if remove_id in ids:
        index = ids.index(remove_id)
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("Removed")
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
 return sum(rank in {"captain", "commander"} for rank in ranks

def main():
    user = input ("enter your name")
    name,rank,div,id = init_database()

    while true:
      choice = display_menu(user)

      if int(choice) ==1:
       add_member(name,rank,div,id)
      elif int(choice) ==2:
        remove_member(name,rank,div,id)
      elif int(choice) ==3:
        update_rank(name,rank,div,id)
      elif int(chooice) ==4:
         display_roster(name,rank,div,id)
      elif int(choice) ==5:
        search_crew(name,rank,div,id)
      elif int(choice) ==6:
        filter_by_division(name,rank,div,id)
      elif int(choice) ==7:
        print(f"total payroll: {calculate_payroll(ranks)} british_pounds\n")
      elif int(choice) ==8:
       print(f"Senior officers: {count_officers(ranks)}\n")
      elif int(choice) ==9:
        print("excape") 
        break
main()
      
      




          
            

      
            
                        
