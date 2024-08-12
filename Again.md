# Again

## Решение

К заданию приложено видео в формате mp4 c заставкой сериала Better Call Saul.

1. При анализе видео с помощью hex-редактора можно обнаружить строку `flag_is_UVhacFlWTmhiR1Z6ZTBKbFZGUmxVbDlEWVNGTUxVTlVSbjA9.` Этот текст является закодированным сообщением, которое содержит флаг.
[![imageup.ru](https://imageup.ru/img131/4885131/snimok-ekrana-ot-2024-08-12-19-06-06.png)](https://imageup.ru/img131/4885131/snimok-ekrana-ot-2024-08-12-19-06-06.png.html)
2. Если декодировать строку из base64 формата один раз, а затем повторить этот процесс еще раз, мы получим флаг.
[![imageup.ru](https://imageup.ru/img146/4885133/snimok-ekrana-ot-2024-08-12-19-08-12.png)](https://imageup.ru/img146/4885133/snimok-ekrana-ot-2024-08-12-19-08-12.png.html)
[![imageup.ru](https://imageup.ru/img126/4885134/snimok-ekrana-ot-2024-08-12-19-08-21.png)](https://imageup.ru/img126/4885134/snimok-ekrana-ot-2024-08-12-19-08-21.png.html)

## Флаг

AviaSales{BeTTeR_Ca!L-CTF}