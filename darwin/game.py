import cmd
from room import get_room
import textwrap


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.loc = get_room(1)
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("you can't go that way")
        else:
            self.loc = get_room(newroom)
            self.look()

        if newroom==6:
            print("You Win!")
            # do_save()
            exit()

    def _parse(self, command):
        words = command.split()
        verb = words[0]
        noun = " ".join(words[1:])
        return verb, noun

    def _has_condition(self, node, condition):
        required = node.get(condition)
        if required is None:
            return default

    def look(self):
        """Look at an item, direction, or area:"""
        print(self.loc.name)
        print("")
        if item in get_room(newroom):
            print("You see a " + room[newroom["item"]])
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def _take(self, noun):
        for item in get_room(id):
            if item in room[current_room]:
                # remove the item from the current area
                self._room.remove(item)
                # add it to the player's inventory
                self._player.append(item)
                return "You've taken the %s." % noun
        return "You don't see any %s." % noun

        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_inventory(self, noun):
        """Display a list of items player has taken."""
        result = []
        for item in self._player.findall("item"):
            result.append(item.get("name"))
        if result:
            return "\n".join(result)
        return "You don't have anything in your inventory."
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

    def do_take(self, noun):
        """Take an item from the room"""

    def do_parse(self, args):
        """parses console commands"""

    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing")
        return True

    def do_save(self, args):
        """Saves the game state"""
        # shutil.copyfile(self.dbfile, args)
        print("The game was saved to {0}".format(args))

if __name__ == "__main__":
    g = Game()
    g.cmdloop()