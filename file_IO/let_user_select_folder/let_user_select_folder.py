

def setup():
    # call-back based folder selection
    select_folder("Select a folder to process:", "folderSelected")
    background(0)


def draw():
    ellipse(50, 50, frame_count, frame_count)


def folder_selected(selection):
    """will be executed after user interacts with selection window"""
    from os import listdir
    from os.path import isfile, join
    if selection is None:
        print("Window was closed or the user hit cancel.")
    else:
        path = selection.get_absolute_path()
        print("User selected " + path)
        print("-----------------------------------------")
        for f in listdir(path):
            if isfile(join(path, f)):
                print(f)
