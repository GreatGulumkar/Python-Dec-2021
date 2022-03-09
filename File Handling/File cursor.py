"""
File cursor

File cursor is a pointer that points to the current location of the program in the file.

In python we can manually change the cursor position.

"""

from nbformat import read


#fo = open("Cursor.txt", 'w+')

# fo.write(fo.__doc__)

# empty string is printed because file cursor is at the end of the file.
# print(fo.read())

# seek() allows us to move the file cursor.
# seek(offset[,from])
# offset - how many positions to move from the "From".
# from - 0,1,2 - 0 - start of the file. 1 - current location. 2 - end of the file.
# fo.close()

fo = open("Cursor.txt", 'r')

fo.seek(0, 0)  # move the cursor to the start of the file

print(fo.read(10))

fo.seek(5, 0)  # move the cursor to 5th position from start of the file.

print(fo.read(10))

# tell() will return the current location of file cursor.
print(fo.tell())


fo.seek(5, 0)  # move the cursor to 5th position from start of the file.

print("Starting from", fo.tell())

i = 1
while i <= 10:
    print(fo.read(1), fo.tell())
    i += 1

fo.seek(0, 2)  # move 10 position from current location

print(fo.tell())

fo.seek(0)

print(len(fo.read()))

print(fo.tell())


fo.seek(4, 0)
print('\n' == (fo.read(1)))
print('\n' == (fo.read(1)))
print('\n' == (fo.read(1)))
