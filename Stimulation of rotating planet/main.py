import genesis as gs
import numpy as np

scene = gs.Scene() 

planet = scene.add_entity(
    gs.morphs.Sphere(radius=1.0)
)

cam = scene.add_camera(
    res=(320, 240),
    pos=(3.5, 2.0, 2.5),
    lookat=(0, 0, 0),
    fov=30
)

scene.build()
for i in range(1000):  
    scene.step() 

