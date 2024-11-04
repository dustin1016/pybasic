import getdatatype
def eval_bool(param):
    if isinstance(param, bool):
        return True
    else:
        return False

x = "hello"

# print(type(x))
# print(isinstance(x, int))
b = True
f = str(b)
# print(eval_bool(b))
getdatatype.main()