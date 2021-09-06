
class Monkey(object):
    '''Store data of placed monkey'''
    def __init__(self, position=None, name=None, mtype=None) -> None:
        '''
        :arg position: position, list
        :arg name: name
        :arg mtype: type of monkey (get from action.action)
        '''
        self.position = position
        self.upgrades = [0,0,0]
        self.name = name
        self.mtype = mtype

    def upgrade(self, path):
        '''
        Increase the stored paths of a monkey when upgrading.
        
        :arg path: Path of upgrade taking place.
            <1, 2, 3> (1 being the top path)
        '''
        if path == 1:
            self.upgrades[0] += 1
            if self.upgrades[0] > 5 and (self.mtype != 'Dart Monkey' or self.mtype != 'Boomerang Monkey'):
                print('invalid upgrade (higher than 5)')
        if path == 2:
            self.upgrades[1] += 1
            if self.upgrades[1] > 5 and (self.mtype != 'Dart Monkey' or self.mtype != 'Boomerang Monkey'):
                print('invalid upgrade (higher than 5)')
        if path == 3:
            self.upgrades[2] += 1
            if self.upgrades[2] > 5 and (self.mtype != 'Dart Monkey' or self.mtype != 'Boomerang Monkey'):
                print('invalid upgrade (higher than 5)')

                