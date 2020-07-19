def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeoui":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("enter a word:")))
