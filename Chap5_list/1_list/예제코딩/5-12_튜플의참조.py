singer='bts','a','bts','ace','bts'
song=0,1,2,3,4
print(singer)
print(song)
print(singer.count('bts'))
print(singer.index('a'))
print(singer.index('bts'))

for _ in range(len(singer)): # 0~4
    print(" _의 값은 : ",_)
    print("%s : %s"%(singer[_],song[_]))
# _의값은: 0
# bts: 0
# _의값은: 1
# a: 1
# _의값은: 2
# bts: 2
# _의값은: 3
# ace: 3
# _의값은: 4
# bts: 4