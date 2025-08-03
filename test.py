# handling close manually
# f = open ("test.log", "w") # create file handler
# f.write("hello world") # write to buffer › file
# f.close()

# __init__
# __exit__
with open("test.log", "w") as f:
    f.write("hello world")
