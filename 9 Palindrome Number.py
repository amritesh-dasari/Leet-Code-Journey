def isPalindrome(x: int) -> bool:
    xcopy = x
    reverse=0
    while xcopy>0:
        reverse=(reverse*10)+(xcopy%10)
        xcopy = xcopy//10
    if reverse == x:
        return True
    else:
        return False