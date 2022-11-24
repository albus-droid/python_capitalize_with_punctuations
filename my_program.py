def sentence_maker(phrase):
    question = ("How","When","Why","What","Who")
    phrase = phrase.capitalize()
    if phrase.startswith(question):
        return f"{phrase}?"
    else:
        return f"{phrase}."

sentence = []

while True:
    text = input("Say something: ")
    if text == "\\end":
        break
    else:
        sentence.append(sentence_maker(text))
        
print(" ".join(sentence))

