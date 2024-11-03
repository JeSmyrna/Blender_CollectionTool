# Blender_CollectionTool
A small Blender Addon, for managing and exporting collections

Brief Description on which button does what:

Create Collections:
    - It looks at the active collection
    - goes through all the models in the collection (if models available)
    - creates new sub collections under active collections, with the name of the model
    - makes model a child of new sub collection

Export Collections:
    - It looks at the active collection
    - goes through all sub (visible) collections
    - selects all (visible) models
    - export selected models with the name of the sub collection
    - deselects models and goes to the next sub collection, till the end

Export Settings:
    setting are currently hardcoded for Unity fbx
    