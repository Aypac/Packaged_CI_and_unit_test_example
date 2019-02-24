def _sum(list):
    s = 0
    for a in list:
        s += float(a)
    return s

def addition(*arg, **args):
    s = 0
    if arg:
        s += _sum(arg)
    if args:
        s += _sum(args.values())
    return s
