import re

def seven_ate9(str_):
    return re.sub(r"(?<=7)9(?=7)", "", str_)