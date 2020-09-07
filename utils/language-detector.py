from textblob import TextBlob
inText = TextBlob("Merhaba arkadaşlar!")
detect = inText.detect_language()
print(detect)

# uses Google API
# needs an internet connection
