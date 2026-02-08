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

