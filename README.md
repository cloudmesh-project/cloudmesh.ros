# cloudmesh.ros
Prepatory Steps
1. Copy ~/.ssh/known_hosts
	Since most of us have created and deleted multiple VMs on Chameleon Cloud, it is possible that the your computer's known hosts file already has a public key associated with an ip address that may be assigned during the cluster cretion process.  If that happens, the process will fail.  I could have programmatically handled it, but out of respect for you, the end user, I chose not to manipulate your known hosts file.

	Use these commands to save a copy and create a blank known hosts file:
	
	mv ~/.ssh/known_hosts ~/.ssh/known_hosts.BAK
	touch ~/.ssh/known_hosts

2. Retrieve the startup script
	Type or paste the follwing command into a terminal in order to retrieve the script to start the cluster creation process:

	wget -P ~ https://raw.githubusercontent.com/cloudmesh/cloudmesh.ros/master/rosProjFinal/begin

3. Make the startup script executable
	chmod +x ~/begin

4. Ensure cloudmesh access
	The process depends on cloudmesh_client commands.  You must have access to them in order for the process to succeed.

Known Problems
 1. Simulation Software Fails
 	In some circumstances, the simulation software, Gazebo, will fail to launch properly.  The failure results from the method ROS' *roslaunch* command initializes Gazebo.  Possible solutions involve issuing the following commands from the terminal from the mybot_ws directory:
 	a. source  /home/cc/mybot_ws/devel/setup.bash
 	   rosrun gazebo_ros gzclient
 	   roslaunch mybot_gazebo mybot_world.launch
 	b. source /home/cc/mybot_ws/devel/setup.bash
 	   killall gzserver
 	   roslaunch mybot_gazebo mybot_world.launch