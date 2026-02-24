print("Hello world, learn python from Docker")
with open("names.txt") as f:
    names = f.read().split()
    for name in names:
        print("Hello", name)