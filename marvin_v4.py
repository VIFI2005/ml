# I improved the logic in marvin_v4.py so it now extracts more useful features from the user’s input before responding:

# word count
# first word / question type
# noun phrases
# part-of-speech tags
# polarity and subjectivity
# question/exclamation detection
# topic-based follow-up prompts
# This makes Marvin respond more naturally instead of using only a simple sentiment check.

# Example of the new behavior
# It now distinguishes things like:

# “why”, “what”, “who”, “how” questions
# strongly positive vs negative sentiment
# long, opinion-heavy input vs short replies
# noun-based follow-up prompts

import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()

random_responses = [
    "That is interesting. Can you tell me more?",
    "I see. What makes you think that?",
    "Thanks for sharing that with me.",
    "That sounds like a strong opinion. Tell me more about it.",
]


def extract_features(user_input_blob):
    """Return useful language features from the input text."""
    words = user_input_blob.words
    tags = user_input_blob.tags[:10]
    noun_phrases = user_input_blob.noun_phrases
    first_word = words[0].lower() if words else ""

    return {
        "word_count": len(words),
        "first_word": first_word,
        "noun_phrases": noun_phrases,
        "tags": tags,
        "polarity": user_input_blob.polarity,
        "subjectivity": user_input_blob.subjectivity,
        "is_question": user_input_blob.endswith("?"),
        "is_exclamation": user_input_blob.endswith("!"),
        "top_noun": noun_phrases[0] if noun_phrases else None,
    }


def build_response(user_input_blob):
    """Choose a response using the question type, sentiment, and topic."""
    features = extract_features(user_input_blob)
    words = user_input_blob.words
    noun_phrases = features["noun_phrases"]
    first_word = features["first_word"]

    if first_word in {"why", "when", "where", "how", "what", "who", "which"}:
        question_response = {
            "why": "That is a thoughtful question. What do you think is the reason?",
            "how": "There may be several ways to approach that. What would you try first?",
            "what": "That depends on what interests you most. Can you tell me more?",
            "who": "People can be complicated. What would you like to know about them?",
            "when": "Timing matters. What makes this moment important?",
            "where": "Location can change the meaning. Where does that happen?",
            "which": "There may be more than one option. What are your choices?",
        }
        return question_response.get(first_word, "That sounds like a good question. Tell me more.")

    if features["polarity"] <= -0.5:
        response = "Oh dear, that sounds very negative. "
    elif features["polarity"] <= 0:
        response = "Hmm, that sounds a little negative. "
    elif features["polarity"] <= 0.5:
        response = "That sounds fairly positive. "
    else:
        response = "Wow, that sounds genuinely positive. "

    if features["word_count"] > 20:
        response += "You shared a lot there. "

    if features["subjectivity"] > 0.6:
        response += "Your opinion feels quite personal. "

    if noun_phrases:
        topic = noun_phrases[0].capitalize()
        response += "Can you tell me more about " + topic + "?"
        return response

    if features["tags"]:
        common_tag = features["tags"][0][1]
        response += "What do you think about that " + common_tag + "?"
        return response

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
