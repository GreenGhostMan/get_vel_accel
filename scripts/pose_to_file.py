#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
import time

class GetVelAccel(object):
	def __init__(self):
		self._file = open("linear_vel_accel.txt",'w')
		self._linear_vel = "Velocity"
		self._linear_accel = "Accereration"
		self._angular_vel= "Velocity"
		self._time = "Time"
		self._file.write("\n---------------------------------------------------------------\n")
		self._file.write(self._time + "\t" + self._linear_vel + "\t" + self._linear_accel+"\n")

		self._pose_sub = rospy.Subscriber('/odom',Odometry,self.callback)
		self.doSomething()

	def callback(self,msg):
		self._linear_vel  = str(msg.twist.twist.linear.x)
		self._angular_vel = str(msg.twist.twist.angular.z)
		self._time = str(msg.header.stamp)
		self._file.write(self._time + "\t" + self._linear_vel + "\t" + self._linear_accel+"\n")

	def doSomething(self):

		#self._file.close()
		rospy.loginfo("Written all Poses to txt file")


if __name__ == "__main__":
	rospy.init_node("recorder", log_level=rospy.INFO)
	obj = GetVelAccel()
	rospy.spin()
	
