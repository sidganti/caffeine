# Caffeine

Keeps the screen awake by moving the mouse randomly.

## Description

Caffeine is intended to be used as a cli tool or imported to another python project.

If used as a cli tool or with importing caffeine(), Caffeine will move the mouse for the specified runtime. While under the runtime the mouse will move to a random location on the screen. This process will repeat at random intervals. The movement of the mouse is achieved using the pyautogui library. Pyautogui's duration and tweening parameters allow for more natural mouse movement patterns across the screen. To terminate Caffeine, simply press any key on the keyboard.

For more granular control over the logic, the Caffeine class can be imported. The class, along with its public methods, allows for customized use cases to be implemented. An example may be to have the mouse move for an unknown duration of time that would be determined by another process.

## Installation

1. Have Python 3.12+ installed
    - [How to install](https://www.python.org/downloads/)

2. Execute the following command in your console

```console
pip install git+https://github.com/sidganti/caffeine.git
```

## Documentation

### CLI

#### Run indefinitely

```console
caffeine
```

#### Run for a specified time in seconds

Limited to one day aka 86,400 seconds.

If 0 is given as an argument then Caffeine will run indefinitely.

```console
caffeine <0-86400>
```

or

```console
caffeine -t <0-86400>
```

or

```console
caffeine --time <0-86400>
```

#### Hotcorner protection

Pass the flag to prevent triggering [hotcorners](https://support.apple.com/guide/mac-help/use-hot-corners-mchlp3000/mac) enabled on your device.

```console
caffeine -c
```

or

```console
caffeine --corners
```

#### End Caffeine manually

Press any key on the keyboard.

In case something went wrong you have two options. Use you operating systems preferred termination signal: <kbd>ctrl</kbd>+<kbd>c</kbd> on Mac/Linux or <kbd>ctrl</kbd>+<kbd>z</kbd> on Windows. Since pyautogui's failsafe option is enabled you can also drag your mouse to the top left corner of the screen to terminate.

#### Help

Provides detail on CLI's usage.

```console
caffeine -h
```

or

```console
caffeine --help
```

#### Version

Prints the version of Caffeine

```console
caffeine -v
```

or

```console
caffeine --version
```

### caffeine() function

Functions nearly identical to the CLI. The CLI is essentially a wrapper for the caffeine function.

```python
# caffeine function definition
def caffeine(runtime: int = 0, hotcorners: bool = False) -> None:
```

- runtime
    - duration the instance should run
    - if 0 is passed in to the function then caffeine will run indefinitely
- hotcorners
    - prevents mouse from reaching the edges of the screen

### Caffeine class

Encapsulates all of the data and logic required to move the mouse for a specified duration of time.

```python
# Caffeine class constructor definition
def __init__(self, runtime: int = 0, hotcorners: bool = False, animate: bool = True) -> None:
```

- runtime
    - duration the instance should run
- hotcorners
    - prevents mouse from touching the edges of the screen
- animate
    - flag to determine write to console

#### start() method

Starts logic to run Caffeine for a specified duration.

```python
# start method definition
def start(self):
```

#### run() method

Alias for the start() method

```python
# run method definition
def run(self):
```

#### move_mouse() method

Moves the mouse to a random position on the screen for a random duration. Also takes advantage of pyautogui's tweening functions to make mouse movement more natural.

```python
# move_mouse method definition
def move_mouse(self) -> None:
```

#### stop() method

Safely terminates Caffeine instance

```python
# stop method definition
def stop(self) -> None:
```

## License

[LICENSE](LICENSE)