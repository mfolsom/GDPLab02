import unreal

editorLevelLibrary = unreal.EditorLevelLibrary
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# Initialize new level
newLevel = "mainLevel"

# Create new level
mainLevel = levelSubSys.new_level("/Game/Maps/mainLevel.umap")

# Set level as the current level
levelSubSys.set_current_level_by_name(newLevel)

# Save level
levelSubSys.save_current_level()
