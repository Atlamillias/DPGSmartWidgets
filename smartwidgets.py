from dearpygui.core import *
from dearpygui.simple import show_about, show_debug, show_metrics, show_style_editor
from typing import Any, Callable
from bases import SmartObject, SmartProperty


class Window(SmartObject):
    _func = add_window
    width = SmartProperty()
    height = SmartProperty()
    x_pos = SmartProperty()
    y_pos = SmartProperty()
    autosize = SmartProperty()
    no_resize = SmartProperty()
    no_title_bar = SmartProperty()
    no_move = SmartProperty()
    no_scrollbar = SmartProperty()
    no_collapse = SmartProperty()
    horizontal_scrollbar = SmartProperty()
    no_focus_on_appearing = SmartProperty()
    no_bring_to_front_on_focus = SmartProperty()
    menubar = SmartProperty()
    no_close = SmartProperty()
    no_background = SmartProperty()
    label = SmartProperty()
    show = SmartProperty()
    on_close = SmartProperty()

    def __init__(self, name: str, *, width: int = None, height: int = None, x_pos: int = None, y_pos: int = None,
                 autosize: bool = False, no_resize: bool = False, no_title_bar: bool = False, no_move: bool = False,
                 no_scrollbar: bool = False, no_collapse: bool = False, horizontal_scrollbar: bool = False,
                 no_focus_on_appearing: bool = False, no_bring_to_front_on_focus: bool = False, menubar: bool = False,
                 no_close: bool = False, no_background: bool = False, label: str = None, show: bool = True,
                 on_close: Callable = None):
        super().__init__(name)

        self.width = width or 0
        self.height = height or 0
        self.x_pos = x_pos or 200
        self.y_pos = y_pos or 200
        self.autosize = autosize
        self.no_resize = no_resize
        self.no_title_bar = no_title_bar
        self.no_move = no_move
        self.no_scrollbar = no_scrollbar
        self.no_collapse = no_collapse
        self.horizontal_scrollbar = horizontal_scrollbar
        self.no_focus_on_appearing = no_focus_on_appearing
        self.no_bring_to_front_on_focus = no_bring_to_front_on_focus
        self.menubar = menubar
        self.no_close = no_close
        self.no_background = no_background
        self.label = label or self.name
        self.show = show
        self.on_close = on_close

    @property
    def current_pos(self):
        # for self.configure
        config = get_item_configuration(self.name)
        return config["x_pos"], config["y_pos"]

    def configure(self, sender, data):
        x_pos, y_pos = self.current_pos
        prop = sender.split('.')[-1]
        configure_item(
            self.name,
            x_pos=x_pos,  # will rerender where object was previously closed
            y_pos=y_pos,
            **{prop: getattr(self, prop)}
        )


class Child(SmartObject):
    _func = add_child
    show = SmartProperty()
    tip = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    width = SmartProperty()
    height = SmartProperty()
    border = SmartProperty()
    autosize_x = SmartProperty()
    autosize_y = SmartProperty()
    no_scrollbar = SmartProperty()
    horizontal_scrollbar = SmartProperty()
    menubar = SmartProperty()

    def __init__(self, name: str, *, show: bool = True, tip: str = None, parent: str or SmartObject = None,
                 before: str or SmartObject = None,
                 width: int = None, height: int = None, border: bool = False, autosize_x: bool = False,
                 autosize_y: bool = False, no_scrollbar: bool = False, horizontal_scrollbar: bool = False,
                 menubar: bool = False):
        super().__init__(name)

        self.show = show
        self.tip = tip or ''
        self.parent = parent or ''
        self.before = before or ''
        self.width = width or 0
        self.height = height or 0
        self.border = border or True
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar


class Group(SmartObject):
    _func = add_group
    show = SmartProperty()
    tip = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    width = SmartProperty()
    horizontal = SmartProperty()
    horizontal_spacing = SmartProperty()

    def __init__(self, name: str, *, show: bool = True, tip: str = None, parent: str or SmartObject = None,
                 before: str or SmartObject = None, width: int = None, horizontal: bool = False,
                 horizontal_spacing: float = None):
        super().__init__(name)

        self.show = show
        self.tip = tip or ''
        self.parent = parent or ''
        self.before = before or ''
        self.width = width or 0
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing or -1.0


class MenuBar(SmartObject):
    _func = add_menu_bar
    show = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()

    def __init__(self, name: str, *, show: bool = True, parent: str or SmartObject = None, before: str or SmartObject = None):
        super().__init__(name)

        self.show = show
        self.parent = parent or ''
        self.before = before or ''


class Menu(SmartObject):
    _func = add_menu
    label = SmartProperty()
    show = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    enabled = SmartProperty()

    def __init__(self, name: str, *, label: str = None, show: bool = True, parent: str or SmartObject = None, before: str or SmartObject = None, enabled: bool = True):
        super().__init__(name)

        self.label = label or self.name
        self.show = show
        self.parent = parent or ''
        self.before = before or ''
        self.enabled = enabled


