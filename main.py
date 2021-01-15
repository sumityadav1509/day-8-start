# #Simple Function
# def greet():
#   print("Hello Angela")
#   print("How do you do Jack Bauer?")
#   print("Isn't the weather nice today?")
# greet()

# #Function that allows for input
# #'name' is the parameter.
# #'Jack Bauer' is the argument.
# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
# greet_with_name("Jack Bauer")

# #Functions with more than 1 input
# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}?")

# #Calling greet_with() with Positional Arguments
# greet_with("Jack Bauer", "Nowhere")
# #vs.
# greet_with("Nowhere", "Jack Bauer")


# #Calling greet_with() with Keyword Arguments
# greet_with(location="London", name="Angela") 

# def greet():
#   print("Hello Sumit")
#   print("How are you doing Today !")
#   print("The weather seems to be pretty nice today") 

# greet() 

def greet_with_name(user_input):
  print(f"How are you doing today {user_input} !")
  print(f"Hello {user_input}") 

greet_with_name(input("What is your name ?")) 

def greet_with(name,location):
  print(f"Hello {name}")
  print(f"What is it like in  {location}")

greet_with(input("Name: "), input("Location: ")) 