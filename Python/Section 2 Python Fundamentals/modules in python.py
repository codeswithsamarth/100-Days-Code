# Modules are files which contains code written by someone else whe import it use it in our code
# pip is a package manager which is used to install  modules

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Samarth Patil")
# engine.runAndWait()

import pyjokes
jokes = pyjokes.get_joke()
print(jokes)
