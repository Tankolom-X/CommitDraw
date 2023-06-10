# Commit Draw

## Allows you to convert your image into the activity on your GitHub heatmap, as well as fill it randomly
**`CommitDraw` is a tool to decorate your GitHub contribution heatmap
based on the git's ability to accept commits _in the past_.**

---
## Modes of use:

### Image convert
**The image that was provided:**\
![example](https://github.com/Tankolom-X/CommitDraw/blob/main/media/example.png?raw=True "example") \
From left to right: turtle, hedgehog, mushroom, smile, penguin

**The result:**\
![result](https://github.com/Tankolom-X/CommitDraw/blob/main/media/result.png?raw=True "result")

### Fill randomly
**The result:**\
![result](https://github.com/Tankolom-X/CommitDraw/blob/main/media/random_filling.png?raw=True "result")



---

## How does it work?

### Image convert

`CommitDraw` analyzes a picture that you provide to the
program, then generates an array of commits. After all starts to draw by making commits
from the date you have chosen.
>  **Warning**
>  If your beginning date is not Sunday, the program will pass pixels from the Sunday
>  to the date you have chosen

> **Note**
>  A picture that you provide to the program should be **7 pixels in height**.\
> Otherwise, the result may be blurred.

### Fill randomly
`CommitDraw` makes commits for the period you have chosen in randomly amount in range of specified
minimal and maximal values

---

## How to use?
1. **You can download and launch built program for your os**
   <table>
      <thead>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_windows.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/windows_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/windows.png">
                     <img alt="windows" src="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/windows.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_macos.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/apple_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/apple.png">
                     <img alt="apple" src="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/apple.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_linux.zip?raw=True" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/linux_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/linux.png">
                     <img alt="linux" src="https://github.com/Tankolom-X/CommitDraw/blob/main/media/os_icons/linux.png">
                  </picture>
               </a>
            </p>
         </th>
      </thead>
      <tbody>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_windows.zip?raw=True">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_macos.zip?raw=True">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/CommitDraw/blob/main/build/CommitDraw_linux.zip?raw=True">Download</a>
         </th>
      </tbody>
   </table>
   
   <br>
   
   >   *Or run from source following the instructions:*
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
   >   > Linux and Mac users may be forced to install *tkinter* via their distribution's package managers
   >   
   >   + Run main.py
   >   ```bash
   >   python main.py
   >   ``` 

2. **In the menu select the activity you want to do**
   + Convert an image to your GitHub heatmap activity
   + Fill you GitHub heatmap activity randomly
   > **Note**\
   > For the best result the picture should be **7 pixels in height**\
   > The date must be in **YYYY-MM-DD format**
3. **Follow the prompts** 
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
   >  **Warning**
   >  The years you used to draw cannot be removed from the activity on GitHub
   
---
### Selecting the picture

Your picture should be **7 pixels in height**. Otherwise, the result may be blurred.

White color means no activity(Empty cell on your GitHub heatmap).\
The darker the color of your image the darker the color of the cell on your GitHub heatmap.

Examples you can find here: https://github.com/Tankolom-X/CommitDraw/tree/main/samples

