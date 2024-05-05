"""
Command-line interface for Caffeine
"""
import argparse
from caffeine import caffeine


# TODO: add version argument, add hotcorners argument
def main():
    parser = argparse.ArgumentParser(
        prog='Caffeine',
        description='Command-line tool for keeping your computer awake',
        epilog="""
            Terminate at any time by pressing any key
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
    parser.add_argument(
        '-c', '--hotcorners',
        default=False,
        action='store_true',
        help='duration you want the program to run (0 runs indefinitely) [default=0]',
    )
    args = parser.parse_args()

    caffeine(args.time, args.hotcorners)


if __name__ == '__main__':
    main()
