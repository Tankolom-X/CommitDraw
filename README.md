# Commit Draw

**Allows you to convert your image to the activity on your GitHub heatmap**

The image that was provided:
![example](https://github.com/Tankolom-X/commit-draw/blob/main/media/example.png?raw=True "example") \
From left to right: turtle, hedgehog, mushroom, smile, penguin

The result:
![result](https://github.com/Tankolom-X/commit-draw/blob/main/media/result.png?raw=True "result")


**`commit-draw` is a tool to decorate your GitHub contribution heatmap
based on the git's ability to accept commits _in the past_.**

---

### How does it work?
`commit-draw` analyzes a picture that you provide to the
program, then generates and executes a script that makes commits
for the year you have chosen in the program.

A picture that you provide to the program should be **51x7 pixels**. Otherwise, the result may be blurred.

It is highly recommended that you create a ***new GitHub repository*** when using Commit Draw.

---

### How to use?
1. **You can download and launch built program for your os**
   <table>
      <thead>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/windows/commit-draw.exe" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/windows_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/windows.png">
                     <img alt="windows" src="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/windows.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/macos/commit-draw.app" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/apple_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/apple.png">
                     <img alt="apple" src="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/apple.png">
                  </picture>
               </a>
            </p>
         </th>
         <th>
            <p align="center">
               <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/linux/comment-draw.bin" target="_blank">
                  <picture>
                     <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/linux_white.png">
                     <source media="(prefers-color-scheme: light)" srcset="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/linux.png">
                     <img alt="linux" src="https://github.com/Tankolom-X/commit-draw/blob/main/media/os_icons/linux.png">
                  </picture>
               </a>
            </p>
         </th>
      </thead>
      <tbody>
         <th>
            <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/windows/commit-draw.exe">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/macos/commit-draw.app">Download</a>
         </th>
         <th>
            <a href="https://github.com/Tankolom-X/commit-draw/blob/main/build/linux/comment-draw.bin">Download</a>
         </th>
      </tbody>
   </table>
   
   <br>
   
   *Or run from source following the instructions:*
   + Execute ```git clone https://github.com/Tankolom-X/commit-draw.git```
   + Make sure you have an actual version of pip: 
   ```bash
   pip install --upgrade pip 
   ```
   + Then install required dependencies: *Pillow*, *GitPython* and *tkinter*:
   ```bash
   pip install -r requirements.txt 
   ```
   
   > **Note**
   > Linux and Mac users may be forced to install *tkinter* via their distribution's package managers
   
   + Run main.py
   ```bash
   python main.py
   ```
3. **In the dialog menu select the picture which you want to transform**
   > **Note**
   > For the best result the picture should be _51x7_ pixels
4. **In the next dialog menu create or select an empty directory for the result of the program**
5. **In the opened console insert the year you want to paint**
6. **Wait until the program will finish and close**
7. **In GitHub create a new repository**
8. **Push the repository on your PC with commits from the command line to the GitHub's repository using:**
    ```
   git remote add origin https://github.com/[username]/[repositoryName]
    ```
    ```
   git branch -M main
    ```
    ```
   git push -u origin main
    ```
9. **Wait. GitHub will update your contribution heatmap soon**
> 
> **Warning**
> The years you used to draw cannot be removed from the activity on GitHub

---

### Selecting the picture

Your picture should be **_51x7_ pixels**. Otherwise, the result may be blurred.

White color means no activity(Empty cell on your GitHub heatmap).\
The darker the color of your image the darker the color of the cell on your GitHub heatmap.

Examples you can find here: https://github.com/Tankolom-X/commit-draw/tree/main/samples


