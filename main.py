from PIL import Image
import datetime as dt
import os
from git import rmtree
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

SIZE = (51, 7)
colors_amount = 4


def modal_image_select():
    Tk().withdraw()
    path_to_image = askopenfilename(title='Select an image')
    if not path_to_image:
        exit()
    return path_to_image


def modal_directory_select():
    directory = askdirectory(title='Select a directory')
    if not directory:
        exit()
    return directory


def date_select(only_year=True):
    if only_year:
        year = int(input('Year for commits:\n'))
        if not year:
            exit()
        return year


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


path_to_image = modal_image_select()
directory = modal_directory_select()
year = date_select()

prepare_for_commit(directory)
commits = get_commits(path_to_image)
commit_date = first_date(year)
make_commits(commit_date, commits)
