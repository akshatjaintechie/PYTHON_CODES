with open("log.txt")as f:
    content = f.read()

if ("python" in content):
    print("Yes python is present")

else:
    print("NO python is not present")