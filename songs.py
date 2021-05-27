import os
song_name= "songs"
song_list=os.listdir(song_name)
print(song_list)

while True:
    for i in range(len(song_list)):
        print(i+1,".",song_list[i][:-4])
    song_name = int(input("enter song name"))
    for i in range(1,len(song_list)+1):
        if song_name == i:
            fo = open(f'songs/{song_list[i-1]}','r')
            print(fo.read())
            fo.close()
            break


    else:
        print("invalid")

    f=input("if u want to continoue press *")
    if "*"!=f:
        break
