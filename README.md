# dumbstuff
This library isn't meant for serious use, however is open source and changes may be made to it on a personal level. 
This code may prove to be of some help to people starting out for python, not in a productive way though it's seriously dumb stuff.
The code used may help someone undrstand the basics of python, and how fun and flexible of a programming language it is.


-------------------------------
DOCUMENTATION

(by order of how I wrote the code)

    sortlist(list, operator: str, ifprint: bool)

This function sorts the list passed into it, according to the operator specified: "<" sorts the list in ascending order, ">" sorts the list in descending order.
The ifprint bool value (True/False) dictates whether or not the the sorted list will be printed out to the screen; setting it to false will result in no print.

Example:

  `sortedList = dumbstuff.sortlist(mylist, "<", ifprint=False)`

Incorrect operator leads to the array not being sorted at all, the passed list will be returned as it was.

    jumblelist(list)
   
This function jumbles up the index positions of the passed list, and swaps it with random positions.

Example:

`jumbledlist = dumbstuff.jumblelist(mylist)`

 
