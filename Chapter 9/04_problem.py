word = "Donkey"

with open("Donkey.txt", "r")as f:
    content = f.read()

countnew = content.replace(word, "######")

with open("Donkey.txt", "w")as f:
    f.write(countnew)