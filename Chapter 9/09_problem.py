with open("this.txt") as f:
    content1 = f.read()
with open("poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes these both File's content are same")

else:
    print("no these both File's content are not same")