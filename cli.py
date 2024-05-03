"""
Command-line interface for Caffeine
"""
import argparse
from caffeine import caffeine


# TODO: add version argument
def main():
    parser = argparse.ArgumentParser(
        prog='Caffeine',
        description='Command-line tool for keeping your computer awake',
        epilog="""
            Terminate at any time by moving the mouse to the top left of the screen
            or pressing escape key
        """
    )
    parser.add_argument(
        '-t', '--time',
        default=0,
        type=int,
        choices=range(0, 86400),
        help='duration you want the program to run (0 runs indefinitely) [default=0]',
        metavar='[0-86400]'
    )
    args = parser.parse_args()

    # TODO: move try catch to caffeine when converted to class
    try:
        caffeine(args.time)
    except KeyboardInterrupt:
        print('killed by term')
        quit()



if __name__ == '__main__':
    main()
