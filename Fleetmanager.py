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

def update_ranks(name,rank,id):
  search_id = int(input("Id update: "))
  if search_id in id:
    index = id.index(search_id)
    rank[index] = input ("New Rank")
    print(" New rank Updated")
  else:
    print("Id not found")

 def search_crew(name,rank,div,id):
   search=input("look for name: ").lower()
   print()
   for i in range(len(name)):
     if search in name [i].lower():
          print(f"{id[i]} | {name[i]} | {rank[i]} | {div[i]}")
   print()

 def display_roster(name,rank,div,id):
   print("\n-roster-")
   for i in range(len(name)):
     print(f"{id[i]} | {name[i]} | {rank[i]} | {div[i]}")
     print()

