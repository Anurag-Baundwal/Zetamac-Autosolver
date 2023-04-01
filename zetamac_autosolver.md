zetamac_autosolver.py - script completely written in python. fairly speedy - scores around 2000 in 120s. to run it you need to have python installed on your pc. In addtion to that you will need to pip install selenium to get selenium. You'll also need to download chromedriver (probably from https://chromedriver.chromium.org/downloads). Once downloaded, extract it and find chromedriver.exe in the extracted folder. Copy the path to the exe and replace the following line in the zetamac_autosolver.py code - 
driver_path = "C:\\Users\\Anurag Baundwal\\Downloads\\chromedriver_win32\\chromedriver.exe" (line 16)

solver.js - fast js script that runs directly in the browser. scores around 7000 in 120s. to run it, open the browser, open zetamac, click start, and then open chrome dev tools, paste the javassript  code into the console and hit enter

solver-v2.js - faster version of solver.js. solves around 20000 problems in 120s

solver_dragon.py - same as solver-vs.js but you can run it from the terminal once you have the required stuff installed (python, selenium, chromedriver)