def additions(*my_arguments):
    '''
    :param any number of arguments:
    :return: sum of all arguments
    '''
    result = 0
    try:
        for element in my_arguments:
            result = element + result
    except Exception as e:
        print(e)
        result = 'FAIL'
    return result

def append(*my_arguments):
    '''
    :param any number of arguments:
    :return: appended all arguments
    '''
    result = []
    try:
        for element in my_arguments:
            result.append(element)
    except Exception as e:
        print(e)
        result = 'FAIL'
    return result

def extend(*my_arguments):
    '''
    :param any number of arguments:
    :return: appended all arguments
    '''
    result = []
    try:
        for element in my_arguments:
            result.extend(element)
    except Exception as e:
        print(e)
        result = 'FAIL'
    return result

