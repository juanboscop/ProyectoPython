print("\n\t\t--> Welcome to the yes or no poll program <--\n")

issue = input("\nWhat issue would you like to vote on --> ")
voters = int(input("\nEnter number of voters --> "))
passw = input("\nEnter password to see poll results --> ")

count_y = 0
count_n = 0
i = 0
results_poll = {}
#the range() function acts as a repeater of the whole for loop.
for i in range(voters):
    name = input("\n\tEnter name --> ")
    if name in results_poll:
        print(f"\nSorry {name} but it appears you have already voted \n")
    else:
        print(f"\nHello {name} the issue you are voting on is\n\n\t\t--->{issue}")
#Now after I introduce the vote variable The += means that each time Y or N is voted 1 will be added.
        vote = input("\nEnter Y/N = ").upper()
        if vote == "Y":
            count_y += 1
        if vote == "N":
            count_n += 1

        results_poll[name]= vote

print(f"\n\nthe results are {count_y} voted for yes\n\nAnd {count_n} voted for no.")
poll_p = input("\n\t\t----> If you would like to see the poll results please enter the password:")
if poll_p == passw:
    print(results_poll)
else:
    print("I'm sorry but you're not authorised to see this poll.")



