#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def perform_trajectory():
    rospy.init_node('dual_arm_trajectory_publisher')
    contoller_name='/arm1_trajectory_controller/command'
    trajectory_publihser = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10)
                                
    dual_armRjoints = ['arm1_a_joint','arm1_b_joint']
    goal_positions = [3.14,1.57]
    rospy.sleep(1)
            ## creating a message to send Joint Trajectory type
    arm_trajectory = JointTrajectory()
    arm_trajectory.joint_names = dual_armRjoints
    arm_trajectory.points.append(JointTrajectoryPoint())
    arm_trajectory.points[0].positions = goal_positions
    arm_trajectory.points[0].velocities = [0.0 for i in dual_armRjoints]
    arm_trajectory.points[0].accelerations = [0.0 for i in dual_armRjoints]
    arm_trajectory.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publihser.publish(arm_trajectory)
            ## trajecotry will be executed while the node will complete execution
            ## task will be sent before that with time delays


if __name__ == '__main__':
    perform_trajectory()

