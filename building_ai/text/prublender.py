import bpy

verts = [(-1,  1,   0),
         ( 1,  1,   0),
         ( 2, -3,   0),
         (-2, -1,   0),
         (-1,  1.5, 1),
         ( 1,  1.5, 1),
        ]

# faces are a list of indices to each vertex from the above list
faces = [[0, 1, 2, 3], [0, 1, 5, 4]]

mesh = bpy.data.meshes.new(name="New Mesh")
mesh.from_pydata(verts, [], faces)
obj = bpy.data.objects.new('New object', mesh)
bpy.context.collection.objects.link(obj)