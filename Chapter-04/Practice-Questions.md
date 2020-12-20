# Solutions for the Practice Questions in Chapter 04

## 1. What is []?
[] is an empty list with no elements inside it

## 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
```
spam = [2,4,6,8,10]
spam[2] = 'hello'
```

### For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

## 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
spam[int(int('3'*2)//11)] will be evaluated to 'd'

## 4. What does spam[-1] evaluate to?
spam[-1] will evaluate to 'd'

## 5. What does spam[:2] evaluate to?
spam[:2] will be evaluated to the list ['a','b']

### For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

## 6. What does bacon.index('cat') evaluate to?
```
bacon = [3.14,'cat',11,'cat',True]
```
bacon.index('cat') will be returning the integer 1

## 7. What does bacon.append(99) make the list value in bacon look like?
bacon.append(99) will append the integer 99 to the end of the original list of bacon thus, making bacon = [3.14,'cat',11,'cat',True,99]

## 8. What does bacon.remove('cat') make the list value in bacon look like?
bacon.remove('cat') will remove the first instance of 'cat' it finds in the list thus, making bacon = [3.14,11,'cat',True]

## 9. What are the operators for list concatenation and list replication?
operator for list concatenation is +, while for replication it's *

## 10. What is the difference between the append() and insert() list methods?
the append() method adds an element to the list of a list, while the insert() method allows you to insert a value into any position in the list

## 11. What are two ways to remove values from a list?
We can use the list.pop() method or the list.remove() method

## 12. Name a few ways that list values are similar to string values.
indexes of elements can be accessed in a similar way in both lists and strings\
slices can be used in both lists and strings\
2 or more lists can be concatenated, 2 or more strings can be concatenated\
both can be used in a for in loop

## 13. What is the difference between lists and tuples?
lists are mutable, tuples are immutable (elements in tuples can't be modified in any way)

## 14. How do you type the tuple value that has just the integer value 42 in it?
tupl = (42)

## 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
```
lst = ['cat',1]
tupl = ('dog',2)
print(list(tupl))
print(tuple(lst))
```

## 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
They contain references to the values, not the values themselves

## 17. What is the difference between copy.copy() and copy.deepcopy()?
copy.copy() will just add new references to the variable and point them towards the old list\
copy.deepcopy() will create a whole new list with new references
