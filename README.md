# scout_mini_navigation
|Package|Launch/run|Description|
|--|--|--|
|scout_base|scout_mini_base.launch.py|connect scout mini|
|scout_description|scout_base_description.launch.py|scout mini robot model + nav rviz setting(local, global)|
|scout_msgs|ScoutActuatorState.msg, ScoutLightCmd.msg, ScoutLightState.msg, ScoutRCState.msg, ScoutStatus.msg||
|ros2_mapping|online_async_launch.py, provide_map.launch.py|online_async_launch.py : make a map  provide_map.launch.py : global map publish|
|velodyne_driver|velodyne_driver_node-VLP16-launch.py|connect velodyne|
|velodyne_laserscan|velodyne_laserscan_node-launch.py|laserscan publish|
|velodyne_pointcloud|velodyne_transform_node-VLP16-launch.py||
|velodyne_msgs|VelodynePacket.msg, VelodyneScan.msg||
|learning_tf2_py|turtle_tf2_demo.launch.py|odom -> base_link|
|tf2_ros|static_transform_publisher|map -> odom|
---
Ready
+ scout connect with can
  ```
  sudo apt-get update
  sudo apt -y install can-utils
  ```
  ```
  sudo modprobe can
  sudo ip link set can0 up type can bitrate 500000
  sudo ip link set up can0
  ```
+ velodyne driver connect with Ethernet
  ```
  sudo ifconfig
  sudo ifconfig <connect_id> 192.168.1.100
  ```
![KakaoTalk_20230323_164212920](https://user-images.githubusercontent.com/41955439/227136149-929a6d2c-d9c1-4e23-81cc-dc3fc238ee02.png) 
![Screenshot from 2023-01-09 11-10-08](https://user-images.githubusercontent.com/41955439/212530103-fb12a85d-ffbf-4a14-85a3-c8fa3e74c62b.png)
![Screenshot from 2023-01-09 11-13-25](https://user-images.githubusercontent.com/41955439/212530109-b07cce64-a5ac-4a56-93c2-dcf0cf78ec4d.png)
![Screenshot from 2023-01-09 11-47-51](https://user-images.githubusercontent.com/41955439/212530116-84b161fd-a5ec-42ca-8914-e2187dbee092.png)

https://user-images.githubusercontent.com/41955439/212530466-7c2e5210-51a9-4efd-af42-84a2c7104b4f.mp4

https://user-images.githubusercontent.com/41955439/227136596-065799f0-bfd9-42c0-8b01-026cfe4b9ee6.mp4


