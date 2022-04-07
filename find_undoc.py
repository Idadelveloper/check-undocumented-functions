from inspect import getmembers, isfunction

# Import the module first

def findUndocumentedFunction(module):
    """
        This function finds all functions in a module which has not been documented and returns them as a list.
    """
    functions = getmembers(module, isfunction)
    funcs = [f[0] for f in functions]
    undoc = []
    for func in funcs:
        if getattr(module, func).__doc__ == None:
            undoc.append(func)

    return(undoc)


