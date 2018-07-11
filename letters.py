
def a_dey():
    string = (input("Write anything: "))
    for s in string:
        if s.lower() == 'a':
            return True
    return False

def any_dey():
    string = (input("Write anything: "))
    for s in string:
        if s.isalpha():
            return True
    return False   


def snm_dey():
    string = (input("Write anything: "))
    for s in string:
        if s.lower() == 'a' or s.lower() == 'm':
            return True
    return False
