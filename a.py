a = ['dan', 'shuchen', 'dog', 'cat']
b = 'shuchen'
counter = 0
for i in a:
	if b == i:
		counter=1

if counter ==1:
	print('there is a match!')
else:
	print('there is no match!!!!!!!!!')
a="<title>hello   </title>"
import re
print(re.search(r'<title>([\w\s]+)</title>',a).group(1))