# R2D2 ROS2 Package

This will be used to control my R2D2 using ROS2.  My plan is to have a package for each feature.  Then you can utilize those features only.  Most of the packages will utilize a Raspberry Pi 3 board.  This is cheap to buy and control most hardware like servos and motor controllers.

## Build

``` bash
rm -rf install
rm -rf build
colcon build
source install/setup.bash
source install/local_setup.bash
```

## Run

### Arm Control

The Arm control will control the movement of the arm.  There is a web interface that can publish messages to the topic /r2d2_arm_topic.  This will make the arm move.  There are orchestrated movements or simple movements.

This will start the subscriber to listen for messages on the /r2d2_arm_topic

```bash
 ros2 run r2d2_ros2_arm_control arm_ctrl_sub
```

Test message you can send to verify functionality

```bash
ros2 topic pub /r2d2_arm_topic std_msgs/String "data: test_arms"
```
