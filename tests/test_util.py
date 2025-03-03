from i3_resurrect import config
from i3_resurrect import util


def test_build_tree(monkeypatch):
    # Monkeypatch config.
    monkeypatch.setattr(
        config,
        '_config',
        {
            'window_swallow_criteria': {
                'Ario': ['class', 'instance'],
            },
        },
    )

    workspace_container = {
        "id": 94067986102992,
        "type": "workspace",
        "orientation": "horizontal",
        "scratchpad_state": "none",
        "percent": None,
        "urgent": False,
        "focused": False,
        "output": "HDMI-1-1",
        "layout": "splith",
        "workspace_layout": "default",
        "last_split_layout": "splith",
        "border": "normal",
        "current_border_width": -1,
        "rect": {
            "x": 1366,
            "y": 0,
            "width": 1920,
            "height": 1048
        },
        "deco_rect": {
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        "window_rect": {
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        "geometry": {
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0
        },
        "name": "8",
        "num": 8,
        "gaps": {
            "inner": 0,
            "outer": 0
        },
        "window": None,
        "nodes": [
            {
                "id": 94067985558992,
                "type": "con",
                "orientation": "none",
                "scratchpad_state": "none",
                "percent": 0.5,
                "urgent": False,
                "focused": False,
                "output": "HDMI-1-1",
                "layout": "splith",
                "workspace_layout": "default",
                "last_split_layout": "splith",
                "border": "pixel",
                "current_border_width": 2,
                "rect": {
                    "x": 1376,
                    "y": 10,
                    "width": 945,
                    "height": 1028
                },
                "deco_rect": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "window_rect": {
                    "x": 2,
                    "y": 2,
                    "width": 941,
                    "height": 1024
                },
                "geometry": {
                    "x": 2049,
                    "y": 486,
                    "width": 553,
                    "height": 107
                },
                "name": "Ario",
                "title_format": " %title ",
                "window": 140509206,
                "window_properties": {
                    "class": "Ario",
                    "instance": "ario",
                    "title": "Ario",
                    "transient_for": None
                },
                "nodes": [],
                "floating_nodes": [],
                "focus": [],
                "fullscreen_mode": 0,
                "sticky": False,
                "floating": "auto_off",
                "swallows": []
            },
            {
                "id": 94067986549632,
                "type": "con",
                "orientation": "vertical",
                "scratchpad_state": "none",
                "percent": 0.5,
                "urgent": False,
                "focused": False,
                "output": "HDMI-1-1",
                "layout": "splitv",
                "workspace_layout": "default",
                "last_split_layout": "splitv",
                "border": "normal",
                "current_border_width": -1,
                "rect": {
                    "x": 2326,
                    "y": 0,
                    "width": 960,
                    "height": 1048
                },
                "deco_rect": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "window_rect": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "geometry": {
                    "x": 0,
                    "y": 0,
                    "width": 0,
                    "height": 0
                },
                "name": None,
                "window": None,
                "nodes": [
                    {
                        "id": 94067986605168,
                        "type": "con",
                        "orientation": "none",
                        "scratchpad_state": "none",
                        "percent": 0.5,
                        "urgent": False,
                        "focused": False,
                        "output": "HDMI-1-1",
                        "layout": "splith",
                        "workspace_layout": "default",
                        "last_split_layout": "splith",
                        "border": "pixel",
                        "current_border_width": 2,
                        "rect": {
                            "x": 2331,
                            "y": 10,
                            "width": 945,
                            "height": 509
                        },
                        "deco_rect": {
                            "x": 0,
                            "y": 0,
                            "width": 0,
                            "height": 0
                        },
                        "window_rect": {
                            "x": 2,
                            "y": 2,
                            "width": 941,
                            "height": 505
                        },
                        "geometry": {
                            "x": 2331,
                            "y": 10,
                            "width": 941,
                            "height": 1024
                        },
                        "name": "Faster Melee - Slippi (r18)",
                        "title_format": " %title ",
                        "window": 142606648,
                        "window_properties": {
                            "class": "Dolphin-emu",
                            "instance": "dolphin-emu",
                            "title": "Faster Melee - Slippi (r18)",
                            "transient_for": None
                        },
                        "nodes": [],
                        "floating_nodes": [],
                        "focus": [],
                        "fullscreen_mode": 0,
                        "sticky": False,
                        "floating": "auto_off",
                        "swallows": []
                    },
                    {
                        "id": 94067986105456,
                        "type": "con",
                        "orientation": "none",
                        "scratchpad_state": "none",
                        "percent": 0.5,
                        "urgent": False,
                        "focused": False,
                        "output": "HDMI-1-1",
                        "layout": "splith",
                        "workspace_layout": "default",
                        "last_split_layout": "splith",
                        "border": "pixel",
                        "current_border_width": 2,
                        "rect": {
                            "x": 2331,
                            "y": 529,
                            "width": 945,
                            "height": 509
                        },
                        "deco_rect": {
                            "x": 0,
                            "y": 0,
                            "width": 0,
                            "height": 0
                        },
                        "window_rect": {
                            "x": 2,
                            "y": 2,
                            "width": 941,
                            "height": 505
                        },
                        "geometry": {
                            "x": 2542,
                            "y": 344,
                            "width": 518,
                            "height": 356
                        },
                        "name": "Dolphin NetPlay Setup",
                        "title_format": " %title ",
                        "window": 142607489,
                        "window_properties": {
                            "class": "Dolphin-emu",
                            "instance": "dolphin-emu",
                            "title": "Dolphin NetPlay Setup",
                            "transient_for": None
                        },
                        "nodes": [],
                        "floating_nodes": [],
                        "focus": [],
                        "fullscreen_mode": 0,
                        "sticky": False,
                        "floating": "auto_off",
                        "swallows": []
                    }
                ],
                "floating_nodes": [],
                "focus": [
                    94067986105456,
                    94067986605168
                ],
                "fullscreen_mode": 0,
                "sticky": False,
                "floating": "auto_off",
                "swallows": []
            }
        ],
        "floating_nodes": [],
        "focus": [
            94067986549632,
            94067985558992
        ],
        "fullscreen_mode": 0,
        "sticky": False,
        "floating": "auto_off",
        "swallows": []
    }
    expected_tree = [
        {
            "border": "pixel",
            "current_border_width": 2,
            "floating": "auto_off",
            "fullscreen_mode": 0,
            "geometry": {
                "x": 2049,
                "y": 486,
                "width": 553,
                "height": 107
            },
            "layout": "splith",
            "name": "Ario",
            "orientation": "none",
            "percent": 0.5,
            "scratchpad_state": "none",
            "type": "con",
            "workspace_layout": "default",
            "swallows": [
                {
                    "class": "^Ario$",
                    "instance": "^ario$"
                }
            ],
            "nodes": []
        },
        {
            "border": "normal",
            "current_border_width": -1,
            "floating": "auto_off",
            "fullscreen_mode": 0,
            "geometry": {
                "x": 0,
                "y": 0,
                "width": 0,
                "height": 0
            },
            "layout": "splitv",
            "name": None,
            "orientation": "vertical",
            "percent": 0.5,
            "scratchpad_state": "none",
            "type": "con",
            "workspace_layout": "default",
            "nodes": [
                {
                    "border": "pixel",
                    "current_border_width": 2,
                    "floating": "auto_off",
                    "fullscreen_mode": 0,
                    "geometry": {
                        "x": 2331,
                        "y": 10,
                        "width": 941,
                        "height": 1024
                    },
                    "layout": "splith",
                    "name": "Faster Melee - Slippi (r18)",
                    "orientation": "none",
                    "percent": 0.5,
                    "scratchpad_state": "none",
                    "type": "con",
                    "workspace_layout": "default",
                    "swallows": [
                        {
                            "class": "^Dolphin\\-emu$",
                            "instance": "^dolphin\\-emu$",
                            "title": "^Faster\\ Melee\\ \\-\\ Slippi\\ \\(r18\\)$"
                        }
                    ],
                    "nodes": []
                },
                {
                    "border": "pixel",
                    "current_border_width": 2,
                    "floating": "auto_off",
                    "fullscreen_mode": 0,
                    "geometry": {
                        "x": 2542,
                        "y": 344,
                        "width": 518,
                        "height": 356
                    },
                    "layout": "splith",
                    "name": "Dolphin NetPlay Setup",
                    "orientation": "none",
                    "percent": 0.5,
                    "scratchpad_state": "none",
                    "type": "con",
                    "workspace_layout": "default",
                    "swallows": [
                        {
                            "class": "^Dolphin\\-emu$",
                            "instance": "^dolphin\\-emu$",
                            "title": "^Dolphin\\ NetPlay\\ Setup$"
                        }
                    ],
                    "nodes": []
                }
            ]
        }
    ]
    tree = util.build_tree(workspace_container, ['class', 'instance', 'title'])
    assert tree == expected_tree


def test_windows_in_container(monkeypatch):
    workspace_tree = {
        'id': 93860418230528,
        'type': 'workspace',
        'orientation': 'horizontal',
        'scratchpad_state': 'none',
        'percent': 0.5,
        'urgent': False,
        'focused': False,
        'output': 'HDMI-1-1',
        'layout': 'splith',
        'workspace_layout': 'default',
        'last_split_layout': 'splith',
        'border': 'normal',
        'current_border_width': -1,
        'rect': {'x': 1366, 'y': 0, 'width': 1920, 'height': 1048},
        'deco_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
        'window_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
        'geometry': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
        'name': '2',
        'num': 2,
        'gaps': {'inner': 0, 'outer': 0},
        'window': None,
        'nodes': [
            {
                'id': 93860418434672,
                'type': 'con',
                'orientation': 'vertical',
                'scratchpad_state': 'none',
                'percent': 0.5,
                'urgent': False,
                'focused': False,
                'output': 'HDMI-1-1',
                'layout': 'splitv',
                'workspace_layout': 'default',
                'last_split_layout': 'splitv',
                'border': 'normal',
                'current_border_width': -1,
                'rect': {'x': 1366, 'y': 0, 'width': 960, 'height': 1048},
                'deco_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'window_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'geometry': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'name': None,
                'window': None,
                'nodes': [
                    {
                        'id': 93860418452384,
                        'type': 'con',
                        'orientation': 'none',
                        'scratchpad_state': 'none',
                        'percent': 0.5,
                        'urgent': False,
                        'focused': False,
                        'output': 'HDMI-1-1',
                        'layout': 'splith',
                        'workspace_layout': 'default',
                        'last_split_layout': 'splith',
                        'border': 'pixel',
                        'current_border_width': 2,
                        'rect': {
                            'x': 1376,
                            'y': 10,
                            'width': 945,
                            'height': 509
                        },
                        'deco_rect': {
                            'x': 0,
                            'y': 0,
                            'width': 0,
                            'height': 0
                        },
                        'window_rect': {
                            'x': 2,
                            'y': 2,
                            'width': 941,
                            'height': 505
                        },
                        'geometry': {
                            'x': 0,
                            'y': 0,
                            'width': 724,
                            'height': 412
                        },
                        'name': '~/Projects',
                        'title_format': ' %title ',
                        'window': 52428803,
                        'window_properties': {
                            'class': 'Alacritty',
                            'instance': 'Alacritty',
                            'title': '~/Projects',
                            'transient_for': None
                        },
                        'nodes': [

                        ],
                        'floating_nodes':[

                        ],
                        'focus':[

                        ],
                        'fullscreen_mode':0,
                        'sticky':False,
                        'floating':'auto_off',
                        'swallows':[

                        ]
                    },
                    {
                        'id': 93860418285248,
                        'type': 'con',
                        'orientation': 'none',
                        'scratchpad_state': 'none',
                        'percent': 0.5,
                        'urgent': False,
                        'focused': False,
                        'output': 'HDMI-1-1',
                        'layout': 'splith',
                        'workspace_layout': 'default',
                        'last_split_layout': 'splith',
                        'border': 'pixel',
                        'current_border_width': 2,
                        'rect': {
                            'x': 1376,
                            'y': 529,
                            'width': 945,
                            'height': 509
                        },
                        'deco_rect': {
                            'x': 0,
                            'y': 0,
                            'width': 0,
                            'height': 0
                        },
                        'window_rect': {
                            'x': 2,
                            'y': 2,
                            'width': 941,
                            'height': 505
                        },
                        'geometry': {
                            'x': 0,
                            'y': 0,
                            'width': 724,
                            'height': 412
                        },
                        'name': '~/.dotfiles',
                        'title_format': ' %title ',
                        'window': 6291459,
                        'window_properties': {
                            'class': 'Alacritty',
                            'instance': 'Alacritty',
                            'title': '~/.dotfiles',
                            'transient_for': None
                        },
                        'nodes': [

                        ],
                        'floating_nodes':[

                        ],
                        'focus':[

                        ],
                        'fullscreen_mode':0,
                        'sticky':False,
                        'floating':'auto_off',
                        'swallows':[]
                    }
                ],
                'floating_nodes':[],
                'focus':[93860418285248, 93860418452384],
                'fullscreen_mode':0,
                'sticky':False,
                'floating':'auto_off',
                'swallows':[

                ]
            },
            {
                'id': 93860418798800,
                'type': 'con',
                'orientation': 'vertical',
                'scratchpad_state': 'none',
                'percent': 0.5,
                'urgent': False,
                'focused': False,
                'output': 'HDMI-1-1',
                'layout': 'splitv',
                'workspace_layout': 'default',
                'last_split_layout': 'splitv',
                'border': 'normal',
                'current_border_width': -1,
                'rect': {'x': 2326, 'y': 0, 'width': 960, 'height': 1048},
                'deco_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'window_rect': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'geometry': {'x': 0, 'y': 0, 'width': 0, 'height': 0},
                'name': None,
                'window': None,
                'nodes': [
                    {
                        'id': 93860418425760,
                        'type': 'con',
                        'orientation': 'none',
                        'scratchpad_state': 'none',
                        'percent': 0.5,
                        'urgent': False,
                        'focused': False,
                        'output': 'HDMI-1-1',
                        'layout': 'splith',
                        'workspace_layout': 'default',
                        'last_split_layout': 'splith',
                        'border': 'pixel',
                        'current_border_width': 2,
                        'rect': {
                            'x': 2331,
                            'y': 10,
                            'width': 945,
                            'height': 509
                        },
                        'deco_rect': {
                            'x': 0,
                            'y': 0,
                            'width': 0,
                            'height': 0
                        },
                        'window_rect': {
                            'x': 2,
                            'y': 2,
                            'width': 941,
                            'height': 505
                        },
                        'geometry': {
                            'x': 0,
                            'y': 0,
                            'width': 1366,
                            'height': 736
                        },
                        'name': 'System Monitor',
                        'title_format': ' %title ',
                        'window': 54525962,
                        'window_properties': {
                            'class': 'ksysguard',
                            'instance': 'ksysguard',
                            'window_role': 'MainWindow#1',
                            'title': 'System Monitor',
                            'transient_for': None
                        },
                        'nodes': [

                        ],
                        'floating_nodes':[

                        ],
                        'focus':[

                        ],
                        'fullscreen_mode':0,
                        'sticky':False,
                        'floating':'auto_off',
                        'swallows':[

                        ]
                    },
                    {
                        'id': 93860418808208,
                        'type': 'con',
                        'orientation': 'none',
                        'scratchpad_state': 'none',
                        'percent': 0.5,
                        'urgent': False,
                        'focused': False,
                        'output': 'HDMI-1-1',
                        'layout': 'splith',
                        'workspace_layout': 'default',
                        'last_split_layout': 'splith',
                        'border': 'pixel',
                        'current_border_width': 2,
                        'rect': {
                            'x': 2331,
                            'y': 529,
                            'width': 945,
                            'height': 509
                        },
                        'deco_rect': {
                            'x': 0,
                            'y': 0,
                            'width': 0,
                            'height': 0
                        },
                        'window_rect': {
                            'x': 2,
                            'y': 2,
                            'width': 941,
                            'height': 505
                        },
                        'geometry': {
                            'x': 0,
                            'y': 0,
                            'width': 724,
                            'height': 412
                        },
                        'name': '~/.dotfiles',
                        'title_format': ' %title ',
                        'window': 50331651,
                        'window_properties': {
                            'class': 'Alacritty',
                            'instance': 'Alacritty',
                            'title': '~/.dotfiles',
                            'transient_for': None
                        },
                        'nodes': [

                        ],
                        'floating_nodes':[

                        ],
                        'focus':[

                        ],
                        'fullscreen_mode':0,
                        'sticky':False,
                        'floating':'auto_off',
                        'swallows':[

                        ]
                    }
                ],
                'floating_nodes':[],
                'focus':[93860418425760, 93860418808208],
                'fullscreen_mode':0,
                'sticky':False,
                'floating':'auto_off',
                'swallows':[]
            }
        ],
        'floating_nodes': [],
        'focus': [93860418434672, 93860418798800],
        'fullscreen_mode': 0,
        'sticky': False,
        'floating': 'auto_off',
        'swallows': []
    }
    windows = util.windows_in_container(workspace_tree)
    assert windows != None


def test_get_window_command(monkeypatch):
    # Monkeypatch config.
    monkeypatch.setattr(
        config,
        '_config',
        {
            'window_command_mappings': [
                {
                    'class': 'Program1'
                },
                {
                    'class': 'Program1',
                    'title': 'Main window title',
                    'command': 'run_program1'
                },
                {
                    'title': 'Some arbitrary title'
                }
            ],
        },
    )

    # Test class + title mapping.
    program1_main = {
        'class': 'Program1',
        'title': 'Main window title'
    }
    assert util.get_window_command(program1_main, ['program1']) == [
        'run_program1',
    ]

    # Test class only mapping.
    program1_secondary = {
        'class': 'Program1',
        'title': 'Blah random title'
    }
    assert util.get_window_command(program1_secondary, ['program1']) == []

    # Test with separate program window with matching title but not class.
    program2_main = {
        'class': 'Program2',
        'title': 'Main window title',
    }
    assert util.get_window_command(program2_main, ['program2']) == ['program2']

    # Test that title only mapping matches any window with matching title.
    program3 = {
        'class': 'Program3',
        'title': 'Some arbitrary title',
    }
    assert util.get_window_command(program3, ['program3']) == []
