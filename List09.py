def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    fruits = ["apple", "banana", "apple", "pear", "apple"]
    i = 0
    result =0
    while i < len(fruits):
        if fruits[i] == 'apple':
            result +=1
        i += 1
    return result
print(main( fruits = ["apple", "banana", "apple", "pear", "apple"]))