from dearpygui.core import *
from dearpygui.simple import show_about, show_debug, show_metrics, show_style_editor
from typing import Any, Callable


class SmartObject:
    _func = None

    def __init__(self, name: str):
        self.__properties = [prop for prop, value in self.__class__.__dict__.items() if isinstance(value, SmartProperty)]

        self.name = name
        self.has_rendered = False  # for SmartProperty configuration via __set__

    def __getitem__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __enter__(self):
        self._func(
            name=self.name,
            **self.properties()
        )
        self.has_rendered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end()

    def __repr__(self):
        return str(self.name)

    def add(self):
        self._func(
            name=self.name,
            **self.properties()
        )
        self.has_rendered = True

    def end(self):
        return end()

    def set_value(self, prop, value):
        add_value(f'{self.name}.{prop}', value)
        set_value(f'{self.name}.{prop}', value)

    def get_value(self, prop):
        return get_value(f'{self.name}.{prop}')

    def properties(self, as_storage_properties=False):
        if as_storage_properties:
            return {f'{self.name}.{prop}': value for prop, value in self.__dict__.items() if prop in self.__properties}
        else:
            return {prop: value for prop, value in self.__dict__.items() if prop in self.__properties}

    def configure(self, sender, data):
        prop = sender.split('.')[-1]
        configure_item(
            self.name,
            **{prop: getattr(self, prop)}
        )


class SmartProperty:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # updates value from value store first because it
        # may have been changed externally i.e. core.set_value
        instance.__dict__[self.name] = instance.get_value(self.name)
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if isinstance(value, SmartObject):
            value = value.name

        instance.set_value(self.name, value)
        instance.__dict__[self.name] = value
        # reconfigures only if object has been rendered
        instance.has_rendered and configure_item(
            instance.name, **{self.name: value})
