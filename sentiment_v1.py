# # from textblob import  TextBlob
# # blob = TextBlob("it is a truth universal that a single man in possession of a good fortune must be in want of a wife")
# # print(blob.translate(to='fr'))

# # from deep_translator import GoogleTranslator
# # text = "it is a truth"
# # print(GoogleTranslator(source='auto', target='fr').translate(text))

# from textblob import TextBlob
# quote1 = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."""

# quote2 = """Darcy, as well as Elizabeth, really loved them; and they were both ever sensible of the warmest gratitude towards the persons who, by bringing her into Derbyshire, had been the means of uniting them."""

# sentiment1 = TextBlob(quote1).sentiment
# sentiment2 = TextBlob(quote2).sentiment

# print(quote1 + " has a sentiment of " + str(sentiment1))
# print(quote2 + " has a sentiment of " + str(sentiment2))




from textblob import TextBlob
with open("pnp.txt", encoding="utf8") as f:
    file_contents = f.read()
book_pride = TextBlob(file_contents)
positive_sentiment_sentences = []
negative_sentiment_sentences = []
for sentence in book_pride.sentences:
    if sentence.sentiment.polarity == 1:
        positive_sentiment_sentences.append(sentence)
    if sentence.sentiment.polarity == -1:
        negative_sentiment_sentences.append(sentence)
print("The " + str(len(positive_sentiment_sentences)) + " r most positive sentences:")
for sentence in positive_sentiment_sentences:
    print("+ " + str(sentence.replace("\n", "").replace("      ", " ")))
print("The " + str(len(negative_sentiment_sentences)) + " r most negative sentences:")
for sentence in negative_sentiment_sentences:
    print("- " + str(sentence.replace("\n", "").replace("      ", " ")))