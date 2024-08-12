Never gonna give you up...

Найди рикролл-флаг

Формат флага: AviaSales{...}

Files attached: **AviaSales.docx**
Points offered: 100

### Врайтап

В том, что отображает word ничего полезного нет (кроме конечно же ссылки на легендарнейшое видео этой планеты на YouTube). Распаковав **AviaSales.docx** как архив с помощью того же `unzip` идём в `word/media/` и восхищаемся, увидив там файл `one_more.jpg`. Картинка тоже содержит легендарное, но нам нужны exif-метаданные:

```bash
exiftool one_more.jpg
```

Ищем строчку:

```
Comment                         : AviaSales{r1ckr0ll_mA5t3r!}
```

**PROFIT!**

### Флаг

```
AviaSales{r1ckr0ll_mA5t3r!}
```

