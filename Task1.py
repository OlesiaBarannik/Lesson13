def culculate_local_variables():
    x = 1
    y = 2
    i = "y"
    r = 4

print(culculate_local_variables.__code__.co_nlocals)

