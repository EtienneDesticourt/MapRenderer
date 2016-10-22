import sys
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from shape_parser import parse_map, parse_path, get_extreme_pos, reset_origin

FRAME_SIZE = (10000, 10000)


class Renderer(object):

    def __init__(self, map_file, frame_size=FRAME_SIZE):
        self.frame_size = frame_size
        self.frame = None
        self.figure = plt.figure()

        # Parse map
        with open(map_file, "r") as f:
            map_data = f.read()
        self.map_polygons = parse_map(map_data)
        self.map_polygons = reset_origin(self.map_polygons)
        self.frame_size = get_extreme_pos(self.map_polygons, max)

        # Render map
        self.draw_map(self.map_polygons)
        self.image = plt.imshow(self.frame)

    def draw_path(self, path):
        if len(path) < 2:
            return
        draw = ImageDraw.Draw(self.frame)
        draw.line(path, fill=0, outline=(255, 0, 0))

    def draw_map(self, map_polygons):
        self.frame = Image.new("RGB", self.frame_size)
        draw = ImageDraw.Draw(self.frame)
        for polygon in map_polygons:
            try:
                draw.polygon(polygon, fill=0, outline=(0, 255, 0))
            except:
                print(polygon)

    def render(self, path):
        self.draw_map(self.map_polygons)
        self.draw_path(path)
        self.image.set_data(self.frame)
        self.figure.canvas.draw()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        map_path = sys.argv[1]
    else:
        print("Usage: mix run | python renderer.py MAP_PATH")

    renderer = Renderer(map_path)
    renderer.render([])
    plt.show()
    sys.exit(0)
    for line in sys.stdin:
        print(line)
        data = line.split("[debug] ")
        if len(data) < 2:
            continue

        path_data = data[1]
        path = parse_path(path_data)
        renderer.render(path)
