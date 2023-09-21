import pickle
import os
import fnmatch

DICTS_DIR = "./char-dicts"
FNAME_PATTERN = "*-chars-*.txt"

def find_files(directory, pattern):
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

if __name__ == "__main__":
    for fname in find_files(DICTS_DIR, FNAME_PATTERN):
        print (fname)
        with open(fname, "r") as f:
            chars = f.read()
            chars = list(chars)

        out_fname = os.path.splitext(os.path.basename(fname))[0]

        with open(os.path.join(os.path.join(DICTS_DIR, f"{out_fname}.cmap")), "wb") as f:
            pickle.dump(chars, f)

