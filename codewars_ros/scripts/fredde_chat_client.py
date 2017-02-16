# !/usr/bin/env python

import rospy
import sys
from chat_server.msg import Message

def callback(data):
    print rospy.get_caller_id + ":" + data.data

def run_client():
    rospy.init_node('client', anonymous=True)
    rospy.Subscriber("chat_out", Message, callback)

def publish_message(message):
    pub = rospy.Publisher('chat_in', Message)
    pub.publish(message)

if __name__ == '__main__':
    publish_message(sys.argv)





