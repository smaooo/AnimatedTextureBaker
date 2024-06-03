import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty
class AnimatedTextureBakerProperties(PropertyGroup):
    output_path: StringProperty(name="Output Path", default="", subtype='DIR_PATH')
    image_prefix: StringProperty(name="Image Prefix", default="baked_image")
    bake_type: bpy.props.EnumProperty(
        name="Bake Type",
        items=[
            ("COMBINED", "Combined", "Combined"),
            ("AO", "Ambient Occlusion", "Ambient Occlusion"),
            ("SHADOW", "Shadow", "Shadow"),
            ("POSITION", "Position", "Position"),
            ("NORMAL", "Normal", "Normal"),
            ("UV", "UV", "UV"),
            ("ROUGHNESS", "Roughness", "Roughness"),
            ("EMIT", "Emission", "Emission"),
            ("ENVIRONMENT", "Environment", "Environment"),
            ("DIFFUSE", "Diffuse", "Diffuse"),
            ("GLOSSY", "Glossy", "Glossy"),
            ("TRANSMISSION", "Transmission", "Transmission")
        ]
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