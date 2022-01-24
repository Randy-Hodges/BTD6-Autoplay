
class Action(object):
    '''
    Perform one action in a script.
    '''
    def __init__(self, type, action=None, name=None, cost = None, position = None):
        '''
        Params:
        :arg type: type of action
            <'place', 'upgrade', 'target', 'start', 'finish', 'click'>
        :arg action: specific action to be performed (full list of options in monkey_hotkeys.py)
        :arg name: name of monkey. Make it unique to the monkey. REQUIRED WHEN PLACING, UPGRADING
        :arg cost: cost of action (Not required. All monkey upgrade data is in monkey_info.py)
        :arg position: Position of cursor when placing monkey. REQUIRED WHEN PLACING
        '''
        self.type = type
        self.name = name
        self.action = action
        self.cost = cost
        self.position = position

