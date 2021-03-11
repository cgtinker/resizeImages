from . import AvailableOutputTypes


def get_by_output_type(output_img_types):
    output_dict = AvailableOutputTypes.get_resolutions()

    dist_output_dict = []
    for entry in output_dict:
        for output_type in output_img_types:
            if entry.img_type == output_type:
                dist_output_dict.append(entry)

    return dist_output_dict


def filter_by_slug_type(output_dict, slugs):
    filtered_dict = []
    for entry in output_dict:
        for slug in slugs:
            if entry.slug == slug:
                filtered_dict.append(entry)

    return filtered_dict
