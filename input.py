import ast
import pprint
file = open("data.txt", "r")

rawdata = file.read()
data = ast.literal_eval(rawdata)
file.close()

newdata = {
    'name':'test',
    'age':22,
    'program':'BSA',
    'hobbies':['Mobile legends','youtube','twitter']
}

data.append(newdata)
data.pop(2)
data.sort()
pprint.pprint(data)
#save the updated data to the file
# with open("data.txt", "w") as file:
#     file.write(str(data))

