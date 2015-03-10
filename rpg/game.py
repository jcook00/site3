import cmd
from room import get_room
import textwrap


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.loc = get_room(1)
        self.look()

    def move(self, dir):
        # move is a method only, not a command
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("you can't go that way")
        else:
            self.loc = get_room(newroom)
            self.look()

    def look(self):
        """Look at an item, direction, or area:"""
        # look is a method only, not a command
        print(self.loc.name)
        print("")
        # textwrap makes the formatting fit into the command window
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_inventory(self, arg):
        """Display a list of items player has taken."""

        if len(inventory) == 0:
            print('Inventory:\n (nothing')
            return
        # get a count of distinct items in players inventory

        itemCount = {}
        for item in inventory:
            if item in itemCount.keys():
                itemCount[item] += 1
            else:
                itemCount[item] = 1

        # remove duplicates from players inventory

        print('Inventory:')
        for item in set(inventory):
            if itemCount[item] > 1:
                print(' %s (%s)' % (item, itemCount[item]))
            else:
                print(' ' + item)
    do_inv = do_inventory

    def do_up(self, args):
        """Go up"""
        self.move('up')

    def do_down(self, args):
        """Go down"""
        self.move('down')

    def do_n(self, args):
        """Go north"""
        self.move('n')

    def do_s(self, args):
        """Go south"""
        self.move('s')

    def do_e(self, args):
        """Go east"""
        self.move('e')

    def do_w(self, args):
        """Go west"""
        self.move('w')

    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing")
        return True

if __name__ == "__main__":
    g = Game()
    g.cmdloop()