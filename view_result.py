import os
import numpy as np
import open3d as o3d
from typing import Union
from copy import deepcopy

x_pts_file_path = './output/test1_x.txt'
y_pts_file_path = './output/test1_y.txt'

def loadTXT(txt_file_path: str) -> Union[np.ndarray, None]:
    if not os.path.exists(txt_file_path):
        print('[ERROR][view_result::loadTXT]')
        print('\t txt file not exist!')
        print('\t txt_file_path:', txt_file_path)
        return None

    with open(txt_file_path, 'r') as f:
        lines = f.readlines()

    points_list = []

    for line in lines:
        if ' ' in line or '\t' in line:
            point = line.split('\n')[0].split()
        elif ',' in line:
            point = line.split('\n')[0].split(',')
        else:
            print('[ERROR][view_result::loadTXT]')
            print('\t extract point from line failed!')
            print('\t line:', line)
            return None

        points_list.append(point)

    points_array = np.asarray(points_list, dtype=np.float64)

    return points_array

def toPointCloud(points: np.ndarray) -> o3d.geometry.PointCloud:
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd

def loadPcdFromTXT(txt_file_path: str) -> Union[o3d.geometry.PointCloud, None]:
    points = loadTXT(txt_file_path)

    if points is None:
        print('[ERROR][view_result::loadPcdFromTXT]')
        print('\t loadTXT failed!')
        return None

    pcd = toPointCloud(points)

    return pcd

def toDeformLineSet(pts: np.ndarray, vector: np.ndarray) -> o3d.geometry.LineSet:
    N = pts.shape[0]
    points = np.vstack([pts, pts + vector])
    lines = [[i, i + N] for i in range(N)]
    colors = [[1, 0, 0] for _ in range(N)]

    line_set = o3d.geometry.LineSet()
    line_set.points = o3d.utility.Vector3dVector(points)
    line_set.lines = o3d.utility.Vector2iVector(lines)
    line_set.colors = o3d.utility.Vector3dVector(colors)

    return line_set

x_pcd = loadPcdFromTXT(x_pts_file_path)
y_pcd = loadPcdFromTXT(y_pts_file_path)
assert x_pcd is not None
assert y_pcd is not None

y_pcd.translate([1, 0, 0])

deform_vectors = loadTXT('./output/test1_v.txt')
assert deform_vectors is not None

print(np.linalg.norm(deform_vectors))
print(np.max(deform_vectors))
print(np.mean(deform_vectors))
print(np.min(deform_vectors))

lineset = toDeformLineSet(np.asarray(x_pcd.points), deform_vectors)

o3d.visualization.draw_geometries([x_pcd, y_pcd, lineset])
