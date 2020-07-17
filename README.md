# dumbstuff
This library isn't meant for serious use, however is open source and changes may be made to it on a personal level. 
This code may prove to be of some help to people starting out for python, not in a productive way though it's seriously dumb stuff.
The code used may help someone understand the basics of python, and how fun and flexible of a programming language it is.


-------------------------------
# DOCUMENTATION

###### (by order of appearance in code)

    numlist()
   
This function returns a list of digits from 0 to 9, because who wants to type it out

Example:

`listofnumbers = dumbstuff.numlist()`

    charlist()
   
This function returns a list of characters from a to z, because who wants to type it out

Example:

`listofchar = dumbstuff.charlist()`

    sortlist(list, operator: str)

This function sorts the list passed into it, according to the operator specified: "<" sorts the list in ascending order, ">" sorts the list in descending order.


Example:

  `sortedList = dumbstuff.sortlist(mylist, "<")`

Incorrect operator leads to the array not being sorted at all, the passed list will be returned as it was.

    jumblelist(list)
   
This function jumbles up the index positions of the passed list, and swaps it with random positions.

Example:

`jumbledlist = dumbstuff.jumblelist(mylist)`

 
