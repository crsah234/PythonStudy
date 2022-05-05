word=list('삶꿈정')
word.extend('복빛')
print(word) # ['삶', '꿈', '정', '복', '빛']
word.sort()
print(word) # ['꿈', '복', '빛', '삶', '정']

fruit=['복숭아','자두','골드키위','귤']
print(fruit) #  ['복숭아', '자두', '골드키위', '귤']

fruit.sort(reverse=True)
print(fruit) # ['자두', '복숭아', '귤', '골드키위']

mix=word+fruit
print(sorted(mix)) # ['골드키위', '귤', '꿈', '복', '복숭아', '빛', '삶', '자두', '정']
print(sorted(mix,reverse=True)) # ['정', '자두', '삶', '빛', '복숭아', '복', '꿈', '귤', '골드키위']





