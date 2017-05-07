from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class RosCommand(PluginCommand):

    @command
    def do_ros(self, args, arguments):
        """
        ::

          Usage:
                ros -f FILE
                ros FILE
                ros list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



