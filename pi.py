text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO


text = text.replace(",", "").replace(".", "")
words = text.split()
num = ""
for i in range(len(words)):
    num += str(len(words[i]))

print(num)