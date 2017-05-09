# cloudmesh.ros
In order to deploy the virtual swarm, please follow the steps outlined below. 

1. Prequisites
	a. Linux || The deployment uses several bash scripts developed on a machine using Ubuntu 16.xx.  It might work on OSX, but it has not been tested in that environment.

	b. Cloudmesh Client || The deployment integrates the cloudmesh_client developed at Indiana University.  We suggest installing it in a virtual environment.

2. Retrieve the Startup Script
	Type or paste the follwing command into a terminal in order to retrieve the script to start the cluster creation process:

	wget -P ~ https://raw.githubusercontent.com/cloudmesh/cloudmesh.ros/master/rosProjFinal/begin

3. Make the Startup Script Executable
	chmod +x ~/begin

Known Problems
 	In some circumstances, the simulation software, Gazebo, will fail to launch properly.  The failure results from the method ROS' *roslaunch* command initializes Gazebo.  The article accompanying this code outlines possible solutions.
 	