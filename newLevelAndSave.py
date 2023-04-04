import unreal

def spawn_actor(actor_class, actor_name, location, rotation):
    return unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, rotation)

editorLevelLibrary = unreal.EditorLevelLibrary
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# Initialize new level
newMap = "mainMap"

# Create new level
mainMap = levelSubSys.new_level("/Game/Maps/" + newMap + ".umap")


# Set level as the current level
levelSubSys.set_current_level_by_name(newMap)

# Create a SkyLight
sky_light = spawn_actor(unreal.SkyLight.static_class(), "SkyLight", unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))

# Create a DirectionalLight
directional_light = spawn_actor(unreal.DirectionalLight.static_class(), "DirectionalLight", unreal.Vector(0, 0, 300), unreal.Rotator(-45, 45, 0))

# Create a SkyAtmosphere
sky_atmosphere = spawn_actor(unreal.SkyAtmosphere.static_class(), "SkyAtmosphere", unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))


# Create an ExponentialHeightFog
fog = spawn_actor(unreal.ExponentialHeightFog.static_class(), "ExponentialHeightFog", unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))

# Create a PostProcessVolume
post_process_volume = spawn_actor(unreal.PostProcessVolume.static_class(), "PostProcessVolume", unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))


# Save level
levelSubSys.save_current_level()

