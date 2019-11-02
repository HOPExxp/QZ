f = open('xyj.txt','r',encoding='utf-8')
characters = []
stat = {}
for line in f:
    line = line.strip()
    if len(line) == 0:
        continue
    for x in range(len(line)):
        if line[x] in [' ','\t','\n','。','，',':','?','!','《','》','(',')'
            , '/','[', '（','）','、',';','‘','’','”','“','......'
            , '￥', '？', '；', '：', '．', '＋', '！','']:
            continue
        if not line[x] in characters:
            characters.append(line[x])
        # 判断
        if line[x] not in stat.keys():
        # if not stat.has_key(line[x]):
            stat[line[x]] = 0
        stat[line[x]] += 1
stat = sorted(stat.items(),key = lambda d:d[1],reverse = True)
fw = open('result2.csv','w',encoding='utf-8')
for key,value in stat:
    fw.write(key + ',' + str(value) + '\n')

