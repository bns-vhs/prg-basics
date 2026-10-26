def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def inches_to_cm(n):
    return n*2.54

def feet_to_cm(n):
    return n*30.48
def cm_to_inches(n):
    return n/2.54

def cm_to_feet(n):
    return n/30.48

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'10in = {inches_to_cm(10)}cm')
    print(f'10ft = {feet_to_cm(10)}cm')
    print(f'10cm = {cm_to_inches(10)}in')
    print(f'10cm = {cm_to_feet(10)}ft')

