# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added 

- **SmartAttribute** class (empty subclass of **SmartProperty**). **SmartProperty** is now strictly used internally for passing required arguments to assigned **dearpygui.core** functions. Subclass **SmartProperty** or use this new subclass when you want to add additional "smart" properties.
- **MenuBar** class now has a **height** property. Useful when programatically positioning widgets and you want to avoid them overlapping the menu bar.
- Smartwidgets will now auto-generate a "name" (i.e. ID) if one is not provided using the class name and a number (auto-increments +1 for now).

### Changed
- **name** attribute is now optional for many classes in **smartwidgets.py**.
- **keyword-only** removed from many classes in **smartwidgets.py**.

### Fixed

- **SmartObject** now checks for **SmartProperty**'s via **type** instead of **isinstance**. Attributes that are subclass instances of **SmartProperty** are no longer sent as arguments to the assigned **dearpygui.core** function.
- Passing the number 0 for **Window** attributes **x/y_pos** now works as intended. The new default value for these attributes has also been changed from 200 to 0.
- Type hints that used **or** now use **Union**.
