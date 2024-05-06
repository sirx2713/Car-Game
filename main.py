command = ""
started = False
stopped = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car has stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I do not understand that.")
