# Commit Draw

## Allows you to convert your image into the activity on your GitHub heatmap, as well as fill it randomly

**`CommitDraw` is a tool to decorate your GitHub contribution heatmap
based on the git's ability to accept commits _in the past_.**

---

## Modes of use:

### Image convert

**The image that was provided:**\
![example](https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/example.png?raw=True "example") \
From left to right: turtle, hedgehog, mushroom, smile, penguin

**The result:**\
![result](https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/result.png?raw=True "result")

### Fill randomly

**The result:**\
![result](https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/random_filling.png?raw=True "result")\
On the left side of the image settings of random filling are not specified, on the right are specified


---

## How does it work?

### Image convert

`CommitDraw` analyzes a picture that you provide to the
program, then generates an array of commits. After all it starts to draw by making commits
from the date you have chosen.
> **Warning**
> If your beginning date is not Sunday, the program will pass pixels from the Sunday
> to the date you have chosen

> **Note**
> A picture that you provide to the program should be **7 pixels in height**.\
> Otherwise, the result may be blurred.

### Fill randomly

`CommitDraw` makes commits for the period you selected,
in amount of randomly selected value from the generated array (you can [**specify it
yourself**](https://github.com/Tankolom-X/CommitDraw#settings-of-the-filling), or
only specify the minimum and maximum values).It can also [**exclude days of the
week**](https://github.com/Tankolom-X/CommitDraw#exclude-days-of-the-week) that you have chosen.
</br>
</br>
</br>

| ***In the result:***<br/> **1. Commits will be generated which you can push to the GitHub repository<br/>2.You will get the same image in the selected folder on your PC as when you push the commits to the GitHub** |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


**Generated image in the selected folder on your PC:**\
![generated image](https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/generated_image.png?raw=True "generated image on the PC")

---

## How to use?

1. **You can download and launch built program for your os**
   <table>
      <thead>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_windows.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/windows_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/windows.png">
                     <img alt="windows" src="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/windows.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_macos.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/apple_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/apple.png">
                     <img alt="apple" src="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/apple.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_linux.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/linux_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/linux.png">
                     <img alt="linux" src="https://github.com/Tankolom-X/CommitDraw/blob/1.x/media/os_icons/linux.png">
                  </picture>
               </a>
            </p>
         </th>
      </thead>
      <tbody>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_windows.zip?raw=True">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_macos.zip?raw=True">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/1.x/build/CommitDraw_linux.zip?raw=True">Download</a>
         </th>
      </tbody>
   </table>

   <br>

   > *Or run from source following the instructions:*
   >   + Execute ```git clone https://github.com/Tankolom-X/CommitDraw.git```
   >   + Make sure you have an actual version of pip:
   >   ```bash
   >   pip install --upgrade pip 
   >   ```
   >   + Then install required dependencies: *Pillow*, *GitPython* and *tkinter*:
   >   ```bash
   >   pip install -r requirements.txt 
   >   ```
   >
   >   > **Note**
   > > Linux and Mac users may be forced to install *tkinter* via their distribution's package managers
   >
   >   + Run main.py
   >   ```bash
   >   python main.py
   >   ``` 

2. **In the menu select the activity you want to do**
    + Convert an image to your GitHub heatmap activity
    + Fill you GitHub heatmap activity randomly
   > **Note**
   > For the best result the picture should be **7 pixels in height**\
   > The date must be in **YYYY-MM-DD format**
3. **Follow the prompts**
   > :bulb:
   > Learn more about [*customizing random
   filling*](https://github.com/Tankolom-X/CommitDraw#customizing-the-random-filling)\
   > Learn more about [*selecting an image for the image
   conversion*](https://github.com/Tankolom-X/CommitDraw#selecting-the-picture)
4. **Wait until the program will finish and close**
5. **In GitHub create a new repository**
6. **Push the repository on your PC with commits from the command line to the GitHub's repository using:**
   ```
   git remote add origin https://github.com/[username]/[repositoryName]
   ```
   ```
   git branch -M main
   ```
   ```
   git push -u origin main
   ```
7. **Wait. GitHub will update your contribution heatmap soon**
   > **Warning**
   > The years you used to draw cannot be removed from the activity on GitHub

---

## Selecting the picture

Your picture should be **7 pixels in height**. Otherwise, the result may be blurred.

White color means no activity(Empty cell on your GitHub heatmap).\
The darker the color of your image the darker the color of the cell on your GitHub heatmap.

Examples you can find here: https://github.com/Tankolom-X/CommitDraw/tree/1.x/samples

---

## Customizing the random filling

### Exclude days of the week

> To do it, on question:\
> `To exclude days of the week from your activity, insert "Y"`\
> `(press enter to skip)`\
> You should insert Y
>
>  You should insert only one line with numbers of days separated by a whitespace
>

|     Day      | Number |
|:------------:|:------:|
|    Sunday    |   0    |
|    Monday    |   1    |
|   Tuesday    |   2    |
|  Wednesday   |   3    |
|   Thursday   |   4    |
|    Friday    |   5    |
|   Saturday   |   6    |

> **Example**: 0 6\
> This means exclude Sunday and Saturday from the random filling

### Settings of the filling

> To specify the random filling in the program on question:\
> `To specify the random filling, insert "Y"`\
> `(press enter to skip)`\
> You should insert Y
>
>  After that you should insert only one line with commands separated by a whitespace
>
>  For each day the program will randomly choose a number of commits from the **array**, generated by these *settings*

|     Command      |                                   Description                                   |
|:----------------:|:-------------------------------------------------------------------------------:|
| number*frequency | This means that this "number" of commits <br> will appear with some "frequency" |
| number1-number2  |             This means numbers in range from "number1" to "number2"             |
|      number      |                       This means that "number" of commits                       |

> From these **commands** will be generated an **array** with numbers, from which *will be selected
> an amount of commits* for each day
>
>  **Example**: 1*2 2-4 7\
> `1*2` - means **1** commit will appear with frequency **2**\
> `2-4` - means numbers from **2** to **4**\
> `7`   - means number **7** in array
>
>  This example generates an array **[1, 1, 2, 3, 4, 7]**