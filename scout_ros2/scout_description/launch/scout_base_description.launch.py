import os
import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import FindExecutable, PathJoinSubstitution
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    model_name = 'scout_v2.xacro'
    pkg_share = launch_ros.substitutions.FindPackageShare(package='scout_description').find('scout_description')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/nav2_rviz.rviz')
    # model_path = os.path.join(get_package_share_directory('scout_description'), "urdf", model_name)
    # print(model_path)
    robot_description_content = Command([
        PathJoinSubstitution([FindExecutable(name="xacro")]), " ",
        PathJoinSubstitution(
            [FindPackageShare("scout_description"), "urdf", model_name]
        ),
    ])
    
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    )
    
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    robot_state_publisher = launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': launch.substitutions.LaunchConfiguration('use_sim_time'),
                'robot_description':robot_description_content
            }]
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        
        DeclareLaunchArgument('use_sim_time', default_value='false',
            description='Use simulation clock if true'),

        launch.actions.LogInfo(msg='use_sim_time: '),
        launch.actions.LogInfo(msg=launch.substitutions.LaunchConfiguration('use_sim_time')),
        
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        robot_state_publisher,
        joint_state_publisher_node,
        rviz_node
    ])
