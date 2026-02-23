import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=2)
body = bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.4, location=(0,0,1.5))
head = bpy.context.object

mat = bpy.data.materials.new(name="Chrome")
mat.use_nodes = True
nodes = mat.node_tree.nodes
principled = nodes.get("Principled BSDF")
principled.inputs["Metallic"].default_value = 1.0
principled.inputs["Roughness"].default_value = 0.05

body.data.materials.append(mat)
head.data.materials.append(mat)

bpy.ops.export_scene.gltf(filepath="static/models/robot.glb", export_format='GLB')