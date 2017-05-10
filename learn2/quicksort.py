

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print (quicksort([3, 6, 8, 10, 1, 2, 1, 100, 200, 100, 200, 3, 6, 8, 8, 6, 3]))

lists_of_lists = [[1, 2, 3], [4, 5, 6]]
print([sum(x) for x in zip(*lists_of_lists)])

# When a final formal parameter of the form **name is present,
# it receives a dictionary (see Mapping Types — dict) containing all keyword arguments
# except for those corresponding to a formal parameter. This may be combined with a formal parameter
# of the form *name (described in the next subsection) which receives a tuple containing
# the positional arguments beyond the formal parameter list.
# (*name must occur before **name.)
# For example, if we define a function like this:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)
#print(sum(arr))
s = 0
for x in arr:
    s += x
print(s)

