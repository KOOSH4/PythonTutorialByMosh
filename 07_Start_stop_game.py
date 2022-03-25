i = 10
is_startet = False
is_Stoped = False
is_quit = False
print("type help to get help!")
while i > 0:
    command = input("")

    if command.lower() == "help":
        print("Start - to start the car.")
        print("Stop - to stop the car.")
        print("quit - to turn off the car.")
        print("exit - to exit the game!")

    elif command.lower() == "start":
        if is_startet:
            print("its already started!")
            is_Stoped = False
            is_quit = False
        else:
            print("Car Started!")
            is_startet = True

    elif command.lower() == "stop":
        if is_Stoped:
            print("its already stoped!")
        else:
            print("Car Stoped!")
            is_Stoped = True
            is_startet = False
            is_quit = False

    elif command.lower() == "quit":
        if is_quit:
            print("its already turned off!")
        else:
            print("Car turned off!!")
            is_quit = True
            is_startet = False
            is_Stoped = False

    elif command.lower() == "exit":
        print("Bye")
        break

    else:
        print("i dont undrtstand!")
    i += 1
