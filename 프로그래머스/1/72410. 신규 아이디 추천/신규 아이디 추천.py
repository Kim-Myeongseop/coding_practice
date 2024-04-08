def solution(new_id):
    # step1
    new_id = new_id.lower()
    
    # step2
    c_list = '~!@#$%^&*()=+[{]}:?,<>/'
    for c in c_list:
        new_id = new_id.replace(c, '')
    
    # step3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # step4
    if not new_id or new_id == '.':
        return 'aaa'
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # step5
    if not new_id:
        return 'aaa'
    
    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # step7
    while len(new_id) < 3:
        new_id = ''.join([new_id, new_id[-1]])
        
    return new_id



