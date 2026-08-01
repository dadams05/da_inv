"""
A script that will scan a directory and its subdirectories and return a list of all unique filenames found.
"""

import os
import argparse

DIR: str = r"."
PRINT_TO_CONSOLE: bool = True
SAVE_TO_FILE: bool = False
FILE_PATH: str = "./unique_names.txt"


def get_unique_filenames(target_directory: str = DIR, case_insensitive: bool = True) -> set:
    """Scans a directory and all subdirectories, returning a set of all unique filenames found. """
    unique_files = set()
    total_files_scanned = 0

    print(f"Scanning: {target_directory}\n" + "-" * 40)

    # os.walk recursively visits every folder and subfolder
    for _, _, files in os.walk(target_directory):
        for file in files:
            total_files_scanned += 1
            if case_insensitive:
                unique_files.add(file.lower())
            else:
                unique_files.add(file)

    print(f"Scan complete")
    print(f"Total file instances checked: {total_files_scanned}")
    print(f"Total unique filenames found: {len(unique_files)}")
    print("-" * 40)

    return unique_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a directory and its subdirectories and return a list of all unique filenames found")
    parser.add_argument(
        "-d", 
        "--directory", 
        type=str, 
        help="Directory to scan through"
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store_true",
        help="Store results in output file \"unique_names.txt\""
    )

    args = parser.parse_args()
    unique_names = get_unique_filenames(args.directory or DIR, case_insensitive=True)

    print("Unique Filenames Found:")
    for name in sorted(unique_names):
        print(f"- {name}")

    if args.output:
        with open(FILE_PATH, "w") as f:
            for name in sorted(unique_names):
                f.write(name + "\n")
