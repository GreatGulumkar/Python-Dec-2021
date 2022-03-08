'''
In this file we will perform file handling on binary files.

binary files can be - images, videos files, audio file.

'''

fbo = open("honey wallpaper.png", 'rb')

h = fbo.read()

fbo.close()


fbo1 = open("My wallpaper.png", 'wb')

fbo1.write(h)