class TabBar(SmartObject):
    _func = add_tab_bar
    reorderable = SmartProperty()
    callback = SmartProperty()
    callback_data = SmartProperty()
    show = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()

    def __init__(self, name: str, *, reorderable: bool = False, callback: Callable = None,
                 callback_data: Any = None, show: bool = True, parent: str or SmartObject = None, before: str or SmartObject = None):
        super().__init__(name)

        self.reorderable = reorderable
        self.callback = callback
        self.callback_data = callback_data
        self.show = show
        self.parent = parent or ''
        self.before = before or ''


class Tab(SmartObject):
    _func = add_tab
    closable = SmartProperty()
    label = SmartProperty()
    show = SmartProperty()
    no_reorder = SmartProperty()
    leading = SmartProperty()
    trailing = SmartProperty()
    no_tooltip = SmartProperty()
    tip = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()

    def __init__(self, name: str, *, closable: bool = False, label: str = None, show: bool = True,
                 no_reorder: bool = False, leading: bool = False, trailing: bool = False,
                 no_tooltip: bool = False, tip: str = None, parent: str or SmartObject = None, before: str or SmartObject = None):
        super().__init__(name)

        self.closable = closable
        self.label = label or self.name
        self.show = show
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip
        self.tip = tip or ''
        self.parent = parent or ''
        self.before = before or ''


class Popup(SmartObject):
    _func = add_popup
    popupparent = SmartProperty()
    mousebutton = SmartProperty()
    modal = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    width = SmartProperty()
    height = SmartProperty()
    show = SmartProperty()

    def __init__(self, name: str, popupparent: str or SmartObject, *, mousebutton: int = None, modal: bool = False,
                 parent: str or SmartObject = None, before: str or SmartObject = None, width: int = None, height: int = None,
                 show: bool = True):
        super().__init__(self, name)

        self.popupparent = popupparent
        self.mousebutton = mousebutton or 1
        self.modal = modal
        self.parent = parent or ''
        self.before = before or ''
        self.width = width or 0
        self.height = height or 0
        self.show = show


class Tooltip(SmartObject):
    _func = add_tooltip
    tipparent = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    show = SmartProperty()

    def __init__(self, name: str, tipparent: str or SmartObject, *, parent: str or SmartObject = None, before: str or SmartObject = None, show: bool = True):
        super().__init__(name)

        self.tipparent = tipparent
        self.parent = parent or ''
        self.before = before or ''
        self.show = show


class Tree(SmartObject):
    _func = add_tree_node
    label = SmartProperty()
    show = SmartProperty()
    tip = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    default_open = SmartProperty()
    open_on_double_click = SmartProperty()
    open_on_arrow = SmartProperty()
    leaf = SmartProperty()
    bullet = SmartProperty()

    def __init__(self, name: str, *, label: str = None, show: bool = True, tip: str = None,
                 parent: str or SmartObject = None, before: str or SmartObject = None, default_open: bool = False,
                 open_on_double_click: bool = False, open_on_arrow: bool = False, leaf: bool = False,
                 bullet: bool = False):
        super().__init__(name)

        self.label = label or self.name
        self.show = show
        self.tip = tip or ''
        self.parent = parent or ''
        self.before = before or ''
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


class ManagedColumns(SmartObject):
    _func = add_managed_columns
    columns = SmartProperty()
    border = SmartProperty()
    show = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()

    def __init__(self, name: str, columns: int, *, border: bool = False, show: bool = True,
                 parent: str or SmartObject = None, before: str or SmartObject = None):
        super().__init__(name)

        self.columns = columns
        self.border = border
        self.show = show
        self.parent = parent or ''
        self.before = before or ''


class Table(SmartObject):
    _func = add_table
    headers = SmartProperty()
    parent = SmartProperty()
    before = SmartProperty()
    width = SmartProperty()
    height = SmartProperty()
    show = SmartProperty()

    def __init__(self, name: str, headers: list = None, *, callback: Callable = None,
                 callback_data: Any = None, parent: str or SmartObject = None, before: str or SmartObject = None,
                 width: int = None, height: int = None, show: bool = True):
        super().__init__(name)

        self.headers = headers or []
        self.callback = callback
        self.callback_data = callback_data
        self.parent = parent or ''
        self.before = before or ''
        self.width = width or 0
        self.height = height or 0
        self.show = show

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # Placeholders
    def add_headers(self):
        pass

    def set_headers(self):
        pass

    def delete_column(self):
        pass

    def insert_row(self):
        pass

    def insert_column(self):
        pass

    def delete_row(self):
        pass

    def get_table_item(self):
        pass

    def get_table_data(self):
        pass

    def get_table_selections(self):
        pass

    def set_table_item(self):
        pass

    def set_table_data(self):
        pass

    def set_table_selections(self):
        pass

    def clear(self):
        """Wrapper for core.clear_table"""
        return clear_table(self.name)
