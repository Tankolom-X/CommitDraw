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


def exclude_days():
    if input('To exclude days of the week from your activity, insert "Y"\n(press enter to skip)\n') != 'Y':
        return set()
    else:
        excluding_days = set([int(day) for day in input(
            'Please, specify the days you don`t want to have any activity'
            '\n(numbers of days of the week in a line separated by a space)\n'
            '\n--To pass press enter--\n'
            '\nSunday - 0'
            '\nMonday - 1'
            '\nTuesday - 2'
            '\nWednesday - 3'
            '\nThursday - 4'
            '\nFriday - 5'
            '\nSaturday - 6\n').split()])
        return excluding_days


def random_conversion(beginning, ending, minimal, maximal, excluding_days=None):
    empty_amount = (beginning.weekday() + 1) % 7

    line = list()
    for i in range((ending - beginning).days + 1 + empty_amount):
        if len(line) == 7:
            commits.append(line)
            line = list()
        if i in range(empty_amount) or ((i % 7) in excluding_days if excluding_days else False):
            line.append(0)
        else:
            line.append(randint(minimal, maximal))
    if line:
        while len(line) < 7:
            line.append(0)
        commits.append(line)


def ask_git_configs():
    if input('To specify commits configs(author, email), insert "Y"\n(press enter to skip)\n') != 'Y':
        return {'author': None, 'e_mail': None}
    else:
        author = input('Specify the commits author (press enter to set by default): ')
        e_mail = input('Specify email (press enter to set by default): ')
        return {'author': author, 'e_mail': e_mail}


def set_git_config(configs):
    if configs['author']:
        os.system(f'git config --local user.name "{configs["author"]}"')
    if configs['e_mail']:
        os.system(f'git config --local user.email {configs["e_mail"]}')


def prepare_to_commits(directory_path, configs=None):
    os.chdir(directory_path)
    if os.path.isfile('commits_file.txt'):
        os.remove('commits_file.txt')
    if os.path.isdir('.git'):
        rmtree('.git')
    os.system('git init')
    if configs:
        set_git_config(configs)


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
        print()
        excluding_days = exclude_days()
        minimal = int(input('Specify the minimal amount of commits \n'))
        maximal = int(input('Specify the maximal amount of commits \n'))

        if beginning == ending:
            print('Dates are the same')
            exit()

        random_conversion(beginning, ending, minimal, maximal, excluding_days=excluding_days)

    configs = ask_git_configs()
    prepare_to_commits(directory, configs=configs)
    make_commits(beginning)


if __name__ == '__main__':
    main()
