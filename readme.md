##  Парсер тердов Двача

![ДвачСрач](https://lh3.googleusercontent.com/qmhyOfP6VWErBYXFYqBuH7s-TSaIj_F1RsidZRY7r1e5WeOyw8KWUfC6EkK17i6Mk4g=h1024-no-tmp__apk.jpg)

Построено на базе [api2ch](https://github.com/uburuntu/api2ch).

Скорость работы: 3Gb за 1 час работы

Работать можно как с Jupyter так и из консоли

#### Пример запуска из консоли:

Запустит парсер по всем доскам и тредам
```bash
python main.py --save_dir='./boards'
```

Запустит парсер по доска b,hw

```bash
python main.py --board=b,hw --save_dir='./boards'
```
