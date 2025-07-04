import genesis as gs
import numpy as np

scene = gs.Scene()
scene.set_background((0.0, 0.0, 0.0))  

planet = scene.add_entity(
    gs.Sphere(radius=1.0),
    material=gs.Rigid(diffuse=(0.0, 0.5, 1.0))
)
marker = scene.add_entity(
    gs.Box(width=0.1, height=0.1, depth=0.2),
    material=gs.Rigid(diffuse=(1.0, 1.0, 1.0)),
)
marker.set_position((1.0, 0.0, 0.0))  

angle = 0.0
while scene.update():
    angle += 0.05
    rotation_matrix = gs.rotation_matrix(axis=(0, 1, 0), angle=angle)
    marker.set_transform(rotation_matrix @ gs.translation_matrix((1.0, 0, 0)))

