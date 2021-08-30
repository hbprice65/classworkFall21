def interface():
    keep_running = True
    print("My Program")
    print("Options")
    print("9 - Quit")
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
    print(choice)
    return choice

interface()