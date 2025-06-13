import os


path = os.path.join("/Program")

for paste in os.listdir(path):
    path_complete = os.path(path, paste)
    print(paste)

    if not os.path.isdir(path_complete):
        continue
    print(oi)
