# re import built in regular expression package in python
import re
# text = "The quick brown fox jumps over the lazy dog"
# match = re.search('brown',text)
# print(match)
# if match:
#     print("Math Found")
#     print(f"Start = {match.start()}")
#     print(f"End = {match.end()}")

# matches = re.findall('the',text,re.IGNORECASE)
# print("Matches = ",matches)

# replace = re.sub('fox','cat',text)
# print(replace)

# pattern = "World War"
text = """"

AWorld War II[b] or the Second BWorld War (1 September 1939 – 2 September 1945) was a global conflict between two coalitions: the Allies and the Axis powers. Nearly all of the world's countries participated, with many nations mobilising all resources in pursuit of total war. Tanks and aircraft played major roles, enabling the strategic bombing of cities and delivery of the first and only nuclear weapons ever used in war. World War II is the deadliest conflict in history, causing the death of 70 to 85 million people, more than half of whom were civilians. Millions died in genocides, including the Holocaust, and by massacres, starvation, and disease. After the Allied victory, Germany, Austria, Japan, and Korea were occupied, and German and Japanese leaders were tried for war crimes.
The causes of CWorld War II included unresolved tensions in the aftermath of World War I and the rise of fascism in Europe and militarism in Japan. Key events preceding the war included Japan's invasion of Manchuria in 1931, the Spanish Civil War, the outbreak of the Second Sino-Japanese War in 1937, and Germany's annexations of Austria and the Sudetenland. World War II is generally considered to have begun on 1 September 1939, when Nazi Germany, 
"""

# match = re.search(pattern,text)
# if match:
#     print("Math Found")
#     print(f"Start = {match.start()}")
#     print(f"End = {match.end()}")

# match = re.findall(pattern,text,re.IGNORECASE)
# print(match)

# replace = re.sub(pattern,"Unkind War 2",text,re.IGNORECASE)
# print(replace)

pattern = r"[A-Z]+World War"

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
