d={} #Empty dictionary
marks = {
    "akshat":100,
    "shubham":55,
    "rohan":67
}

print(marks)
print(type(marks))
print(marks["akshat"])
print(marks.keys())
print(marks.items())
marks.update({"akshat":89, "renuka":34})  #because dictionary is mutuable
print(marks.items())
print(marks.get("akshat"))
marks.clear()
print(marks)
