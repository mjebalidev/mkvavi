#!/usr/bin/python

import sys, getopt, subprocess

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('conv.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('conv.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    command = f"ffmpeg -i {inputfile} -f avi -c:v mpeg4 -b:v 4000k -c:a libmp3lame -b:a 320k -y {outputfile}"
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
   main(sys.argv[1:])

