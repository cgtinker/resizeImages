
class Resolution:
    def __init__(self, suffix, resolution, sub_path, img_type, slug):
        self.suffix = suffix
        self.res = resolution
        self.sub_path = sub_path
        self.img_type = img_type
        self.slug = slug

    def print_contents(self):
        print("generating img ",
              "suffix:", self.suffix,
              "res:", self.res,
              "path:", self.sub_path,
              "type:", self.img_type,
              "slug:", self.slug)


def get_resolutions():
    resolution_dict = []

    for dict_entry in dicts:
        entry = Resolution(
            dict_entry["suffix"],
            dict_entry["resolution"],
            dict_entry["path"],
            dict_entry["img_type"],
            dict_entry["slug"]
        )
        resolution_dict.append(entry)
    return resolution_dict


dicts = [
    # textures
    {"suffix": "1k", "resolution": 1024, "path": "1k/", "img_type": "texture", "slug": "1k"},
    {"suffix": "2k", "resolution": 2048, "path": "2k/", "img_type": "texture", "slug": "2k"},
    {"suffix": "4k", "resolution": 4096, "path": "4k/", "img_type": "texture", "slug": "4k"},

    # marketing
    {"suffix": "1024px", "resolution": 1024, "path": "marketing/", "img_type": "icon", "slug": "marketing"},
    {"suffix": "512px", "resolution": 512, "path": "marketing/", "img_type": "icon", "slug": "marketing"},

    # android api 26+
    {"suffix": "api_26_xxx_hdpi", "resolution": 432, "path": "api26/", "img_type": "icon", "slug": "android_26"},
    {"suffix": "api_26_xx_hdpi", "resolution": 324, "path": "api26/", "img_type": "icon", "slug": "android_26"},
    {"suffix": "api_26_x_hdpi", "resolution": 216, "path": "api26/", "img_type": "icon", "slug": "android_26"},
    {"suffix": "api_26_hdpi", "resolution": 162, "path": "api26/", "img_type": "icon", "slug": "android_26"},
    {"suffix": "api_26_mdpi", "resolution": 108, "path": "api26/", "img_type": "icon", "slug": "android_26"},
    {"suffix": "api_26_ldpi", "resolution": 81, "path": "api26/", "img_type": "icon", "slug": "android_26"},

    # android legacy
    {"suffix": "legacy_xxx_hdpi", "resolution": 192, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},
    {"suffix": "legacy_xx_hdpi", "resolution": 144, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},
    {"suffix": "legacy_x_hdpi", "resolution": 96, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},
    {"suffix": "legacy_hdpi", "resolution": 72, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},
    {"suffix": "legacy_mdpi", "resolution": 48, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},
    {"suffix": "legacy_ldpi", "resolution": 36, "path": "legacy/", "img_type": "icon", "slug": "android_legacy"},

    # iphone icons
    {"suffix": "60pt_x3", "resolution": 180, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},
    {"suffix": "60pt_x2", "resolution": 120, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},

    {"suffix": "40pt_x3", "resolution": 120, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},
    {"suffix": "40pt_x2", "resolution": 80, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},

    {"suffix": "29pt_x3", "resolution": 87, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},
    {"suffix": "29pt_x2", "resolution": 58, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},
    {"suffix": "29pt_x1", "resolution": 29, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},

    {"suffix": "20pt_x3", "resolution": 60, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},
    {"suffix": "20pt_x2", "resolution": 40, "path": "iphone/", "img_type": "icon", "slug": "ios_iphone"},

    # ipad icons
    {"suffix": "83_5pt_x2", "resolution": 167, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},
    {"suffix": "76pt_x2", "resolution": 152, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},
    {"suffix": "76pt_x1", "resolution": 76, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},

    {"suffix": "40pt_x2", "resolution": 80, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},
    {"suffix": "40pt_x1", "resolution": 40, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},

    {"suffix": "29pt_x2", "resolution": 58, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},
    {"suffix": "29pt_x1", "resolution": 29, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},

    {"suffix": "20pt_x2", "resolution": 40, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"},
    {"suffix": "20pt_x1", "resolution": 20, "path": "ipad/", "img_type": "icon", "slug": "ios_ipad"}
]
