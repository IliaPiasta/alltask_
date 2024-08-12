while True:
    a = int(input("Enter a number (enter '0' to restart) -> "))
    
    if a == 0:
        print("Restarting...")
        continue

    print(f"You entered: {a}")