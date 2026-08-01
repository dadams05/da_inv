"""
A script that will scan a directory and its subdirectories and delete files with any keyword(s) in their names.
"""

import os
import argparse

DIR: str = r"."
# KEYWORDS_TO_MATCH: list = [
#     "import", "xml", "appeal", "bite", "bow", "carefulwalk", "charge", "chop", "credits", 
#     "cringe", "cry", "dance", "deepbreath", "digin", "digout", "double", 
#     "eat", "emit", "eventsleep", "faint", "flaparound", "float", "gas", 
#     "head", "hitground", "hop", "hover", "hurt", "injured", "jab", "jump", 
#     "kick", "laying", "leapforth", "lick", "lookup", "lostbalance",
#     "multiscratch", "nod", "offsets", "pain", "pose", "pull", "punch", 
#     "quickstrike", "raisearms", "rearup", "ricochet", "roar", "rotate",
#     "rumble", "scratch", "shadow", "shake", "shock", "shoot", "sing", 
#     "sink", "sit", "slam", "slap", "slice", "spattack", "special", "stomp", 
#     "standingup", "strike", "swell", "swing", "tailwhip", "trip", "tumble", 
#     "twirl", "uppercut", "wake", "wave", "wiggle", "withdraw", "yawn",
# ]
KEYWORDS_TO_MATCH = [".tar"]


def delete_files_by_keyword(target_directory: str = DIR, keywords: list = KEYWORDS_TO_MATCH, dry_run: bool = True) -> None:
    """Loops through a directory and its subdirectories, deleting files that contain any of the specified keywords in their filenames."""
    keywords = [kw.lower() for kw in keywords]

    deleted_count = 0
    skipped_count = 0

    print(f"Scanning: {target_directory}")
    print(f"Keywords: {keywords}")
    print(f"Dry Run Mode: {dry_run}\n" + "-" * 40)

    # os.walk loops through the folder, all subfolders, and all files
    for root, _, files in os.walk(target_directory):
        for file in files:
            file_lower = file.lower()

            if any(keyword in file_lower for keyword in keywords):
                full_path = os.path.join(root, file)

                if dry_run:
                    print(f"[WOULD DELETE] {full_path}")
                    deleted_count += 1
                else:
                    try:
                        os.remove(full_path)
                        print(f"[DELETED] {full_path}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"[ERROR] Could not delete {full_path}: {e}")
                        skipped_count += 1

    print("-" * 40)
    if dry_run:
        print(f"Dry run complete. Total files that would be deleted: {deleted_count}")
        print("Set \"dry_run=False\" or use \"-r\" or \"--remove\" when you are ready to actually delete them.")
    else:
        print(f"Finished. Deleted: {deleted_count} | Errors/Skipped: {skipped_count}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a directory and its subdirectories and delete files with any keyword(s) in their names. Use -r to remove")
    parser.add_argument(
        "-r", 
        "--remove", 
        action="store_true",
        help="The script will not delete files by default. Pass this to confirm deleting the files"
    )
    parser.add_argument(
        "-d", 
        "--directory", 
        type=str, 
        help="Directory to scan through"
    )

    args = parser.parse_args()
    delete_files_by_keyword(target_directory = args.directory or DIR, keywords = KEYWORDS_TO_MATCH, dry_run = not args.remove)
