# Solutions for the Practice Questions in Chapter 05

## 1. What does the code for an empty dictionary look like?
{} is an empty dictionary

## 2. What does a dictionary value with a key 'foo' and a value 42 look like?
{'foo': 42}

## 3. What is the main difference between a dictionary and a list?
list items are ordered, dict items are not

## 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
A KeyError is displayed

## 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
No difference

## 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam will check for key 'cat'\
'cat' in spam.values() wil check for value 'cat'

## 7. What is a shortcut for the following code?
```
if 'color' not in spam:
    spam['color'] = 'black'
```
```
spam.setdefault('color', 'black')
```
## 8. What module and function can be used to “pretty print” dictionary values?
pprint.pprint()