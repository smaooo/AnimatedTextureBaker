import bpy

from bpy.types import Panel


class AnimatedTextureBaker_PT_UI(Panel):
    bl_label = "Animated Texture Baker"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Animated Texture Baker'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.animated_texture_baker, "output_path")
        layout.prop(context.scene.animated_texture_baker, "image_prefix")
        layout.prop(context.scene.animated_texture_baker, "bake_type")   
        layout.prop(context.scene.animated_texture_baker, "texture_size")
        layout.prop(context.scene.animated_texture_baker, "direct_light_contrib")
        layout.prop(context.scene.animated_texture_baker, "indirect_light_contrib")
        layout.prop(context.scene.animated_texture_baker, "color_contrib")

        print("UI Drawn")     

def register():
    bpy.utils.register_class(AnimatedTextureBaker_PT_UI)

def unregister():
    bpy.utils.unregister_class(AnimatedTextureBaker_PT_UI)