Words = ["Donkey", "bad" , "gande", "bhai"]

with open("Donkey.txt", "r")as f:
    content = f.read()

for word in Words:
    content = content.replace(word, "#" * len(word))

with open("Donkey.txt", "w")as f:
    f.write(content)