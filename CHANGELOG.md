# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
## Added
- **widgets.py** for upcomming widget classes (button, etc).

### Changed
- **smartwidgets.py** has been renamed to **containers.py**.
- **Table** class moved to **widgets.py**.

## 0.2.0 - 2019-02-15

### Changed
- "Container" widgets now subclass **SmartContainer** instead of **SmartObject**.
- Original **SmartProperty** class renamed to **SmartConfigProperty**. **SmartProperty** now subclasses **SmartConfigProperty**.
- **SmartConfigProperty** is now strictly used for passing required arguments to assigned dearpygui.core functions.
- **name** attribute is now optional for many classes in **smartwidgets.py**.
- **keyword-only** removed from many classes in **smartwidgets.py**.
- Default values for **Window.x/y_pos** changed from 200 to 0.
- **SmartObject** methods **set/get_value** are now marked as private.

### Added
- SmartObjects will now auto-generate a __name__ (i.e. ID) if one is not provided using the class name and a number (auto-increments +1 for now).
- **add** method added to **SmartObjects** so they can be placed/used outside of context managers.
- **MenuBar** class now has a **height** property. Useful when programatically positioning widgets when you want them to avoid overlapping the menu bar.
- **keep_pos_on_config** parameter added to **Window** (**True** by default). If **False**, the widget will return to it's original position (on creation) when **Window.configure** is called.
- **SmartContainer** added to **bases.py** (subclass of **SmartObject**)
  - new **children** method.
- Added **NodeEditor** and **NodeAttribute** classes in **smartwidgets.py**.

### Fixed
- **SmartObject** now checks for **SmartProperty**'s via **type** instead of **isinstance**. Attributes that are subclass instances of **SmartProperty** are no longer sent as arguments to the assigned **dearpygui.core** function.
- Passing the number 0 for **Window** attributes **x/y_pos** now works as intended instead of using the default value (was previously 200).
- Type hints that used **or** now use **Union**.
- **Window.configure** now works properly when controlling **x/y_pos**.
