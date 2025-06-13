# Dictionary is a collection of keys value pair

marks =  {
    "Harry":85,
    "Sanket":76,
    "Samarth":86
}

# print(marks["Sam"]) # if wrong key give key error
print(marks.get("Saarth")) # if wrong key give none

print(marks.keys())
print(marks.values())
print(marks.items())

print(marks.update({"Harshit":92}))
print(marks)

final_marks = marks.copy()
print(final_marks.keys())

# from keys:- sequence assign:-counting

vote =  ["BJP","Congress","BJP","BJP","Congress","Shivsena","Shivsena"]*500

vote_count = dict.fromkeys(list(vote),0)
for count in vote:
    vote_count[count]+=1
    print(vote_count)

winner = max(vote_count,key=vote_count.get)

print("Winner = ",winner)

my_dict = {'a':1,'b':2}
keys,value = (my_dict.popitem())
print(f"{keys},{value}")

my_dict =  {"Samarth":97}
a = my_dict.setdefault("sanket",10)
print(a)
print(my_dict)

dict = {}
print(dict)