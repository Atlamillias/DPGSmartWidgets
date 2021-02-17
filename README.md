# DPGSmartWidgets
Limited OO-bindings for DearPyGui (https://github.com/hoffstadt/DearPyGui)

## Usage

Typical usage is intended to be identical to DearPyGui.

```Python
from smartwidgets import *
# Note: wildcard import for smartwidgets also 
# wildcard imports dearpygui.core

with Window("main", width=1000, height=500):
    pass

start_dearpygui(primary_window="main")
```

...with some extended functionality:

```Python
# Instantiate before rendering
# and bind widgets to variables.
viewport = Window(name="viewport",width=1000, height=500)

# Easy access via <object>.<attribute>.
print(viewport.height)
# >>> 500

# Widget properties are also stored in the value
# storage system, and can be accessed using the
# same lookup structure, but as a string.
print(get_value(name="viewport.width"))
# >>> 1000

# Setting attribute values will also update the
# same value in value storage.
viewport.height = 300
print(get_value(name="viewport.height"))
# >>> 300

# and vice-versa
set_value("viewport.height", 800)
print(viewport.height)
# >>> 800
```

Using widgets to control another widgets' attributes with **SmartObject.configure**:

```Python
from smartwidgets import *

with Window("not_viewport", width=500, height=200) as not_viewport:
        pass

with Window(name="viewport",width=1000, height=500) as viewport:
    add_checkbox('not_viewport.menubar', label='Menubar', default_value=False, callback=not_viewport.configure)
    add_checkbox('not_viewport.no_close', label='No Close', default_value=False, callback=not_viewport.configure)
    add_slider_int('not_viewport.height', label='Height', default_value=not_viewport.height, min_value=10, max_value=1000, callback=not_viewport.configure)
    add_slider_int('not_viewport.width', label='Width', default_value=not_viewport.width, min_value=10, max_value=1000, callback=not_viewport.configure)

start_dearpygui(primary_window=viewport.name)
```


