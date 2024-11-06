# 1_quaternions
Кватернионы в Python

## Task
Название проекта: **1_quaternions**

1. класс кватернионов
2. основные арифметические операции (алгебра кватернионов)
3. повороты пространства через кватернионы

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

Примеры использования

Сложение:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)
b = q.Quaternion(5, 15, 25, 35)

print(a + b)
```
Вычитание:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)
b = q.Quaternion(5, 15, 25, 35)

print(a + b)
```
Умножение:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)
b = q.Quaternion(5, 15, 25, 35)

print(a * b)
```
Деление:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)
b = q.Quaternion(5, 15, 25, 35)

print(a / b)
```
Инверсия:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)

print(a.inverse())
```
Норма:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)

print(a.norm)
```
Нормализация:
```python
import quaternion as q

a = q.Quaternion(10, 20, 30, 40)

print(a.normalized)
```


## Contributing

Предварительно нужно создать и активировать виртуальное окружение, а также установить в него зависимости проекта

```bash
pip install -r requirements.txt
```

Алгоритм внесения изменений выглядит следующим образом:

1. Создаём новую ветку от ветки `main`. Название состоит из английских букв в нижнем регистре, цифр и тире. Название должно отражать суть происходящего в ветке.
```bash
git checkout main
git pull
git checkout -b <branch-name>
```
2. Делаем коммиты с осмысленными названиями и делаем их часто. В рамках каждого коммита должны быть изменения только с одинаковой смысловой нагрузкой. Коммиты лучше называть на русском, если не уверены в своём английском, главное, чтобы другие участники процесса могли быстро разобраться в том, что вы делали.
3. Мерджим `main` в нашу ветку, чтобы захватить изменения, сделанные другими разработчиками, и разрешаем возможные конфликты.
```bash
# Эта команда спулит main и вмерджит в вашу ветку
git pull origin main
```
4. Тестируем работоспособность кода. Желательно, конечно, сразу покрывать новый код тестами.
```bash
pytest tests
```
5. Пушим изменения в своей ветке и создаём Pull Request. Задаём ему осмысленное название и описание, если это необходимо. Указываем как минимум одного разработчика в списке Reviewers.
```bash
# При первом пуше
git push -u origin <branch_name>
# При последующих
git push
```