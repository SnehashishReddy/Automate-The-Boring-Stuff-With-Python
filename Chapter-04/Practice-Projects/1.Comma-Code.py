# Comma Code

# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# Assuming space separated input()
lst = list(map(str, input().split()))
ans = ''
for x in range(0,len(lst)):
    if x < len(lst) - 1:
        ans = ans + lst[x] + ', '
    else:
        ans+=lst[x]
    if x == len(lst)-2:
        ans+='and '
print(ans)