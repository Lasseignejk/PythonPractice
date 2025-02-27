# Closure is a function having access to the scope of its parent function after the parent function has returned.

# In Python, closures are a way to retain access to variables from an enclosing scope even after that scope has finished executing. They are created when a nested function remembers the variables from its enclosing function even if the enclosing function has returned. 

def parent_function(person):
	coins = 3

	def play_game():
		nonlocal coins
		coins -= 1

		if coins > 1:
			print("\n" + person + " has " + str(coins) + " coins left.")
		elif coins == 1: 
			print("\n" + person + " has " + str(coins) + " coin left.")
		else: 
			print("\n" + person + " is out of coins.")
	return play_game

tommy = parent_function("Tommy")
jenny = parent_function("Jenny")
tommy()
tommy()

jenny()

def outer_function(message):
	def inner_function():
		print(f"Message: {message}") #'message' comes from the outer scope 
	return inner_function

closure_example = outer_function('Hello, Closure!')
closure_example()

# `outer_function("Hello, Closure!")` runs, creating `inner_function` with access to `message` 
# It returns `inner_function`, but doesn't execute it yet
# When we call closure_example(), it prints "Message: Hello, Closure!", even though `outer_function` has already finished executing.


