from PIL import Image
import datetime as dt
import os
from git import rmtree
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from random import randint

SIZE = (51, 7)
colors_amount = 4


def modal_image_select():
    root = tk.Tk()
    root.attributes('-alpha', 0.0)
    root.attributes('-topmost', True)
    path_to_image = tk.filedialog.askopenfilename(parent=root, title='Select an image')
    root.destroy()
    if not path_to_image:
        exit()
    return path_to_image


def modal_directory_select():
    input('To select a directory, press enter ')
    root = tk.Tk()
    root.attributes('-alpha', 0.0)
    root.attributes('-topmost', True)
    directory = tk.filedialog.askdirectory(parent=root, title='Select a directory')
    root.destroy()
    if not directory:
        exit()
    return directory


def year_select():
    year = int(input('Year for commits:\n'))
    if not year:
        exit()
    return year


def date_select():
    message = 'Please specify the beginning date in day-month-year format \n'
    day, month, year = input(message).split('-')
    beginning = dt.datetime(day=int(day), month=int(month), year=int(year), hour=12)

    message = 'Please specify the ending date in day-month-year format \n'
    day, month, year = input(message).split('-')
    ending = dt.datetime(day=int(day), month=int(month), year=int(year), hour=12)

    return beginning, ending


def get_commits(image_path):
    global colors_amount

    im = Image.open(image_path)
    if im.size != SIZE:
        im = im.resize(SIZE)

    im = im.convert('L')
    pixels = im.load()
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if pixels[i, j] == 255:
                colors_amount = 5
                break
        else:
            continue
        break

    result = im.quantize(colors_amount)

    if len(result.getcolors()) == 1 and colors_amount == 5:
        print('Cannot transform white image')
        exit()

    max_color = len(result.getcolors()) - 1
    pixels = result.load()
    colors = list()
    for i in range(SIZE[0]):
        line = list()
        for j in range(SIZE[1]):
            line.append(4 if pixels[i, j] == max_color else pixels[i, j])
        colors.append(line)

    return colors


def first_date(year):
    day = 1
    month = 1
    if dt.date(year, month=month, day=day).weekday() == 6:
        date = dt.datetime(year, month=1, day=8, hour=12)
    else:
        while dt.date(year, month=month, day=day).weekday() != 6:
            day += 1
        else:
            date = dt.datetime(year, month=month, day=day, hour=12)

    return date


def prepare_for_commit(directory_path):
    os.chdir(directory_path)
    if os.path.isfile('commits_file.txt'):
        os.remove('commits_file.txt')
    if os.path.isdir('.git'):
        rmtree('.git')
    os.system('git init')


def make_commits(commit_date, commits):
    k = 1 if colors_amount == 4 else 0
    for row in range(SIZE[1]):
        for col in range(SIZE[0]):
            for i in range(commits[col][row] + k):
                f = open('commits_file.txt', 'a')
                f.write('0')
                f.close()
                os.system('git add commits_file.txt')
                command = f'git commit -m \"{commit_date.date()} {i + 1}\" --no-edit --date=\"{commit_date}\"'
                os.system(command)
            commit_date += dt.timedelta(days=7)
        commit_date -= dt.timedelta(days=7 * 51 - 1)
    print('Commits were generated. You can push them to your empty GitHub repository')

def menu():
    while True:
        print('\n' * 2)
        print('Please select the action')
        print('1. Convert an image to your GitHub heatmap activity')
        print('2. Fill you GitHub heatmap activity randomly')
        index = int(input('Your choice: '))
        if index in [1, 2]:
            return index
        else:
            print('Choice is incorrect')


index = menu()
if index == 1:
    path_to_image = modal_image_select()

    directory = modal_directory_select()
    year = year_select()

    prepare_for_commit(directory)
    commits = get_commits(path_to_image)
    commit_date = first_date(year)
    make_commits(commit_date, commits)

elif index == 2:
    directory = modal_directory_select()
    beginning, ending = date_select()
    minimal = int(input('Specify the minimal amount of commits \n'))
    maximal = int(input('Specify the maximal amount of commits \n'))

    prepare_for_commit(directory)

    if beginning == ending:
        print('Dates are the same')
        exit()

    commit_date = beginning
    for _ in range((ending - beginning).days + 1):
        for i in range(randint(minimal, maximal)):
            f = open('commits_file.txt', 'a')
            f.write('0')
            f.close()
            os.system('git add commits_file.txt')
            command = f'git commit -m \"{commit_date.date()} {i + 1}\" --no-edit --date=\"{commit_date}\"'
            os.system(command)
        commit_date += dt.timedelta(days=1)
    print('Commits were generated. You can push them to your empty GitHub repository')

