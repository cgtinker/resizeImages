from methods import DesignatedOutput, Pathing, ResizeImages

# manual set a path to a folder containing images or to an image file
# manual set the output types / slugs (either for 3d textures or app icon sets)

manual_set_path = "/Users/Scylla/Desktop/App Icon/"


def manual_set_output_types():
    output_types = [
        "icon",
        #"texture"
    ]
    return output_types


def manual_set_slug_types():
    slug_types = [
        #"1k",
        #"2k",
        #"4k",
        "marketing",
        "android_26",
        "android_legacy",
        "ios_iphone",
        #"ios_ipad"
    ]
    return slug_types


def start():
    filtered_dict = get_manual_set_output()
    dir_path, m_dir = handle_pathing(filtered_dict)
    for entry in filtered_dict:
        entry.print_contents()
        for file in m_dir:
            resize_image(dir_path, entry, file)


def get_manual_set_output():
    type_dict = DesignatedOutput.get_by_output_type(manual_set_output_types())
    filtered_dict = DesignatedOutput.filter_by_slug_type(type_dict, manual_set_slug_types())
    return filtered_dict


def handle_pathing(filtered_dict):
    unique_paths = Pathing.get_unique_paths(filtered_dict)
    dir_path = set_output_folders(unique_paths)
    m_dir = Pathing.get_files_in_dir(dir_path)
    return dir_path, m_dir


def set_output_folders(unique_paths):
    dir_path = ""
    for path in unique_paths:
        if Pathing.is_file(manual_set_path):
            dir_path = Pathing.get_dir_name(manual_set_path) + "/"
        elif Pathing.is_dir(manual_set_path):
            dir_path = manual_set_path
        Pathing.create_dir(dir_path + path)
    return dir_path


def resize_image(dir_path, entry, file):
    if not file.startswith('.') and Pathing.is_file(Pathing.join_paths(dir_path, file)):
        ResizeImages.resize(dir_path, dir_path + entry.sub_path, entry.res, "_" + entry.suffix, file)


start()
