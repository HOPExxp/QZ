with open('C:/Users/xxp/Desktop/latex.log', 'r', encoding='utf-8') as f:
    s,c=0,0
    for line in f:
        line=line.strip('\n')
        if line=='':
            continue
        s+=len(line)
        c+=1
    print(round(s/c))