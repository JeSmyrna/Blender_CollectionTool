import bpy, os, sys
from bpy.props import *
from bpy.utils import unregister_class, register_class
from bpy.types import Panel, Operator, Menu

from . import Func_MakeSubCollection, Func_ExportCollections

bl_info = {
    "name" : "Collection_Tool",
    "author" : "Spark3dvision, Gwynn Schoeppler",
    "version" : (0, 1),
    "blender" : (3, 60, 1),
    "location" : "View3D > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Import-Export",
    "description" : "Tool for managing Collections: Create Sub Collections with OBJ Name, Export Sub Collections with Collection Name",
}

class Create_Collection(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Create Collections"

    def execute(self, context):
        Func_MakeSubCollection.make_new_collection()
        return {"FINISHED"}
    
class Export_Collections(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator_b"
    bl_label = "Export Collections"

    def execute(self, context):
       Func_ExportCollections.export_collections()
       return {"FINISHED"}

# UI in 3D Viewport
class Collection_Tool(bpy.types.Panel):
    
    bl_label = "Collection_Tool"
    bl_idname = "CollectionTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Collection_Tool"
    bl_context_mode = "OBJECT"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text = "Make Collection")
        row = layout.row()
        row.operator(Create_Collection.bl_idname)

        row = layout.row()
        row.label(text = "Export Collection")
        row = layout.row()
        row.operator(Export_Collections.bl_idname)

def draw_item(self, context):
    layout = self.layout
    layout.menu(Collection_Tool.bl_idname)

classes = [Collection_Tool, Create_Collection, Export_Collections]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.utils.register_class(Collection_Tool)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    #bpy.utils.unregister_class(Collection_Tool)

if __name__ == "__main__":
    register()
