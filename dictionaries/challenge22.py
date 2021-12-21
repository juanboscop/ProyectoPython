from collections import defaultdict

print("\n\t\t----> Welcome to bosco's admin/database program.\n")
list_all = {1:{
       "username":["bosco123"],
       "password":["12345678"]},
    2:{"username":["pope123"],
       "password":["pope2004"]},
    3:{"username":["admin001"],
       "password":["piñata2004"]},
    4:{"username":["leonel1"],
       "password":["leonel123"]}
       
                                }
while True:

   usern = input("Enter username--> ").lower()
   if usern in list_all:
      passw = input("Enter password--> ").lower()
      
      if passw in list_all:
         print("hello")
   else:
      print("the username you have typed does not exist!\n\n",usern)
      break


if "admin001" in usern:
   print("\n hello admin001\n\nThese are your usernames and passwords in your database==> \n")
   dictionary_items = list_all.items()
   for item in dictionary_items:
      print(item)


