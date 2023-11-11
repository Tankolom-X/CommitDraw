import datetime as dt
import os
from git import rmtree
from PIL import Image
from ImageConverter import ImageConverter
import json


class Commiter:
    def __init__(self, commits, directory, beginning, author=None, email=None):
        self.commits = commits
        self.directory = directory
        self.beginning = beginning
        self.author = author
        self.email = email

    def set_git_configs(self):
        os.chdir(self.directory)
        if self.author:
            os.system(f'git config --local user.name "{self.author}"')
        if self.email:
            os.system(f'git config --local user.email {self.email}')

    def prepare_to_commits(self):
        os.chdir(self.directory)
        if os.path.isfile('result.png'):
            os.remove('result.png')
        if os.path.isfile('result.txt'):
            os.remove('result.txt')
        if os.path.isdir('.git'):
            rmtree('.git')
        os.system('git init')
        self.set_git_configs()

    def make_commits(self):

        commit_date = self.beginning

        commits_json = json.dumps(self.commits)
        with open(f'{self.directory}/result.txt', mode='a') as f:
            f.write(commits_json)
        os.system('git add result.txt')

        converter = ImageConverter()
        converter.set_commits(self.commits)
        converter.image_setup(path=self.directory)
        image = Image.open('result.png')

        for week in range(len(self.commits)):
            for day in range((self.beginning.weekday() + 1) % 7 if week == 0 else 0, len(self.commits[0])):
                for commit in range(self.commits[week][day]):
                    image = converter.paint_pixel(image, week, day)
                    converter.save_result_image(image, self.directory)
                    os.system('git add result.png')
                    command = f'git commit -m \"{commit_date.date()} {commit + 1}\"' \
                              f' --no-edit --date=\"{commit_date}\" --allow-empty'
                    os.system(command)
                commit_date += dt.timedelta(days=1)
