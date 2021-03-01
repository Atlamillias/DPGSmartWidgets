# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added 

- **SmartAttribute** class (empty subclass of **SmartProperty**). **SmartProperty** is now strictly used internally for passing required arguments to assigned **dearpygui.core** functions. Subclass **SmartProperty** or use this new subclass when you want to add additional "smart" properties.
- **MenuBar** class now has a **height** property. Useful when programatically positioning widgets and you want to avoid them overlapping the menu bar.

### Fixed

- **SmartObject** now checks for **SmartProperty**'s via **type** instead of **isinstance**. Attributes that are subclass instances of **SmartProperty** are no longer sent as arguments to the assigned **dearpygui.core** function.
