def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """ 
    zores = 0
    ones = 0
    i =0
    result = []
    while i < len(list1):
        if list1[i] == 1:
            ones +=1
        i += 1
        zeros = len(list1)-ones
    result.append(ones)
    result.append(zeros)
    return result
print(main(list1=[0,1,0,0,1,1,0]))