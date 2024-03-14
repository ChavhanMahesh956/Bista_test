from collections import Counter


def nested_dic():
    
    file_paths = [
    "/home/user/documents/report.txt",
    "/home/user/documents/project1/specs.txt",
    "/home/user/documents/project1/code.main.py",
    "home/user/documents/project2/notes.txt",
    "/home/user/pictures/image.jpg"
    ]
    
    result = []
    word_list=[]
    
    for i in range(len(file_paths)):  
        result.append(file_paths[i].split("/"))
    
    for word in (len(dict)):
            count = word_list.count(word)
            print(count)
    return result

print(nested_dic())

