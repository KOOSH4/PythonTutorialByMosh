i=10
while i > 0:
    command = input("")
    if command.lower() == "help":
        print("Start - to start the car.")
        print("Stop - to stop the car.")
        print("quit - to turn off the car.")
        print("exit - to exit the game!")
        i+=1
    elif command.lower() == "start":
        print("Car Started!")
        break
    elif command.lower() == "stop":
        print("car stoped!")
        break
    elif command.lower() == "quit":
        print("car turned off!")
        break
    elif command.lower() == "exit":
        print("Bye")
        break
    else:
        print("i dont undrtstand!")
        i+=1

