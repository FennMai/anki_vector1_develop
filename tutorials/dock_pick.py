import anki_vector
from anki_vector.util import distance_mm, speed_mmps, degrees
import time

# 连接到Vector机器人
with anki_vector.Robot() as robot:
    # If necessary, move Vector's Head and Lift down
    robot.behavior.set_head_angle(degrees(-5.0))
    robot.behavior.set_lift_height(0.0)

    print("Connecting to a cube...")
    robot.world.connect_cube()
    time.sleep(2.0)
    #if robot.world.connected_light_cube:
    print("Begin cube docking...")
    dock_response = robot.behavior.dock_with_cube(
        robot.world.connected_light_cube,
        num_retries=3)
    if dock_response:
                docking_result = dock_response.result

    time.sleep(1)

    print("举")
    robot.behavior.pickup_object(robot.world.connected_light_cube, use_pre_dock_pose=False)


    # 等待Cube被拾起
    time.sleep(0.5)

    # 推动Cube
    print("推")
    drive_future = robot.behavior.drive_straight(distance_mm(500), speed_mmps(50))

    # 让机器人行驶2秒，模拟中途取消的操作
    time.sleep(4.0)

