# filter() function that returns even numbers from a list
def even(x):
    if x%2==0:
        return True
    else:
        return False
# print(even(76))
# let us take a list of numbers
# list1 = [10, 23, 45, 46, 70, 99]
z=[int(x) for x in input().split()]

#call filter() with is_even and lst
# r = list(filter(even, list1))
q = list(filter(even, z))
# print("From the list1 the even values are:",r)
print("From the z the even values are:",q)