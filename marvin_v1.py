import random
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello! I'm Marvin. How can I assist you today?")
print("Type 'exit' to end the conversation.")
print("After typing each answer, press 'enter'")

while True:
    user_input = input(" >")
    if user_input.lower() == 'exit':
        break
    else:
        response =random.choices(random_responses)[0]
    print(response)
print("Goodbye ! It was nice talking to you.")

