# MKVBatchMux
Batch runner of MKVToolNix mux commands.

This tool allows to run a MKVToolNix command in batch by detecting all files that are in the directory of one of the input files.

## Dependencies
-  [Python 3.9 or higher](https://www.python.org/downloads/)
-  [MKVToolNix (with mkvmerge.exe as Path variable)](https://www.fosshub.com/MKVToolNix.html)

## Usage
```console
$ mkvbatchmux --help
usage: mkvbatchmux [-h] [-af ATTACHMENTS_FOLDER] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -af ATTACHMENTS_FOLDER, --attachments-folder ATTACHMENTS_FOLDER
                        Directory path containing multiple folders with
                        attachments
  -o OUTPUT, --output OUTPUT
                        Output format string. %F0 = filename of 1st given
                        input file, %I2+1 = index of file in directory with
                        minimum of 2 digits and offset +1
```

## Roadmap
- Automatic detection of separate attachments folders per mux vs. single attachments folder for all muxes (as replacement of the  current manual --atachments-folder).
- Mux in xml chapter files
- File title in metadata (currently removes any titles present)
- Algorithm to work with inconsistently ordered tracks by detecting tracks using their name, language, etc.