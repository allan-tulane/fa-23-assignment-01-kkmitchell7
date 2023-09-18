"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        return foo(x-1)+foo(x-2)

def longest_run(mylist, key):
    longestrun = 0
    counter = 0
    for i in range(0, len(mylist)):
        if mylist[i] == key:
            counter += 1
            if counter > longestrun:
                longestrun = counter
        else:
            counter = 0
    
    return longestrun


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    


'''def longest_run_recursive(mylist, key, count = 0, longest = 0):
    if mylist:
        if mylist[0] == key:
            count += 1
            print("found key!")
            if count > longest:
                longest = count
        else:
            count = 0
        return longest_run_recursive(mylist[1:], key, count, longest)
    else:
        return longest
'''

def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            ans = Result(1,1,1,True)
        else:
            ans = Result(0,0,0,False) 
    else:
        leftside = longest_run_recursive(mylist[:len(mylist)//2], key)
        rightside = longest_run_recursive(mylist[len(mylist)//2:], key)
        if leftside.is_entire_range == True and rightside.is_entire_range == True:
            ans = Result(leftside.longest_size,rightside.longest_size, leftside.longest_size + rightside.longest_size,True)
        elif leftside.is_entire_range == True and rightside.is_entire_range == False:
            ans = Result(leftside.longest_size + rightside.left_size, rightside.longest_size, leftside.longest_size + rightside.left_size,False)
        elif leftside.is_entire_range == False and rightside.is_entire_range == True:
            ans = Result(leftside.longest_size, rightside.longest_size + leftside.right_size, rightside.longest_size + leftside.right_size,False)
        else:
            ans = Result(leftside.longest_size, rightside.longest_size, max(leftside.right_size+rightside.left_size, leftside.longest_size, rightside.longest_size),False)
    return ans


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

