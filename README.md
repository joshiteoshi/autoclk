## AUTOCLK: A GARBAGE MACRO
Why are you here? There are much better autoclicker macros out there. I literally wrote this at work out of boredom to ineffectively cheat at Cookie Clicker.

Really? You actually want to know how to use this? Ok then. Just know I'm not editing or fixing this script unless it is for myself.

### How to use this script

1. This script was written in Python 3.9. You can use the standard CPython interpreter found [here](https://www.python.org/downloads/).
    - The script might work on earlier or later versions of Python but I'm not checking
    - Again, I literally am writing this on a work computer 
2. You will also need `pynput`. You can do this using
    ```
    pip install pynput
    ````
3. Clone this repository or just download the `clkmacro.py` file
4. From the directory you downloaded `clkmacro.py` to, run the auto clicker using
    ```
    python3 clkmacro.py
    ```
    - If this doesn't work, try `py clkmacro.py` or `python clkmacro.py`
    - Windows likes to be funny with python aliases
5. Use ``<Ctrl> + ` `` to toggle the auto clicker on or off

### Other features

1. You can adjust the click rate of the autoclicker at run time using
    ```
    python3 clkmacro.py [clicks per second]
    ```
3. The toggle macro for the autoclicker can be used anywhere; even outside the terminal window thanks to pynput magic
4. `<Ctrl> + c` kills the program from terminal, like it does most other programs
