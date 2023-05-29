import rospy
from std_srvs.srv import Empty, EmptyResponse

def robot_on(request):
    rospy.loginfo("Power on")
    rospy.sleep(2)
    rospy.loginfo("Opening")
    return EmptyResponse()

def robot_run(request):
    rospy.loginfo("Robot working")
    rospy.sleep(2)
    rospy.loginfo("Turning on the machine")
    return EmptyResponse()

def robot_off(request):
    rospy.loginfo("Power off")
    rospy.sleep(2)
    rospy.loginfo("Shutdown")
    return EmptyResponse()

def navigation_server():
    rospy.init_node('navigation_server')
    rospy.Service('/robot_on', Empty, robot_on)
    rospy.Service('/robot_run', Empty, robot_run)
    rospy.Service('/robot_off', Empty, robot_off)
    rospy.spin()

if __name__ == '__main__':
    navigation_server()
