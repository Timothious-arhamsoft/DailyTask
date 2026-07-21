def palindrome_num(num , rev = 0):
    if num == 0:
        return rev

    # here instead of passing num//10 i passed num%10
    return palindrome_num(num%10, rev*10 + num%10)

num = 123321
pal = palindrome_num(num)
if num == pal:
    print("its a Palindrome")
else:
    print("it is not a Palindrome")
