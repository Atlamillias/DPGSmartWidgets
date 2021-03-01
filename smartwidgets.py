from dearpygui.core import *
from dearpygui.simple import show_about, show_debug, show_metrics, show_style_editor
from typing import Any, Callable, Union
from bases import SmartObject, SmartContainer, SmartConfigProperty

__all__ = [
    "Window",
    "Child",
    "Group",
    "MenuBar",
    "Menu",
    "TabBar",
    "Tab",
    "Group",
    "Popup",
    "Tooltip",
    "Tree",
    "ManagedColumns",
    "NodeEditor",
    "NodeAttribute",
    "Table",
]


class Window(SmartContainer):
    _func = add_window
    width = SmartConfigProperty()
    height = SmartConfigProperty()
    x_pos = SmartConfigProperty()
    y_pos = SmartConfigProperty()
    autosize = SmartConfigProperty()
    no_resize = SmartConfigProperty()
    no_title_bar = SmartConfigProperty()
    no_move = SmartConfigProperty()
    no_scrollbar = SmartConfigProperty()
    no_collapse = SmartConfigProperty()
    horizontal_scrollbar = SmartConfigProperty()
    no_focus_on_appearing = SmartConfigProperty()
    no_bring_to_front_on_focus = SmartConfigProperty()
    menubar = SmartConfigProperty()
    no_close = SmartConfigProperty()
    no_background = SmartConfigProperty()
    label = SmartConfigProperty()
    show = SmartConfigProperty()
    on_close = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        width: int = None,
        height: int = None,
        x_pos: int = None,
        y_pos: int = None,
        autosize: bool = False,
        no_resize: bool = False,
        no_title_bar: bool = False,
        no_move: bool = False,
        no_scrollbar: bool = False,
        no_collapse: bool = False,
        horizontal_scrollbar: bool = False,
        no_focus_on_appearing: bool = False,
        no_bring_to_front_on_focus: bool = False,
        menubar: bool = False,
        no_close: bool = False,
        no_background: bool = False,
        label: str = None,
        show: bool = True,
        on_close: Callable = None,

        keep_pos_on_config: bool = True
    ):
    
        super().__init__(name)

        self.width = width or 0
        self.height = height or 0
        self.x_pos = x_pos if isinstance(x_pos, int) else 0
        self.y_pos = y_pos if isinstance(y_pos, int) else 0
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

        self.keep_pos_on_config = keep_pos_on_config

    @property
    def current_pos(self):
        # for self.configure
        config = get_item_configuration(self.name)
        return config["x_pos"], config["y_pos"]

    def configure(self, sender, data):
        x_pos, y_pos = self.current_pos
        prop = sender.split(".")[-1]

        if self.keep_pos_on_config:
            configure_item(
                self.name,
                x_pos=x_pos,  # will rerender where object was previously closed
                y_pos=y_pos,
                **{prop: getattr(self, prop)}
            )
        else:
            configure_item(
                self.name,
                **{prop: getattr(self, prop)}
            )


class Child(SmartContainer):
    _func = add_child
    show = SmartConfigProperty()
    tip = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    width = SmartConfigProperty()
    height = SmartConfigProperty()
    border = SmartConfigProperty()
    autosize_x = SmartConfigProperty()
    autosize_y = SmartConfigProperty()
    no_scrollbar = SmartConfigProperty()
    horizontal_scrollbar = SmartConfigProperty()
    menubar = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        width: int = None,
        height: int = None,
        border: bool = False,
        autosize_x: bool = False,
        autosize_y: bool = False,
        no_scrollbar: bool = False,
        horizontal_scrollbar: bool = False,
        menubar: bool = False
    ):

        super().__init__(name)

        self.show = show
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.border = border or True
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar


class Group(SmartContainer):
    _func = add_group
    show = SmartConfigProperty()
    tip = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    width = SmartConfigProperty()
    horizontal = SmartConfigProperty()
    horizontal_spacing = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        width: int = None,
        horizontal: bool = False,
        horizontal_spacing: float = None
    ):

        super().__init__(name)

        self.show = show
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing or -1.0


class MenuBar(SmartContainer):
    _func = add_menu_bar
    show = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):

        super().__init__(name)

        self.show = show
        self.parent = parent or ""
        self.before = before or ""

    @property
    def height(self):
        return get_item_configuration(self.name)['height']


class Menu(SmartContainer):
    _func = add_menu
    label = SmartConfigProperty()
    show = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    enabled = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        label: str = None,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        enabled: bool = True
    ):

        super().__init__(name)

        self.label = label or self.name
        self.show = show
        self.parent = parent or ""
        self.before = before or ""
        self.enabled = enabled


