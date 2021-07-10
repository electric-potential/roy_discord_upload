import os

def decompress(fname, path_to_file="./", path_to_write="./", max_bytes=7999999):
    num = 0
    try:
        with open(path_to_file+fname, "rb") as f:
            r = f.read(max_bytes)
            while len(r) != 0:
                num += 1
                with open(path_to_write+fname+"."+str(num)+".rdu", "wb") as g:
                    g.write(r)
                r = f.read(max_bytes)
    except Exception as e:
        for i in range(1, num+1):
            try:
                os.remove(path_to_write+fname+"."+str(num)+".rdu")
            except Exception:
                pass
        raise e
    return

def recombine(fname, path_to_files="./", path_to_write="./", *_):
    num = 1
    try:
        with open(path_to_write+fname, "wb") as f:
            while os.path.isfile(path_to_files+fname+"."+str(num)+".rdu"):
                with open(path_to_files+fname+"."+str(num)+".rdu", "rb") as g:
                    f.write(g.read())
                num += 1
    except Exception as e:
        try:
            os.remove(path_to_write+fname)
        except Exception:
            pass
        raise e
    return

if __name__ == "__main__":
    import sys
    import getopt
    try:
        funcs = {"decompress": decompress, "recombine": recombine}
        opts, args = getopt.getopt(sys.argv[1:], "hi:r:w:b:")
        f = args[0]
        i = args[1]
        r = None
        w = None
        b = None
        for opt, arg in opts:
            if opt == "-h":
                print("usage: rdu.py -i <path to read file(s)> -w <path to write file(s)> -b <max decompress filesize bytes> <mode (either decompress or recombine)> <filename>")
                sys.exit()
            elif opt == "-r":
                r = arg
            elif opt == "-w":
                w = arg
            elif opt == "-b":
                b = arg
        funcs[f](i, r if r is not None else "./", w if w is not None else "./", int(b) if b is not None else 7999999)
        sys.exit(0)
    except Exception as e:
        print("usage: rdu.py -i <path to read file(s)> -w <path to write file(s)> -b <max decompress filesize bytes> <mode (either decompress or recombine)> <filename>")
        print("")
        raise e
        sys.exit(2)
