import argparse
from .server import Server


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-t', '--terminal',
        choices=['xterm', 'xfce4-terminal'],
        default=None,
        help='Start SiriDB servers in a terminal. If no terminal is given '
        'process put their output in log files.')

    parser.add_argument(
        '-m', '--mem-check',
        action='store_true',
        help='Use `valgrind` for memory errors and leaks.')

    parser.add_argument(
        '-k', '--keep',
        action='store_true',
        help='Only valid when a terminal is used. This will keep the terminal '
        'open.')

    parser.add_argument(
        '-b', '--build',
        choices=['Release', 'Debug'],
        default='Release',
        help='Choose either the Release or Debug build.')

    parser.add_argument(
        '-l', '--log-level',
        default='critical',
        help='set the log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'])

    args = parser.parse_args()

    Server.MEM_CHECK = args.mem_check
    Server.HOLD_TERM = args.keep
    Server.TERMINAL = args.terminal
    Server.BUILDTYPE = args.build
    Server.LOG_LEVEL = args.log_level.upper()
