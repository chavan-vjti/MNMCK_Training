import sys
def training(*args, **kargs):
    sep = kargs.get('sep',' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
#         print(arg)
#         print(type(arg))
        first = False
        file.write(output + end)