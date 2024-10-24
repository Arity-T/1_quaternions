# 1_quaternions
Кватернионы в Python

## Installation

Создать виртуальное окружение

```bash
virtualenv venv
```

И активировать его
```powershell
# Для Windows
venv\Scripts\activate
```

```bash
# Для Linux
source venv/bin/activate
```

В корневой директории проекта выполнить

```bash
pip install .
```

## Usage

Пример использования

```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)
b = q.Quaternion(5, 15, 25, 35)

print(a + b)
```

## Tests

Для запуска тестов необходимо установить `pytest`.

В корневой директории проекта запустить

```bash
pytest tests
```