# Above all
## Решение
Приложен файл в формате docx.  
1.При детальном анализе этого файла внутри можно обнаружить лишний xml файл (word/base.xml), который представляет собой zip архив.  
2.Внутри zip архива можно найти два файла: текстовый файл и зашифрованный zip архив. Текстовый файл написан на немецком языке и содержит зашифрованное сообщение с использованием шифра Энигмы, а также параметры, необходимые для его расшифровки.  
```
Aufmerksamkeit! Dringende Nachricht aus der Reichskanzlei.
Entfernen Sie Leerzeichen nach der Entschlüsselung.
Modell: M3
Reflektor: UKW B
ROTOR/POSITION/RING
VI/1A/1A
I/17Q/1A
III/12L/1A
STECKPLATTE: bq cr di ej kw mt os px uz gh

Text:

xaxng lqdmy mfwcp drycv etqar yjuqb whcp
```  
3.Сначала необходимо расшифровать текстовый файл с использованием предоставленных параметров шифра Энигмы, например на сайте https://cryptii.com/pipes/enigma-decoder. Важно отметить, что для корректного ответа после расшифрования нужно убрать все пробелы в строке, как это указано в самом файле.  
4.После того как текстовый файл будет расшифрован и получен пароль от zip, необходимо извлечь из него информацию, где в текстовом файле будет флаг.  
##   Флаг
AviaSales{aRe_y0u_Tur1nG?}