"""
The command-line interface for mkvBatchMux
"""
import os
import sys
import json
import argparse
from .mkvbatchmux import BatchMuxer


def read_mktvoolnix_options():
    """ Function to read MKVToolNix json input, since these are multi-line. """
    print("Paste MKVToolNix option files (JSON-formatted)")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
            if (len(lines) == 1 and line != "[") or line == "]":
                break
        else:
            break
    try:
        return json.loads('\n'.join(lines))
    except json.decoder.JSONDecodeError:
        print("Invalid json input, please try again.")
        return None


def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument('-af', '--attachments-folder',
                        help='Directory path containing multiple folders with attachments')
    parser.add_argument('-s', '--skip', default=0,
                        help='Skip the first X number of files, handy if you had to \
                            interrupt a previous mux and want to continue it')
    parser.add_argument('-o', '--output', default=None,
                        help='''Output format string. %%F0 = filename of 1st given input file,
                %%I2+1 = index of file in directory with minimum of 2 digits and offset +1''')
    args = parser.parse_args()

    if args.attachments_folder and not os.path.isdir(args.attachments_folder):
        raise argparse.ArgumentTypeError(
            "--attachments-folder must be a valid directory")

    toolnix_options = None
    while not toolnix_options:
        toolnix_options = read_mktvoolnix_options()

    try:
        batch_muxer = BatchMuxer(toolnix_options, args.output, int(args.skip))
    except ValueError:
        sys.exit("Skip argument must be an integer")

    if args.attachments_folder:
        batch_muxer.load_attachments_per_folder(args.attachments_folder)

    batch_muxer.mux()


if __name__ == "__main__":
    main()
