#Decompostion, Abstraction, and Functions
recap:
* string manipulation
* for loops over strings
* different implementations for the same problem
* Bisection method

today:
* how to structure your programs
* functions

##How do we write code
* As code scales it becomes harder to track changes
* add more functionality to your code
* functions allow for decomposition and abstraction

Abstraction
* none of us know how to build a projector but we know how to use it
* details can be supressed so you dont have to keep writing the same thing over and over

Decomposition
* different devices work together for the same common goal
* dividing code into modules

##Functions
* think about them as someone who is writting them
* think about them as someone who is just using the function

* have a name
* have parameters
* have a docstring(optional but recomended)
* have a body 
* returns something

###Variable Scope
* formal parameter gets bound to the value of actual parameter when the fucntion is called

* new scope/frame/environment created when enter a function
* scope is mapping name to objects

```
    def f(x):
        x = x + 1
        print('in f(x): x =', x)
        return x

    x = 3
    z = f(x)
```

* any arguments for the function are called formal parameters
* you only know what value it takes when the function is called
* the ones that are put into the function are called actual functions

* You can take a piece of paper and write down what is what if you are struggling

* happens if there is no return statement
* python will add a return none which is similar to null 
* represents the abscence of a value

* print statements are not the same as return statements
* you can use functions as parameters inside of functions

####Scope examples
* inside a function, can acess a varaible defined outise
* inside a function, cannot modify a veriable defined outside 
* you can use global variables but this is frowned upon
* global variables give a loop whole that can lead to messy code

* You can go on pythontutor and it allows you to see it's scope step by step

You only need to debug a single function once

