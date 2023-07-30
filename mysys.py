tickets_file="tickets.txt"#define the path of file
ticket_list=[]#CREATE an empty list to store all tickets
#Read tickets from txt file 
def read_file_ticket():
    with open(tickets_file,"r")as file:
        for line in file:#https://www.pythontutorial.net/python-basics/python-read-text-file/
            ticket_data=line.strip().split(",")#use strip method to remove trailing space and split to seprated stored data with comma
            ticket_list.append(ticket_data)#with append method we add ticket data to ticket list


def display_statictics():
    #the funtion take a list of ticket as input(ticket_list)
    #check if ticket_list is empty
    if not ticket_list:
        print("No tickets found. ")
        return
    #if ticket_list is not empty the function continue to calculate statistics
    #use dictinnary to store the count of each event id
    event_count={}
    # use for to loop through the ticket_list and count occurences of each event_id
    for ticket in ticket_list:
        event_id=ticket[1]
        event_count[event_id]=event_count.get(event_id,0)+1
    # Find the event_id with highest number of tickets
    #use key argument in max function to compare the element in dictionnary and find the
    #max value where event_id is the key and the ticket count is value the value:https://www.programiz.com/python-programming/methods/built-in/max
    #use get method to retrieve the value assotiated with a given key
    max_event_id=max(event_count,key=event_count.get)
    max_tickets=event_count[max_event_id]
    #f-string used to format the output with concatinating variable and expression in some way to appear
    print(f"Event Id with the highest number of tickets:{max_event_id} ({max_tickets})tickets)")
def book_ticket():
    ticket_id=f"tick{len(ticket_list)+1:03d}"#the tick number formated as 3 digits
    event_id=input("Enter the event ID : ")
    user_name=input("Enter the user name : ")
    date=input("Enter the date of the evenr (YYYMMDD): ")
    priority=int(input("Enter the priority : "))
    new_ticket=[ticket_id,event_id,user_name,date,priority]
    ticket_list.append(new_ticket)
    print("Ticket Booked Successfully !! ")
def display_all_tickets():
    if not ticket_list:
        print("No tickets Found .")
        return
    #show all tickets ordered by event's date and event ID
    # here the lamda function is used to extract elemetn form the list and use it as a key:https://www.programiz.com/python-programming/methods/built-in/max
    sorted_tickets=sorted(ticket_list,key=lambda x:(x[3],x[1]))
    for ticket in sorted_tickets:
        #join method convert every ticket to strings seperated by comma
        print(" , ".join(ticket))
def change_ticket_priority():
    ticket_id=input("Enter the ticket ID to change the priority : ")
    for ticket in ticket_list:
        if ticket[0]==ticket_id:
            new_priority=int(input("Enter the new priority : "))
            ticket[4]=new_priority
            print("Priority changed successfuly !!")
            return
    print("Ticket not found .")

def disable_ticket():
    #removing ticket from system by ticket ID
    ticket_id=input("Enter the ticket ID to disable : ")
    for ticket in ticket_list:
        if ticket[0]==ticket_id:
            ticket_list.remove(ticket)
            print("Ticket disabled successfully!")
            return
    print("Ticket not found ")

def run_event():
    #display today's events found in the list, sorted by priority,and remove them from the list.
    
    today=input("Enter today's date (YYYYMMDD): ")
    for ticket in ticket_list:
        if today==ticket[3]:
            sorted_events=sorted(today,key=lambda x: x[4])
        if not today:
            print("No events Today .")
            return
        for event in sorted_events:
            print(",".join(event))
            ticket_list.remove(event)
                            
def admin_menu():
    attempts=0
    while attempts<5:
        user_name=input("Enter your user name : ")
        password=input("Enter your password : ")
        if user_name=="admin" and password=="admin123123":
            while True:
                print("\nAdmin Menu:")
                print("1. Display Statistics ")
                print("2. Book Ticket ")
                print("3. Display all Tickets ")
                print("4. Change Ticket's Priority ")
                print("5. Disable Ticket ")
                print("6. Run Events ")
                print("7. Exit ")
                choice=input("Enter your Choice please : ")
                if choice=="1":
                    display_statictics()
                elif choice=="2":
                    book_ticket()
                elif choice=="3":
                    display_all_tickets()
                elif choice=="4":
                    change_ticket_priority()
                elif choice=="5":
                    disable_ticket()
                elif choice=="6":
                    run_event()
                elif choice=="7":
                    print("Exiting the program")
                    return
                else:
                    print("Invalid choice.please enter a correct choice from 1-7 .")
        else:
            print("Incorrect Username and/or password.")
            attempts+=1

    print("Maximum attempts reached.Exit the program .")

def user_menu():
    while True:
        print("\nUser Menu : ")
        print("1. Book a Ticket ")
        print("2. Exit ")
        choice=input("Enter your choice 1-2 ? ")
        if choice=="1":
            book_ticket()#already defined 
        elif choice=="2":
            print("Saving  tickets and exit the program. ")
            with open(tickets_file,"w")as file:
                for ticket in ticket_list:
                    file.write(",".join(ticket)+"\n")
            return
        else:
            print("Invalid choice.Try again .")

#write a main  function name main as the starting point of the program
def main():
    read_file_ticket()
    print("Welcome to the Corrupted Ticketing System ! ")
    
    user_input=input("Type if you are Admin or User : """)
    if user_input.lower()=="admin":
        admin_menu()
    elif user_input.lower()=="user":
        user_menu()
    else:
        print("Invalid user type.")
print(main())
