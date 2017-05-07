from cloudmesh.common.console import Console
from cloudmesh.common.Shell import Shell
import textwrap
import os

# just some ideas

# but may be better of to use https://pypi.python.org/pypi/libtmux

class tmux(object):

    def __init__(self):
        pane = -1

    def setup(self):
        script = textwrap.dedent("""
        export ROS_MASTER_URI=http://$node_ip02:11311
        SESSION=$USER
        byobu-tmux -2 new-session -d -s $SESSION
        byobu-tmux split-window -v
        byobu-tmux select-pane -t 1
        byobu-tmux split-window -h
        """)
        for line in script:
            os.system(line)

    def run(self, pane, script):
        if type(script) is str:
            lines = script.split()
        elif type(script) is list:
            lines = script
        else:
            Console.error ("script type not supported")
        # r = Shell.execute("byobu-tmux", ["select-pane", "-t", "1"])
        #for line in lines:

    def _pane_setup(self):
        pass

    def _pane_select(self, pane):
        if self.pane != pane:
            r = Shell.execute("byobu-tmux", ["select-pane", "-t", pane])
            self.pane = pane

    def _send(self, line, pane=None):
        if pane is None:
            pane = self.pane
        self._pane_select(pane)
        r = Shell.execute("byobu-tmux", ["-2", "send-keys", line,"C-m"])

    def session_create(self, session):
        r = Shell.execute("byobu-tmux", ["-2", "new-session", "-d", "-s", "$SESSION"])

    def session_attach(self, session):
        r = Shell.execute ("byobu-tmux",  ["-2", "attach-session", "-t", "$SESSION"])

    """
    #!/usr/bin/env bash
    cut -d' ' -f1 ~/addMeToHostFiles.list > ~/inventoryInter.txt
    
    node_ip01=$(sed -n '1p' ~/inventoryInter.txt)
    #echo $node_ip01
    ssh -o StrictHostKeyChecking=no cc@$node_ip01 hostname
    
    node_ip02=$(sed -n '2p' ~/inventoryInter.txt)
    #echo $node_ip02
    ssh -o StrictHostKeyChecking=no cc@$node_ip02 hostname
    
    node_ip03=$(sed -n '3p' ~/inventoryInter.txt)
    #echo $node_ip03
    ssh -o StrictHostKeyChecking=no cc@$node_ip03 hostname
    
    export ROS_MASTER_URI=http://$node_ip02:11311
    SESSION=$USER
    byobu-tmux -2 new-session -d -s $SESSION
    byobu-tmux split-window -v
    byobu-tmux select-pane -t 1
    byobu-tmux split-window -h
    
    byobu-tmux select-pane -t 1
    byobu-tmux -2 send-keys "export ROS_MASTER_URI=http://$node_ip02:11311" C-m
    byobu-tmux -2 send-keys "roscore" C-m

    byobu-tmux select-pane -t 2
    byobu-tmux -2 send-keys "export ROS_MASTER_URI=http://$node_ip02:11311" C-m
    byobu-tmux -2 send-keys "rosrun rospy_tutorials talker.py" C-m

    byobu-tmux select-pane -t 0
    byobu-tmux -2 send-keys "ssh -o StrictHostKeyChecking=no  cc@$node_ip03" C-m
    byobu-tmux -2 send-keys "export ROS_MASTER_URI=http://$node_ip02:11311" C-m
    byobu-tmux -2 attach-session -t $SESSION
    """