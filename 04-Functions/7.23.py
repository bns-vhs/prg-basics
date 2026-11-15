# szesc znakow i moga sie pojawiac tylko raz

def f(password):
    if len(password)<6:
        return False

    if len(password) == len(set(password)):
        return True
    else:
        return False



print(f('1233456'))