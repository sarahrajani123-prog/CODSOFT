import re
import random


class SimpleChatbot:
    def __init__(self, name="Bot"):
        self.name = name
        self.rules = [
            (r'\b(hi|hello|hey)\b', [
                "Hello! How can I help you today?",
                "Hey there! What's on your mind?"
            ]),
            (r'\bmy name is (\w+)', [
                "Nice to meet you, {0}!",
                "Hello, {0}! How can I assist you?"
            ]),
            (r'\bhow are you\b', [
                "I'm just a program, but I'm running smoothly! How about you?",
                "Doing great, thanks for asking!"
            ]),
            (r'\b(bye|goodbye|exit|quit)\b', [
                "Goodbye! Have a great day!",
                "See you later!"
            ]),
            (r'\bwhat is your name\b', [
                f"I'm {self.name}, your friendly chatbot."
            ]),
            (r'\b(thanks|thank you)\b', [
                "You're welcome!",
                "No problem at all!"
            ]),
            (r'\bweather\b', [
                "I can't check live weather, but I hope it's nice where you are!"
            ]),
            (r'\bhelp\b', [
                "I can chat about basic topics. Try greeting me, asking my name, "
                "or telling me yours!"
            ]),
        ]
        self.fallbacks = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting — tell me more.",
            "I don't have a response for that yet."
        ]

    def respond(self, user_input):
        text = user_input.lower().strip()
        for pattern, responses in self.rules:
            match = re.search(pattern, text)
            if match:
                response = random.choice(responses)
                return response.format(*match.groups())
        return random.choice(self.fallbacks)

    def is_exit(self, user_input):
        return bool(re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()))


def main():
    bot = SimpleChatbot(name="Chatty")
    print(f"{bot.name}: Hi! Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue
        reply = bot.respond(user_input)
        print(f"{bot.name}: {reply}")
        if bot.is_exit(user_input):
            break


if __name__ == "__main__":
    main()
# CODESOFT-TASK1