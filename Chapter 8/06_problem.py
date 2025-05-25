def remove(l, word):
    n=[]
    
    for items in l:
        if not (items==word):
            n.append(items.strip(word))   
    return n 

l =["Harry", "antra", "anushka", "akshat"]

print(remove(l, "an"))