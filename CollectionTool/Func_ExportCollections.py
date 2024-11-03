import bpy

def export_collections():
    active_collection = bpy.context.collection
    for sub_collection in active_collection.children:
        sub_collection_name = sub_collection.name

        if not sub_collection.hide_viewport:
            
            #select all objects that are visible
            for obj in sub_collection.objects:
                if obj.visible_get():
                    obj.select_set(True)
                    
            #Check if objectes selected
            selected_objects = [obj for obj in bpy.context.selected_objects]
        
            if selected_objects:
                # Construct the export file path with the collection name
                file_path = bpy.path.abspath("//") + sub_collection_name + ".fbx"
                
                # Export selected objects as FBX
                bpy.ops.export_scene.fbx(
                    filepath=file_path,
                    use_selection=True,
                    global_scale=1.0,
                    axis_forward='-Z',
                    axis_up='Y',
                    object_types={'MESH'},
                    use_mesh_modifiers=True,
                    add_leaf_bones=False,
                )
            
            # Deselect all objects after exporting
            bpy.ops.object.select_all(action='DESELECT')
    print("Done Exporting")
