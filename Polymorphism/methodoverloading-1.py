#to take multiple arguments into the function as parameters
def add(datatype,*args):
    if datatype=="int":
        answer=0
    if datatype=="str":
        answer=""
    for i in args:
        answer+=i

    print(answer)
add("int",5,6)
add("str","Hi","Geeks")