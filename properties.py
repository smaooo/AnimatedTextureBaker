import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty
class AnimatedTextureBakerProperties(PropertyGroup):
    output_path: StringProperty(name="Output Path", default="", subtype='DIR_PATH')
    image_prefix: StringProperty(name="Image Prefix", default="baked_image")
    bake_type: bpy.props.EnumProperty(
        name="Bake Type",
        items=[
            ("DIFFUSE", "Diffuse", "Bake Diffuse Color"),
            ("EMISSION", "Emission", "Bake Emission Color"),
            ("NORMAL", "Normal", "Bake Normal Map"),
            ("ROUGHNESS", "Roughness", "Bake Roughness Map"),
            ("METALLIC", "Metallic", "Bake Metallic Map"),
            ("AO", "Ambient Occlusion", "Bake Ambient Occlusion Map"),
            ("ALPHA", "Alpha", "Bake Alpha Map"),
            ("SPECULAR", "Specular", "Bake Specular Map"),
            ("TRANSMISSION", "Transmission", "Bake Transmission Map")]
    )   
    texture_size: bpy.props.IntVectorProperty(
        name="Texture Size",
        default=(1024, 1024),
        subtype='XYZ',
        size=2
    )

    direct_light_contrib: bpy.props.BoolProperty(
        name="Direct Light Contribution",
        default=False
    )

    indirect_light_contrib: bpy.props.BoolProperty(
        name="Indirect Light Contribution",
        default=False
    )

    color_contrib: bpy.props.BoolProperty(
        name="Color Contribution",
        default=True
    )


def register():
    bpy.utils.register_class(AnimatedTextureBakerProperties)
    bpy.types.Scene.animated_texture_baker = bpy.props.PointerProperty(type=AnimatedTextureBakerProperties)

def unregister():
    bpy.utils.unregister_class(AnimatedTextureBakerProperties)
    del bpy.types.Scene.animated_texture_baker