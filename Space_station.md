# Space station

Let's travel in the space... And tabulation

Files attached: **an_article.txt**
Points offered: **250**

dxctf{...}

### Врайтап

Открыв файл сперва не заметим ничего, что могло бы навлечь на ответ. Пытаясь искать шифры выходим из себя. Выйдя из себя начинаем долбить по мышке. Долбя по мышке нечаянно выделяем непечатаемые символы в области между абзацами. Вспомиинаем про рофлоязык Whitespace (таб/пробел). Описание таски - небольшой хинт. Открываем vim и пишем автодешифровку:

```python
# Open, read and parse contents

file = open("an_article.txt","r")

contentslist = file.read().split("\n")

# Filter useful whitespace strings

usefullist = []

for i in contentslist:
    if len(i) == 0 or i[-1] == " " or i[-1] == "\t":
        usefullist.append(i)

usefulcontent = "\n".join(usefullist)

# Writing useful content and closing files

ww = open("result.txt","w")
ww.write(usefulcontent)

file.close()
ww.close()
```

На выходе получаем `result.txt`, данные из которого помещаем в Whitespace интерпретатор. Например, в https://naokikp.github.io/wsi/whitespace.html. Нормальный интерпретатор даст нам флаг.

### Флаг

```
dxctf{wh1t3spAc3_g3niu$!}
```