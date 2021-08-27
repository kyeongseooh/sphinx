def convert_bytes(size):
    '''byte를 변환해주는 함수

    :param float size: 파일의 용량

    how to use
        >>> convert_bytes(1000)
    
    '''
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GM', 4: 'TB'}
    while size >= power:
        size /= power
        n += 1
        size = round(size,1)
    return (f"{size}{power_labels[n]}")