class TabBar(SmartContainer):
    _func = add_tab_bar
    reorderable = SmartConfigProperty()
    callback = SmartConfigProperty()
    callback_data = SmartConfigProperty()
    show = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        reorderable: bool = False,
        callback: Callable = None,
        callback_data: Any = None,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):

        super().__init__(name)

        self.reorderable = reorderable
        self.callback = callback
        self.callback_data = callback_data
        self.show = show
        self.parent = parent or ""
        self.before = before or ""


class Tab(SmartContainer):
    _func = add_tab
    closable = SmartConfigProperty()
    label = SmartConfigProperty()
    show = SmartConfigProperty()
    no_reorder = SmartConfigProperty()
    leading = SmartConfigProperty()
    trailing = SmartConfigProperty()
    no_tooltip = SmartConfigProperty()
    tip = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        closable: bool = False,
        label: str = None,
        show: bool = True,
        no_reorder: bool = False,
        leading: bool = False,
        trailing: bool = False,
        no_tooltip: bool = False,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):

        super().__init__(name)

        self.closable = closable
        self.label = label or self.name
        self.show = show
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""


class Popup(SmartContainer):
    _func = add_popup
    popupparent = SmartConfigProperty()
    mousebutton = SmartConfigProperty()
    modal = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    width = SmartConfigProperty()
    height = SmartConfigProperty()
    show = SmartConfigProperty()

    def __init__(
        self,
        name: str,
        popupparent: Union[str, SmartObject],
        *,
        mousebutton: int = None,
        modal: bool = False,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        width: int = None,
        height: int = None,
        show: bool = True
    ):

        super().__init__(self, name)

        self.popupparent = popupparent
        self.mousebutton = mousebutton or 1
        self.modal = modal
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.show = show


class Tooltip(SmartObject):
    _func = add_tooltip
    tipparent = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    show = SmartConfigProperty()

    def __init__(
        self,
        name: str,
        tipparent: Union[str, SmartObject],
        *,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        show: bool = True
    ):
        super().__init__(name)

        self.tipparent = tipparent
        self.parent = parent or ""
        self.before = before or ""
        self.show = show


class Tree(SmartObject):
    _func = add_tree_node
    label = SmartConfigProperty()
    show = SmartConfigProperty()
    tip = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    default_open = SmartConfigProperty()
    open_on_double_click = SmartConfigProperty()
    open_on_arrow = SmartConfigProperty()
    leaf = SmartConfigProperty()
    bullet = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        
        label: str = None,
        show: bool = True,
        tip: str = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        default_open: bool = False,
        open_on_double_click: bool = False,
        open_on_arrow: bool = False,
        leaf: bool = False,
        bullet: bool = False
    ):
        super().__init__(name)

        self.label = label or self.name
        self.show = show
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


class ManagedColumns(SmartObject):
    _func = add_managed_columns
    columns = SmartConfigProperty()
    border = SmartConfigProperty()
    show = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()

    def __init__(
        self,
        name: str,
        columns: int,
        *,
        border: bool = False,
        show: bool = True,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None
    ):
        super().__init__(name)

        self.columns = columns
        self.border = border
        self.show = show
        self.parent = parent or ""
        self.before = before or ""


class NodeEditor(SmartContainer):
    _func = add_node_editor
    show = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    link_callback = SmartConfigProperty()
    delink_callback = SmartConfigProperty()

    def __init__(
        self, 
        name: str = None,
        show: bool = True,
        parent: str = None,
        before: str = None,
        link_callback: Callable = None,
        delink_callback: Callable = None
    ):
        super().__init__(name)
        self.show = show
        self.parent = parent or ""
        self.before = before or ""
        self.link_callback = link_callback
        self.delink_callback = delink_callback


class NodeAttribute(SmartContainer):
    _func = add_node_attribute
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    show = SmartConfigProperty()
    output = SmartConfigProperty()
    static = SmartConfigProperty()

    def __init__(
        self, 
        name: str = None,
        show: bool = True,
        parent: str = None,
        before: str = None,
        output: bool = False,
        static: bool = False
    ):

        super().__init__(name)
        self.show = show
        self.parent = parent or ""
        self.before = before or ""
        self.output = output
        self.static = static


class Table(SmartObject):
    _func = add_table
    headers = SmartConfigProperty()
    parent = SmartConfigProperty()
    before = SmartConfigProperty()
    width = SmartConfigProperty()
    height = SmartConfigProperty()
    show = SmartConfigProperty()

    def __init__(
        self,
        name: str = None,
        headers: list = None,
        
        callback: Callable = None,
        callback_data: Any = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        width: int = None,
        height: int = None,
        show: bool = True
    ):
        super().__init__(name)

        self.headers = headers or []
        self.callback = callback
        self.callback_data = callback_data
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.show = show

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


    def clear(self):
        """Wrapper for core.clear_table"""
        return clear_table(self.name)
