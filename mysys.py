tickets_file="tickets.txt"#define the path of file
ticket_list=[]#CREATE an empty list to store all tickets
#Read tickets from txt file 
with open(tickets_file,"r")as file:
    for line in file:#https://www.pythontutorial.net/python-basics/python-read-text-file/
        ticket_data=line.strip().split(",")#use strip method to remove trailing space and split to seprated stored data with comma
        ticket_list.append(ticket_data)#with append method we add ticket data to ticket list



#write a main  function name main as the starting point of the program
def main():
    print("Welcome to the Corrupted Ticketing System ! ")
    max_attempts=5
    while max_attempts>0:#O(1) user can try to enter his pass until 5 attempts
        user_input =input("Enter your user_name : ")
        password=input("If your are an Admin Enter your password/if you'r user quit empty : """)
        if user_input.lower()=="admin"and password.lower()=="admin123123":
            return admin_menu()
        elif password=="":
           return user_menu()
        else:
           max_attempts-=1
           print("Incorrect user_Name and or password")
    print("Maximum login exceeded....")
           
                      
print(main())
