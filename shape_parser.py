import re

FACE_LIST_PATTERN = '{(.*?})}'
FACE_POINT_TUPLE_PATTERN = '"v.":{".":(.*?),".":(.*?)}'

POINT_LIST_PATTERN = '{"vertices":\[(.*?)]}'
PATH_POINT_TUPLE_PATTERN = '{".":(.*?),".":(.*?)}'


def parse_map(map_data):
    faces_data = re.findall(FACE_LIST_PATTERN, map_data)
    faces = [[(float(x), float(y)) for y, x in re.findall(FACE_POINT_TUPLE_PATTERN, face_data)] for face_data in faces_data]
    return faces


def parse_path(path_data):
    points_data = re.findall(POINT_LIST_PATTERN, map_data)
    point_strings = re.findall(POINT_TUPLE_PATTERN, points_data)
    points = [(float(x), float(y)) for y, x in point_strings]
    return points
