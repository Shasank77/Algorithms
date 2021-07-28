def linear_search(list, target):
    """
   if found return the index position of target else return none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"target found at index: {index} ")
    else:
        print("target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 7)
verify(result)