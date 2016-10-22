import sys

class Renderer(object):
    pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        map_path = sys.argv[1]
    else:
        print("Usage: mix run | python renderer.py MAP_PATH")

    for line in sys.stdin:
        print(line)
