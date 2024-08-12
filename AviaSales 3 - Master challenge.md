
Если ты решил две предыдущие таски, предлагаю проявить своё мастерство на высшем уровне!

Найди третий флаг

AviaSales{...}

Files attached: **AviaSales.docx**
Points offered: 300
### Врайтап

Я не знаю, будут ли меня бить за триплеты, но для того чтобы решить эту таску, надо иметь два других флага. За идею спасибо Дане. В принципе это может рассматриваться как три отдельные таски, хз. В любом случае всегда можно подкорректировать разбаловку. Итак. Распаковав **AviaSales.docx** как архив, идём в `word/media` и видим там image1.jpeg. Просмотр метаданных не даст результата. Однако, в самом файле может содержаться ЧТО-ТО. Пройдём по нему binwalk-ом:

```bash
binwalk image1.jpeg
```

Вывод его будет следующий:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, EXIF standard
12            0xC             TIFF image data, little-endian offset of first image directory: 8
12081         0x2F31          Zip archive data, at least v1.0 to extract, compressed size: 171, uncompressed size: 171, name: flag.rar
12318         0x301E          Zip archive data, at least v2.0 to extract, compressed size: 158, uncompressed size: 220, name: howtoflag.txt
12708         0x31A4          End of Zip archive, footer length: 22
```

Виднеются какие-то архивы. Распаковочка:

```bash
binwalk -e image1.jpeg
```

Видим два файла: `howtoflag.txt` и `flag.rar`. В первом из них вроде бы понятен порядок следующих действий, берём два флага ставим рядом, скармливаем MD5 и расшифровываем архив. Распаковка даст `flag.txt` с ответом.

**PROFIT!**
### Флаг

```
AviaSales{y0U_b3aT_m3!}
```