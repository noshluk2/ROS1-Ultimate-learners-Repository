#!/usr/bin/env python
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


def action_interface():

    rospy.init_node('dual_dual_arm_trajectorymsg_actionLib')
    dual_arm_Rjoints = ['arm1_a_joint','arm1_b_joint']
    dual_arm_Ljoints = ['arm2_a_joint','arm2_b_joint']

    joint_Rpositions = [3.14,3.14]
    joint_Lpositions = [3.14,3.14]
    rospy.loginfo('Now Lets call the action lib interface')
            
    dual_arm_Rclient = actionlib.SimpleActionClient('arm1_trajectory_controller/follow_joint_trajectory',
                                                    FollowJointTrajectoryAction)
    dual_arm_Lclient = actionlib.SimpleActionClient('arm2_trajectory_controller/follow_joint_trajectory',
                                                    FollowJointTrajectoryAction)
    dual_arm_Rclient.wait_for_server()
    dual_arm_Lclient.wait_for_server()
    rospy.loginfo('Connected to the server')
    rospy.sleep(1)
            
    dual_arm_Rtrajectorymsg = JointTrajectory()
    dual_arm_Rtrajectorymsg.joint_names = dual_arm_Rjoints
    dual_arm_Rtrajectorymsg.points.append(JointTrajectoryPoint())
    dual_arm_Rtrajectorymsg.points[0].positions = joint_Rpositions
    dual_arm_Rtrajectorymsg.points[0].velocities = [0.0 for i in dual_arm_Rjoints]
    dual_arm_Rtrajectorymsg.points[0].accelerations = [0.0 for i in dual_arm_Rjoints]
    dual_arm_Rtrajectorymsg.points[0].time_from_start = rospy.Duration(3)
    goalR_positions = FollowJointTrajectoryGoal()
    goalR_positions.trajectory = dual_arm_Rtrajectorymsg
    goalR_positions.goal_time_tolerance = rospy.Duration(0)
    dual_arm_Rclient.send_goal(goalR_positions)
    rospy.sleep(1)
    rospy.loginfo('Lets see the Right arm in action ')

    dual_arm_Ltrajectorymsg = JointTrajectory()
    dual_arm_Ltrajectorymsg.joint_names = dual_arm_Ljoints
    dual_arm_Ltrajectorymsg.points.append(JointTrajectoryPoint())
    dual_arm_Ltrajectorymsg.points[0].positions = joint_Lpositions
    dual_arm_Ltrajectorymsg.points[0].velocities = [0.0 for i in dual_arm_Ljoints]
    dual_arm_Ltrajectorymsg.points[0].accelerations = [0.0 for i in dual_arm_Ljoints]
    dual_arm_Ltrajectorymsg.points[0].time_from_start = rospy.Duration(3)
            
    goalL_positions = FollowJointTrajectoryGoal()
    goalL_positions.trajectory = dual_arm_Ltrajectorymsg
    goalL_positions.goal_time_tolerance = rospy.Duration(0)
    dual_arm_Lclient.send_goal(goalL_positions)
    rospy.sleep(1)
    rospy.loginfo('Lets see the Left arm in action ')


if __name__ == '__main__':
    action_interface()