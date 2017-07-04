def data_type(arg):
    if arg == None:
        return "no value"
    if isinstance(arg,str):
        if len(arg)==0:
            return "no value"
        else:
            return len(arg)
    elif isinstance(arg,bool):
        return arg

    elif isinstance(arg,int):
        if arg<100:
            return  "less than 100"
        elif arg==100:
            return "eqaul to 100"
        else:
            return "more than 100"

    elif isinstance(arg,list):
        if len(arg) >=3:
            return arg[2]
        else:
            return None