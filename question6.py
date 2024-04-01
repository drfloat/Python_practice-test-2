def cal(n):
    spliter=[words for items in n for words in items.split('/')]
    for i in spliter:
        if i == '':
            spliter.remove(i)
    count={}
    a=0
    for i in range(0,len(spliter)):
        for j in range(i,len(spliter)):
            if spliter[i]==spliter[j]:
                a+=1
        count.update({spliter[i]:a})
        a=0
    print(count)






file_paths=[
    "/home/user/documents/report.txt",
    "/home/user/documents/report.txt",
    "/home/user/documents/report.txt",
    "/home/user/documents/report.txt",
    "/home/user/pictures/image.jpg",
]

cal(file_paths)

