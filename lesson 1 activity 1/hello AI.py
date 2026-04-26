
name = input("Hello! What's your name? ")
print(f"Nice to meet you, {name}!")

while True:
    # Ask mood
    mood = input("How are you feeling today? (good / bad / neutral): ").lower()

    if mood == "good":
        print("That's great to hear! 😊 Keep it up!")
    elif mood == "bad":
        print("Sorry to hear that. Things will get better 💙")
    elif mood == "neutral":
        print("Alright, hope your day gets more exciting!")
    else:
        print("Hmm, I didn't understand that, but that's okay!")

    
    hobby = input("What do you like to do in your free time? ")
    print(f"Wow, {hobby} sounds fun!")

  
    choice = input("Do you want to continue chatting? (yes / no): ").lower()

    if choice != "yes":
        print(f"Goodbye, {name}! Have a great day! 👋")
        break