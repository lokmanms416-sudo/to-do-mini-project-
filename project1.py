tasks = input("enter your tasks separated by comma").split(", ")
tasks_finish = []
tasks_not_finish = []
for task in tasks:
    the_state = input(f"did you finish {task} already\n")
    if the_state == "yes":
        print("nice job")
        tasks_finish.append(task)
    else:
        print("try not put it off")
        tasks_not_finish.append(task)
allow = input("do you want to see your today s progress?(yes or no)")
if allow == "yes":
    print("--------- done tasks ---------")
    print(tasks_finish)
    print("--------- ongoing tasks ---------")
    print(tasks_not_finish)