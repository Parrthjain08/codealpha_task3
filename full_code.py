#simple chat bot
print("I am a simple chatbot.")
print("I can  answer only greeting questions")
def chatbot():
    while True:
        
        print("Enter your question choice:")
        print("1. Hello")
        print("2. How are you?")
        print("3. bye")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("HI!")
        elif choice == 2:
            print("I am fine, thank you!")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("Thank you for chatting with me!")
chatbot()
