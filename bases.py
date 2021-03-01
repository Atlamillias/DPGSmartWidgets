from dearpygui.core import *

__all__ = [
    "SmartObject", 
    "SmartConfigProperty", 
    "SmartProperty", 
    "SmartContainer"
]


class SmartObject:
    """Base class for smartwidgets."""

    _func = None
    _ids = 0

    def __init__(self, name: str = None):
        self.__properties = [
            prop for prop, value in self.__class__.__dict__.items() if type(value) == SmartConfigProperty
        ]
        
        # "name" should honestly be "id" instead, but kept as "name"
        # so arguments match dearpygui's arguments
        if not name:
            self.name = f'{self.__class__.__name__}{self.__class__._ids + 1}'
            self.__class__._ids += 1
        else:
            self.name = name
        
        self.has_rendered = False  # for SmartConfigProperty configuration via __set__


    def __getitem__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __enter__(self):
        self._func(name=self.name, **self.properties())
        self.has_rendered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end()

    def __repr__(self):
        return str(self.name)

    def _set_value(self, prop, value):
        add_value(f"{self.name}.{prop}", value)
        set_value(f"{self.name}.{prop}", value)

    def _get_value(self, prop):
        return get_value(f"{self.name}.{prop}")

    def add(self):
        self._func(name=self.name, **self.properties())
        self.has_rendered = True

    def end(self):
        return end()

    def properties(self, as_storage_properties=False):
        """Returns a dictionary of the attributes used by dearpygui
        to make the object from value storage. If as_storage_properties
        is True, the keys will include the object name (so they can be
        used as a direct reference to value storage)."""

        if as_storage_properties:
            return {f"{self.name}.{prop}": value for prop, value in self.__dict__.items() if prop in self.__properties}
        else:
            return {prop: value for prop, value in self.__dict__.items() if prop in self.__properties}

    def configure(self, sender, data):
        prop = sender.split(".")[-1]
        configure_item(self.name, **{prop: getattr(self, prop)})


class SmartContainer(SmartObject):
    def __init__(self, name: str = None):
        super().__init__(name)

    @property
    def children(self):
        return get_item_children(self.name)



class SmartConfigProperty:
    """Descriptor for smartwidget properties. Retrieves and
    updates properties in the value storage system. Used for 
    the *required* arguments for DPG API. Do not use directly - 
    use SmartProperty or subclass this."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # updates value from value store first because it
        # may have been changed externally i.e. core.set_value
        instance.__dict__[self.name] = instance._get_value(self.name)
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # can pass SmartObject instead of SmartObject.name
        # as arguments for other SmartObjects (i.e. parent, before, etc.)
        if isinstance(value, SmartObject):
            value = value.name

        instance._set_value(self.name, value)
        instance.__dict__[self.name] = value
        # reconfigures only if object has been rendered
        instance.has_rendered and configure_item(instance.name, **{self.name: value})


class SmartProperty(SmartConfigProperty):
    """"""
    pass
