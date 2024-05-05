"""
Command-line interface for Caffeine
"""
import argparse
from caffeine import caffeine


# TODO: add version argument
def main():
    parser = argparse.ArgumentParser(
        prog='Caffeine',
        conflict_handler='resolve',
        description='Command-line tool for keeping your computer awake',
        epilog="""
            Terminate at any time by pressing any key
        """
    )
    runtime_group = parser.add_mutually_exclusive_group()
    runtime_group.add_argument(
        'runtime',
        nargs='?',
        default=0,
        type=int,
        choices=range(0, 86400),
        help='duration you want the program to run (0 runs indefinitely) [default=0]',
        metavar='[0-86400]'
    )
    runtime_group.add_argument(
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
        help='Prevents mouse from reaching corners of display',
    )
    args = parser.parse_args()

    runtime = args.time if args.runtime == 0 and args.time != 0 else args.runtime

    caffeine(runtime, args.hotcorners)


if __name__ == '__main__':
    main()
