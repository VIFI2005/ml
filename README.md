# Marvin NLP Experiments

A small Python project exploring conversational AI and text analysis with `textblob`. The repository contains a series of progressively more advanced versions of a simple chatbot, along with a sentiment-analysis script that reads text from a local file.

## Overview

This project was built as a learning exercise to explore:

- basic chatbot behavior
- sentiment analysis
- noun phrase extraction
- question detection
- more advanced conversational responses based on language features
- reading source text from a `.txt` file for analysis

## Repository structure

- `marvin_v1.py` — simple random-response chatbot
- `marvin_v2.py` — chatbot with sentiment-aware replies and noun-phrase detection
- `marvin_v3.py` — chatbot with question handling and more structured responses
- `marvin_v4.py` — enhanced chatbot using extracted text features
- `sentiment_v1.py` — reads `pnp.txt` and prints the most positive and negative sentences
- `pnp.txt` — source text used for sentiment analysis

## Requirements

Install the required Python package:

```bash
python3 -m pip install textblob
```

If you are using a fresh environment, you may also want the NLTK corpora used by TextBlob:

```bash
python3 -m textblob.download_corpora
```

## Running the scripts

From the project root:

### 1. Marvin v1

```bash
python3 marvin_v1.py
```

A very simple chatbot that responds randomly.

### 2. Marvin v2

```bash
python3 marvin_v2.py
```

Adds basic sentiment detection and noun phrase extraction.

### 3. Marvin v3

```bash
python3 marvin_v3.py
```

Adds question-aware responses such as `why`, `what`, `how`, and `who`.

### 4. Marvin v4

```bash
python3 marvin_v4.py
```

Includes richer feature extraction from the user input, including:

- word count
- first-word detection
- noun phrases
- POS tags
- polarity and subjectivity
- follow-up topic prompts

### 5. Sentiment analysis on the source text

```bash
python3 sentiment_v1.py
```

This script reads the contents of `pnp.txt` and analyzes sentence-level sentiment.

## How the project evolved

### Marvin v1

The first version is a simple command-line chatbot with random responses.

### Marvin v2

This version begins using `TextBlob` to evaluate the emotional tone of the input and to detect noun phrases for more contextual follow-ups.

### Marvin v3

This adds a more conversational structure by identifying basic question types and tailoring replies accordingly.

### Marvin v4

This version goes further by extracting multiple language features from the input and using them to decide how to respond.

### Sentiment analysis

The project also explores how to analyze a larger body of text from a local file rather than a single sentence.

## Example interaction

```text
Hello, I am Marvin, the friendly robot.
You can end this conversation at any time by typing 'bye'
After typing each answer, press 'enter'
How are you today?
> I feel excited about my new project
That sounds fairly positive. Can you tell me more about Project?
> Why do you think this works?
That is a thoughtful question. What do you think is the reason?
> bye
It was nice talking to you, goodbye!
```

## Notes

- This project is intentionally educational and lightweight.
- It demonstrates how simple NLP ideas can be built step by step.
- The chatbot is not a production-grade assistant; it is a learning project for experimenting with language processing.

## License

This project is provided for educational purposes.

## Author

Vicky
