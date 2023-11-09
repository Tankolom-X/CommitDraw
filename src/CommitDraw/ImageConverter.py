from PIL import Image
import datetime as dt
from math import ceil


class ImageConverter:
    def __init__(self):
        self.SIZE = (51, 7)
        self.colors_amount = 4
        self.activity_colors = ((255, 255, 255), (155, 233, 168), (64, 196, 99), (48, 161, 78), (33, 110, 57))
        self.commits = list()

    def image_conversion_to_commits(self, image_path):

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
                    self.colors_amount = 5
                    break
            else:
                continue
            break

        result = im.quantize(self.colors_amount)
        if len(result.getcolors()) == 1 and self.colors_amount == 5:
            return False

        delta = 1 if self.colors_amount == 4 else 0
        max_color = len(result.getcolors()) - 1
        pixels = result.load()
        for i in range(width):
            line = list()
            for j in range(height):
                line.append(4 if pixels[i, j] == max_color else pixels[i, j] + delta)
            self.commits.append(line)
        return True

    def make_a_result_image(self, beginning, image_path):
        commit_date = beginning

        if not self.image_conversion_to_commits(image_path):
            return False

        self.image_setup()
        image = Image.open('../../samples/result.png')

        for week in range(len(self.commits)):
            for day in range((beginning.weekday() + 1) % 7 if week == 0 else 0, len(self.commits[0])):
                for commit in range(self.commits[week][day]):
                    image = self.paint_pixel(image, week, day)
                commit_date += dt.timedelta(days=1)
        self.save_result_image(image)

        return True

    def image_setup(self, path='../../samples'):
        directory_path = path
        length = len(self.commits)
        image = Image.new("RGB", (length, 7), self.activity_colors[0])
        self.save_result_image(image, directory_path)

    def calculate_ratio(self):
        amounts = list()
        for week in self.commits:
            for day in week:
                amounts.append(day)
        return max(amounts) / 4.5

    def get_activity_color(self, days_commits):
        ratio = self.calculate_ratio()
        if not ratio:
            return 0

        current_level = ceil(days_commits / ratio)
        if round(ratio * 4.5) == 2:
            return 4
        if current_level >= 4:
            return 4
        if not current_level and days_commits > 0:
            return 1
        return current_level

    def save_result_image(self, image, path='../../samples'):
        directory_path = path
        image.save(f'{directory_path}/result.png')
        return directory_path

    def paint_pixel(self, image, week, day):
        new_image = image
        pixels = image.load()
        pixels[week, day] = self.activity_colors[self.get_activity_color(self.commits[week][day])]
        return new_image

    def set_commits(self, commits):
        self.commits = commits

    def get_commits(self):
        return self.commits
