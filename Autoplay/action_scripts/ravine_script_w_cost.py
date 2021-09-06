from os import name
from monkey_hotkeys import hotkeys as h
from class_definitions import Action

place = 'place'
upgrade = 'upgrade'
target = 'target'


script = [
    Action(place, name='Psi', action='Hero', cost=780, position=(502, 778)), # Psi
    Action(target, name = 'Psi', action='Strong'),
    Action(place, name='dart1', action='dart', position=(1051, 344)), # dart
    Action('start', action='start'),

    Action(place, name = 'ninjar', action='ninja', cost=580, position=(740,813)), # Ninja
    Action(place, name= 'ninjal', action='ninja', cost=580, position=(281,666)), # Ninja

    Action(upgrade, name='ninjar', action='upgrade 1', cost=325),
    Action(upgrade, name='ninjal', action='upgrade 1', cost=325),

    Action(upgrade, name='ninjar', action='upgrade 3', cost=270),
    Action(upgrade, name='ninjal', action='upgrade 3', cost=270),

    Action(upgrade, name='ninjar', action='upgrade 1', cost=380), # 201
    Action(upgrade, name='ninjal', action='upgrade 1', cost=380), # 201

    Action(upgrade, name='ninjar', action='upgrade 1', cost=820), # 301
    Action(upgrade, name='ninjal', action='upgrade 1', cost=820), # 301

    Action(upgrade, name='ninjar', action='upgrade 3', cost=430), # 302

    Action(place, name='alch1', action='alch', cost = 595, position=(549, 861)), # Alchemist
    Action(upgrade, name='alch1', action='upgrade 1', cost=270), # 100
    Action(upgrade, name='alch1', action='upgrade 1', cost=380), # 200

    Action(place, name='ace1', action='ace', cost=820, position=(420, 896)), # Ace. cost might be wrong
    Action(upgrade, name='ace1', action='upgrade 3', cost=540), # 001
    Action(upgrade, name='ace1', action='upgrade 3', cost=325), # 002
    Action(upgrade, name='ace1', action='upgrade 3', cost=2375), # 003
    Action(upgrade, name='ace1', action='upgrade 1', cost=700), # 103
    Action(upgrade, name='ace1', action='upgrade 1', cost=700), # 203

    Action(upgrade, name='ninjal', action='upgrade 3', cost=430), # 302 Ninja (Left)
    Action(upgrade, name='alch1', action='upgrade 3', cost=700), # 201 Alch

    Action(place, name='sniper1', action='sniper', cost=360, position=(262, 733)), # Sniper
    Action(upgrade, name='sniper1', action='upgrade 1', cost=380), # 200
    Action(target, name = 'sniper1', action='Strong'),

    Action(upgrade, name='alch1', action='upgrade 1', cost=1350), # 301 Alch

    Action(place, name='village1', action='Village', cost=1270, position=(397, 799)), # Village
    Action(upgrade, name='village1', action='upgrade 2', cost=270), # 010
    Action(upgrade, name='village1', action='upgrade 2', cost=2160), # 020
    Action(upgrade, name='village1', action='upgrade 1', cost=430), # 120
    Action(upgrade, name='village1', action='upgrade 1', cost=1620), # 220

    Action(place, name='ace2', action='ace', cost=820, position=(261, 805)), # Ace2
    Action(upgrade, name='ace2', action='upgrade 3', cost=540), # 001
    Action(upgrade, name='ace2', action='upgrade 3', cost=325), # 002
    Action(upgrade, name='ace2', action='upgrade 3', cost=2375), # 003
    Action(upgrade, name='ace2', action='upgrade 1', cost=700), # 103
    Action(upgrade, name='ace2', action='upgrade 1', cost=700), # 203

    Action(place, name='heli1', action='heli', cost=1640, position=(266, 925)), # Heli
    Action(upgrade, name='heli1', action='upgrade 1', cost=865), # 100
    Action(upgrade, name='heli1', action='upgrade 1', cost=540), # 200
    Action(upgrade, name='heli1', action='upgrade 3', cost=270), # 201
    Action(upgrade, name='heli1', action='upgrade 3', cost=380), # 202
    Action(upgrade, name='heli1', action='upgrade 3', cost=3780), # 203
    Action(upgrade, name='heli1', action='upgrade 3', cost=9180), # 203

    Action(upgrade, name='alch1', action='upgrade 1', cost=3240), # Alch 302
    Action(upgrade, name='ace2', action='upgrade 3', cost=25920), # Ace 204
    Action('finish', action='finish')

    
]