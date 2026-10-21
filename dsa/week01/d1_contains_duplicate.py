

def foo(nums):
    s = set ()
    for e in nums:
        if e in s:
            return True 
        s.add(e)
    return False

a = [1, 2, 3, 1]
print(foo(a))
b = [1, 2, 3, 4]
print(foo(b))