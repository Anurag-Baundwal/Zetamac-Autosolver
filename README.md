Zetamac Autosolver

A collection of scripts to automatically solve arithmetic problems on Zetamac (https://www.zetamac.com/).

1. zetamac_autosolver.py

   A Python script that scores around 2000 problems in 120 seconds.

   Requirements:
   - Python installed on your PC
   - Selenium package: Install it using 'pip install selenium'
   - ChromeDriver: Download it from https://chromedriver.chromium.org/downloads

   Usage:
   - Extract ChromeDriver and find 'chromedriver.exe' in the extracted folder.
   - Copy the path to the 'chromedriver.exe'.
   - Replace the following line in the 'zetamac_autosolver.py' code:
      driver_path = "C:\\Users\\Anurag Baundwal\\Downloads\\chromedriver_win32\\chromedriver.exe"  # line 16
   - Run the script using 'python zetamac_autosolver.py'.

2. solver.js

   A fast JavaScript script that runs directly in the browser and scores around 7000 problems in 120 seconds.

   Usage:
   1. Open Zetamac in your browser and click "Start".
   2. Open Chrome DevTools (Ctrl + Shift + J).
   3. Paste the JavaScript code from 'solver.js' into the console and hit Enter.

3. solver-v2.js

   A faster version of 'solver.js' that solves around 20,000 problems in 120 seconds. Follow the same usage instructions as 'solver.js'.

4. solver_dragon.py

   A Python script with similar functionality to 'solver-v2.js', but can be run from the terminal. Requires the same setup as 'zetamac_autosolver.py'. Usage is the same as for 'zetamac_autosolver.py'.