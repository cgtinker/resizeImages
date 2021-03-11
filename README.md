# resize square images in batches

resizes square images to common texture and app icon formats

there are apps around which aren't modifiyable, therefore I created this setup.
it's easy to extend but requires manual modification and running of _main.py_

requirements:
**pillow**
```
sudo pip install pillow
```

## how to use
**1. manual_set_path**
manual set a path to a directory containing squared images or to a square image file

**2. manual_set_ouput_type**
manual set the output types like textures or icons, just comment out the once you don't need

**3. manual_set_slug_types**
every exportable format contains a slug, just comment out the onces you don't need


## how to modify
**available output types**
in the _available output types_ script you'll find a dictionary called _dicts_ in which you can add new entries.
1. **suffix** gets added to the resized file name
2. **path** suffix will be the output directory of the file
2. **resolution** describes the output resolution (only supports square formats)
3. **img_type** describes the output type for filtering in _main.py_
4. **slug** it's not always required to add an unique slug for filtering as you may always export certain sizes based on the output type

sample:
    {"suffix": "1k", "resolution": 1024, "path": "1k/", "img_type": "texture", "slug": "1k"},

don't forget to add the newly created _output types and slugs_ to the **main.py** _manual_set_ouput_type & manual_set_slug_types_
