"""20 gb file"""
import time

s = time.time()
repeat, lines_num = 100, 5_000_000
with open('really_big_file.txt', 'w', encoding='utf-8') as f:
    for i in range(lines_num):
        print("abc bca cba ccc" * repeat, file=f)

with open('really_big_file.txt', 'a', encoding='utf-8') as f:
    print("1 а Роза упала на лапу Азора", file=f)

with open('really_big_file.txt', 'a', encoding='utf-8') as f:
    for i in range(lines_num):
        print("abc aaa cba ccc" * repeat, file=f)

with open('really_big_file.txt', 'a', encoding='utf-8') as f:
    print("2 а Роза упала на лапу Азора", file=f)

with open('really_big_file.txt', 'a', encoding='utf-8') as f:
    for i in range(lines_num):
        print("abc aaa cba ccc" * repeat, file=f)

print(int(time.time() - s))
