##  Парсер тредов Двача

![ДвачСрач](https://lh3.googleusercontent.com/qmhyOfP6VWErBYXFYqBuH7s-TSaIj_F1RsidZRY7r1e5WeOyw8KWUfC6EkK17i6Mk4g=h1024-no-tmp__apk.jpg)

Построено на базе [api2ch](https://github.com/uburuntu/api2ch).

Скорость работы: 3Gb за 1 час работы

Работать можно как с Jupyter так и из консоли
#### Запуск
```bash
git clone https://github.com/mr8bit/dvach_parse.git
```

```bash
cd dvach_parse && virtualenv venv && source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

#### Пример запуска из консоли:

Запустит парсер по всем доскам и тредам
```bash
python main.py --save_dir='./boards'
```

Запустит парсер по доскам b,hw

```bash
python main.py --board=b,hw --save_dir='./boards'
```
