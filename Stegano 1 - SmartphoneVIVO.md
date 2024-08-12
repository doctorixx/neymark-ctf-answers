
\<DELETED\>

dxctf{...}

Files attached: **smartphoneVIVO.png**
Points offered: 300

### Врайтап

Да, я обажаю мемные таски поэтому держите ещё одну в копилку

Мы имеем фотку лучшего в мире смартфона VIVO! Её также можно потрясти на наличие всяких штук, но лучше начать сразу с `binwalk`-а. Моего любимого кст

```bash
binwalk smartphoneVIVO.png
```

Вывод будет многообещающим:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 221 x 228, 8-bit/color RGB, non-interlaced
62            0x3E            Zlib compressed data, default compression
33953         0x84A1          Zip archive data, at least v1.0 to extract, compressed size: 187, uncompressed size: 187, name: flag.rar
34206         0x859E          Zip archive data, at least v2.0 to extract, compressed size: 1485187, uncompressed size: 2000164, name: smartphoneVIVO.txt
1519635       0x173013        End of Zip archive, footer length: 22
```

Опять же распаковочка:

```bash
binwalk -e smartphoneVIVO.png
```

Распаковка даст нам `flag.rar` и `smartphoneVIVO.txt`. RAR понятно дело шифрованный. Тут немного сложнее относительно задач от AviaSales, ведь `smartphoneVIVO.txt` это тупо куча ASCIIшного бреда. Может прийти логичная идея поискать по каким-нибудь кейвордам типа dxctf, flag, key, task и тп. Но к результатам не приведёт, ведь все кейворды были УДАЛЕНЫ (DELETED) из сообщения. Вспоминаем про описание таски. Ищем по кейворду DELETED:

```bash
grep -r "DELETED" smartphoneVIVO.txt > result
cat result
```

Даст:

```
HiThankstoyouforfindingmeIhaveareallynice<DELETED>foryouBeatingthis<DELETED>willgiveyoua<DELETED>HeresthestringbTMwd19zbWFydHBob25lVklWT19tMzB3decryptitandenjoy!
```

Ну вроде бы видно английские словечки. Расставив пробелы получаем шифр `bTMwd19zbWFydHBob25lVklWT19tMzB3`. Ну не думаю что составит труда пробить её на http://dcrypt.fr, понять что это base64 и получить пароль от архива: `m30w_smartphoneVIVO_m30w`. Распаковывем и достаём `flag.txt` с ответом.

**PROFIT!**
### Флаг

```
dxctf{smArtph0n3_VIVOVIVO_123456_m30w}
```