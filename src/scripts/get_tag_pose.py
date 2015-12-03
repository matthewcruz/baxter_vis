#!/usr/bin/env python 

#import cv2
#import cv_bridge
import rospy
import ar_track_alvar_msgs/AlvarMarker
from sensor_msgs.msg import Image
#from geometry_msgs.msg import 
#from std_msgs.msg import Header


def callback(data):
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=10)
    pub.publish(data)


    
def get_image():
    rospy.init_node('image_data', anonymous=False)
    rate = rospy.Rate(1) # 10hz
   
    #may add some comment about timing
    while not rospy.is_shutdown():
        rospy.Subscriber("/usb_cam/image_raw", Image, callback)
        #replace subscibed topic to /cameras/head_camera
        # Sleep to allow for image to be published.
        rate.sleep()

    
if __name__ == '__main__':
    get_image()
