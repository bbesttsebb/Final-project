import rospy
from std_srvs.srv import Empty

def main():
    rospy.wait_for_service('/robot_run')
    rospy.wait_for_service('/robot_off')
    rospy.wait_for_service('/robot_on')

    try:
        robot_run = rospy.ServiceProxy('/robot_run', Empty)
        robot_off = rospy.ServiceProxy('/robot_off', Empty)
        robot_on = rospy.ServiceProxy('/robot_on', Empty)

        robot_run()
        robot_off()
        robot_on()
        robot_off()

    except rospy.ServiceException as e:
        print("Service call failed:", str(e))

if __name__ == '__main__':
    rospy.init_node('main')
    main()

