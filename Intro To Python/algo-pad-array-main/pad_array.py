#REMEMBER TO PSEUDOCODE

def pad(array, min_size, value = None):
    if min_size <= len(array):
        return array
    for x in range(min_size - len(array)):
        array.append(value)
    return array