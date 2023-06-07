from PIL import Image
import datetime as dt
import os
from git import rmtree
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from random import randint

SIZE = (51, 7)
colors_amount = 4
commits = list()


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


def date_select(beginning=True):
    if beginning:
        message = 'Please specify the beginning date in YYYY-MM-DD format \n'
        year, month, day = input(message).split('-')
        date = dt.datetime(day=int(day), month=int(month), year=int(year), hour=12)
    else:
        message = 'Please specify the ending date in YYYY-MM-DD format \n'
        year, month, day = input(message).split('-')
        date = dt.datetime(day=int(day), month=int(month), year=int(year), hour=12)
    return date


def image_conversion(image_path):
    global colors_amount, commits

    im = Image.open(image_path)
    width, height = im.size

    if height != 7:
        new_height = 7
        new_width = new_height * width / height
        im = im.resize((int(new_width), new_height), Image.LANCZOS)

    width, height = im.size
    im = im.convert('L')
    pixels = im.load()
    for i in range(width):
        for j in range(height):
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

    delta = 1 if colors_amount == 4 else 0
    max_color = len(result.getcolors()) - 1
    pixels = result.load()
    for i in range(width):
        line = list()
        for j in range(height):
            line.append(4 if pixels[i, j] == max_color else pixels[i, j] + delta)
        commits.append(line)


def random_conversion(beginning, ending, minimal, maximal):
    empty_amount = (beginning.weekday() + 1) % 7

    line = list()
    for i in range((ending - beginning).days + 1 + empty_amount):
        if len(line) == 7:
            commits.append(line)
            line = list()
        if i in range(empty_amount):
            line.append(0)
        else:
            line.append(randint(minimal, maximal))
    if line:
        while len(line) < 7:
            line.append(0)
        commits.append(line)


def prepare_to_commits(directory_path):
    os.chdir(directory_path)
    if os.path.isfile('commits_file.txt'):
        os.remove('commits_file.txt')
    if os.path.isdir('.git'):
        rmtree('.git')
    os.system('git init')


def make_commits(beginning):
    commit_date = beginning
    for week in range(len(commits)):
        for day in range((beginning.weekday() + 1) % 7 if week == 0 else 0, len(commits[0])):
            for commit in range(commits[week][day]):
                f = open('commits_file.txt', 'a')
                f.write('0')
                f.close()
                os.system('git add commits_file.txt')
                command = f'git commit -m \"{commit_date.date()} {commit + 1}\" --no-edit --date=\"{commit_date}\"'
                os.system(command)
            commit_date += dt.timedelta(days=1)
    print('Commits were generated. You can push them to your empty GitHub repository')


def menu():
    while True:
        print('\n' * 2)
        print('Please select the action')
        print('1. Convert an image to your GitHub heatmap activity')
        print('2. Fill you GitHub heatmap activity randomly')
        index = input('Your choice: ')
        if index in ['1', '2']:
            return int(index)
        else:
            print('Choice is incorrect')


def main():
    index = menu()

    if index == 1:
        path_to_image = modal_image_select()
        directory = modal_directory_select()
        beginning = date_select()

        image_conversion(path_to_image)

    elif index == 2:
        directory = modal_directory_select()
        beginning = date_select()
        ending = date_select(beginning=False)
        minimal = int(input('Specify the minimal amount of commits \n'))
        maximal = int(input('Specify the maximal amount of commits \n'))

        if beginning == ending:
            print('Dates are the same')
            exit()

        random_conversion(beginning, ending, minimal, maximal)

    prepare_to_commits(directory)
    make_commits(beginning)


if __name__ == '__main__':
    main()
