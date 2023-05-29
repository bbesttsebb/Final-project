import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received message : %s",data.data)
    rospy.init_node('nevigation_subscriber')
    rospy.Subscriber('/robot_ststus',String, callback)

    rospy.spin()

