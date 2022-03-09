"""

File Handling

File handling allows us to read and write data to/from files.
Python combined with some modules can read wide varity of files.

Syntax:
file_object = open(file_name [, access_mode][, buffering])

"""

fo = open("MyFile.txt", 'w')

print(dir(fo))

fo.write("Eat well, stay fit, die anyway. We will now upgrade your brain, please wait... Searching...searching...still searching... Sorry, NO BRAIN found…!")

fo.write("""
    I realized that you will always be my friend when our depressive and manic episodes synchronized.
    It's so fun to do crazy stuff and then cry all night long with someone like you, buddy.
""")

print(fo.closed)
fo.close()
print(fo.closed)

del fo

"""

modes                               usages                                  file_content                    pointer/cursor              File creation

r  read                           reading                               keep previous data                  Start of the file                  false

rb read binary                    reading binary files                  keep previous data                  Start of the file                  false

r+ read plus                      reading and writing                   keep previous data                  Start of the file                  false

rb+ read binary plus              reading and writing binary            keep previous data                  Start of the file                  false

w  write                          writing                               clear previous data                  Start of the file                 True

wb write bianry                   writing binary files                  clear previous data                  Start of the file                 True

w+ write plus                     writing and read                      clear previous data                  Start of the file                 True

wb+ write plus binary             writing and reading binary            clear previous data                  Start of the file                 True

a  append                         append                                keep previous data                  end of the file                    True

ab append bianry                  append bianry                         keep previous data                  end of the file                   True

a+ append plus                    append and read                       keep previous data                  end of the file                   True

ab+ append plus binary            append and read binary                keep previous data                  end of the file                   True


Default mode of opening file is read or read binary depending on the type of file.

"""


fo = open('MyFile.txt', 'r')

s = fo.read(15)
# fo.write("Trying to write this in the file")  # not allowed
s1 = fo.read(20)

print(s)
print(s1)

fo.close()

fo = open('MyFile.txt', 'a')

fo.write("Writing at the end of the file")

fo.close()


fo = open('MyFile.txt', 'r+')

s = fo.read(15)
# in r+ mode writing is done at the end of the file.
fo.write("Trying to write this in the file")
s1 = fo.read(20)

print(s)
print(s1)

fo.close()
