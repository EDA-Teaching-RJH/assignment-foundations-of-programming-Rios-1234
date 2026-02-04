def name,rank,div 
n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print ("loading module " + str(loading)) # You can format numbers, padding, precision, etc., inside the braces:
        loading += 1 
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ").strip() # .strip() removes leading/trailing spaces e.g  ("1 ")
        
        if opt == "1":# == asks a question: Is opt equal to "1"? whereas = is setting a value 
            print("Current Crew List:")
            
            for i in range(10):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + str(count)) # Fix print statement for high ranking officers count
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = len(n) #  When you want x to match the size of a list/string/etc. not just a value.
        if x > 0:   # This only prints for numbers strictly above 5.(if x > 5:) whereas (if x > 0:) prints for any positive number.
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        else: # saying if 0 is not greater than 0 print database empty
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()# this result of calling the function instead of just the function itself.

