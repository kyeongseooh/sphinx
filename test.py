import fnmatch
def s3Recursive(s3_path : list, path_condition : str, recursive : bool):
    '''검색 조건에 맞는 s3 path list를 찾아주는 함수

    :param list s3_path: s3_path의 리스트
    :param str path_condition: 검색 조건
    :param bool recursive: path를 재귀적으로 탐색 (default=`False`)

    how to use
        >>> s3Recursive(s3_path, "/*", True)
    
    '''
    list = []
    destination_file_name = []
    ori_length = len(path_condition.lstrip("/").rstrip("/").split("/"))
    r = recursive
    if r == False:
        for i in range(len(s3_path)):
            if fnmatch.fnmatch(s3_path[i],path_condition) :  
                if len(s3_path[i].split("/")) <= ori_length:
                    list.append(s3_path[i])
    else:
        for i in range(len(s3_path)):
            if fnmatch.fnmatch(s3_path[i],path_condition) : 

                list.append(s3_path[i])

    for i in range(len(list)):
        destination_file_name.append("/".join(list[i].split("/")[ori_length-1:]))
 
    return list, destination_file_name # return -> list