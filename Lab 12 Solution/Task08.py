from poodle import Object, schedule
from typing import Set

class Location(Object):
    def __str__(self):
        if not hasattr(self, "name"):
            return "undefined"
        return self.name

class HeightAttribute(Object):
    height: int

class PositionAttribute(Object):
    location: Location

class Monkey(HeightAttribute, PositionAttribute):
    pass

class PalmTree(HeightAttribute, PositionAttribute):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 2

class Crate(HeightAttribute, PositionAttribute):
    pass

class Fruit(HeightAttribute, PositionAttribute):
    holder: Monkey
    attached_to: PalmTree

class World(Object):
    locations: Set[Location]

loc_a = Location()
loc_a.name = "Location A"
loc_b = Location()
loc_b.name = "Location B"
loc_c = Location()
loc_c.name = "Location C"

world = World()
world.locations = {loc_a, loc_b, loc_c}

monkey = Monkey()
monkey.height = 0
monkey.location = loc_a

crate = Crate()
crate.height = 2
crate.location = loc_b

palm_tree = PalmTree()
palm_tree.location = loc_c

banana = Fruit()
banana.attached_to = palm_tree

def move_monkey(monkey: Monkey, destination: Location):
    assert destination in world.locations
    assert monkey.height < 1, "Monkey must be on the ground to move"
    monkey.location = destination
    return f"Monkey moves to {destination}"

def push_crate(monkey: Monkey, crate: Crate, destination: Location):
    assert monkey.location == crate.location
    assert destination in world.locations
    assert monkey.height < 1, "Monkey must be on the ground to push the crate"
    monkey.location = destination
    crate.location = destination
    return f"Monkey pushes crate to {destination}"

def climb_crate(monkey: Monkey, crate: Crate):
    assert monkey.location == crate.location
    monkey.height += crate.height
    return "Monkey climbs onto the crate"

def take_fruit(monkey: Monkey, fruit: Fruit):
    assert monkey.height == fruit.height
    assert monkey.location == fruit.location
    fruit.holder = monkey
    return "Monkey takes the fruit"

def set_fruit_location_from_tree(palm_tree: PalmTree, fruit: Fruit):
    assert fruit.attached_to == palm_tree
    fruit.location = palm_tree.location
    return "Fruit location is set to the palm tree's location"

def set_fruit_height_from_tree(palm_tree: PalmTree, fruit: Fruit):
    assert fruit.attached_to == palm_tree
    fruit.height = palm_tree.height
    return "Fruit height is set to the palm tree's height"

print('\n'.join(action() for action in schedule(
    [move_monkey, push_crate, climb_crate, take_fruit, set_fruit_height_from_tree, set_fruit_location_from_tree],
    [world, loc_a, loc_b, loc_c, monkey, crate, palm_tree, banana],
    goal=lambda: banana.holder == monkey
)))
