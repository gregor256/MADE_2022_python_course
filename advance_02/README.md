Приложение для обкачки урлов
----
Многопоточное клиент-серверное приложение для обкачки урлов. Работает на порте 5004. 
Нужные урлы содержатся в файле `urls.txt`. <br> 
Пользователь задает топ-k самый частых слов, встречающихся на странице. Программа выводит их в формате строки <br>
следующего вида: `"example.com: {'word1': 100, 'word2': 50}"`. Словом считается последовательность <br>
латинских или кириллических букв длины больше двух от пробела до пробела.
# Start:
```
pip instal -r requirements.txt
```
# Usage:
## Start server:
```
python server.py NUM_WORKERS TOP_K_WORDS
```
NUM_WORKERS - число потоков на сервере.
TOP_K_WORDS - число самых популярных слов, которые хочет увдеть пользователь.

### Example:

```
python server.py 10 4
```


## Start client:

```
python client.py NUM_WORKERS FILE_CONTAINIG_URLS
```

NUM_WORKERS - число потоков на клиентском приложениии.
FILE_CONTAINIG_URLS - файл, в котором перечислены урлы, каждый урл на новой строке.

### Example:

```
python client.py 10 urls.txt
```


# Testing:
```
pytest
```




