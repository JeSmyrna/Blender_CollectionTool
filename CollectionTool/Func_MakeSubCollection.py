import bpy

def make_new_collection():
    # Get the active collection
    active_collection = bpy.context.collection

    if active_collection is not None:
        print(f"Active Collection: {active_collection.name}")
        # Check if Collection has objects
        if len(active_collection.objects) <= 0:
            print("nothing to do")
        else:
            #get object, make new collection with object name, make object child of new subcollection
            for col in active_collection.objects:
                print(f"Make new Collection for {col.name}")
                new_collection = bpy.data.collections.new(col.name)
                active_collection.children.link(new_collection)
                new_collection.objects.link(col)
                active_collection.objects.unlink(col)
        print("Finished")
    else:
        print("No active collection selected.")