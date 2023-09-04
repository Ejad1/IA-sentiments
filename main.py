import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Instancier l'analyseur de sentiment VADER
sia = SentimentIntensityAnalyzer()


# Définir une fonction pour l’IA qui analyse le sentiment
def analyse_sentiment(phrase):
    sentiments = sia.polarity_scores(phrase)

    # Interpréter le score de sentiment
    if sentiments['compound'] >= 0.0005:
        return "positif"
    elif sentiments['compound'] <= -0.0005:
        return "négatif"
    else:
        return "neutre"


# Boucle principale
while True:
    user_input = input("Entrez une phrase (ou 'exit' pour quitter) : ")
    if user_input.lower() == "exit":
        print("IA : Au revoir!")
        break
    sentiment = analyse_sentiment(user_input)
    print("IA : Le sentiment de cette phrase est", sentiment)
