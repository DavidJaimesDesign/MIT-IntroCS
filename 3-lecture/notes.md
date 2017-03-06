#String manipulation, Guess and Check, Approximations, Bisection

#####quick recap 
* last time we talked about strings
* branching(if, else, elsif)
* iteration(while and for)

#####Today
* String Manipulation
* guess and check algos
* approximate solutions
* bisection method

##Strings
* sequences of chars
* they are objects
* introduction to functions

###len()
* Returns the number of chars are in the string

###indexing
* we can know the character at a certain position
* s[0]
* the negative indexes also work(unlike some languages looking at you JS)
* if s[index] is greater then its actual size it will return an index error

###Slicing
* s[start:stop:step]
* you can also omit numbers and just leave the colons for the default
* ex s[2:100:5] = start at 2 and by intervals of 5 go all the way to 100
* you can reverse a string with [::-1]
* strings are immutable once it is created it cannot be modified

##For loops and strings
* for var in range is the basic syntax 
* for loops can iterate over any sequence of values
```
    s = "abcdefg"
    for char in s:
        if char == 'i' or char == 'u'
            print("there is an i or a u")
```
* pythonic code is asthetic and is easily readable

* we are ready for algorithms

##Algorithms
* we are looking at 3 that all find the cube root of a number

###Guess and check method
```
    cube = 8
    for guess in range(cube + 1):
        if guess**3 >= abs(cube):
            break
        if guesss**3 != abs(cube):
            print(cube, "is not a perfect cube")
        else:
            if cube < 0:
                guess = -guess
            print("Cube root of", cube, "is", guess)
```

* this is a brute force algo
* it takes it returns an error if not perfect cube
* can deal with negative cubes
* it also stops once we have found the cube root this reduces time to
* best case cuberoot(N) worst case is N

###Aproximate solutions
* you can start at 0 and increment by 0.001
* keep guessing as long as we are closer to the response
* the more precise the guess the longer it will take
* add incrementation and an epsilon to the guess and check method
* be careful of infinite loops

###Bisection Search
* divide and conquer
* keep cutting in half until you get an answer
* this incredibly fast 
* everything has to be sorted
* numbers only 

```
    cube = 27 
    epsilon = 0.01
    num_guesses = 0
    low = 0 
    high = cube

    guess = (high + low)/2.0
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else: 
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    print 'num_guesses = ', num_guesses
```
* time is log2N
* check the code examples

    
