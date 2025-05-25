f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word twinkle is present in the content")
else:
    print("the word twinkle is not prensent in the content")
    
f.close()