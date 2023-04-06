import unreal

#Access the current level
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()

# Spawn DirectionalLight actor
dir_light = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.DirectionalLight, unreal.Vector(0, 0, 300), unreal.Rotator(0, 0, 0)
)

# Access the DirectionalLightComponent and set intensity
dirLightComp = unreal.DirectionalLightComponent()
dirLightComp.set_intensity(new_intensity=20.0)





