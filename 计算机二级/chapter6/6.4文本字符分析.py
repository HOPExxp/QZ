def handletxt(txt):
    counts = {}
    for char in txt:
        counts[char] = counts.get(char,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse = True)
    for item in items:
        cha , count = item
        print('字符[{}] 数量[{}]'.format(cha,count))

str = 'ajkfjkwaji24h3toiqiog4oigjfif4faklj402u'
handletxt(str)