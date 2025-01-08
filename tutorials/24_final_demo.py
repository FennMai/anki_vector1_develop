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
    robot.behavior.go_to_object(robot.world.connected_light_cube, distance_mm(200.0))
    
    #robot.motors.stop_all_motors()
    
    try:
        robot.anim.play_animation_trigger('GreetAfterLongTime')  # 开心的动画
        robot.behavior.set_eye_color(0.05, 0.95)  # 例如，设置为橙色 (开心的颜色)
        time.sleep(2)  # 等待动画完成
    except anki_vector.exceptions.VectorTimeoutException:
        print("动画加载超时，请重试或检查网络连接。")
    print("Begin cube docking...")
    dock_response = robot.behavior.dock_with_cube(
        robot.world.connected_light_cube,
        num_retries=3)
    if dock_response:
                docking_result = dock_response.result
    
    #if dock_response:
        #docking_result = dock_response.result
    
    # 确保机器人已完全启动，增加等待时间
    #time.sleep(2)

    # 让Vector跑到Cube旁边，距离Cube 70mm
    #robot.behavior.go_to_object(robot.world.connected_light_cube, distance_mm(20.0))

    # 等待Vector到达Cube位置
    time.sleep(1)

    # 设置开心的表情
    

    # 播放开心的动画，增加等待时间以确保动画触发
    #try:
        #robot.behavior.set_eye_color(0.05, 0.95)  # 例如，设置为橙色 (开心的颜色)
        #robot.anim.play_animation_trigger('DriveLoopAngry')  # 开心的动画
        #time.sleep(2)  # 等待动画完成
    #except anki_vector.exceptions.VectorTimeoutException:
        #print("动画加载超时，请重试或检查网络连接。")
    
    #robot.behavior.say_text("Yay! I'm happy!")

    # 让Vector举起Cube
    print("举")
    robot.behavior.pickup_object(robot.world.connected_light_cube, use_pre_dock_pose=False)


    # 等待Cube被拾起
    time.sleep(0.5)

    # 推动Cube
    print("推")
    drive_future = robot.behavior.drive_straight(distance_mm(500), speed_mmps(100))

    # 让机器人行驶2秒，模拟中途取消的操作
    time.sleep(2.0)

    

#else:
    #print("Cube未连接，请检查Cube是否正确放置并与Vector连接。")
