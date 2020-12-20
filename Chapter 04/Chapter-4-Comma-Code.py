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