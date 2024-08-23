# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
Qustion Section:
1. How does this solution ensure data immutability?

The data in the array cannot be changed or deleted by the function.

2. Is this solution a pure function? Why or why not?

This function is pure, because it makes an output that's unique and repeatable for each input.

3. Is this solution a higher order function? Why or why not?

This function doesn't take another function as an argument or return a function, making it not a higher order function.

4. Would it have been easier to solve this problem using a different programming style?

If I wanted to do more things with the data or complicate the data itself, OOP would be much more helpful for the variety of tasks.
However, because the request is simple, the functional programming approach works here.

5. Why in particular is functional programming a helpful paradigm when solving this problem?

Functional programming principles help in creating functions like these by encouraging immutability, 
purity, and higher-order functions. These principles lead to code that is more predictable, 
reusable, and easier to understand, which in turn makes software development more robust and maintainable.

'''

# OOP Section

# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

'''
Make sure to answer the following prompts about your coding experience:

1. How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

It demonstrates encapsulation by creating a class to summarize multiple pieces of data into a single, more-useful unit. In a
similar way, this demonstrates inheritance, like when we made the special pods that inherit the Podracer class. The two pods we handmade,
Sebulba and Anakin, demonstrate polymorphism by allowing the two unique pods to be treated as part of the same class: podracer.
The code has no abstraction, as no aspects of a class are hidden or highlighted by the code.

2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

I think using OOP is by far the easiest solution for questions like these, as it leaves opportunity in the hypothetical to keep
adding podracers with unique properties without having to redo the entire podracer class. You could copypaste the podracer attributes
repeatedly into an array, but it would be meticulous and hard to read.

3. How in particular did Object Oriented Programming assist in the solving of this problem?

OOP prevented us from rewriting the code for the podracer class, as well as allowed us to make unique modifications to polymorph the 
podracers while keeping them in the same race (class). 

'''