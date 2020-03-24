started = False
stopped= True
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            stopped= False
            print("Car is already started")
        else:
            started = True
            print("Ready to go!")
    elif command == "stop":
        if stopped:
            print("Car is already stopped.")
        else:
            stopped = True
            print("Car stopped")
    elif command == "help":
        print("""
Help- to see commands
Start- to start the car
Stop- to stop the car
Quit- to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")

