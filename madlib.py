# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
#instagram  = "hetal" # some string variable

# # a few ways to do this
 #print("follow me on " + instagram)
 #print("follow me on {}".format(instagram))
 #print(f"follow me on {instagram}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlibs = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlibs)

