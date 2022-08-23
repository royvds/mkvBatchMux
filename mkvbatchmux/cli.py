"""
The command-line interface for mkvBatchMux
"""
import os
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
            if (len(lines) == 0 and line != "[") or line == "]":
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
    parser.add_argument('-o', '--output',
                        help='''Output format string. %%F0 = filename of 1st given input file,
                %%I2+1 = index of file in directory with minimum of 2 digits and offset +1''')
    args = parser.parse_args()

    if args.attachments_folder and not os.path.isdir(args.attachments_folder):
        raise argparse.ArgumentTypeError(
            "--attachments-folder must be a valid directory")

    toolnix_options = None
    while not toolnix_options:
        toolnix_options = read_mktvoolnix_options()

    batch_muxer = BatchMuxer(
        toolnix_options, args.output) if args.output else BatchMuxer(toolnix_options)
    if args.attachments_folder:
        batch_muxer.load_attachments_per_folder(args.attachments_folder)

    batch_muxer.mux()


if __name__ == "__main__":
    main()
