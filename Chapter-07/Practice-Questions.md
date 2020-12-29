# Solutions for the Practice Questions in Chapter 07

## 1. What is the function that creates Regex objects?
re.compile()
## 2. Why are raw strings often used when creating Regex objects?
In Raw Strings, backslashes don't have to be escaped
## 3. What does the search() method return?
It returns Match objects.
## 4. How do you get the actual strings that match the pattern from a Match object?
By using group(0)
## 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
group(0) is the full match\
group(1) is the match before the first set of parentheses\
group(2) is the 2nd set
## 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
By using the backslash
## 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
If the regex has no groups, a list is returned else a list of tuples is returned
## 8. What does the | character signify in regular expressions?
It signifies or
## 9. What two things does the ? character signify in regular expressions?
Non-greedy matching
## 10. What is the difference between the + and * characters in regular expressions?
\+ matches one or more\
\* matches zero or more
## 11. What is the difference between {3} and {3,5} in regular expressions?
{3} will match exactly 3 instances\
{3,5} will match between 3 and 5 instances
## 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
Single Digit, Word and Space respectively
## 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
Will match anything that's NOT a Single Digit, Word and Space respectively
## 14. What is the difference between .* and .*??
Greedy and Non-greedy match respectively
## 15. What is the character class syntax to match all numbers and lowercase letters?
Either \[0-9a-z] or \[a-z0-9]
## 16. How do you make a regular expression case-insensitive?
Using re.IGNORECASE
## 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
It normally matches anything except the newline character. If re.DOTALL is passed then, even newline will be matched
## 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
'X drummers, X pipers, five rings, X hens'.
## 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
We can then add whitespaces to the string
## 20. How would you write a regex that matches a number with commas for every three digits?
```
It must match the following:

'42'
'1,234'
'6,368,745'

but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
```
```
re.compile(r'^\d{1,3}(,\d{3})*$')
```
## 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter.
```
The regex must match the following:

    'Haruto Watanabe'
    'Alice Watanabe'
    'RoboCop Watanabe'

but not the following:

    'haruto Watanabe' (where the first name is not capitalized)
    'Mr. Watanabe' (where the preceding word has a nonletter character)
    'Watanabe' (which has no first name)
    'Haruto watanabe' (where Watanabe is not capitalized)
```
```
re.compile(r'[A-Z][a-z]*\sWatanabe')
```
## 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive.
```
It must match the following:

    'Alice eats apples.'
    'Bob pets cats.'
    'Carol throws baseballs.'
    'Alice throws Apples.'
    'BOB EATS CATS.'

but not the following:

    'RoboCop eats apples.'
    'ALICE THROWS FOOTBALLS.'
    'Carol eats 7 cats.'
```
```
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
```