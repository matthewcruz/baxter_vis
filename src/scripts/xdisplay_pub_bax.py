#!/usr/bin/env python 

#import cv2
#import cv_bridge
import rospy
from sensor_msgs.msg import Image


def xdisplay_pub(data):
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=10)
    print "out"
    pub.publish(data)


    
def get_image():
    rospy.init_node('image_data', anonymous=False)
    rate = rospy.Rate(10) # 10hz
   
    #may add some comment about timing
    while not rospy.is_shutdown():
        print "in"
        #does the topic need to be /cameras/head_camera/image?
        rospy.Subscriber("/cameras/head_camera", Image, xdisplay_pub)
        #replace subscibed topic to /cameras/head_camera
        # Sleep to allow for image to be published.
        rate.sleep()

    
if __name__ == '__main__':
    get_image()
