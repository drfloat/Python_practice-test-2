def cal(n):
    root = {}
    for path in n:
        parts = path.split('/')[1:]
        current = root
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = 1

    return root

file_paths = [
    "/home/user/documents/report.txt",
    "/home/user/documents/project1/specs.txt",
    "/home/user/documents/project1/code/main.py",
    "/home/user/documents/project2/notes.txt",
    "/home/user/pictures/image.jpg",
]

result = cal(file_paths)
print(result)