import json
import datetime
import argparse
from random import randint as rd
from pprint import pprint

parser = argparse.ArgumentParser(description="Note v. 0.1")

parser.add_argument('command', type=str, help='Название команды: add, list, find, update, delete')
parser.add_argument('-t', '--title', type=str, help='Название заметки')
parser.add_argument('-c', '--content', type=str, help='Текст заметки')
args = parser.parse_args()

filename = 'v:\\note.json'

# получаем текущее время и дату и конвертируем в int
dt = datetime.datetime.now()
int_dt = int(dt.strftime("%Y%m%d%H%M%S"))

# новая заметка
def add(title, content):
    new_data = {
        "id": rd(0, 10000),
        "title": title,
        "content": content,
        "datetime": int_dt
    }
    new_data = json.dumps(new_data)
    new_data = json.loads(str(new_data))

    with open(filename, encoding = 'utf-8') as file:
        data = json.load(file)
        data['notes'].append(new_data)
        with open(filename, 'w', encoding = 'utf-8') as outfile:
            json.dump(data, outfile, indent = 4)

# изменение текста существующей заметки по названию
def update(title, content):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['title'] == str(title):
                note['content'] = content
                note['datetime'] = int_dt
            else:
                None
            index = index + 1
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii = False, indent = 4)

# список всех заметок, отсортированных по дате добавления
def list():
    with open(filename, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        new_data = sorted(data['notes'], key=lambda k: k['datetime'], reverse = True)
        pprint(new_data)

# поиск заметки по названию
def find(title):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['title'] == str(title):
                pprint(data['notes'][index])
            else:
                None
            index = index + 1

# удаление заметки по названию
def delete(title):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        index = 0
        for note in data['notes']:
            if note['title'] == str(title):
                data['notes'].pop(index)
            else:
                None
            index = index + 1
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii = False, indent = 4)


if args.command == 'add':
    add(args.title, args.content)
elif args.command == 'update':
    update(args.title, args.content)
elif args.command == 'list':
    list()
elif args.command == 'find':
    find(args.title)
elif args.command == 'delete':
    delete(args.title)
else:
    print("Введите корректную команду")