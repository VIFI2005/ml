import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()

random_responses = [
    "That is interesting. Can you tell me more?",
    "I see. What makes you think that?",
    "Thanks for sharing that with me.",
]


def build_response(user_input_blob):
    """Choose a response using the question type, sentiment, and topic."""
    words = user_input_blob.words
    noun_phrases = user_input_blob.noun_phrases
    first_word = words[0].lower() if words else ""

    if first_word == "why":
        return "That is a thoughtful question. What do you think is the reason?"
    if first_word == "how":
        return "There may be several ways to approach that. What would you try first?"
    if first_word == "what":
        return "That depends on what interests you most. Can you tell me more?"
    if first_word == "who":
        return "People can be complicated. What would you like to know about them?"

    if user_input_blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad. "
    elif user_input_blob.polarity <= 0:
        response = "Hmm, that's not great. "
    elif user_input_blob.polarity <= 0.5:
        response = "Well, that sounds positive. "
    else:
        response = "Wow, that sounds great. "

    if noun_phrases:
        return response + "Can you tell me more about " + noun_phrases[0].pluralize() + "?"
    return response + random.choice(random_responses)


def main():
    print("Hello, I am Marvin, the friendly robot.")
    print("You can end this conversation at any time by typing 'bye'")
    print("After typing each answer, press 'enter'")
    print("How are you today?")

    while True:
        user_input = input("> ")

        if user_input.lower() == "bye":
            break

        user_input_blob = TextBlob(user_input, np_extractor=extractor)
        print(build_response(user_input_blob))

    print("It was nice talking to you, goodbye!")


if __name__ == "__main__":
    main()
