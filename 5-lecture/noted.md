#Tubles, Lists, Aliasing, Mutability, and cloning
* Recap on functions
* They will continue to be used during the course of the lecture
* Decomposition and Abstraction
* Reusable and structure

#Compond data types
* data types made up of different data types
* tuples and lists

##Tuples
* similar to strings
* sequences of data
* can contain different data types inside the same tuple
* immutable once created you cannot modify it

```
    te = ()
    te = (2,"mit", 3)
```

* we can index into tuples
* we can run len(tuple)
* they can be concatenated
* we can slice into tuples t[1:2]

####example usage

```
    #we could use but that would not work
    x = y
    y = x
    
    #or this
    temp = x
    x = y
    y = templ
    
    #with tuples now 
    (x, y) = (y, x)
```

* with tuples we can return more then one object from a f()
* since f() can only return one object returning a tuple is a way to go around that
* importance to think about the mutability of the data you return

##Lists
* Mutable
* sequence of data
* also called array :D
* you cant index outside of the list

basically arrays
* you can iterate through the elements directly 
* you can iterate over with indexes as well
* I have been doing this for a looooong time
* you can append to the array using .append() 
* you can add lists together to make them larger
* you can delete from list using .del(index)
* you can pop using .pop(index)
* I wonder the efficiency of these functions, they probably use the most efficient alg
* .sort() and .reverse() mutates sorted(L) does not 
* you can have more then one variable pointing to the same object
* this can be good or bad

###What side affects might happen from change?
* you can clone to prevent spreading chill = cool[:]
* be aware of these, you have seen the effects in person

