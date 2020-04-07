from datetime import date
# from project import *
from autonote import instagram
# import autonote
Dict={} #We have declared a dictionary to store birthday.
#Run loop till the user wants.
while True:
  print ("_____Birthday Wisher_____\n")
  print ("1.Show Birthday")
  print ("2.Add to the Birthday list")
  
  print("3.Wish the birthday girl/boy on Instagram")
  print ("4.Exit")
  choice = int(input("Enter the choice\n"))
  if choice == 1:
      if len(Dict) == 0: #If no data in dictionary
          print("Nothing to show")
      else : #If data is there ask him whose data he wants
        name = input("Enter name to look for birthday")
        birthday = Dict.get(name,"No data found")
        print (birthday)
  elif choice == 2:  #Adding data
      name = input ("Enter Name")
      date = input ("Enter Birthdate")
      insta= input("Enter the instagram handle")
      Dict[name] = date
      print ("Birthday Added")
  elif choice == 3:
      instagram(insta)
  elif choice == 4: #close the program
      print("======Exiting program========")
      break
  else: #if he has chosen none of above input please ask him to chose valid option
      print("Choose a valid option")