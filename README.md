# Progress Bar

A simple progress bar for loop progress measurement and time estimation.

## Features+

* Simple and easy to use (create a progress bar and update it)
* Colorful output so that you always see how your loop is progressing
* Estimated time of completion prediction. No need to stare at the screen for minutes!
* Elapsed time display. Know the efficiency of your loops!

## Installation

### macOS / UNIX

```bash
# Clone the repository:
git clone https://github.com/erlete/progress-bar

# Copy the `progress-bar.py` file to your project folder:
cp progress-bar/progress-bar.py path/to/your/project/folder
```

## Usage

Just import the `ProgressBar` class and it will be ready to go!

```python
from progress_bar import ProgressBar
```

## Example

```python
from time import sleep
from progress_bar import ProgressBar

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
