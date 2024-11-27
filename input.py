import ast
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

#save the updated data to the file
with open("data.txt", "w") as file:
    file.write(str(data))