def init_database():
  names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
  ranks = ["Captain", "Cadet", "Lieutenant Commander", "Lieutenant", "Commander"]
  divs =  ["Command", "Command", "Operations", "Operations", "Sciences"]
  ids = [1001, 1002, 1003, 1004, 1005]
  return names,ranks,divs,ids

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
 new-id = int(input("ID: "))

 if new_ID not in ids:
  names.append(name)
  rank.append(rank)
  div.append(div)
  id.appends(new_id)
  print("sucessfully added")
 else:
  print("Id already exsists")

def remove_memeber(name,rank,div,id):
  remove id=int(input("reomve id: ")
  if remove_id in id:
    index = id.index(remove_id)
    name.pop.(index)
    rank.pop(index)
    div.pop(index)
    id.pop(index)
    print("memebr removed")
else:
    print("Id not ffound ")
  

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

def calculating_payroll
    pay={
      "captin":1000,
      "cadet":500,
      "lieutenant comander":800,
      "lieutenant":750
      "comander":900
    }
    return sum(pay.get(rank,0) for rank in ranks)

def counting_officers(ranks)
 return sum(rank in {"captin", "commander"} for rank in ranks




          
            

      
            
                        
