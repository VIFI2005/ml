import random
import re

from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()

QUESTION_WORDS = {
    "why": "That is a thoughtful question. What do you think is the real reason?",
    "what": "That depends on what matters most to you. Can you tell me more?",
    "when": "Timing matters. What makes this moment important?",
    "where": "Context matters. Where does that happen most often?",
    "who": "People can be complicated. What would you like to know about them?",
    "how": "There are often several ways to look at it. What would you try first?",
    "which": "There may be more than one option. What are your choices?",
    "can": "Possible, but I would like to know more about the situation.",
    "could": "Interesting. What would happen if you explored that idea more?",
    "should": "That depends on your priorities. What matters most here?",
    "would": "That sounds like a decision point. What are your options?",
    "do": "That is a good question. What are you hoping to learn?",
    "does": "What makes you ask that?",
    "is": "That is worth unpacking. What makes it feel that way?",
    "are": "What stands out most to you about that?",
}

POSITIVE_KEYWORDS = {
    "good", "great", "happy", "love", "excellent", "amazing", "awesome",
    "enjoy", "fun", "fantastic", "positive", "excited", "success", "better"
}

NEGATIVE_KEYWORDS = {
    "bad", "terrible", "worst", "hate", "angry", "sad", "upset", "stress",
    "frustrated", "negative", "hard", "difficult", "awful", "worse"
}

GENERIC_RESPONSES = [
    "That is interesting. Can you tell me more?",
    "I see. What makes you feel that way?",
    "Thanks for sharing that with me.",
    "That sounds thoughtful. Tell me more about it.",
    "Interesting point. What stands out most to you?",
]


def normalize_text(text):
    """Clean user input so NLP analysis is more stable."""
    cleaned = text.strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def extract_features(user_input):
    """Return structured NLP features from the user message."""
    if isinstance(user_input, TextBlob):
        blob = user_input
        cleaned = normalize_text(str(user_input))
    else:
        cleaned = normalize_text(str(user_input))
        blob = TextBlob(cleaned, np_extractor=extractor)

    words = [w.lower() for w in blob.words]
    tags = blob.tags[:12]
    noun_phrases = [phrase.lower() for phrase in blob.noun_phrases]
    first_word = words[0] if words else ""

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    word_count = len(words)

    is_question = cleaned.endswith("?") or first_word in QUESTION_WORDS
    is_exclamation = cleaned.endswith("!")
    has_positive_keyword = any(word in POSITIVE_KEYWORDS for word in words)
    has_negative_keyword = any(word in NEGATIVE_KEYWORDS for word in words)

    return {
        "text": cleaned,
        "words": words,
        "tags": tags,
        "noun_phrases": noun_phrases,
        "first_word": first_word,
        "word_count": word_count,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "is_question": is_question,
        "is_exclamation": is_exclamation,
        "has_positive_keyword": has_positive_keyword,
        "has_negative_keyword": has_negative_keyword,
        "top_topic": noun_phrases[0] if noun_phrases else None,
    }


def detect_intent(features):
    """Classify the input into simple conversation intents."""
    text = features["text"].lower()

    if features["is_question"]:
        return "question"
    if features["has_negative_keyword"]:
        return "negative"
    if features["has_positive_keyword"]:
        return "positive"
    if features["subjectivity"] > 0.55:
        return "opinion"
    if features["word_count"] > 20:
        return "long_input"
    return "neutral"


def build_response(user_input):
    """Generate a more natural and context-aware NLP response."""
    if not user_input or not user_input.strip():
        return "I did not catch that. Can you say it again?"

    features = extract_features(user_input)
    intent = detect_intent(features)
    text = features["text"]
    first_word = features["first_word"]

    if first_word in QUESTION_WORDS:
        return QUESTION_WORDS[first_word]

    if intent == "question":
        if first_word in QUESTION_WORDS:
            return QUESTION_WORDS[first_word]
        return "That is a good question. What are you hoping to learn from it?"

    if features["polarity"] <= -0.5 or intent == "negative":
        response = "That sounds quite negative. I am sorry you are feeling that way. "
    elif features["polarity"] >= 0.5 or intent == "positive":
        response = "That sounds genuinely positive. I am glad you feel that way. "
    elif features["polarity"] > 0:
        response = "That sounds fairly positive. "
    elif features["polarity"] < 0:
        response = "That sounds a bit negative. "
    else:
        response = "That is interesting. "

    if features["word_count"] > 20:
        response += "You shared a lot there. "

    if features["subjectivity"] > 0.6:
        response += "Your opinion feels quite personal. "

    if features["top_topic"]:
        topic = features["top_topic"].capitalize()
        response += f"Can you tell me more about {topic}?"
        return response

    if features["tags"]:
        filtered_tags = [
            tag for _, tag in features["tags"]
            if tag not in {"PRP", "PRP$", "DT", "IN", "TO", "CC", "UH", "MD"}
        ]
        if filtered_tags:
            tag = filtered_tags[0]
            response += f"What do you think about that {tag.lower()}?"
            return response

    if intent == "opinion":
        return response + " What influenced that viewpoint?"

    if intent == "long_input":
        return response + " What part of this matters most to you?"

    return response + random.choice(GENERIC_RESPONSES)


def main():
    print("Hello, I am Marvin, the friendly NLP robot.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You> ")

        if user_input.lower().strip() in {"bye", "exit", "quit"}:
            print("Marvin> It was nice talking to you. Goodbye!")
            break

        response = build_response(user_input)
        print(f"Marvin> {response}")


if __name__ == "__main__":
    main()
