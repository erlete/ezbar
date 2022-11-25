# EZ Bar

A simple progress bar for loop progress measurement and time estimation.

_The original idea and base script for this repository was created by @carlospuenteg. I just decided to refactor the code and add some nice features such as remaining and elapsed time counting._

## Features

* Simple and easy to use (create a progress bar and update it)
* Colorful output so that you always see how your loop is progressing
* Estimated time of completion prediction. No need to stare at the screen for minutes!
* Elapsed time display. Know the efficiency of your loops!

https://user-images.githubusercontent.com/76848729/203904191-c975cd6f-94e9-4f93-820b-88c714252ccc.mp4

## Installation

The installation of this module is performed via the Python Package Index (PyPI).

### macOS / UNIX

```bash
python3 -m pip install ezbar
```

### Windows

```cmd
py -m pip install ezbar
```

## Usage

Just import the `ProgressBar` class and it will be ready to go!

```python
from ezbar import ProgressBar
```

## Example

```python
from time import sleep
from ezbar import ProgressBar

ITERATIONS = 100

# Use default settings:

pb = ProgressBar(ITERATIONS)

for i in range(ITERATIONS):
    sleep(0.05)
    pb.update(i)

# Or customize them all you want!

pb = ProgressBar(ITERATIONS, text="Loading...", width=30)

for i in range(ITERATIONS):
    sleep(0.05)
    pb.update(i)
```

## Disclaimer

This progress bar does not serve a performance counting purpose. It is only meant to be used for orientative loop progress measurement and time estimation. Do not use it for strict performance measurements.
