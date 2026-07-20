# TODO: Implement more efficient monotonic heuristic
#
# Every function receive coordinates of two grid points returns estimated distance between them.
# Each argument is a tuple of two or three integer coordinates.
# See file task.md for description of all grids.

import math
from graphs import Grid2D, GridDiagonal2D, GridGreatKing2D, GridRook2D, GridJumper2D, Grid3D, GridFaceDiagonal3D, GridAllDiagonal3D

# For two points a and b in the n-dimensional space, return the d-dimensional point r such that r_i = | a_i - b_i | for i = 1...d
def distance_in_each_coordinate(x, y):
    return [ abs(a-b) for (a,b) in zip(x, y) ]

# Manhattan Distance
def grid_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return dx + dy

# Move along horizontal, vertical and the diagonal. Fix 2 coordinates in a move
def grid_diagonal_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return max(dx, dy)

# move along x y z one coordinate per move
def grid_3D_heuristic(current, destination):
    dx, dy, dz = distance_in_each_coordinate(current, destination)
    return dx + dy + dz

# move along axis, face diagonal, space diagonal, reduce all
def grid_face_diagonal_3D_heuristic(current, destination):
    dx, dy, dz = distance_in_each_coordinate(current, destination)
    return max(dx, dy, dz, (dx + dy + dz + 1) // 2)

# oaxis face digaonal, max 2 coordinates can be fixed not more
def grid_all_diagonal_3D_heuristic(current, destination):
    dx, dy, dz = distance_in_each_coordinate(current, destination)
    return max(dx, dy, dz)

# Move up to 8 squares in x and y 
def grid_great_king_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return max((dx + 7) // 8, (dy + 7) // 8)

# 8 cells to move in one dir. Not diagonal, dont consider them
def grid_rook_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return (dx + 7) // 8 + (dy + 7) // 8

# (3,2), (2,3) 
def grid_jumper_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    if dx < dy:
        dx, dy = dy, dx
    base = max((dx + 2) // 3, (dx + dy + 4) // 5)
    if base % 2 != (dx + dy) % 2:
        base += 1
    return base
