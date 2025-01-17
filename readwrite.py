with open('name.txt') as f:
    my_name = f.read()
print(my_name)

with open('output/hello.txt', 'w') as f:
    f.write('Hello, my name is ')
    f.write(my_name)
