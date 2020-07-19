def censor(text, word):
    result = ""
    stars = "*" * len(word)
    text_list = text.split()
    count = 0
    for i in text_list:
        if i == word:
            text_list[count] = stars
        count += 1
    result = " ".join(text_list)
    return result
print(censor("this hack is wack hack", "hack"))


# def censor(text, word):
#     words = text.split()
#     result = ''
#     stars = '*' * len(word)
#     count = 0
#     for i in words:
#         if i == word:
#             words[count] = stars
#         count += 1
#     result = ' '.join(words)
#     return result
#
#
# print(censor("this hack is wack hack", "hack"))