from datetime import date
# from project import *
from autonote import instagram
# import autonote
Dict={} #We have declared a dictionary to store birthday.
#Run loop till the user wants.
while True:
  print ("_____Birthday Adder_____\n")
  print ("1.Show Birthday")
  print ("2.Add to the Birthday list")
  print("3.Wish the birthday girl/boy on Instagram")
  print ("4.Exit")
  choice = int(input("Enter the choice\n"))
  if choice == 1:
      if len(Dict) == 0: #If no data in dictionary
          print("Nothing to show")
      else : #If data is there ask him whose data he want
        name = input("Enter name to look for birthday")
        birthday = Dict.get(name,"No data found")
        print (birthday)
  elif choice == 2:  #If he want to add user data let him add in dictionary as key-value pair.
      name = input ("Enter Name")
      date = input ("Enter Birthdate")
      Dict[name] = date
      print ("Birthday Added")
  elif choice == 3:
      instagram()
  elif choice == 4: #close program
      print("======Exiting program========")
      break
  else: #if he has chosen none of above input plese ask him to chose valid option
      print("Choose a valid option")