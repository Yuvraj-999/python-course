import re, random
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORS_ACTIVE = True
except ImportError:
    COLORS_ACTIVE = False
   
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = MockColor()
    Style = MockColor()



def get_weather():
    """Simulates weather responses."""
    options = [
        "The sun is shining and it's 75°F.",
        "It's a bit cloudy, but no rain is expected.",
        "Light showers are moving through the area."
    ]
    return random.choice(options)

def get_news():
    """Simulates news updates."""
    updates = [
        "Scientists discover a new species of deep-sea fish.",
        "The local library is hosting a book fair this weekend.",
        "New updates released for your favorite operating system."
    ]
    return random.choice(updates)

def get_time():
    """Returns the current local time."""
    return f"The current time is {datetime.now().strftime('%I:%M %p')}."



def get_chatbot_response(user_text):
    """
    Matches user keywords to responses.
    This fulfills Step 2 (Improved Input Handling) and Step 5 (Organize with Functions).
    """
    user_text = user_text.lower()

    
    responses = {
        "weather": (get_weather(), Fore.CYAN),
        "news": (get_news(), Fore.YELLOW),
        "time": (get_time(), Fore.GREEN),
        "hello": ("Hi there! How can I help you today?", Fore.MAGENTA),
        "hi": ("Hello! Need any help?", Fore.MAGENTA),
        "bye": ("Goodbye! Have a wonderful day.", Fore.RED),
        "exit": ("Closing the chat... Goodbye!", Fore.RED)
    }

    
    for keyword, (reply, color) in responses.items():
        if keyword in user_text:
            return reply, color

    
    return "I'm not sure I understand. Try asking about the weather, news, or time.", Fore.WHITE



def main():
    if not COLORS_ACTIVE:
        print("(Note: Install 'colorama' via pip to see colored text!)\n")

    print(f"{Fore.BLUE}{Style.BRIGHT}=== Welcome to the Python Chatbot ===")
    print("Commands: weather, news, time, hello, exit\n")

    while True:
       
        user_input = input("You: ").strip()

        if not user_input:
            continue

       
        reply, text_color = get_chatbot_response(user_input)

    
        print(f"{text_color}Bot: {reply}")


        if "exit" in user_input.lower() or "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()