from os import listdir, path

flist = listdir('.')
for name in flist:
    print(path.join(path, name))
