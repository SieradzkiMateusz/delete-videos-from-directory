import os
import sys
from argparse import ArgumentParser

#----------------------------------------------------------------------------

def main():
    parser = ArgumentParser(description="Remove videos and gifs from directory.")
    parser.add_argument("dir", help="Directory path")

    args = parser.parse_args()

    imageDirectory = args.dir

    #file extentions to remove
    ext = (".gif", ".webm", ".mp4", ".flv", ".avi", ".mov", ".mpg",
             ".mpeg", ".wmv", ".asf", ".3g2", ".3gp", ".m2ts", ".mkv")

    fileCounter = 0
    if os.path.exists(imageDirectory):
        for root, dirs, files in os.walk(imageDirectory):
            for File in files:
                if File.endswith(ext):
                    os.remove(os.path.join(imageDirectory, File))
                    fileCounter += 1

        
        print("Operation successful")
        print("Removed {} files.".format(fileCounter))
    else:
        print("Directory not found.")
        sys.exit(1)

#----------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------