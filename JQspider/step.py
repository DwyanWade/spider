import re

a = " 26326浏览"
pattern = '\d+'
r = re.search(pattern, a)
result = int(r.group())
print(type(result))
print(result)