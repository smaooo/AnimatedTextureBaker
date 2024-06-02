import bpy
from bpy.types import Operator
from pathlib import Path

class AnimatedTextureBaker_OT_bake(Operator):
    bl_idname = "animated_texture_baker.bake"
    bl_label = "Bake"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object

        baked_image = bpy.data.images.new(name="BakedNormalMap", width=context.scene.animated_texture_baker.texture_size[0] , height=context.scene.animated_texture_baker.texture_size[0])

        if not obj.data.uv_layers:
            raise ValueError(f"Object '{obj.name}' has no UV map")
        
        # Create a temporary material with an image texture
        material = obj.data.materials[0]

        bsdf_node = material.node_tree.nodes.get("Principled BSDF")
        texture_node = material.node_tree.nodes.new('ShaderNodeTexImage')
        texture_node.image = baked_image
        texture_node.image.colorspace_settings.name = "Non-Color"
        material.node_tree.nodes.active = texture_node


        bake_type = context.scene.animated_texture_baker.bake_type
        
        bpy.context.scene.render.engine = 'CYCLES'

        bpy.context.scene.render.bake.use_pass_direct = context.scene.animated_texture_baker.direct_light_contrib
        bpy.context.scene.render.bake.use_pass_indirect = context.scene.animated_texture_baker.indirect_light_contrib
        bpy.context.scene.render.bake.use_pass_color = context.scene.animated_texture_baker.color_contrib

        bpy.context.scene.render.bake.use_selected_to_active = False
        bpy.context.scene.render.bake.target = "IMAGE_TEXTURES"
        bpy.context.scene.render.bake.use_clear = True

        bpy.context.scene.cycles.bake_type = bake_type

        # Frame range
        start_frame = bpy.context.scene.frame_start
        end_frame = bpy.context.scene.frame_end

        output_dir = context.scene.animated_texture_baker.output_path
        image_prefix = context.scene.animated_texture_baker.image_prefix

        # Bake frame by frame
        for frame in range(start_frame, end_frame + 1):
            bpy.context.scene.frame_set(frame)
            baked_image.filepath_raw = f"{output_dir}/{image_prefix}{frame:04d}.png"
            bpy.ops.object.bake(type=bake_type)
            baked_image.save()

        material.node_tree.nodes.remove(texture_node)
        bpy.data.images.remove(baked_image) 

        return {'FINISHED'}
    
    @classmethod    
    def poll(cls, context):
        return context.scene.animated_texture_baker.output_path != ""
    
    def modal(self, context, event):
        if event.type == 'ESC':
            return {'CANCELLED'}
        
        return {'PASS_THROUGH'}
    
def register():
    bpy.utils.register_class(AnimatedTextureBaker_OT_bake)

def unregister():
    bpy.utils.unregister_class(AnimatedTextureBaker_OT_bake)

if __name__ == "__main__":
    register()