import os
import argparse
import datetime
from colorama import init, Fore, Style
init(autoreset=True)


parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("-t", "--text", help="text for search")  # сделать текст неопциональным
parser.add_argument("--full", help="all places",
                    action="store_true")
args = parser.parse_args()

if os.path.isdir(args.file):
    files = [os.path.join(args.file, name) for name in sorted(os.listdir(args.file))]
else:
    files = [args.file]


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as logs:
        for line in logs.readlines():
            yield line


def is_date(string):
    try:
        datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")
        return string
    except ValueError:
        return None


def parse_file(path):
    events = {}
    last_date = ''
    for line in read_file(path):
        date = is_date(line[:23])
        if date:
            last_date = date
            events[date] = line[23:]
        else:
            events[last_date] += line
    return events


def output_text(text, word, n=5):
    words = text.split()
    for i, w in enumerate(words):
        if word in w:
            return ' '.join(words[max(0, i - n):i + n + 1])
    return None


for path in files:
    name = os.path.basename(path)
    for date, text in parse_file(path).items():
        search_result = output_text(text, args.text)
        if search_result is not None:
            print(Fore.CYAN + name, Fore.GREEN + date, Fore.RED + search_result)
