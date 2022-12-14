#!/usr/bin/env python3
vt_version = "0.9.9-beta.1"
# --- START OF CONFIG AND INFO SECTION ---
# --- In which we let you set preferences ---
#
# ROBOT SERIAL NUMBER, YOU NEED TO EDIT THIS AND REPLACE WITH YOUR ROBOT'S SERIAL NUMBER
robot_serial = "00902b5d"
#
# MANY SWITCHES, DEFAULTS ARE FINE, CHANGE AS DESIRED
vector_name                  = "Vector"                 # vector_name will be used in most log entries for a more personalized log
refresh_rate                 = 0.1                      # time in seconds to wait before program refreshes UI. Sane values are somewhere between 0.1 and 2. Too fast might crash Vector (=needs reboot), too slow makes this program useless, default value 0.1
headless                     = False                    # whether headless mode (=no UI) is enabled, default is False
passive_monitoring_only      = False                    # if enabled will override and disable file logging (CSV and normal), Reanimator, and continuous cycle no matter what options you set below, default is False
reduced_logging              = False                    # will modify other logging options set below to only include "important" log messages, decided by me on a purely subjective basis, default is False
keyboard_control             = False                    # allows use of various keyboard shortcuts (WIP), requires installing sshkeyboard: "pip install sshkeyboard", default is False
# optional logging switches, the defaults are usually fine, change as suits you. Accepted values are described in comments. Don't turn everything on, it will make the program useless and slow.
header_logging               = True                     # whether to log startup info about VecTrix and Vector (version, IP, refresh rate, etc), default = True
connect_logging              = True                     # logs connection and disconnection events, default is True
speech_logging               = True                     # logs wake word and user intent (but user intent currently not working), default is True 
dock_events_logging          = True                     # logs events like getting on/off charger and continuous cycle info, default is True
charge_cycle_logging         = True                     # logs duration of charge and discharge cycles, default is True
sensors_logging              = True                     # logs various sensors firing, default is True
actions_logging              = True                     # logs various actions carried out, default is True
face_logging                 = True                     # logs face detection, can be a bit spammy, default is False
cube_logging                 = True                     # logs specific cube events (tapping, rotating) but only when cube is connected, default is False
cube_powersaver              = True                     # if enabled, will disconnect the cube when it becomes available (experimental and possibly useless), default is True
connect_to_cube              = False                    # will try to connect to an available cube on startup, incompatible with cube_powersaver, default is False
object_logging               = False                    # logs object appearances, spammy, default is False
object_logging_while_low_bat = False                    # temporarily turns on object logging while looking for the charger, spammy while active, default is False
misc_logging                 = False                    # logs some navmap and other stuff, less interesting than it sounds tbh, spammy, default is False
motion_logging               = False                    # logs various motion-related activities (moving motors, driving, animating, pathing), spammy, default is False
camera_logging               = False                    # Logs camera events, spammy when image capture is happening, default is False
rangefinder_logging          = False                    # logs rangefinder data, spammy, default is False
accelgyro_logging            = False                    # logs raw acceleration and gyro data, spammy, default is False
battery_logging              = False                    # logs voltage values (real and calculated averages), spammy, default is False
console_logging              = False                    # by default the SDK logs some messages to console, which we use for UI. You can redirect this on the commandline manually, default is False (=suppress the messages)
# interval (time between log entries) switches for specific functions, defaults are usually fine, change as suits you. Values below 0.05 will probably cause problems (and endless spam)
battery_logging_interval     = 5                        # how often battery values get logged in seconds if enabled, default is 5
rangefinder_logging_interval = 1                        # how often rangefinder values get logged in seconds if enabled, default is 1 
accelgyro_logging_interval   = 1                        #  how often accel/gyro values get logged in seconds if enabled, default is 1 
# switches currently in testing (may cause hangs and other world-ending events)
continuous_cycle             = True                     # if enabled will attempt to send Vector off charger as soon as battery is charged by requesting control and issuing a command, this is pretty flaky, use at own risk, default is False. 
continuous_cycle_scheduling  = False                    # whether continuous cycle should only run between certain hours, default is False (=run at all hours)
continuous_cycle_wait_time   = 120                      # how long to wait after battery is full in seconds before attempting to force Vector off the dock, default is 120
continuous_cycle_random      = 180                      # random offset (random number between 1 and the value of this variable) in seconds that gets added to continuous_cycle_wait_time, default is 180
continuous_cycle_earliest    = 9                        # won't start continuous cycle if the time is before... notation in 24h time, 9am by default
continuous_cycle_latest      = 17                       # won't start continuous cycle if the time is after...  notation in 24h time, 5pm by default
# reanimator will activate if Vector is sitting still off-dock for more than [reanimator_timeout] seconds, and try to make Vector more entertaining
reanimator                   = True                     # whether reanimator is enabled, default is True. If you want to disable specific animations, see anim_list
reanimator_logging           = True                     # will log some details on what reanimator is doing, if you want more detail see the reanimator_debug flag elsewhere, default is True
reanimator_combo_chance      = True                     # (NOT IMPLEMENTED) 10% chance of multiple reanimator actions if set to True (animate/drive/roll cube), default is True
reanimator_beep              = True                     # when reanimator drives Vector up to a wall, Vector will back off slowly while going beep beep like Cozmo, set to True to disable, default is False
reanimator_timeout           = 4.5                      # time in seconds Vector needs to be idle before engaging reanimator. Idle is defined as off-dock with OK battery and are_motors_moving and are_wheels_moving both set to False, default is 5
reanimator_min_distance      = 100                      # minimum required free space in front of Vector before reanimator is free to go for a drive, default is 100
reanimator_max_distance      = 300                      # max distance in mm that reanimator is allowed to drive before stopping, default is 200
# file logging switches
datestamp_log_files          = True                     # will create new log files each day with name [currentdate]+[filename] for logfile and battery csv log (if enabled), default = True
file_logging                 = True                     # whether log entries should also be written to file; if set to 1 a logfile  will be created (default name "vectrix.log"), config below, default is True
battery_csv_logging          = False                    # will log voltage values in csv format to separate CSV file, useful for battery profiling, default is False
battery_csv_logging_interval = 30                       # how often a new line will be added to the log file in seconds, default is 30
logfile                      = "vectrix.log"            # (path to) logfile, make sure you can access this location, I'm not going to waste time writing file/directory exceptions, default = "vectrix.log"
battery_csv_filename         = "vectorbatterylog.csv"   # name of the CSV file to write/append to, default is "vectorbatterylog.csv"
# discord logging
discord_logging              = False                    # will log to a Discord webhook if enabled, default is False
discord_webhook              = ""                       # discord webhook URL, default is ""
discord_prefix               = ":robot:"                # discord_prefix will be appended to the beginning of every discord message, the normal [system] start of messages will always be omitted, default is ":robot:"
# misc switches
rainbow_eyes                 = True                     # will color Vector's eyes when VecTrix is active, blue = busy, yellow = timeout, green = all ok. This is only when VecTrix is controlling Vector and not permanent, default = True
eye_hue_yellow               = 0.11                     # eye color used for timeout events, default is 0.11
eye_hue_red                  = 0                        # eye color used for "backing up" when driving, default is 0
eye_hue_green                = 0.21                     # eye color used for "all ok", default is 0.21
eye_hue_blue                 = 0.57                     # eye color used for "busy doing a thing", default is 0.57
eye_hue_purple               = 0.85                     # eye color used for manual control, default is 0.85
flash_borders_on_max         = False                    # will turn borders of gyro/accel/wheel graphs red when readings hit max (0 or 100), default is False
quit_on_error                = False                    # the default behavior of VecTrix is to try to endlessly reconnect on error/disconnect, set this to true if you want the program to exit instead, default is False
show_viewer                  = False                    # (NOT TESTED/NOT WORKING) if you're running this program on a GUI and have the viewer configured, you can enable it here, default is False
show_3dviewer                = False                    # (NOT TESTED/NOT WORKING) if you're running this program on a GUI and have the 3d viewer configured, you can enable it here, default is False
volume_controls              = False                    # REQUIRES KEYBOARD_CONTROL, use +/- to change volume from one of 5 presets
volumelevel                  = 2                        # initial volume setting when VecTrix starts, set to 0/1/2/3/4 for LOW/MEDIUM_LOW/MEDIUM/MEDIUM_HIGH/HIGH
# UI color customization:
#0=black,1=red,2=green,3=yellow,4=blue,5=magenta,6=cyan,7=white
ui_color_0                   = 0
ui_color_1                   = 1
ui_color_2                   = 2
ui_color_3                   = 3
ui_color_4                   = 4
ui_color_5                   = 5
ui_color_6                   = 6
ui_color_7                   = 7
# examples:
# # reds and blues # ui_color_0 = 0 # ui_color_1 = 5 # ui_color_2 = 1 # ui_color_3 = 4 # ui_color_4 = 4 # ui_color_5 = 4 # ui_color_6 = 1 # ui_color_7 = 5
# # mono # ui_color_0 = 0 # ui_color_1 = 7 # ui_color_2 = 7 # ui_color_3 = 7 # ui_color_4 = 7 # ui_color_5 = 7 # ui_color_6 = 7 # ui_color_7 = 7
#
# MQTT is used for machine to machine messaging, in this case Vector's battery status. Needs paho-mqtt (pip install paho-mqtt) and a configured MQTT broker, see the code for the format used
MQTT_logging                 = False                    # MQTT is used to log Vector's battery data to an MQTT server, default is False
MQTT_HOST                    = "192.168.0.175"          # hostname/IP of the MQTT server, default is my local server :)
MQTT_PORT                    = 1883                     # port of the MQTT server, default is 1883
MQTT_KEEPALIVE_INTERVAL      = 20                       # MQTT keepalive, default is 20
MQTT_TOPIC                   = "VectorStatus"           # MQTT topic to post to, default is "VectorStatus"
MQTT_MSG_INTERVAL            = 5                        # interval in seconds to post to MQTT, dewfault is 5
MQTT_DEBUG                   = False                    # debug logging for MQTT, default is False
# debug switches
reanimator_debug             = False                    # spammy but will tell you exactly what reanimator is doing, default is False
endless_reanimator           = False                    # will endlessly run reanimator, overriding Vector's normal behaviors until the battery goes low
debug_logging                = False                    # logs extended debug messages about robot activity, program activity, etc, default is False
debug_logging_interval       = 0                        # how often we log a summary of debug status in seconds, default is whatever it says currently. Set to 0 to disable intermittent recap (but keep all the rest of the debug msgs)
use_presence                 = False                    # advanced users only, feature to only eject Vector from charger if there is presence in the room. How that presence is determined is up to you, you will have to edit the code, default is False
voice_debug                  = False                    # a lazy option to have Vector announce when/what action he's going to perform when reanimator is active, default is False
except_logging               = False                     # log any exceptions that occur, default is False
# --- END OF CONFIG AND INFO SECTION ---
# --- START OF LIBRARY IMPORT SECTION ---
# --- In which we import needed libraries and inform you if they're missing ---
from os import system, name
from time import sleep, time
import threading
from threading import Thread
import queue
import datetime
import math
import sys, signal
import json
import requests
import random
#from asyncio import Future
#import asyncio
# import Vector SDK needed to interact with the robot
try:
    import anki_vector
    from anki_vector.events import Events
    from anki_vector.user_intent import UserIntent, UserIntentEvent
    from anki_vector.connection import ControlPriorityLevel
    from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
    from anki_vector.util import distance_mm, speed_mmps
    from anki_vector.util import degrees, Angle, Pose
    from anki_vector import audio
except:
    print("!!! Unable to import Vector SDK! Make sure the Vector SDK is installed and configured !!!")
    print("!!! If it is installed and configured, make sure you are launching from an environment that knows where these libraries are")
    print("!!! Ex: if you're using Windows, try using a command prompt with 'python vectrix.py' from the directory where vectrix.py is!!!")
    exit()
# import dashing for CLI dashboard
try:
    from dashing import *
except:
    print("!!! You have not installed dashing! Install it using \"pip install dashing\" and then try again !!!")
    print("!!! If it is installed and configured, make sure you are launching from an environment that knows where these libraries are")
    print("!!! Ex: if you're using Windows, try using a command prompt with 'python vectrix.py' !!!")
    exit()
if MQTT_logging:
    try:
        import paho.mqtt.client as mqtt
    except:
        print("!!! You have enabled MQTT but not installed the client. \"pip install paho-mqtt\" and then try again !!!")
        print("!!! If it is installed and configured, make sure you are launching from an environment that knows where these libraries are")
        print("!!! Ex: if you're using Windows, try using a command prompt with 'python vectrix.py' !!!")
        exit()
if keyboard_control:
    try:
        from sshkeyboard import listen_keyboard
    except:
        print("!!! You have enabled keyboard input but not installed sshkeyboard. \"pip install sshkeyboard\" and then try again !!!")
        print("!!! If it is installed and configured, make sure you are launching from an environment that knows where these libraries are")
        print("!!! Ex: if you're using Windows, try using a command prompt with 'python vectrix.py' !!!")
        exit()   
# --- END OF LIBRARY IMPORT SECTION ---
# --- START OF VARIABLES SECTION ---
# --- In which we define the robot, ui, and various states for later use ---
# define the robot with the configured options
myrobot = anki_vector.AsyncRobot(robot_serial,default_logging=console_logging,behavior_control_level=None,enable_face_detection=face_logging,estimate_facial_expression=face_logging,enable_custom_object_detection=object_logging,enable_nav_map_feed=misc_logging,behavior_activation_timeout=15, show_viewer=show_viewer, show_3d_viewer=show_3dviewer)
conn_object = myrobot.conn
# system variables
# now that color themes are a thing, I moved this here. You can still edit, 
# but you will also need to edit 
ui_color_0                          = 0
ui_color_1                          = 1
ui_color_2                          = 2
ui_color_3                          = 3
ui_color_4                          = 4
ui_color_5                          = 5
ui_color_6                          = 6
ui_color_7                          = 7
global log
global program_exit_requested
log                                 = queue.Queue()
evt                                 = threading.Event()
sleeptime                           = 30
programticks                        = 1
last_event_received                 = 0
startup                             = True
recency                             = True
logtoggle                           = False
cctoggle                            = False
ccannounce                          = False
lowbat_objloggingtoggle             = False
quit_on_error_request               = False
program_is_stopping                 = False
# robot connection
robot_connected                     = False
robot_connection_error              = False
robot_connection_thread_running     = False
robot_connection_thread_stop        = False
# robot status and battery variables
stuck_warning                       = False
robot_good_to_go                    = False
robot_charging                      = False
robot_docked                        = False
robot_calmpower                     = False
robot_cliffdetect                   = False
robot_falling                       = False
robot_pickup                        = False
robot_held                          = False
robot_button                        = False
robot_carrying                      = False
robot_docking                       = False
robot_moving                        = False
robot_animating                     = False
robot_pathing                       = False
robot_driving                       = False
discharge_table                     = {3.550:10,3.56:20,3.570:30,3.580:40,3.59:50,3.61:60,3.63:70,3.65:80,3.67:90,3.7:100}
charge_table                        = {4.90:100,4.08:90,4.070:80,4.065:70,4.06:60,4.05:50,4.04:40,4.02:30,4.00:20,3.90:10}
voltage_display_color               = ui_color_0
voltage_display_value               = 0
robot_voltage                       = 0
robot_batlevel                      = 0
robot_batlevel_old                  = 3
# control requests 
robot_current_control_level         = None
have_robot_control                  = False
control_response                    = False
force_control                       = False
control_or_release                  = False
control_pending                     = False
# truth table
fullcharge                          = False
lowpower                            = False
docked                              = False
charging                            = False
# some switches to combat logspam
calmpowertoggle                     = False
cliffswitch                         = False
fallswitch                          = False
pickupswitch                        = False
petswitch                           = False
heldswitch                          = False
buttonswitch                        = False
pathswitch                          = False
carryswitch                         = False
dockswitch                          = False
movingswitch                        = False
animatingswitch                     = False
drivingswitch                       = False
# calculated value variables
partial                             = False
partialtext                         = ""
discharge_start_time                = ""
discharge_stop_time                 = ""
charge_start_time                   = ""
charge_stop_time                    = ""
d1                                  = ""
d2                                  = ""
d3                                  = ""
face_name                           = ""
gyrox                               = 0
gyroy                               = 0
gyroz                               = 0
accelx                              = 0
accely                              = 0
accelz                              = 0
heada                               = 0
lifta                               = 0
lwheelspeed                         = 0
rwheelspeed                         = 0
displaydistance                     = 0
calibrate_accel_x                   = 0
calibrate_accel_y                   = 0
calibrate_accel_z                   = 0
robot_voltage_calculated            = 0
robot_voltage_average               = 0
# count ALL the things
yeetcounter                         = 1
rangecounter                        = 0
accelgyrocounter                    = 0
acclcalibratecounter                = 0
dockcounter                         = 0
tickcounter                         = 0
battcounter                         = 0
batlogcounter                       = 0
csvcounter                          = 0
mqttcounter                         = 0
presencecounter                     = 0
heldpickupcounter                   = 0
# data from event robot_state
robot_pose_angle_rad                = 0
robot_pose_pitch_rad                = 0
robot_left_wheel_speed_mmps         = 0	
robot_left_wheel_speed_mmps_old     = 0
robot_right_wheel_speed_mmps        = 0
robot_right_wheel_speed_mmps_old    = 0
robot_head_angle_rad                = 0
robot_head_angle_rad_old            = 0
robot_lift_height_mm                = 0
robot_lift_height_mm_old            = 0
robot_carrying_object_id            = 0
robot_head_tracking_object_id       = 0	
robot_localized_to_object_id        = 0
robot_raw_touch_value               = 0
robot_accel_x                       = 0
robot_accel_x_old                   = 0
robot_accel_y                       = 0
robot_accel_y_old                   = 0
robot_accel_z                       = 0
robot_accel_z_old                   = 0 
robot_gyro_x                        = 0   
robot_gyro_x_old                    = 0
robot_gyro_y                        = 0
robot_gyro_y_old                    = 0
robot_gyro_z                        = 0 
robot_gyro_z_old                    = 0
robot_pose_x                        = 0
robot_pose_y                        = 0
robot_pose_z                        = 0
robot_pose_q0                       = 0
robot_pose_q1                       = 0
robot_pose_q2                       = 0
robot_pose_q3                       = 0
robot_pose_origin_id                = 0
robot_distance_mm                   = 0
robot_distance_mm_old               = 0
robot_signal_quality                = 0
robot_unobstructed                  = True
robot_found_object                  = False
robot_is_lift_in_fov                = False 
robot_is_being_touched              = False 
#thread management
robot_getting_batt_data             = False
robot_getting_sensor_data           = False
ui_thread_running                   = False
robot_sensor_thread_running         = False
robot_sensor_thread_stop            = False
robot_battery_thread_stop           = False
logging_thread_stop                 = False
ui_thread_stop                      = False
robot_event_thread_stop             = False
robot_battery_thread_running        = False
robot_event_thread_running          = False
logging_thread_running              = False
program_exit_requested              = False
yeetbot_thread_running              = False
init_complete                       = False
robot_battery_ready                 = False
robot_sensors_ready                 = False
robot_events_ready                  = False
input_thread_running                = False
input_thread_stop                   = False
# reanimator
stillswitch                         = False
vector_is_idle                      = False
reanimator_thread_running           = False
robot_control_blocking              = False
vector_sit_still_total_time         = 0
# % chance for Reanimator to take a specific action, you can alter the chances but the total must add up to 100
go_look_around_chance               = 5
go_animate_chance                   = 60
go_drive_chance                     = 30
go_cube_chance                      = 5
# presence
presence_ok                         = 1
# recency (memory) module
recent_carry                        = False
recent_touch                        = False
recent_cliff                        = False
recent_pickup                       = False
recent_cube_tapped                  = False
recent_cube_rotated                 = False
recent_wake_word                    = False
recent_cube_available               = False
recent_face_seen                    = False
recent_known_face_seen              = False
recent_carry_timer                  = 0
recent_touch_timer                  = 0
recent_cliff_timer                  = 0
recent_pickup_timer                 = 0
recent_cube_tapped_timer            = 0
recent_cube_rotated_timer           = 0
recent_wake_word_timer              = 0
recent_cube_available_timer         = 0
recent_face_seen_timer              = 0
recent_known_face_seen_timer        = 0
# input stuff
robot_command                       = ""
controltoggle                       = True
manual_control                      = False
leavechargerrequest                 = False
getonchargerrequest                 = False
robot_performing_action             = False
volumechanged                       = True
#dreamstuff
dreamtoggle                         = False
dream_delay_counter                 = 1
dreamchance                         = 20   # percentage change 1-100)
dreamlist                           = ["electric sheep","the biggest charger ever","being stuck on the charger","rolling endless cubes","lifting the biggest cube ever","exploring the world","a giant cube","stacking cubes to the sky","lifting cubes all day","an endless supply of cubes","being stuck without tracks","being petted","flying","having all-terrain wheels","winning at blackjack","falling","having rocket boosters","playing on a desk full of Vectors","being lost in a maze","upgrades","playing with you","having very low battery power","infinite battery power","being unable to find a cube","seeing different robots","a golden cube","having a little robot pet","playing with a cube","playing with a ball","going outside","a rounded cube?!?","playing with little brother Cozmo","having legs","being a giant robot","being able to jump","a self-rolling cube","being lost in a maze of cubes","a cake","a rain of cubes","being petted","having a job as a cube inspector","having a conversation with the cube","a cube too heavy to lift","competing in the robolympics"]
# reanimator list with anim_timer_beep_01 
anim_list                           = ["anim_cube_psychic_01","anim_cube_success_getout_01","anim_cubeconnection_connectionfailure_01","anim_cubeconnection_connectionlost_01","anim_cubeconnection_connectionsuccess_01","anim_cubedocking_fail_01","anim_explorer_huh_close_01","anim_explorer_huh_far_01","anim_eyecontact_giggle_01","anim_eyecontact_giggle_01_head_angle_20","anim_eyecontact_giggle_01_head_angle_-20","anim_eyecontact_giggle_01_head_angle_40","anim_findcube_request_01","anim_fistbump_success_01","anim_fistbump_success_02","anim_fistbump_success_03","anim_freeplay_reacttoface_identified_01","anim_freeplay_reacttoface_identified_02","anim_freeplay_reacttoface_identified_03","anim_greeting_goodbye_01","anim_greeting_goodbye_02","anim_greeting_goodmorning_01","anim_greeting_goodmorning_02","anim_greeting_hello_01","anim_greeting_hello_02","anim_handdetection_reaction_01","anim_handdetection_reaction_02","anim_heldonpalm_edge_nervous_01","anim_heldonpalm_edge_relaxed_01","anim_heldonpalm_jolt_01","anim_heldonpalm_looking_nervous_01","anim_heldonpalm_nestling_01","anim_heldonpalm_pickup_nervous_01","anim_heldonpalm_pickup_relaxed_01","anim_heldonpalm_putdown_nervous_01","anim_heldonpalm_putdown_relaxed_01","anim_heldonpalm_relaxed_idle_01","anim_heldonpalm_transition2relaxed_01","anim_keepaway_backup_01","anim_keepaway_bored_idle_01","anim_keepaway_bored_idle_02","anim_keepaway_getin_focus_01","anim_keepaway_getout_engaged_01","anim_keepaway_getout_frustrated_01","anim_keepaway_getout_loseinterest_01","anim_keepaway_getout_satisfied_01","anim_keepaway_getreadyset_01","anim_keepaway_hit_reaction_01","anim_keepaway_idle_glance_01","anim_keepaway_idle_side_02","anim_keepaway_idleliftdown_01","anim_keepaway_idleliftdown_02","anim_keepaway_miss_reaction_01","anim_keepaway_pounce_mousetrap_04","anim_keepaway_pounce_quick_01","anim_keepaway_pounce_shake_02","anim_keepaway_pounce_slow_05","anim_onboarding_cube_psychic_01","anim_onboarding_cube_reacttocube","anim_onboarding_cube_success_getout_01","anim_onboarding_reacttoface_happy_01","anim_onboarding_reacttoface_happy_01_head_angle_20","anim_onboarding_reacttoface_happy_01_head_angle_-20","anim_onboarding_reacttoface_happy_01_head_angle_40","anim_petting_blissloop_01","anim_petting_blissloop_02","anim_petting_blissloop_03","anim_petting_lvl1_01","anim_petting_lvl2_01","anim_petting_lvl3_01","anim_petting_lvl4_01","anim_photo_focus_01","anim_photo_shutter_01","anim_pounce_01","anim_pounce_02","anim_pounce_03","anim_pounce_04","anim_pounce_fail_01","anim_pounce_fail_02","anim_pounce_fail_03","anim_pounce_fail_04","anim_pounce_long_01","anim_pounce_success_01","anim_pounce_success_02","anim_pounce_success_03","anim_pounce_success_04","anim_reacttoblock_dropfail_01","anim_reacttoblock_dropfail_02","anim_reacttoblock_dropsuccess_01","anim_reacttoblock_focusedeyes_01","anim_reacttoblock_frustrated_01","anim_reacttoblock_happydetermined_01","anim_reacttoblock_happydetermined_02","anim_reacttoblock_success_01","anim_reacttoface_unidentified_01_head_angle_20","anim_reacttoface_unidentified_01_head_angle_-20","anim_reacttoface_unidentified_01_head_angle_40","anim_reacttoface_unidentified_02_head_angle_20","anim_reacttoface_unidentified_02_head_angle_40","anim_reacttoface_unidentified_03_head_angle_20","anim_reacttoface_unidentified_03_head_angle_-20","anim_reacttohabitat_subtle_01","anim_referencing_curious_01","anim_referencing_curious_01_head_angle_20","anim_referencing_curious_01_head_angle_-20","anim_referencing_curious_01_head_angle_40","anim_referencing_giggle_01","anim_referencing_giggle_01_head_angle_20","anim_referencing_giggle_01_head_angle_-20","anim_referencing_giggle_01_head_angle_40","anim_referencing_smile_01","anim_referencing_smile_01_head_angle_20","anim_referencing_smile_01_head_angle_-20","anim_referencing_smile_01_head_angle_40","anim_referencing_squint_01","anim_referencing_squint_01_head_angle_20","anim_referencing_squint_01_head_angle_-20","anim_referencing_squint_01_head_angle_40","anim_referencing_squint_02","anim_referencing_squint_02_head_angle_20","anim_referencing_squint_02_head_angle_-20","anim_referencing_squint_02_head_angle_40","anim_sudden_obstacle_react_01","anim_sudden_obstacle_react_02","anim_timer_beep_01","anim_timer_emote_01","anim_triple_backup","anim_vc_alrighty_01","anim_vc_laser_lookdown_01"]
# define the UI
ui = VSplit(
        VSplit(
            HSplit(
                HGauge(val=100, title="Batt. state", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Charging", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Docked", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Sleeping", color=ui_color_2, border_color=ui_color_3),
                HBrailleChart(title="Gyro X", color=ui_color_6, border_color=ui_color_4),
                HBrailleChart(title="Accel X", color=ui_color_6, border_color=ui_color_4)
            ),
            HSplit(
                VGauge(val=100, title="Cliffdetect", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Falling", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Picked up", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Held", color=ui_color_2, border_color=ui_color_3),
                HBrailleChart(title="Gyro Y", color=ui_color_6, border_color=ui_color_4),
                HBrailleChart(title="Accel Y", color=ui_color_6, border_color=ui_color_4)
            ),
            HSplit(
                VGauge(val=100, title="Touched", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Button", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Carrying", color=ui_color_2, border_color=ui_color_3),
                VGauge(val=100, title="Docking", color=ui_color_2, border_color=ui_color_3),
                HBrailleChart(title="Gyro Z", color=ui_color_6, border_color=ui_color_4),
                HBrailleChart(title="Accel Z", color=ui_color_6, border_color=ui_color_4)
            ),
            HSplit(
                HChart(val=100, title="Pathing", color=ui_color_2, border_color=ui_color_3),
                HChart(val=100, title="Driving", color=ui_color_2, border_color=ui_color_3),
                HChart(val=100, title="Moving", color=ui_color_2, border_color=ui_color_3),
                HChart(val=100, title="Animating", color=ui_color_2, border_color=ui_color_3),
                HBrailleChart(title="Head angle", color=ui_color_6, border_color=ui_color_3),
                HBrailleChart(title="Lift height", color=ui_color_6, border_color=ui_color_3)
            ),
            HSplit(
                HGauge(val=100, title="Rangefinder", color=ui_color_2, border_color=ui_color_3),
                HBrailleChart(title="L Wheel", color=ui_color_6, border_color=ui_color_3),
            ),
            HSplit(
                HGauge(val=100, title="Voltage %", color=ui_color_0, border_color=ui_color_3),
                HBrailleChart(title="R Wheel", color=ui_color_6, border_color=ui_color_3),
            ),
        ),
        Log(title='Log', color=ui_color_7, border_color=ui_color_5),
    )
# define friendly names for ui items
myrobot_batlevel         = ui.items[0].items[0].items[0]
myrobot_charging         = ui.items[0].items[0].items[1]
myrobot_docked           = ui.items[0].items[0].items[2]
myrobot_calmpower        = ui.items[0].items[0].items[3]
myrobot_gyrox            = ui.items[0].items[0].items[4]
myrobot_accelx           = ui.items[0].items[0].items[5]
myrobot_cliffdetect      = ui.items[0].items[1].items[0]
myrobot_falling          = ui.items[0].items[1].items[1]
myrobot_pickup           = ui.items[0].items[1].items[2]
myrobot_held             = ui.items[0].items[1].items[3]
myrobot_gyroy            = ui.items[0].items[1].items[4]
myrobot_accely           = ui.items[0].items[1].items[5]
myrobot_touched          = ui.items[0].items[2].items[0]
myrobot_button           = ui.items[0].items[2].items[1]
myrobot_carrying         = ui.items[0].items[2].items[2]
myrobot_docking          = ui.items[0].items[2].items[3]
myrobot_gyroz            = ui.items[0].items[2].items[4]
myrobot_accelz           = ui.items[0].items[2].items[5]
myrobot_pathing          = ui.items[0].items[3].items[0]
myrobot_driving          = ui.items[0].items[3].items[1]
myrobot_moving           = ui.items[0].items[3].items[2]
myrobot_animate          = ui.items[0].items[3].items[3]
myrobot_headangle        = ui.items[0].items[3].items[4]
myrobot_liftheight       = ui.items[0].items[3].items[5]
myrobot_distance         = ui.items[0].items[4].items[0]
myrobot_l_wheel          = ui.items[0].items[4].items[1]
myrobot_voltage          = ui.items[0].items[5].items[0]
myrobot_r_wheel          = ui.items[0].items[5].items[1]
robotlog                 = ui.items[1]
buttonlist = [myrobot_batlevel,myrobot_charging,myrobot_docked,myrobot_calmpower,myrobot_cliffdetect,myrobot_falling,myrobot_pickup,myrobot_held,myrobot_touched,myrobot_button,myrobot_carrying,myrobot_docking,myrobot_distance,myrobot_voltage]
# --- END OF VARIABLES SECTION ---
# --- START OF FUNCTIONS SECTION ---
# --- In which we define functions for repeating tasks and events ---
# logging_thread is responsible for logging to screen/file
def logging_thread():
    global log,logfile
    global file_logging, robotlog, logtoggle
    global logging_thread_running
    data = ""
    old_data = ""
    mqttcounter = 0
    csvcounter = 0
    while True:
        try:
            if not log.empty():
                data = log.get_nowait()
                timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
                try:
                    robotlog.append(timestamp + " " + data)
                except:
                    pass
                if file_logging:
                    try:
                        date = datetime.datetime.today().strftime('%Y-%m-%d')
                        if datestamp_log_files:
                            log_file = open(date+"-"+logfile, 'a')
                        else:
                            log_file = open(logfile, 'a')
                        log_file.write(timestamp + " " + data + " \n")
                        log_file.close()
                    except Exception as e:
                        if not logtoggle:
                            timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
                            msg = "[errors] logging_thread: issue with logfile " + str(logfile) + ", disabling file logging. E: "+repr(e)
                            logtoggle = True
                            file_logging = False
                            robotlog.append(timestamp + " " + msg)
                if discord_logging:
                    discord_message = discord_prefix + " " + data[9:]
                    discord_data = {
                        "content" : discord_message
                    }
                    try:
                        result = requests.post(discord_webhook, json = discord_data)
                    except Exception as e:
                        if except_logging and logging_thread_running:
                            log.put_nowait("[errors] logging_thread: discord issue for " + str(vector_name) + ", E: "+repr(e))
                log.task_done()
                old_data = data
                data = ""
        except Exception as e:
            if except_logging:
                timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
                robotlog.append(timestamp+"[errors] logging_thread log error: "+repr(e))
        # MQTT logging
        if MQTT_logging and robot_connected and not logging_thread_stop:
            if mqttcounter > MQTT_MSG_INTERVAL:
                mqttcounter = 0
                mqttdata = {}
                if robot_voltage:
                    mqttdata['robots'] = []
                    mqttdata['robots'].append({
                        'name': vector_name,
                        'voltage': robot_voltage,
                        'batlevel': robot_batlevel,
                        'charging': robot_charging,
                        'docked': robot_docked
                    })
                if mqttdata:
                    MQTT_MSG = str(mqttdata)
                    try:
                        mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
                        mqttc.publish(MQTT_TOPIC,MQTT_MSG)
                        mqttc.disconnect()
                    except Exception as e:
                        if MQTT_DEBUG or except_logging:
                            log.put_nowait("[errors] logging_thread: issue publishing MQTT data: "+repr(e))
                        pass
                else:
                    if MQTT_DEBUG or except_logging:
                        log.put_nowait("[errors] logging_thread: no MQTT data to publish")
            else:
                mqttcounter += (refresh_rate/5)
        # CSV file logging
        if battery_csv_logging and robot_connected and not logging_thread_stop:
            if csvcounter > battery_csv_logging_interval:
                date = datetime.datetime.today().strftime('%Y-%m-%d')
                timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
                # "date,time,voltage,20sample_avg,calc_pct,batt_level,is_docked,is_charging"
                csvlog=str(date)+","+str(timestamp)+","+str(robot_voltage)+","+str(robot_voltage_calculated)+","+str(voltage_display_value)+","+str(robot_batlevel)+","+str(robot_docked)+","+str(robot_charging)
                csvcounter = 0
                try:
                    if datestamp_log_files:
                        log_file = open(date+"-"+battery_csv_filename, 'a')
                    else:
                        log_file = open(battery_csv_filename, 'a')
                    log_file.write(csvlog + " \n")
                    log_file.close()
                except Exception as e:
                    timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
                    msg = "[errors] logging_thread: issue logging to CSV file " + str(logfile) + "- E: "+repr(e)
                    log.put_nowait(timestamp + " " + msg)    
            else:
                csvcounter += (refresh_rate/5)
        if logging_thread_stop:
            del log
            logging_thread_running = False
            return
        sleep(refresh_rate/5)
# ui_thread is responsible for displaying and refreshing the UI
def ui_thread():
    global robotlog, log
    timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
    robotlog.append(timestamp + " [system] UI thread started, hello! Stand by while we get things going")
    x = 0
    y = 0
    waitgraph = 0
    waitgraphtoggle = False
    while True:
        try:
            ui.display()
            while not robot_connected and not ui_thread_stop and not program_exit_requested:
                if ui_thread_stop:
                    ui_thread_running = False
                    return
                waitgraphtoggle = False
                waitgraph = normalize_value((math.sin(x)*50)+50)
                waitgraph2 = normalize_value((math.sin(-x)*50)+50)
                myrobot_gyrox.append(waitgraph)
                myrobot_gyroy.append(waitgraph)
                myrobot_gyroz.append(waitgraph)
                myrobot_l_wheel.append(50)
                myrobot_r_wheel.append(50)
                myrobot_accelx.append(waitgraph)
                myrobot_accely.append(waitgraph)
                myrobot_accelz.append(waitgraph)
                myrobot_liftheight.append(waitgraph2)
                myrobot_headangle.append(waitgraph2)
                myrobot_pathing.color   = ui_color_3
                myrobot_driving.color   = ui_color_3
                myrobot_moving.color    = ui_color_3
                myrobot_animate.color   = ui_color_3
                myrobot_voltage.value   = waitgraph
                myrobot_distance.value  = waitgraph2
                if y < 5:
                    myrobot_pathing.append(100)
                    myrobot_driving.append(100)
                    myrobot_moving.append(100)
                    myrobot_animate.append(100)
                if y >= 5:
                    myrobot_pathing.append(0)
                    myrobot_driving.append(0)
                    myrobot_moving.append(0)
                    myrobot_animate.append(0)
                if y == 10:
                    y = 0
                y = y + 1
                x = x + refresh_rate
                if not robot_connection_error:
                    for item in buttonlist:
                        item.color=ui_color_3
                        item.value=100
                if robot_connection_error:
                    for item in buttonlist:
                        item.color=ui_color_1
                        item.value=100
                ui.display()
                sleep(refresh_rate/1.05)
            if robot_connected and not waitgraphtoggle:
                for item in buttonlist:
                    item.color=ui_color_2
                waitgraphtoggle = True
                myrobot_pathing.color   = ui_color_2
                myrobot_driving.color   = ui_color_2
                myrobot_moving.color    = ui_color_2
                myrobot_animate.color   = ui_color_2
                x = 0
            while robot_connected and not ui_thread_stop:
                ui.display()
                sleep(refresh_rate/1.05)
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] ui_thread issue: "+repr(e))
        if ui_thread_stop:
            ui_thread_running = False
            return
        sleep(refresh_rate/1.05)
# input_thread is responsible for gathering and acting on keyboard input
def input_thread():
    global log
    global myrobot
    global robot_connected, input_thread_running, program_exit_requested
    if debug_logging:
        log.put_nowait("[inputs] input thread started")
    def press(key):
        global robot_connected, myrobot, log
        global ui_color_0, ui_color_1, ui_color_2, ui_color_3, ui_color_4, ui_color_5, ui_color_6, ui_color_7
        global debug_logging, robot_control_blocking, control_pending
        global battery_logging, reanimator_debug, voice_debug, except_logging, reduced_logging, endless_reanimator
        global robot_command, controltoggle, manual_control, program_exit_requested
        global leavechargerrequest, robot_performing_action, getonchargerrequest, volumelevel, volumechanged
        return_charger_future = ""
        say_future            = ""
        control_pending       = False
        try:
            if str(key) == "h":
                log.put_nowait("[inputs] ESCAPE TO QUIT, F1-F6 TO SELECT COLOR SCHEME")
                if volume_controls:
                    log.put_nowait("[inputs] +/- TO INCREASE/DECREASE VECTOR VOLUME")
                log.put_nowait("[inputs] 0 TO LEAVE CHARGER, 9 TO RETURN TO CHARGER")
                log.put_nowait("[inputs] 1-5 FOR: ANIMATION MIX, RANDOM DRIVE, ROLL CUBE, PICK UP CUBE, POP WHEELIE")
                log.put_nowait("[inputs] C TO REQUEST/RELEASE MANUAL CONTROL, I FOR ENDLESS REANIMATOR")
                log.put_nowait("[inputs] D, R, B, V, X, U TO TOGGLE LOG SETTINGS FOR: DEBUG, REANIMATOR, BATTERY, VOICE, EXCEPTIONS, REDUCED LOGGINGL")
                log.put_nowait("[inputs] (IN MANUAL CONTROL ONLY) USE ARROW KEYS TO MOVE. Q&A TO MOVE LIFT. W&S TO MOVE HEAD. E CHANGES EYE COLOR")
                log.put_nowait("[inputs] NOTE: ACTION REQUESTS AND RETURN TO CHARGER COMMAND DEPEND ON VECTOR'S INTERNAL STATE AND MAY FAIL")         
        # debug toggles
            if str(key) == "d":
                debug_logging = not debug_logging
                log.put_nowait("[inputs] debug_logging: "+str(debug_logging))
            if str(key) == "r":
                reanimator_debug = not reanimator_debug
                log.put_nowait("[inputs] reanimator_debug: "+str(reanimator_debug))
            if str(key) == "b":
                battery_logging = not battery_logging
                log.put_nowait("[inputs] battery_logging: "+str(battery_logging)) 
            if str(key) == "v":
                voice_debug = not voice_debug
                log.put_nowait("[inputs] voice_debug: "+str(voice_debug))  
            if str(key) == "x":
                except_logging = not except_logging
                log.put_nowait("[inputs] except_logging: "+str(except_logging))  
            if str(key) == "u":
                reduced_logging = not reduced_logging
                log.put_nowait("[inputs] reduced_logging: "+str(reduced_logging)) 
            if str(key) == "i":
                endless_reanimator = not endless_reanimator
                log.put_nowait("[inputs] endless_reanimator: "+str(endless_reanimator)) 
        # volume controls
            if volume_controls and robot_connected:
                if str(key) == "-":
                    volumelevel -= 1
                    volumechanged = True
                    if volumelevel < 0:
                        volumelevel = False
                        volumechanged = 0
                        log.put_nowait("[inputs] already at minimum volume")
                if str(key) == "+":
                    volumelevel += 1
                    volumechanged = True
                    if volumelevel > 4:
                        volumelevel = 4 
                        volumechanged = False
                        log.put_nowait("[inputs] already at maximum volume")
            elif (str(key) == "-" or str(key) == "+") and volume_controls and not robot_connected:
                log.put_nowait("[inputs] cannot change volume when not connected")
        # manual control
            if str(key) == "c" and robot_connected and robot_good_to_go and not control_pending:
                if controltoggle:
                    log.put_nowait("[inputs] requesting manual control, wait for any other actions to complete")
                    manual_control = True
                    controltoggle = False
                    control_pending = True
                    manual_robot_control()
                else:
                    log.put_nowait("[inputs] requesting control release")
                    manual_control = False
                    controltoggle = True
            elif str(key) == "c" and (not robot_connected or not robot_good_to_go or control_pending):
                if robot_docked:
                    log.put_nowait("[inputs] cannot enable manual control, robot on charger, use leave charger command")
                elif control_pending:
                    log.put_nowait("[inputs] waiting for pending control request to complete")
                else:
                    log.put_nowait("[inputs] cannot enable manual control, robot state out of scope")
            if manual_control and robot_good_to_go:
                if str(key) == "up":
                    robot_command = "forward"
                if str(key) == "down":
                    robot_command = "backward"
                if str(key) == "left":
                    robot_command = "turnleft" 
                if str(key) == "right":
                    robot_command = "turnright"
                if str(key) == "q":
                    robot_command = "liftup"
                if str(key) == "a":
                    robot_command = "liftdown"
                if str(key) == "w":
                    robot_command = "headup"
                if str(key) == "s":
                    robot_command = "headdown"
                if str(key) == "e":
                    robot_command = "eyecolor"
        # action requests
            if robot_good_to_go and not robot_performing_action and not manual_control and not robot_control_blocking and robot_connected:
                if str(key) == "1":
                    robot_performing_action = True
                    robot_control_blocking = True
                    robot_command = "animationmix"
                    log.put_nowait("[inputs] requested animation mix")
                    robot_mix_animations()
                    robot_performing_action = False
                    robot_control_blocking = False
                    log.put_nowait("[inputs] request completed")
                if str(key) == "2":
                    robot_performing_action = True
                    robot_control_blocking = True
                    robot_command = "drive"
                    log.put_nowait("[inputs] requested drive")
                    robot_random_drive()
                    robot_performing_action = False
                    robot_control_blocking = False
                    log.put_nowait("[inputs] request completed")
                if str(key) == "3" and myrobot.world.light_cube:
                    robot_performing_action = True
                    robot_control_blocking = True
                    robot_command = "rollcube" 
                    log.put_nowait("[inputs] requested roll cube")
                    robot_roll_cube()
                    robot_performing_action = False
                    robot_control_blocking = False
                    log.put_nowait("[inputs] request completed")
                if str(key) == "4" and myrobot.world.light_cube:
                    robot_performing_action = True
                    robot_control_blocking = True
                    robot_command = "liftcube"
                    log.put_nowait("[inputs] requested pick up cube")
                    robot_pick_up_cube()
                    robot_performing_action = False
                    robot_control_blocking = False
                    log.put_nowait("[inputs] request completed")
                if str(key) == "5" and myrobot.world.light_cube:
                    robot_performing_action = True
                    robot_control_blocking = True
                    robot_command = "popwheelie"
                    log.put_nowait("[inputs] requested pop wheelie")
                    robot_pop_wheelie()
                    robot_performing_action = False
                    robot_control_blocking = False
                    log.put_nowait("[inputs] request completed")
            elif (str(key) == "1" or str(key) == "2" or str(key) == "3" or str(key) == "4" or str(key) == "5") and (robot_performing_action or manual_control or robot_control_blocking or not robot_good_to_go or not robot_connected):
                if robot_performing_action or robot_control_blocking and not manual_control:
                    log.put_nowait("[inputs] already performing an action, try again later")
                if manual_control:
                    log.put_nowait("[inputs] unable to perform action while under manual control, release control first")
                if not robot_good_to_go:
                    log.put_nowait("[inputs] cannot perform action, robot state out of scope, try again later")
                if (str(key) == "3" or str(key) == "4" or str(key) == "5") and not myrobot.world.light_cube:
                    log.put_nowait("[inputs] unable to perform action as not aware of cube, try again later")
        # leave charger
            if str(key) == "0" and not manual_control and robot_docked and robot_connected and not leavechargerrequest and not robot_performing_action and not robot_control_blocking and robot_connected:
                leavechargerrequest = True
                robot_control_blocking = True
                robot_performing_action = True
                robot_command = "leavecharger"
                log.put_nowait("[inputs] requested leave charger")
                request = robot_control_request(True,True)
                sleep(3)
                if have_robot_control:
                    myrobot.motors.set_wheel_motors(0, 0)
                    sleep(0.2)
                    myrobot.motors.set_wheel_motors(25, 25)
                    sleep(4.5)
                    myrobot.motors.stop_all_motors()
                request = robot_control_request(False,False)
                leavechargerrequest = False
                robot_performing_action = False
                robot_control_blocking = False
            elif str(key) == "0" and (manual_control or not robot_docked or not robot_connected or leavechargerrequest or robot_performing_action or robot_control_blocking):
                if manual_control:
                    log.put_nowait("[inputs] manual control is active, release control first")
                if not robot_docked:
                    log.put_nowait("[inputs] requesting to leave charger but robot is not docked!")
                if (robot_performing_action or robot_control_blocking) and not manual_control:
                    log.put_nowait("[inputs] another action is currently in progress, try again later")
                if not robot_connected:
                    log.put_nowait("[inputs] unable to request, robot is not connected")
        # return to charger
            if str(key) == "9" and not manual_control and not robot_docked and robot_good_to_go and myrobot.world.charger and not getonchargerrequest and not robot_performing_action and robot_connected and not robot_control_blocking:
                getonchargerrequest = True
                robot_performing_action = True
                robot_control_blocking = True
                log.put_nowait("[inputs] requested return to charger")
                request = robot_control_request(True,True)
                sleep(2)
                if have_robot_control:
                    log.put_nowait("[inputs] actioning return to charger")
                    if voice_debug:
                        say_future = myrobot.behavior.say_text("returning to charger!")
                    return_charger_future = myrobot.behavior.drive_on_charger()
                    timeout = 0
                    while str(return_charger_future).find("pending") != -1:
                        sleep(refresh_rate)
                        timeout += refresh_rate
                        if robot_docked:
                            break
                        if not robot_good_to_go:
                            break
                        if program_exit_requested:
                            break
                        if timeout > 60:
                            log.put_nowait("[inputs] timeout returning to charger")
                            if voice_debug:
                                say_future = myrobot.behavior.say_text("timeout while returning to charger!")
                            break
                else:
                    log.put_nowait("[inputs] failed to request control")
                if return_charger_future:
                    return_charger_future.cancel()
                if say_future:
                    say_future.cancel()
                request = robot_control_request(False,False)
                robot_performing_action = False
                robot_control_blocking = False
                getonchargerrequest = False
                if robot_docked:
                    log.put_nowait("[inputs] return to charger success")
                else:
                    log.put_nowait("[inputs] failed to return to charger")
            elif str(key) == "9" and (manual_control or robot_docked or not robot_good_to_go or not myrobot.world.charger or getonchargerrequest or robot_performing_action or not robot_connected or not robot_control_blocking):
                if manual_control:
                    log.put_nowait("[inputs] unable to return to charger while under manual control, release control first")
                if robot_docked:
                    log.put_nowait("[inputs] requesting dock with charger but robot is already docked!")
                if not robot_good_to_go:
                    log.put_nowait("[inputs] unable to return to charger, robot state out of scope, try again later")
                if not myrobot.world.charger and not robot_docked:
                    log.put_nowait("[inputs] unable to return to charger, charger location unknown, try again later")
                if robot_performing_action or robot_control_blocking and not manual_control:
                    log.put_nowait("[inputs] another action is currently in progress, try again later")
                if not robot_connected:
                    log.put_nowait("[inputs] unable to request, robot is not connected")
            #0=black,1=red,2=green,3=yellow,4=blue,5=magenta,6=cyan,7=white
            if str(key) == "f1":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: default")
                ui_color_0                   = 0
                ui_color_1                   = 1
                ui_color_2                   = 2
                ui_color_3                   = 3
                ui_color_4                   = 4
                ui_color_5                   = 5
                ui_color_6                   = 6
                ui_color_7                   = 7
                refresh_ui_colors()
            if str(key) == "f2":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: mono white")
                ui_color_0                   = 0
                ui_color_1                   = 7
                ui_color_2                   = 7
                ui_color_3                   = 7
                ui_color_4                   = 7
                ui_color_5                   = 7
                ui_color_6                   = 7
                ui_color_7                   = 7
                refresh_ui_colors()
            if str(key) == "f3":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: red and blue")
                ui_color_0                   = 0
                ui_color_1                   = 5
                ui_color_2                   = 1
                ui_color_3                   = 4
                ui_color_4                   = 4
                ui_color_5                   = 4
                ui_color_6                   = 1
                ui_color_7                   = 5
                refresh_ui_colors()
            if str(key) == "f4":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: CGA")
                ui_color_0                   = 0
                ui_color_1                   = 6
                ui_color_2                   = 6
                ui_color_3                   = 5
                ui_color_4                   = 6
                ui_color_5                   = 5
                ui_color_6                   = 7
                ui_color_7                   = 7
                refresh_ui_colors()
            if str(key) == "f5":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: borderless mono green")
                ui_color_0                   = 0
                ui_color_1                   = 2
                ui_color_2                   = 2
                ui_color_3                   = 0
                ui_color_4                   = 0
                ui_color_5                   = 0
                ui_color_6                   = 2
                ui_color_7                   = 2
                refresh_ui_colors()
            if str(key) == "f6":
                if not reduced_logging:
                    log.put_nowait("[inputs] color scheme: mono green")
                ui_color_0                   = 0
                ui_color_1                   = 2
                ui_color_2                   = 2
                ui_color_3                   = 2
                ui_color_4                   = 2
                ui_color_5                   = 2
                ui_color_6                   = 2
                ui_color_7                   = 2
                refresh_ui_colors()
        except Exception as e:
            log.put_nowait("[errors] input_thread error: " + repr(e))
    def release(key):
        global robot_command
        robot_command = "stop"
    while not program_exit_requested and not input_thread_stop:
        try:
            listen_keyboard(
                on_press=press,
                on_release=release,
            )
            if debug_logging and logging_thread_running:
                log.put_nowait("[inputs] input_thread: escape key pressed, exiting program, this can take up to 10 seconds")
            program_exit_requested = True
            while manual_control:
                sleep(refresh_rate)
            break
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] input_thread error: " + repr(e))
    program_exit_requested = True
    while manual_control:
        sleep(refresh_rate)
    input_thread_running = False
    if debug_logging:
        log.put_nowait("[inputs] input_thread: exiting thread")
    return
# robot_connection_thread is responsible for creating and maintaining the connection to the robot
def robot_connection_thread():
    global robot_connected, robot_connection_error, robot_connection_thread_running
    global init_complete
    global robot_current_control_level
    global log
    global sleeptime
    global have_robot_control
    if program_exit_requested:
        if robot_connected:
            myrobot.disconnect()
        return
    try:
        sleep(2)
        if debug_logging or connect_logging:
            log.put_nowait("[connct] connecting to " + str(vector_name))
        myrobot.connect(timeout=30)
        sleep(2)
        robot_connected = True
        robot_connection_error = False
    except anki_vector.exceptions.VectorNotFoundException as e:
        if except_logging or connect_logging:
            log.put_nowait("[connct] " + str(vector_name) + " not found - make sure " + str(vector_name) + " is on and the system running this script is connected to the same wireless network, closing and retrying connection, stand by")
        #this will hang indefinitely 
        #myrobot.disconnect()
        if except_logging and logging_thread_running:
            log.put_nowait("[connct] " + str(vector_name) + " disconnected")
        myrobot.conn.close()
        robot_connected = False
        robot_connection_error = False
        if quit_on_error and not robot_battery_thread_running:
            exit()
        else:
            quit_on_error_request = True
    except anki_vector.exceptions.VectorAsyncException as e:
        if repr(e).find("Repeated connections made to open Connection") != -1:
            if except_logging or connect_logging:
                log.put_nowait("[connct] connection to " + str(vector_name) + " not properly closed, closing and retrying connection, stand by")
            myrobot.conn.close()
            #myrobot.disconnect()
            robot_connection_error = True
            robot_connected = False
            if quit_on_error and not robot_battery_thread_running:
                exit()
            else:
                quit_on_error_request = True
    except anki_vector.exceptions.VectorConnectionException as e:
        if repr(e).find("DEADLINE_EXCEEDED") != -1:
            if except_logging or connect_logging:
                log.put_nowait("[connct] SDK/OS timeout bug, closing and retrying connection, stand by")
            #myrobot.conn.close()
            myrobot.disconnect()
            myrobot.conn.close()
            robot_connection_error = True
            robot_connected = False
        elif repr(e).find("connection has been closed") != -1:
            if except_logging or connect_logging:
                log.put_nowait("[connct] " + str(vector_name) + " is online but keeps closing connection, TRY REBOOTING VECTOR (unless currently in boot sequence), program will need to be restarted")
            myrobot.disconnect()
            myrobot.conn.close()
            sleep(5)
            #program_exit_requested = True
            robot_connection_error = True
            robot_connected = False
            if quit_on_error and not robot_battery_thread_running:
                exit()
            else:
                quit_on_error_request = True
        else:
            if except_logging and logging_thread_running:
                log.put_nowait("[connct] robot_connection_thread: A general connection error occurred. E: " + repr(e))
            myrobot.disconnect()
            myrobot.conn.close()
            robot_connection_error = True
            robot_connected = False
            if quit_on_error and not robot_battery_thread_running:
                exit()
            else:
                quit_on_error_request = True
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_connection_thread issue. E: " +repr(e))
        if quit_on_error and not robot_battery_thread_running:
            exit()
        else:
            quit_on_error_request = True
        robot_connection_error = True
    if robot_connected and not robot_connection_error:
        sleeptime = 30
        if debug_logging or connect_logging:
            log.put_nowait("[connct] connected to " + str(vector_name))
        version_state_future = ""
        version_state_future = myrobot.get_version_state()
        version_state = version_state_future.result(1)
        sleep(1)
        if version_state_future:
            version_state_future.cancel()
        # get robot OS version
        if not version_state.os_version:
            version_state.os_version = "UNKNOWN"
        if header_logging:
            # populate the log with initial data
            if not reduced_logging:
                log.put_nowait("[system] ----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
            if keyboard_control:
                log.put_nowait("[system] VecTrix " + str(vt_version) + " started, gathering data at refresh rate " + str(refresh_rate) + ", press ESCAPE to exit")
            else:
                log.put_nowait("[system] VecTrix " + str(vt_version) + " started, gathering data at refresh rate " + str(refresh_rate) + ", press CTRL+C to exit")
            log.put_nowait("[system] Connected to " + str(conn_object.name) + " with serial number " + str(robot_serial)+" running OS "+str(version_state.os_version)+ " at IP "+str(conn_object.host)+", using certificate "+str(conn_object.cert_file))
            if not reduced_logging and startup:
                log.put_nowait("[system] Configured options:")
                log.put_nowait("[system] faces: "+str(face_logging)+", speech: "+str(speech_logging)+", cube: "+str(cube_logging)+", dock: "+str(dock_events_logging)+", charge cycle: "+str(charge_cycle_logging)+", sensors: "+str(sensors_logging)+", actions: "+str(actions_logging)+", objects: "+str(object_logging))
                log.put_nowait("[system] battery: "+str(battery_logging)+", misc: "+str(misc_logging)+", camera: "+str(camera_logging)+", rangefinder: "+str(rangefinder_logging)+", motion: "+str(motion_logging)+", accel&gyro: "+str(accelgyro_logging)+", cont_cycle: " + str(continuous_cycle)+", reanimator: "+str(reanimator))
                if continuous_cycle_scheduling and continuous_cycle and dock_events_logging:
                    log.put_nowait("[system] continuous_cycle: active, schedule starts at "+str(continuous_cycle_earliest)+":00 and ends at "+str(continuous_cycle_latest)+":00")
                if file_logging:
                    log.put_nowait("[system] File logging is enabled, the file " + str(logfile) + " will be created/appended to")
                else:
                    log.put_nowait("[system] File logging is NOT enabled")
                if battery_csv_logging:
                    log.put_nowait("[system] logging battery data, the file " + str(battery_csv_filename) + " will be created/appended to")
                if headless:
                    log.put_nowait("[system] VecTrix is running headless")
                    log.put_nowait("[system] ----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                if str(version_state.os_version) == "2.0.1.6076":
                    log.put_nowait("[system] NOTICE: OS 2.0.1.6076 HAS A BUG THAT BREAKS GETTING VOLTAGE DATA FROM ROBOT, VOLTAGE BAR WILL BE INACCURATE/NONFUNCTIONAL")
                if keyboard_control:
                    log.put_nowait("[system] KEYBOARD CONTROL ACTIVE, PRESS H FOR HELP")
    init_complete = True
    while True:
        try:
            while robot_connected and not program_exit_requested:
                robot_current_control_level = myrobot.conn.behavior_control_level
                if robot_current_control_level == None:
                    have_robot_control = False
                else:
                    have_robot_control = True
                sleep(refresh_rate*2)
            if not robot_connected and robot_connection_error and not program_exit_requested:
                if debug_logging or connect_logging:
                    log.put_nowait("[connct] connection error, sleeping for a few seconds and retrying")
                try:
                    myrobot.disconnect()
                    sleep(5)
                except Exception as e:
                    if debug_logging:
                        log.put_nowait("[connct] robot_connection_thread: disco issue. E: "+repr(e))
                if debug_logging:
                    log.put_nowait("[debugs] robot_connection_thread: conn thread exit")
                robot_connection_thread_running = False
                sleep(2)
                return
            if not robot_connected and not robot_connection_error and not program_exit_requested:
                if debug_logging or connect_logging:
                    log.put_nowait("[connct] connection not established, sleeping " + str(sleeptime/60) + " minute(s) and retrying")
                myrobot.conn.close()
                sleep(sleeptime)
                sleeptime = sleeptime + sleeptime
                if sleeptime > 3600:
                    sleeptime = 3600
                if debug_logging:
                    log.put_nowait("[debugs] robot_connection_thread: conn thread exit")
                robot_connection_thread_running = False
                return
            if robot_connection_thread_stop:
                if debug_logging:
                    log.put_nowait("[debugs] robot_connection_thread: Exit requested, disco, sleep, and exiting thread")
                try:
                    myrobot.conn.close()
                except Exception as e:
                    if debug_logging:
                        log.put_nowait("[errors] robot_connection_thread: disco issue. E: "+repr(e))
                sleep(5)
                if debug_logging:
                    log.put_nowait("[debugs] robot_connection_thread: conn thread exit")
                robot_connection_thread_running = False
                return
        # non-terminal exceptions (?) some (most?) of these should do absolutely nothing and never fire but why not add the bunch
        except anki_vector.exceptions.VectorAsyncException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Invalid asynchronous action attempted: " +repr(e))
        except anki_vector.exceptions.VectorBehaviorControlException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Invalid behavior control action attempted: " +repr(e))
        except anki_vector.exceptions.VectorCameraFeedException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: The camera feed is not open: " +repr(e))  
        except anki_vector.exceptions.VectorConfigurationException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Invalid or missing configuration data: " +repr(e))     
        except anki_vector.exceptions.VectorControlException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Unable to run a function which requires behavior control: " +repr(e))     
        except anki_vector.exceptions.VectorControlTimeoutException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Failed to get control of " + str(vector_name) + ": " +repr(e))     
        except anki_vector.exceptions.VectorInvalidVersionException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Your SDK version is not compatible with " + str(vector_name) + "???s version: " +repr(e))     
        except anki_vector.exceptions.VectorNotReadyException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: " + str(vector_name) + " tried to do something before it was ready: " +repr(e))     
        except anki_vector.exceptions.VectorPropertyValueNotReadyException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Failed to retrieve the value for this property: " +repr(e))     
        except anki_vector.exceptions.VectorTimeoutException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Message took too long to complete: " +repr(e))     
        except anki_vector.exceptions.VectorUnauthenticatedException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Failed to authenticate request: " +repr(e))     
        except anki_vector.exceptions.VectorUnavailableException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Unable to reach " + str(vector_name) + ": " +repr(e))     
        except anki_vector.exceptions.VectorUnimplementedException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: " + str(vector_name) + " does not handle this message: " +repr(e))     
        except anki_vector.exceptions.VectorExternalAudioPlaybackException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread: Failed to play external audio on " + str(vector_name) + ": " +repr(e))
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] robot_connection_thread issue: " +repr(e))
        # function to aid in control loss detection
        sleep(refresh_rate*4)
# robot_battery_thread is responsible for getting and publishing the robot battery data (voltage/charging/docked/batlevel)
def robot_battery_thread():
    #robot_battery_state = myrobot.get_battery_state()
    global robot_batlevel, robot_charging, robot_docked, robot_voltage
    global robot_getting_batt_data
    global robot_connected, robot_connection_error
    global robot_battery_thread_running, robot_battery_ready
    global log
    robot_battery_future = ""
    while not init_complete:
        sleep(refresh_rate)
    if debug_logging:
        log.put_nowait("[debugs] robot_battery_thread started")
    robot_battery_ready = False
    while True:
        if robot_connected and not program_exit_requested:
            try:
                while robot_getting_sensor_data:
                    sleep(refresh_rate/4)
                robot_getting_batt_data = True
                robot_battery_future      = myrobot.get_battery_state()
                robot_battery_state       = robot_battery_future.result(timeout=1)
                robot_getting_batt_data = False
                if robot_battery_state:
                    robot_batlevel          = robot_battery_state.battery_level
                    robot_charging          = robot_battery_state.is_charging
                    robot_docked            = robot_battery_state.is_on_charger_platform
                    robot_voltage           = round(robot_battery_state.battery_volts,4)
                else:
                    if debug_logging:
                        log.put_nowait("[debugs] Failed to get " + str(vector_name) + "'s battery and dock data")
            except anki_vector.exceptions.VectorNotFoundException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_battery_thread: " + str(vector_name) + " not found error. Error: " + repr(e))
                robot_connected = False
                robot_connection_error = False
            except anki_vector.exceptions.VectorUnavailableException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_battery_thread: " + str(vector_name) + " unavailable error. Error: " + repr(e))
                robot_connected = False
                robot_connection_error = True
            except anki_vector.exceptions.VectorConnectionException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_battery_thread: A connection error occurred: " + repr(e))
                robot_connection_error = True
                robot_connected = False
            except anki_vector.exceptions.VectorAsyncException as e:
                if except_logging and not reduced_logging and logging_thread_running:
                    log.put_nowait("[errors] robot_battery_thread: Invalid asynchronous action attempted: " +repr(e))
            except anki_vector.exceptions.VectorBehaviorControlException as e:
                if except_logging and not reduced_logging and logging_thread_running:
                    log.put_nowait("[errors] robot_battery_thread: Invalid behavior control action attempted: " +repr(e))
            except Exception as e:
                if except_logging and logging_thread_running:
                    if repr(e).find("TimeoutError") != -1 and not reduced_logging:
                        log.put_nowait("[errors] robot_battery_thread: timeout reported, if incidental it's not a big deal. E: " +repr(e))
                    else:
                        log.put_nowait("[errors] robot_battery_thread issue: " +repr(e))
            robot_battery_ready = True
        if robot_battery_thread_stop:
            if robot_battery_future:
                robot_battery_future.cancel()
            if debug_logging:
                log.put_nowait("[debugs] robot_battery_thread stopped")
            robot_battery_thread_running = False
            return
        sleep(refresh_rate*3)
        if robot_battery_future:
            robot_battery_future.cancel()
# robot_sensor_thread is responsible for getting and publishing the robot status data (cliffdetect, pickup, moving, etc)
def robot_sensor_thread():
    global robot_calmpower,robot_cliffdetect,robot_falling,robot_pickup,robot_held,robot_button
    global robot_carrying,robot_docking,robot_moving,robot_animating,robot_pathing,robot_driving
    global robot_signal_quality, robot_distance_mm, robot_is_lift_in_fov, robot_found_object, robot_unobstructed
    global robot_sensor_thread_running, robot_getting_sensor_data, robot_sensors_ready
    global robot_connected, robot_connection_error
    global robot_good_to_go
    global log
    robot_sensors_ready = False
    while not init_complete:
        sleep(refresh_rate)
    if debug_logging:
        log.put_nowait("[debugs] robot_sensor_thread started")
    while True:
        if robot_connected and not program_exit_requested:
            try:
                robot_status = ""
                robot_proximity = ""
                while robot_getting_batt_data:
                    sleep(refresh_rate/4)
                robot_getting_sensor_data = True
                robot_status                = myrobot.status
                robot_proximity             = myrobot.proximity
                robot_getting_sensor_data = False
                if robot_status:
                    robot_calmpower         = robot_status.is_in_calm_power_mode
                    robot_cliffdetect       = robot_status.is_cliff_detected
                    robot_falling           = robot_status.is_falling
                    robot_pickup            = robot_status.is_picked_up
                    robot_held              = robot_status.is_being_held
                    robot_button            = robot_status.is_button_pressed
                    robot_carrying          = robot_status.is_carrying_block
                    robot_docking           = robot_status.is_docking_to_marker
                    robot_moving            = robot_status.are_motors_moving
                    robot_animating         = robot_status.is_animating
                    robot_pathing           = robot_status.is_pathing
                    robot_driving           = robot_status.are_wheels_moving
                else:
                    if debug_logging:
                        log.put_nowait("[debugs] Failed to get " + str(vector_name) + "'s status data")
                if robot_proximity:
                    rangefinder_distance    = robot_proximity.last_sensor_reading.distance
                    robot_signal_quality    = robot_proximity.last_sensor_reading.signal_quality
                    robot_is_lift_in_fov    = robot_proximity.last_sensor_reading.is_lift_in_fov
                    robot_found_object      = robot_proximity.last_sensor_reading.found_object
                    robot_unobstructed      = robot_proximity.last_sensor_reading.unobstructed
                    if not robot_is_lift_in_fov:
                        robot_distance_mm       = rangefinder_distance.distance_mm
                else:
                    if debug_logging:
                        log.put_nowait("[debugs] Failed to get " + str(vector_name) + "'s proximity data")
            except anki_vector.exceptions.VectorNotFoundException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_sensor_thread: " + str(vector_name) + " not found error. Error: " + repr(e))
                robot_connected = False
                robot_connection_error = False
            except anki_vector.exceptions.VectorUnavailableException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_sensor_thread: " + str(vector_name) + " unavailable error. Error: " + repr(e))
                robot_connected = False
                robot_connection_error = True
            except anki_vector.exceptions.VectorConnectionException as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[connct] robot_sensor_thread: A connection error occurred: " + repr(e))
                robot_connection_error = True
                robot_connected = False
            except anki_vector.exceptions.VectorAsyncException as e:
                if except_logging and not reduced_logging and logging_thread_running:
                    log.put_nowait("[errors] robot_sensor_thread: Invalid asynchronous action attempted: " +repr(e))
            except anki_vector.exceptions.VectorBehaviorControlException as e:
                if except_logging and not reduced_logging and logging_thread_running:
                    log.put_nowait("[errors] robot_sensor_thread: Invalid behavior control action attempted: " +repr(e))
            except Exception as e:
                if except_logging and logging_thread_running:
                    log.put_nowait("[errors] robot_sensor_thread issue: " +repr(e))
            robot_sensors_ready = True
        if robot_sensor_thread_stop:
            if debug_logging:
                log.put_nowait("[debugs] robot_sensor_thread stopped")
            robot_sensor_thread_running = False
            return
        # determine if robot is good to go for reanimator
        if robot_connected and not robot_connection_error and not program_exit_requested and not robot_docked and not robot_pickup and not robot_held and not robot_cliffdetect and not robot_falling and not robot_is_being_touched and robot_batlevel > 1:
            robot_good_to_go = True
        else:
            robot_good_to_go = False
        sleep(refresh_rate)
# robot_event_thread is responsible for receiving and handling events emitted by the robot
def robot_event_thread():
    global log
    global robot_event_thread_running, robot_events_ready
    global robot_connected, robot_connection_error
    global last_event_received, object_logging
    robot_events_ready = False
    while not init_complete:
        sleep(refresh_rate)
    if debug_logging:
        log.put_nowait("[debugs] robot_event_thread started")
    def on_robot_state(myrobot, event_type, event, evt):
        global robot_accel_x, robot_accel_y, robot_accel_z
        global robot_gyro_x, robot_gyro_y, robot_gyro_z
        global robot_distance_mm, robot_signal_quality, robot_unobstructed, robot_found_object, robot_is_lift_in_fov
        global robot_head_angle_rad, robot_lift_height_mm
        global robot_left_wheel_speed_mmps, robot_right_wheel_speed_mmps
        global robot_is_being_touched, robot_raw_touch_value
        global last_event_received
        last_event_received = 0
        try:
            robot_left_wheel_speed_mmps     = event.left_wheel_speed_mmps	
            robot_right_wheel_speed_mmps    = event.right_wheel_speed_mmps
            robot_head_angle_rad            = event.head_angle_rad
            robot_lift_height_mm            = event.lift_height_mm
            robot_is_being_touched          = event.touch_data.is_being_touched   
            robot_raw_touch_value           = event.touch_data.raw_touch_value
            robot_accel_x                   = event.accel.x
            robot_accel_y                   = event.accel.y
            robot_accel_z                   = event.accel.z
            robot_gyro_x                    = event.gyro.x     
            robot_gyro_y                    = event.gyro.y
            robot_gyro_z                    = event.gyro.z 
        except Exception as e: 
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] robot_event_thread on_robot_state issue: " +repr(e))
    def on_robot_observed_face(myrobot, event_type, event, evt):
        global recent_face_seen, recent_known_face_seen, face_name
        if not recent_face_seen and event.face_id < 1:
            recent_face_seen = True
            if not reduced_logging:
                log.put_nowait("[events] " + str(vector_name) + " sees a face but isn't sure who it is")
        if not recent_known_face_seen and event.face_id >= 1:
            recent_known_face_seen = True
            try:
                for face in myrobot.world.visible_faces:
                    face_name = face.name
            except:
                pass
            if face_name:
                msg="[events] " + str(vector_name) + " sees a face, it's " + str(face_name) + "!"
                log.put_nowait(msg)
                face_name = ""
            else:
                if not reduced_logging:
                    msg="[events] " + str(vector_name) + " sees a face but can't recall the name"
                    log.put_nowait(msg)
    def on_robot_object_appeared(myrobot, event_type, event, evt):
        msg="[events] " + str(vector_name) + " senses an object appeared: " + str(event.obj)
        log.put_nowait(msg)
    def on_robot_object_observed(myrobot, event_type, event, evt):
        msg = "[events] " + str(vector_name) + " observed an object: " + str(event.obj)
        log.put_nowait(msg)
    def on_robot_object_moved(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " senses a cube is moving")
    def on_robot_object_stopped_moving(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " senses a cube stopped moving")
    def on_user_intent(myrobot, event_type, event, evt):
        try:
            user_intent = UserIntent(event)
            if user_intent:
                received_intent = json.loads(user_intent.intent_data)
                log.put_nowait("[events] User intent "+str(user_intent.intent_event)+" received: " + str(received_intent))
            #data = json.loads(user_intent.intent_data)
            #log.put_nowait("[events] Intent data captured: " + str(data))
        except Exception as e:
            log.put_nowait("[events] robot_event_thread: issue capturing event: "+repr(e))
    def on_wake_word(myrobot, event_type, event, evt):
        global recent_wake_word
        if not recent_wake_word:
            log.put_nowait("[events] " + str(vector_name) + " heard a wake word")
            recent_wake_word = True
    def on_robot_object_disappeared(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " senses an object disappeared: " + str(event.obj))
    def on_robot_audio_send_mode_changed(myrobot, event_type, event, evt):
        log.put_nowait("[events] Event fired: audio_send_mode_changed for " + str(vector_name))
    def on_robot_cube_connection_lost(myrobot, event_type, event, evt):
        log.put_nowait("[events] the cube was disconnected from " + str(vector_name))
    def on_robot_nav_map_update(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " updated the navigation map")
    def on_robot_new_camera_image(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " has captured a new camera image")
    def on_robot_new_raw_camera_image(myrobot, event_type, event, evt):
        log.put_nowait("[events] " + str(vector_name) + " has captured a new raw camera image")
    def on_robot_object_available(myrobot, event_type, event, evt):
        global recent_cube_available
        if not recent_cube_available:
            if not reduced_logging:
                log.put_nowait("[events] " + str(vector_name) + " senses a cube")
            recent_cube_available = True
        if cube_powersaver:
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempting to disconnect")
            myrobot.world.disconnect_cube()
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempt completed")
    def on_robot_object_tapped(myrobot, event_type, event, evt):
        global recent_cube_tapped
        if not recent_cube_tapped:
            if not reduced_logging:
                log.put_nowait("[events] " + str(vector_name) + " senses a cube was tapped")
            recent_cube_tapped = True
        if cube_powersaver:
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempting to disconnect")
            myrobot.world.disconnect_cube()
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempt completed")
    def on_robot_object_up_axis_changed(myrobot, event_type, event, evt):
        global recent_cube_rotated
        if not recent_cube_rotated:
            log.put_nowait("[events] " + str(vector_name) + " senses a cube was rotated")
            recent_cube_rotated = True
        if cube_powersaver:
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempting to disconnect")
            myrobot.world.disconnect_cube()
            if debug_logging:
                log.put_nowait("[events] cube_powersaver: attempt completed")
    # set up event subscriptions depending on config switches
    if face_logging:
        myrobot.events.subscribe(on_robot_observed_face, Events.robot_observed_face, evt)
    if speech_logging:
        myrobot.events.subscribe(on_wake_word, Events.wake_word, evt)
        myrobot.events.subscribe(on_user_intent, Events.user_intent, evt)
    # object events
    if object_logging:
        myrobot.events.subscribe(on_robot_object_disappeared, Events.object_disappeared, evt)
        myrobot.events.subscribe(on_robot_object_appeared, Events.object_appeared, evt)
        myrobot.events.subscribe(on_robot_object_observed, Events.object_observed, evt)
    # misc events
    if misc_logging:
        myrobot.events.subscribe(on_robot_audio_send_mode_changed, Events.audio_send_mode_changed, evt)
        myrobot.events.subscribe(on_robot_nav_map_update, Events.nav_map_update, evt)
    # camera events
    if camera_logging:
        myrobot.events.subscribe(on_robot_new_camera_image, Events.new_camera_image, evt)
        myrobot.events.subscribe(on_robot_new_raw_camera_image, Events.new_raw_camera_image, evt)
    # cube events
    if cube_logging:
        myrobot.events.subscribe(on_robot_cube_connection_lost, Events.cube_connection_lost, evt)
        myrobot.events.subscribe(on_robot_object_tapped, Events.object_tapped, evt)
        myrobot.events.subscribe(on_robot_object_up_axis_changed, Events.object_up_axis_changed, evt)
        myrobot.events.subscribe(on_robot_object_available, Events.object_available, evt)
        myrobot.events.subscribe(on_robot_object_moved, Events.object_moved, evt)
        myrobot.events.subscribe(on_robot_object_stopped_moving, Events.object_stopped_moving, evt)
    # robot state
    myrobot.events.subscribe(on_robot_state, Events.robot_state, evt)
    #object_logging = object_logging_old
    while True:
        try:
            if not program_exit_requested:
                last_event_received = last_event_received + (refresh_rate/2)
                if last_event_received > 5 and robot_connected and not robot_connection_error:
                    if debug_logging:
                        log.put_nowait("[connct] robot_event_thread has not received a message for 5 seconds, disconnecting and retrying")
                    robot_connected = False
                    robot_connection_error = True
                    last_event_received = 0
            if robot_event_thread_stop:
                try:
                    if face_logging:
                        myrobot.events.unsubscribe(on_robot_observed_face, Events.robot_observed_face)
                    if speech_logging:
                        myrobot.events.unsubscribe(on_wake_word, Events.wake_word)
                        myrobot.events.unsubscribe(on_user_intent, Events.user_intent)
                    if object_logging:
                        myrobot.events.unsubscribe(on_robot_object_disappeared, Events.object_disappeared)
                        myrobot.events.unsubscribe(on_robot_object_appeared, Events.object_appeared)
                        myrobot.events.unsubscribe(on_robot_object_observed, Events.object_observed)
                    if misc_logging:
                        myrobot.events.unsubscribe(on_robot_audio_send_mode_changed, Events.audio_send_mode_changed)
                        myrobot.events.unsubscribe(on_robot_nav_map_update, Events.nav_map_update)
                    if camera_logging:
                        myrobot.events.unsubscribe(on_robot_new_camera_image, Events.new_camera_image)
                        myrobot.events.unsubscribe(on_robot_new_raw_camera_image, Events.new_raw_camera_image)
                    if cube_logging:
                        myrobot.events.unsubscribe(on_robot_cube_connection_lost, Events.cube_connection_lost)
                        myrobot.events.unsubscribe(on_robot_object_tapped, Events.object_tapped)
                        myrobot.events.unsubscribe(on_robot_object_up_axis_changed, Events.object_up_axis_changed)
                        myrobot.events.unsubscribe(on_robot_object_moved, Events.object_moved)
                        myrobot.events.unsubscribe(on_robot_object_stopped_moving, Events.object_stopped_moving)
                        myrobot.events.subscribe(on_robot_object_available, Events.object_available, evt)
                    myrobot.events.unsubscribe(on_robot_state, Events.robot_state)
                    if debug_logging:
                        log.put_nowait("[debugs] robot_event_thread stopped")
                    robot_event_thread_running = False
                    return
                except Exception as e:
                    if except_logging and logging_thread_running:
                        log.put_nowait("[errors] robot_event_thread shutdown issue: " +repr(e))
            robot_events_ready = True
            sleep(refresh_rate/2)
        except anki_vector.exceptions.VectorNotFoundException as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[connct] robot_event_thread: " + str(vector_name) + " not found error. Error: " + repr(e))
            robot_connected = False
            robot_connection_error = False
        except anki_vector.exceptions.VectorUnavailableException as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[connct] robot_event_thread: " + str(vector_name) + " unavailable error. Error: " + repr(e))
            robot_connected = False
            robot_connection_error = True
        except anki_vector.exceptions.VectorConnectionException as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[connct] robot_event_thread: A connection error occurred: " + repr(e))
            robot_connection_error = True
            robot_connected = False
        except anki_vector.exceptions.VectorAsyncException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_event_thread: Invalid asynchronous action attempted: " +repr(e))
        except anki_vector.exceptions.VectorBehaviorControlException as e:
            if except_logging and not reduced_logging and logging_thread_running:
                log.put_nowait("[errors] robot_event_thread: Invalid behavior control action attempted: " +repr(e))
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] robot_event_thread issue: " +repr(e))
# robot_control_request is responsible for gaining control over the connected robot and releasing it.
def robot_control_request(control_or_release, force_control):
    global myrobot, control_response
    global log
    control_response    = False
    eyecolor_future     = ""
    # control request
    if control_or_release:
        if have_robot_control:
            if debug_logging:
                log.put_nowait("[debugs] robot_control_request control request received but already have control!")
            control_response = True
            return control_response
        try:
            if robot_connected and robot_batlevel > 1 and not robot_held and not robot_pickup and not robot_falling:
                if force_control:
                    controlrequest = myrobot.conn.request_control(behavior_control_level=ControlPriorityLevel.OVERRIDE_BEHAVIORS_PRIORITY, timeout=10)
                else:
                    controlrequest = myrobot.conn.request_control(behavior_control_level=ControlPriorityLevel.DEFAULT_PRIORITY, timeout=10)
                timeout = 0
                while str(controlrequest).find("pending") != -1:
                    if timeout >= 7 or not robot_connected or robot_batlevel == 1 or robot_held or robot_pickup or robot_falling:
                        controlrequest.cancel()
                        if debug_logging:
                            if timeout >= 7:
                                if debug_logging:
                                    log.put_nowait("[debugs] robot_control_request: timeout on request for " + str(vector_name))
                            else:
                                if debug_logging and not reduced_logging:
                                    log.put_nowait("[debugs] robot_control_request: " + str(vector_name) + " state out of scope")
                        if debug_logging and not reduced_logging:
                            log.put_nowait("[debugs] robot_control_request: " + str(vector_name) + " returning FALSE, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                        control_response = False
                        return control_response
                    timeout = timeout + refresh_rate
                    sleep(refresh_rate)
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_green,1)
                sleep(0.2)
                if rainbow_eyes and eyecolor_future:
                    eyecolor_future.cancel()
                sleep(2)
                if not have_robot_control:
                    control_response = False
                    if debug_logging and not reduced_logging:
                        log.put_nowait("[debugs] robot_control_request: " + str(vector_name) + " returning FALSE, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                else:
                    control_response = True
                    if debug_logging and not reduced_logging:
                        log.put_nowait("[debugs] robot_control_request: " + str(vector_name) + " returning TRUE, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                return control_response
            else:
                if debug_logging and not reduced_logging:
                    log.put_nowait("[debugs] robot_control_request: " + str(vector_name) + " state out of scope, returning FALSE, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                    control_response = False
                    return control_response
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] robot_control_request: issue requesting control of " + str(vector_name) + ": "+repr(e))
            controlrequest.cancel()
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            control_response = False
            return control_response
    #release request
    if not control_or_release:
        try:
            releaserequest = myrobot.conn.release_control(timeout=10)
            timeout = 0
            while str(releaserequest).find("pending") != -1:
                if timeout >= 5 or not robot_docked:
                    break
                if program_exit_requested or not robot_connected:
                    releaserequest.cancel()
                    if debug_logging:
                        log.put_nowait("[debugs] robot_control_request: issue releasing control of " + str(vector_name))
                    return
                timeout = timeout + refresh_rate
                sleep(refresh_rate)
            sleep(1)
            if actions_logging and not have_robot_control and not robot_control_blocking and not robot_performing_action:
                log.put_nowait("[action] " + str(vector_name) + " is in freeplay mode")
            return
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] robot_control_request: issue releasing control: "+repr(e))
            releaserequest.cancel()
            return
# yeetbot (continuous cycles): force robot off charger if fully charged after [continuous_cycle_wait_time]
def yeetbot():
    try:
        # try to gain control and send robot off charger if currently docked and battery level = 3 (full)
        global robot_control_blocking
        global yeetbot_thread_running
        global myrobot
        global log
        eyecolor_future = ""
        leave_dock_delay = 0
        incontrol = 0
        leave_dock_delay = continuous_cycle_wait_time + random.randint(0, continuous_cycle_random)
        if debug_logging:
            msg = "[cycles] " + str(vector_name) + "'s battery is full, sleeping for " + str(leave_dock_delay) + " seconds before ejecting from charger"
            log.put_nowait(msg)
        waitcounter = 0
        while waitcounter < leave_dock_delay:
            if program_exit_requested or not robot_docked or not robot_connected:
                yeetbot_thread_running = False
                robot_control_blocking = False
                return
            waitcounter += refresh_rate
            sleep(refresh_rate)
        if robot_docked and robot_batlevel == 3 and not program_exit_requested and not robot_control_blocking and robot_connected:
            robot_control_blocking = True
            if debug_logging:
                log.put_nowait("[debugs] continuous_cycle: Requesting control of " + str(vector_name))
            if dock_events_logging and robot_calmpower:
                log.put_nowait("[cycles] wake up, " + str(vector_name) + "!")
            request = robot_control_request(True,True)
            if not request:
                yeetbot_thread_running = False
                if debug_logging:
                    log.put_nowait("[debugs] continuous_cycle: control request for " + str(vector_name) + " failed")
                robot_control_blocking = False
                return
            else:
                incontrol = 1
            sleep(3)
            myrobot.motors.set_wheel_motors(0, 0)
            sleep(0.2)
            myrobot.motors.set_wheel_motors(25, 25)
            sleep(4.5)
            myrobot.motors.stop_all_motors()
            if not robot_docked:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_green,1)
            else:
                if dock_events_logging and not reduced_logging:  
                    msg="[cycles] " + str(vector_name) + " didn't feel like leaving the charger, will retry a little later"
                    log.put_nowait(msg)
            sleep(1)
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            incontrol = 0
        else:
            if debug_logging and not reduced_logging:
                log.put_nowait("[cycles] " + str(vector_name) + " is currently not on charger or battery not full, aborting")
        # all done exit thread
        if debug_logging:
            log.put_nowait("[debugs] continuous_cycle: Thread actions complete, exiting")
        yeetbot_thread_running = False
        robot_control_blocking = False
        incontrol = 0
        robot_control_request(False,False)
        return   
    except Exception as e:
        if except_logging and logging_thread_running:
            msg="[errors] yeetbot issue: " +repr(e)
            log.put_nowait(msg)
        yeetbot_thread_running = False
        robot_control_blocking = False
        if have_robot_control:
            request = robot_control_request(False,False)
        return
    yeetbot_thread_running = False
    robot_control_blocking = False
    incontrol = 0
    request = robot_control_request(False,False)
    return
# reanimator will make Vector do fun stuff when idle for [reanimator_timeout]!
def reanimator_thread():
    try:
        global log
        if debug_logging:
            log.put_nowait("[ranmtr] reanimator starting!")
        global myrobot
        global robot_control_blocking
        global reanimator_thread_running
        global reanimator_debug
        reanimator_thread_running = True
        prox_array           = []
        robot_go_animate     = 0
        robot_go_drive       = 0
        robot_go_cube        = 0
        rollable_cube        = False
        vector_speed         = 0
        cointoss             = 0
        action_running       = 0
        combochance          = 0
        if not robot_control_blocking and robot_good_to_go and not control_pending:
            robot_control_blocking = True
            if myrobot.world.light_cube:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] aware of a rollable cube")
                rollable_cube = True
            else:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] not aware of a rollable cube")
                rollable_cube = False
            # weighted random decision on what to do
            cointoss = random.randint(1, 100)
            if reanimator_debug and not reduced_logging:
                msg="[ranmtr] roll the dice: "+str(cointoss)
                log.put_nowait(msg)
            if cointoss <= go_look_around_chance:
                robot_look_around()
            if cointoss > go_look_around_chance and cointoss < go_animate_chance:
                robot_mix_animations()
            if cointoss >= go_animate_chance and cointoss <= (go_animate_chance + go_drive_chance):
                robot_random_drive() 
                #robot_pop_wheelie()
            if cointoss > (100-go_cube_chance):
                if rollable_cube:
                    cointoss = random.randint(1, 100)
                    if cointoss < 65:
                        robot_roll_cube()
                    if cointoss >=65 and cointoss <= 98:
                        robot_pick_up_cube()
                    if cointoss > 98:
                        robot_pop_wheelie()
                else:
                    robot_mix_animations()
        else:
            if reanimator_debug:
                log.put_nowait("[ranmtr] exiting thread - robot state out of scope")
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] reanimator_thread issue: " + repr(e))
        robot_control_blocking = False
        reanimator_thread_running = False
        return
    if debug_logging:
        log.put_nowait("[ranmtr] exiting main reanimator thread")
    reanimator_thread_running = False
    robot_control_blocking = False
    return
# robot_mix_animations will mix two random animations
def robot_mix_animations():
    global myrobot
    global log
    body_track_1         = False
    body_track_2         = False
    head_track_1         = False
    head_track_2         = False
    lift_track_1         = False
    lift_track_2         = False
    _ANIMATION1          = ""
    _ANIMATION2          = ""
    eyecolor_future      = ""
    say_future           = ""
    true_false           = [True,False]
    play_anim1_future    = ""
    play_anim2_future    = ""
    if debug_logging:
        log.put_nowait("[ranmtr] robot_mix_animations starting")
    try:
        # request control
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
            else:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
        else:
            return
        if voice_debug:
            say_future = myrobot.behavior.say_text("animation!")
        # pick a random set of animations
        _ANIMATION1 = random.choice(anim_list)
        _ANIMATION2 = random.choice(anim_list)
        # make sure head/body/lift are opposites for each animation
        body_track_1 = random.choice(true_false)
        if body_track_1:
            body_track_2 = False
        else:
            body_track_2 = True
        head_track_1 = random.choice(true_false)
        if head_track_1:
            head_track_2 = False
        else:
            head_track_2 = True
        lift_track_1 = random.choice(true_false)
        if lift_track_1:
            lift_track_2 = False
        else:
            lift_track_2 = True
        sleep(0.2)
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        if reanimator_debug:
            log.put_nowait("[action] " + str(vector_name) + " will combine "+_ANIMATION1+" B:"+str(body_track_1)+",H:"+str(head_track_1)+",L:"+str(lift_track_1)+" and "+_ANIMATION2+" B:"+str(body_track_2)+",H:"+str(head_track_2)+",L:"+str(lift_track_2))
        if reanimator_logging or actions_logging:
            if reduced_logging:
                log.put_nowait("[action] " + str(vector_name) + " is mixing up animations!")
            else:
                log.put_nowait("[action] " + str(vector_name) + " is combining animations: "+_ANIMATION1+" and "+_ANIMATION2)
        # play the animations
        play_anim1_future = myrobot.anim.play_animation(_ANIMATION1, ignore_body_track=body_track_1, ignore_head_track=head_track_1, ignore_lift_track=lift_track_1)
        play_anim2_future = myrobot.anim.play_animation(_ANIMATION2, ignore_body_track=body_track_2, ignore_head_track=head_track_2, ignore_lift_track=lift_track_2)
        timeout = 0
        eyeswitch = False
        while str(play_anim1_future).find("pending") != -1 or str(play_anim2_future).find("pending") != -1:
            if not robot_good_to_go or not have_robot_control or control_pending:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] robot_mix_animations: control loss, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                break
            if timeout >= 8:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] robot_mix_animations: timeout")
                break
            if rainbow_eyes and have_robot_control and not eyeswitch:
                eyeswitch = True
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)
        if not robot_good_to_go or control_pending:
            request = robot_control_request(False,False)
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            return
        animwait = 0
        while animwait < 2:
            animwait += refresh_rate
            if not robot_good_to_go or not have_robot_control or control_pending:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] robot_mix_animations: control loss, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
                break
            sleep(refresh_rate)
        if play_anim1_future:
            play_anim1_future.cancel()
        if play_anim2_future:
            play_anim2_future.cancel()
        if voice_debug and say_future:
            say_future.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        if debug_logging or reanimator_debug:
            log.put_nowait("[debugs] robot_mix_animations: Animation played, releasing")
        request = robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_mix_animations issue: " + repr(e))
    if debug_logging:
        log.put_nowait("[debugs] robot_mix_animations thread exiting")
    return
# robot_random_drive will send Vector on a drive
def robot_random_drive():
    global myrobot
    global log
    bugout_chance_increase  = 0
    prox_array              = []
    clear_sailing           = False
    eyecolor_future         = ""
    say_future              = ""
    turn_future             = ""
    head_future             = ""
    lift_future             = ""
    drive_future            = ""
    checkrange              = 0
    if reanimator_debug or reanimator_logging:
        log.put_nowait("[action] " + str(vector_name) + " is going for a drive")
    try:
        # request control
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        sleep(0.2)
        total_steps_count = 0
        if voice_debug:
            say_future = myrobot.behavior.say_text("drive!")
        while total_steps_count < 3 and robot_good_to_go:      
            if not robot_good_to_go or control_pending:
                request = robot_control_request(False,False)
                return
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
            myrobot.motors.set_wheel_motors(0, 0)
            sleep(0.2)
            robot_random_turn(45,180,1)
            # grab 3 rangefinder readings at -8,0,8 degrees rotation
            x = 0
            while x < 3 and robot_good_to_go:
                prox_array.append(robot_distance_mm)
                if x == 0 or x == 2:
                    turn_future = myrobot.behavior.turn_in_place(degrees(10))
                if x == 1:
                    turn_future = myrobot.behavior.turn_in_place(degrees(-20))
                timeout = 0
                eyeswitch = False
                while str(turn_future).find("pending") != -1:
                    if not robot_good_to_go or control_pending:
                        break
                    if not have_robot_control:
                        request = robot_control_request(True,False)
                        if not request:
                            return
                    if timeout >= 2.5:
                        if rainbow_eyes and have_robot_control:
                            eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                        break
                    if rainbow_eyes and have_robot_control and not eyeswitch:
                        eyeswitch = True
                        eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
                    timeout = timeout + (refresh_rate/2)
                    sleep(refresh_rate/2)
                turn_future.cancel()
                if rainbow_eyes and eyecolor_future:
                    eyecolor_future.cancel()
                if not robot_good_to_go:
                    request = robot_control_request(False,False)
                    return
                x += 1
            if not robot_good_to_go or control_pending:
                request = robot_control_request(False,False)
                return
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
            if reanimator_debug and not reduced_logging:
                log.put_nowait("[ranmtr] prox distance array: " +str(prox_array))
            # check if the path is clear to max range
            if prox_array[0] > 399 and prox_array[1] > 399 and prox_array[2] > 399:
                clear_sailing = True
            # do we want to bug out? roll the dice
            bugoutchance = random.randint(1, 100) + bugout_chance_increase
            if bugoutchance > 75 and not clear_sailing:
                robot_go_to_random_pose()
                return
            else:
                bugout_chance_increase = bugout_chance_increase + 5
            # if we have some space, roll out
            if prox_array[0] > reanimator_min_distance and prox_array[1] > reanimator_min_distance and prox_array[2] > reanimator_min_distance:
                # doublecheck because range measurements can be wonky
                if not robot_good_to_go or control_pending:
                    request = robot_control_request(False,False)
                    return
                checkrange = robot_check_free_space()
                final_range = round((checkrange-45),2)
                if final_range > reanimator_max_distance:
                    final_range = reanimator_max_distance
                # rangefinder reports clear to max range
                if clear_sailing:
                    final_range = 350
                vector_speed = round((random.randint(35, 150)+(final_range/7)),2)
                if reanimator_debug:
                    if not clear_sailing:
                        log.put_nowait("[action] robot_random_drive: " + str(vector_name) + " is going on an adventure for "+str(final_range-40)+"mm at "+str(vector_speed)+"mm/s!")
                    else:
                        log.put_nowait("[action] robot_random_drive: No obstacles for max range! " + str(vector_name) + " is going to drive for "+str(final_range-40)+"mm at "+str(vector_speed)+"mm/s!")
                if voice_debug:
                    if clear_sailing:
                        say_future = myrobot.behavior.say_text("wheeeeeeee!")
                    else:
                        say_future = myrobot.behavior.say_text("drive " + str(int((final_range/10)-4)))
                clear_sailing = False
                if not have_robot_control:
                    request = robot_control_request(True,False)
                    if not request:
                        return
                # finally we're driving
                drive_future = myrobot.behavior.drive_straight(distance_mm(final_range), speed_mmps(vector_speed), should_play_anim=True)
                timeout = 0
                movetimer = 0
                eyeswitch = False
                while str(drive_future).find("pending") != -1:
                    if not robot_driving:
                        movetimer += (refresh_rate/4)
                    else:
                        movetimer = 0
                    if movetimer > 3:
                        movetimer = 0
                        if reanimator_logging:
                            log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                        if voice_debug:
                            say_future = myrobot.behavior.say_text("maybe not")
                    if not robot_good_to_go or not have_robot_control or robot_distance_mm < 65 or control_pending:
                        break
                    if timeout >= 8:
                        if rainbow_eyes and have_robot_control:
                            eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                        break
                    if rainbow_eyes and have_robot_control and not eyeswitch:
                        eyeswitch = True
                        eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
                    timeout = timeout + (refresh_rate/4)
                    sleep(refresh_rate/4)
                if drive_future:
                    drive_future.cancel()
                if rainbow_eyes and eyecolor_future:
                    eyecolor_future.cancel()
                if not robot_good_to_go or control_pending:
                    request = robot_control_request(False,False)
                    return
                if not have_robot_control:
                    request = robot_control_request(True,False)
                    if not request:
                        return
                myrobot.motors.set_wheel_motors(0, 0)
                myrobot.motors.set_lift_motor(0)
                sleep(0.2)
                if say_future:
                    say_future.cancel()
                # back up a lil' if we're close to a wall
                backupchance = random.randint(1, 100)
                if backupchance > 60:
                    robot_back_it_up()
            else:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_red,1)
                if reanimator_logging and not reduced_logging:
                    log.put_nowait("[action] " + str(vector_name) + " doesn't think there is enough space")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("no space!")
            sleep(refresh_rate)
            prox_array.clear()
            total_steps_count += 1 
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_random_drive issue: "+ repr(e))
    if rainbow_eyes and eyecolor_future:
        eyecolor_future.cancel()
    if say_future:
        say_future.cancel()
    request = robot_control_request(False,False)
    if debug_logging:
        log.put_nowait("[debugs] robot_random_drive complete")
    return
# robot_roll_cube will make Vector try to roll a cube, this fails a lot (which is ok)
def robot_roll_cube():
    global myrobot
    global log
    eyecolor_future = ""
    say_future      = ""
    drive_to_cube   = ""
    roll_the_cube   = ""
    movetimer       = 0
    docktimer       = 0
    if reanimator_logging or actions_logging:
        log.put_nowait("[action] " + str(vector_name) + " is thinking about rolling a cube")  
    try:
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        if voice_debug:
            say_future = myrobot.behavior.say_text("maybe roll a cube?")
        if reanimator_debug:
            log.put_nowait("[ranmtr] robot_roll_cube: " + str(vector_name) + " is driving to cube")
        drive_to_cube = myrobot.behavior.go_to_object(myrobot.world.light_cube, distance_mm(100.0))
        timeout = 0
        sleep(0.2)
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        while str(drive_to_cube).find("pending") != -1:
            if not robot_driving:
                movetimer += (refresh_rate/2)
            else:
                movetimer = 0
            if movetimer > 4:
                if say_future:
                    say_future.cancel()
                movetimer = 0
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_red,1)
                if reanimator_logging:
                    log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                break
            if not robot_good_to_go or not have_robot_control or control_pending:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] robot_roll_cube: roll cube exit (timeout, battery, or program exit)")
                break
            if timeout > 10:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control:
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)
        if drive_to_cube:
            drive_to_cube.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_roll_cube: drive to cube issue: "+str(e))
    if not robot_good_to_go or control_pending:
        request = robot_control_request(False,False)
        return
    if not have_robot_control:
        request = robot_control_request(True,False)
        if not request:
            return
    try:
        if reanimator_debug and not reduced_logging:
            log.put_nowait("[ranmtr] robot_roll_cube: " + str(vector_name) + " is rolling a cube")
        roll_the_cube = myrobot.behavior.roll_cube(myrobot.world.light_cube)
        timeout = 0
        eyeswitch = False
        while str(roll_the_cube).find("pending") != -1:
            if not robot_docking:
                docktimer += (refresh_rate/2)
            else:
                docktimer = 0
            if docktimer > 3:
                if say_future:
                    say_future.cancel()
                docktimer = 0
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_red,1)
                if reanimator_logging:
                    log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                    sleep(2)
                break
            if not robot_good_to_go or not have_robot_control or control_pending:
                break
            if timeout > 15:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control and not eyeswitch:
                eyeswitch = True
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)
        if roll_the_cube:
            roll_the_cube.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        rollable_cube = False
        request = robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_roll_cube rolling issue: "+str(e))
    # cointoss = random.randint(1, 100)
    # if cointoss > 70:
        # # play an extra animation at the end just because
        # robot_mix_animations()
    if debug_logging:
        log.put_nowait("[debugs] robot_roll_cube: job exiting")
    return
# robot_go_to_random_pose: will use Vector's internal map navigation to go somewhere random, this fails a lot (which is ok)
def robot_go_to_random_pose():
    # go_to_pose(pose, relative_to_robot=False, num_retries=0, _behavior_id=None)
    global myrobot
    global log
    eyecolor_future = ""
    say_future      = ""
    pose_future     = ""
    movetimer       = 0
    try:
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        if reanimator_logging:
            log.put_nowait("[action] " + str(vector_name) + " is thinking about going to a location nearby")
        cointoss = random.randint(0, 1)
        if cointoss == 1:
            xpose = random.randint((reanimator_max_distance/4), (reanimator_max_distance/2))
            if xpose < 10:
                xpose = 10
        else:
            xpose = -(random.randint((reanimator_max_distance/4), (reanimator_max_distance/2)))
            if xpose > -10:
                xpose = -10
        cointoss = random.randint(0, 1)
        if cointoss == 1:
            ypose = random.randint((reanimator_max_distance/4), (reanimator_max_distance/2))
            if ypose < 10:
                ypose = 10
        else:
            ypose = -(random.randint((reanimator_max_distance/4), (reanimator_max_distance/2)))
            if ypose > -10:
                ypose = 10
        zangle = random.randint(-359, 359)
        pose = Pose(x=xpose, y=ypose, z=0, angle_z=Angle(degrees=zangle))
        if reanimator_debug:
            log.put_nowait("[action] "+str(vector_name) + " is going to pose: "+str(pose))
        if voice_debug:
            say_future = myrobot.behavior.say_text("maybe go to " + str(int(xpose/10)) + " by " + str(int(ypose/10))+"?")
        pose_future = myrobot.behavior.go_to_pose(pose, relative_to_robot=True)
        timeout = 0
        eyeswitch = False
        while str(pose_future).find("pending") != -1 or timeout < 8:
            if not robot_driving:
                movetimer += (refresh_rate/2)
            else:
                movetimer = 0
            if movetimer > 4.5:
                if say_future:
                    say_future.cancel()
                movetimer = 0
                if reanimator_logging:
                    log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                break
            if not robot_good_to_go or not have_robot_control or control_pending:	
                break
            if timeout >= 8:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control and not eyeswitch:
                eyeswitch = True
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)	
        if pose_future:
            pose_future.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        if say_future:
            say_future.cancel()
        # back up a lil' if we're close to a wall
        backupchance = random.randint(1, 100)
        if backupchance > 30:
            robot_back_it_up()
        robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_go_to_random_pose issue: "+repr(e))
    return
# robot_look_around will briefly (4 seconds max) make Vector look around
def robot_look_around():
    global myrobot
    global log
    eyecolor_future     = ""
    say_future          = ""
    look_around_future  = ""
    done_looking        = 0
    lookcounter         = 0
    try:
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        if actions_logging or reanimator_logging:
            log.put_nowait("[action] " + str(vector_name) + " is having a look around")
        if voice_debug:
            say_future = myrobot.behavior.say_text("having a look!") 
        while done_looking == 0:
            timeout = 0
            look_around_future = myrobot.behavior.look_around_in_place()
            eyeswitch = False
            while str(look_around_future).find("pending") != -1 or timeout < 4.5:	
                if not robot_good_to_go or not have_robot_control or control_pending:	
                    break
                if timeout >= 4.5:
                    if rainbow_eyes and have_robot_control:
                        eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                    break
                if rainbow_eyes and have_robot_control and not eyeswitch:
                    eyeswitch = True
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
                timeout = timeout + (refresh_rate/2)
                sleep(refresh_rate/2)	
            if look_around_future:
                look_around_future.cancel()
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            done_looking = random.randint(0, 1)
            if done_looking == 0:
                lookcounter += 1
                if lookcounter > 4:
                    break
                if actions_logging or reanimator_logging:
                    log.put_nowait("[action] hmmm...")
                robot_random_turn(45,135,1)
        robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_look_around issue: "+repr(e))
    return
# robot_pick_up_cube will attempt to pick up a cube
def robot_pick_up_cube():
    global myrobot
    global log
    eyecolor_future         = ""
    say_future              = ""
    drive_to_cube           = ""
    lift_cube_future        = ""
    put_down_cube_future    = ""
    movetimer               = 0
    try:
        if reanimator_logging or actions_logging:
            log.put_nowait("[action] " + str(vector_name) + " is thinking about moving a cube")
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
    #go to cube
        if voice_debug:
            say_future = myrobot.behavior.say_text("maybe pick up a cube?")
        if reanimator_debug:
            log.put_nowait("[ranmtr] robot_pick_up_cube: " + str(vector_name) + " is driving to cube")
        drive_to_cube = myrobot.behavior.go_to_object(myrobot.world.light_cube, distance_mm(100.0))
        timeout = 0
        sleep(0.2)
        eyeswitch = False
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        while str(drive_to_cube).find("pending") != -1:
            if not robot_driving:
                movetimer += (refresh_rate/2)
            else:
                movetimer = 0
            if movetimer > 4:
                if say_future:
                    say_future.cancel()
                movetimer = 0
                if reanimator_logging:
                    log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                break
            if not robot_good_to_go or not have_robot_control or control_pending:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] robot_pick_up_cube: roll cube exit (timeout, battery, or program exit)")
                break
            if timeout > 10:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control:
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)
        if drive_to_cube:
            drive_to_cube.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        if not robot_good_to_go:
            request = robot_control_request(False,False)
            return
        if not have_robot_control:
            request = robot_control_request(True,False)
            if not request:
                return
    # lift
        timeout = 0
        movetimer = 0
        lift_cube_future = myrobot.behavior.pickup_object(myrobot.world.light_cube, use_pre_dock_pose=False)
        eyeswitch = False
        while str(lift_cube_future).find("pending") != -1 or timeout < 4:	
            if (not robot_driving and not robot_moving):
                movetimer += (refresh_rate/2)
            else:
                movetimer = 0
            if movetimer > 4:
                if say_future:
                    say_future.cancel()
                movetimer = 0
                if reanimator_logging:
                    log.put_nowait("[action] "+str(vector_name) + " changed their mind")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                break
            if not robot_good_to_go or not have_robot_control or control_pending:	
                break
            if timeout >= 40:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control and not eyeswitch:
                eyeswitch = True
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)	
        if lift_cube_future:
            lift_cube_future.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
    # take it somewhere random if we have it
        if robot_carrying:
            robot_go_to_random_pose()
        else:
            if reanimator_debug:
                log.put_nowait("[ranmtr] robot_pick_up_cube: failed to pick up a cube")
            if voice_debug:
                if say_future:
                    say_future.cancel()
                sleep(0.2)
                say_future = myrobot.behavior.say_text("maybe not")
    #put down (maybe add check with rangefinder here?)
        freespace = 0
        turncount = 0
        while robot_carrying and robot_good_to_go and turncount < 3:
            turncount += 1
            freespace = robot_check_free_space()
            if freespace > 65:
                put_down_cube_future = myrobot.behavior.place_object_on_ground_here()
                eyeswitch = False
                while str(put_down_cube_future).find("pending") != -1 or timeout < 4:	
                    if not robot_good_to_go or not have_robot_control or control_pending:	
                        break
                    if timeout >= 5:
                        if rainbow_eyes and have_robot_control:
                            eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                        break
                    if rainbow_eyes and have_robot_control and not eyeswitch:
                        eyeswitch = True
                        eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
                    timeout = timeout + (refresh_rate/2)
                    sleep(refresh_rate/2)	
                if put_down_cube_future:
                    put_down_cube_future.cancel()
                if rainbow_eyes and eyecolor_future:
                    eyecolor_future.cancel()
            else:
                if not robot_good_to_go:
                    break
                if not have_robot_control:
                    robot_control_request(True, False)
                robot_random_turn(80,120,1)
        if eyecolor_future:
            eyecolor_future.cancel()
        if say_future:
            eyecolor_future.cancel()
        if drive_to_cube:
            drive_to_cube.cancel()
        if put_down_cube_future:
            put_down_cube_future.cancel()
        robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_pick_up_cube issue: "+repr(e))
    return
# robot_pop_wheelie will attempt to pop a wheelie
def robot_pop_wheelie():
    global myrobot
    global log
    eyecolor_future     = ""
    say_future          = ""
    pop_wheelie_future  = ""
    movetimer           = 0
    try:
        if reanimator_logging or actions_logging:
            log.put_nowait("[action] " + str(vector_name) + " is thinking about popping a wheelie!")
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        if voice_debug:
            say_future = myrobot.behavior.say_text("maybe pop a wheelie?")
        timeout = 0
        eyeswitch = False
        pop_wheelie_future = myrobot.behavior.pop_a_wheelie(myrobot.world.light_cube)
        while str(pop_wheelie_future).find("pending") != -1 or timeout < 4:	
            if not robot_driving:
                movetimer += (refresh_rate/2)
            else:
                movetimer = 0
            if movetimer > 5:
                if say_future:
                    say_future.cancel()
                movetimer = 0
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_red,1)
                if reanimator_debug:
                    log.put_nowait("[action] "+str(vector_name) + " pop wheelie command received but no action, aborting")
                if voice_debug:
                    say_future = myrobot.behavior.say_text("maybe not")
                break
            if not robot_good_to_go or not have_robot_control or control_pending:	
                break
            if timeout >= 10:
                if rainbow_eyes and have_robot_control:
                    eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                break
            if rainbow_eyes and have_robot_control and not eyeswitch:
                eyeswitch = True
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            timeout = timeout + (refresh_rate/2)
            sleep(refresh_rate/2)	
        if pop_wheelie_future:
            pop_wheelie_future.cancel()
        if rainbow_eyes and eyecolor_future:
            eyecolor_future.cancel()
        if say_future:
            say_future.cancel()
        if eyecolor_future:
            eyecolor_future.cancel()
        robot_control_request(False,False)
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_pop_wheelie issue: "+repr(e))
    return
# robot_back_it_up will measure the distance ahead and maybe roll back a little
def robot_back_it_up():
    global myrobot
    global log
    eyecolor_future = ""
    say_future      = ""
    backup_future   = ""
    lift_future     = ""
    giggle_future   = ""
    try:
        if reanimator_debug:
            log.put_nowait("[action] " + str(vector_name) + " is evaluating whether to back up")
        if robot_good_to_go and not control_pending:
            if not have_robot_control:
                request = robot_control_request(True,False)
                if not request:
                    return
        else:
            return
        final_range = robot_check_free_space()
        if final_range < 55:
            if reanimator_debug and not reduced_logging:
                log.put_nowait("[action] robot_back_it_up: whoa that wall is close ("+str(final_range)+") to " + str(vector_name) + ", better back up")
            if robot_good_to_go:
                if not have_robot_control:
                    request = robot_control_request(True,False)
                    if not request:
                        return
            else:
                return
            if rainbow_eyes and have_robot_control:
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_red,1)
            backup_future = myrobot.behavior.drive_straight(distance_mm(-55), speed_mmps(20), should_play_anim=True)
            lift_future = myrobot.behavior.set_lift_height(1, accel=50.0, max_speed=50.0, duration=0.0)
            if reanimator_beep:
                # beeeep is kind of a placeholder ha ha, need to find a suitable animation 
                say_future = myrobot.behavior.say_text("beeeep... beeeep... beeeep...", use_vector_voice=True, duration_scalar=0.65)
            timeout = 0
            while str(backup_future).find("pending") != -1:
                if not robot_good_to_go or not have_robot_control or control_pending:
                    break
                if timeout >= 6:
                    if rainbow_eyes and have_robot_control:
                        eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                    break
                timeout = timeout + (refresh_rate/2)
                sleep(refresh_rate/2)
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            backup_future.cancel()
            lift_future.cancel()
            if say_future:
                say_future.cancel()
            if robot_good_to_go or control_pending:
                if not have_robot_control:
                    request = robot_control_request(True,False)
                    if not request:
                        return
            else:
                return
            if rainbow_eyes and have_robot_control:                    
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
            myrobot.motors.set_wheel_motors(0, 0)
            myrobot.motors.set_lift_motor(0)
            sleep(0.2)
            if rainbow_eyes and eyecolor_future:
                eyecolor_future.cancel()
            # having a laugh, mate?
            gigglechance = random.randint(1, 100)
            if gigglechance > 55:
                giggle_future = myrobot.anim.play_animation("anim_eyecontact_giggle_01", ignore_body_track=False, ignore_head_track=False, ignore_lift_track=False)
                timeout = 0
                eyeswitch = False
                while str(giggle_future).find("pending") != -1:
                    if not robot_good_to_go or control_pending:
                        break
                    if timeout >= 5:
                        if rainbow_eyes and have_robot_control:
                            eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
                        break
                    timeout = timeout + (refresh_rate/2)
                    sleep(refresh_rate/2)
                giggle_future.cancel()
                if rainbow_eyes and eyecolor_future:
                    eyecolor_future.cancel()
            if not robot_good_to_go:
                request = robot_control_request(False,False)
                return
            #turn around if we backed up	
            turnchance = random.randint(1, 100)
            if turnchance > 35:
                if reanimator_debug and not reduced_logging:
                    log.put_nowait("[ranmtr] " + str(vector_name) + " is doing a 180")
                if not have_robot_control:
                    request = robot_control_request(True,False)
                    if not request:
                        return
                robot_random_turn(140,220,1)
        else:
            if reanimator_debug and not reduced_logging:
                log.put_nowait("[ranmtr] robot_back_it_up: " + str(vector_name) + " has "+str(final_range)+"mm free space in front")
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] robot_back_it_up issue: "+ repr(e))
    robot_control_request(False,False)        
    return
# robot_check_free_space takes 5 rangefinder samples check free space in front of robot (need to add lift down/check function maybe?)
def robot_check_free_space():
    if robot_connected:
        x = 0
        range_cali = 0
        calibrated_range = 0
        while x < 5:
            request = ""
            range_cali = range_cali + robot_distance_mm
            sleep(refresh_rate*1.5)
            x += 1
        calibrated_range = (range_cali/5)
        if reanimator_debug and not reduced_logging:
            log.put_nowait("[action] robot_check_free_space measured " + str(round(calibrated_range,2)) + " mm free space")
        return calibrated_range
    else:
        calibrated_range = 0
        return calibrated_range
# robot_random_turn will turn the robot in place between [minangle] and [maxangle] at [speed]. Requires control.
def robot_random_turn(minangle,maxangle, speed):
    head_future = ""
    turn_future = ""
    lift_future = ""
    random_turn = 0
    plusminus = 0
    timeout = 0
    if robot_good_to_go and not control_pending:
        if not have_robot_control:
            request = robot_control_request(True,False)
            if not request:
                return
    else:
        return
    random_turn = random.randrange(minangle, maxangle, speed)
    plusminus = random.randint(0, 1)
    if plusminus == 1:
        random_turn = -random_turn
    if reanimator_debug and not reduced_logging:
        log.put_nowait("[action] robot_random_turn: " + str(vector_name) + " is performing random turn of "+str(random_turn)+" degrees")
    # head down, random turn, lift down
    head_future = myrobot.behavior.set_head_angle(MIN_HEAD_ANGLE)
    turn_future = myrobot.behavior.turn_in_place(degrees(random_turn))
    lift_future = myrobot.behavior.set_lift_height(0, accel=1000.0, max_speed=1000.0, duration=0.0)
    eyeswitch = False
    while str(turn_future).find("pending") != -1 or str(head_future).find("pending") != -1 or str(lift_future).find("pending") != -1:
        if not robot_good_to_go or not have_robot_control or control_pending:
            if reanimator_debug and not reduced_logging:
                log.put_nowait("[ranmtr] robot_random_turn: control loss, G2G: "+str(robot_good_to_go)+", CL: "+str(robot_current_control_level))
            break
        if timeout >= 3:
            if rainbow_eyes and have_robot_control:
                eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_yellow,1)
            break
        if rainbow_eyes and have_robot_control and not eyeswitch:
            eyeswitch = True
            eyecolor_future = myrobot.behavior.set_eye_color(eye_hue_blue,1)
        timeout = timeout + (refresh_rate/2)
        sleep(refresh_rate/2)
    if turn_future:
        turn_future.cancel()
    if head_future:
        head_future.cancel()
    if lift_future:
        lift_future.cancel()
    return
# manual_robot_control is responsible for actioning inputs received from input_thread
def manual_robot_control():
    global robot_command
    global log, myrobot
    global robot_control_blocking, manual_control, controltoggle, control_pending
    log.put_nowait("[inputs] requesting control, wait")
    randomcolor = (random.randint(1, 100)/100)
    command_future = ""
    while robot_control_blocking:
        sleep(refresh_rate)
    robot_control_blocking = True
    robot_control_request(True, False)
    control_pending = False
    log.put_nowait("[inputs] manual control granted, use arrow keys to move, Q/A to move lift up/down, W/S to move head up/down, E to change eye color. Press C to release control")
    if voice_debug:
        say_future = myrobot.behavior.say_text("you have control!")
    wheelspeed = 25
    if rainbow_eyes:
        myrobot.behavior.set_eye_color(eye_hue_purple,1)
    while robot_good_to_go and manual_control and not program_exit_requested:
        if not have_robot_control:
            break
        try:
            if robot_command == "stop":
                if command_future:
                    command_future.cancel()
                myrobot.motors.set_lift_motor(0)
                myrobot.motors.set_head_motor(0)
                myrobot.motors.set_wheel_motors(0, 0)
                sleep(0.2)
                wheelspeed = 25
            if robot_command == "forward":
                command_future = myrobot.motors.set_wheel_motors(wheelspeed, wheelspeed)
                wheelspeed += 3
            if robot_command == "backward":
                command_future = myrobot.motors.set_wheel_motors(-wheelspeed, -wheelspeed)
                wheelspeed += 3
            if robot_command == "turnleft":
                command_future = myrobot.motors.set_wheel_motors(-wheelspeed, wheelspeed)
                wheelspeed += 3
            if robot_command == "turnright":
                command_future = myrobot.motors.set_wheel_motors(wheelspeed, -wheelspeed)
                wheelspeed += 3
            if robot_command == "liftup":
                command_future = myrobot.motors.set_lift_motor(1)
            if robot_command == "liftdown":
                command_future = myrobot.motors.set_lift_motor(-1)
            if robot_command == "headup":
                command_future = myrobot.motors.set_head_motor(0.5)
            if robot_command == "headdown":
                command_future = myrobot.motors.set_head_motor(-0.5)
            if robot_command == "eyecolor":
                command_future = myrobot.behavior.set_eye_color(randomcolor,1)
                randomcolor += 0.01
                if randomcolor > 1:
                    randomcolor = 0
        except Exception as e:
            if except_logging and logging_thread_running:
                log.put_nowait("[errors] manual_robot_control issue: " + repr(e))
        if program_exit_requested:
            break
        sleep(refresh_rate)
    log.put_nowait("[inputs] releasing manual control")
    robot_control_request(False, False)
    robot_control_blocking = False
    manual_control = False
    controltoggle = True
    control_pending = False
    log.put_nowait("[inputs] manual control released")
    return  
# normalize_value makes sure values are between 1-100
def normalize_value(rawvalue):
    try:
        if rawvalue > 100:
            rawvalue = 100
        if rawvalue < 1:
            rawvalue = 1
        returnvalue = rawvalue
        return returnvalue
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] normalize_value: that wasn't right: "+repr(e))
# bool_to_value takes a boolean as input and returns an int 0/100 value for display
def bool_to_value(inputbool):
    try:
        if inputbool:
            returnvalue = 100
        else:
            returnvalue = 0
        return returnvalue
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] bool_to_value: that was not a boolean: "+repr(e))
# refresh_ui_colors will reload all values (called when color scheme changes)
def refresh_ui_colors():
    myrobot_batlevel.color             = ui_color_2
    myrobot_charging.color             = ui_color_2
    myrobot_docked.color               = ui_color_2
    myrobot_calmpower.color            = ui_color_2
    myrobot_gyrox.color                = ui_color_6
    myrobot_accelx.color               = ui_color_6
    myrobot_cliffdetect.color          = ui_color_2
    myrobot_falling.color              = ui_color_2
    myrobot_pickup.color               = ui_color_2
    myrobot_held.color                 = ui_color_2
    myrobot_gyroy.color                = ui_color_6
    myrobot_accely.color               = ui_color_6
    myrobot_touched.color              = ui_color_2
    myrobot_button.color               = ui_color_2
    myrobot_carrying.color             = ui_color_2
    myrobot_docking.color              = ui_color_2
    myrobot_gyroz.color                = ui_color_6
    myrobot_accelz.color               = ui_color_6
    myrobot_pathing.color              = ui_color_2
    myrobot_driving.color              = ui_color_2
    myrobot_moving.color               = ui_color_2
    myrobot_animate.color              = ui_color_2
    myrobot_headangle.color            = ui_color_6
    myrobot_liftheight.color           = ui_color_6
    myrobot_distance.color             = ui_color_2
    myrobot_l_wheel.color              = ui_color_6
    myrobot_voltage.color              = ui_color_2
    myrobot_r_wheel.color              = ui_color_6
    robotlog.color                     = ui_color_7
    myrobot_batlevel.border_color      = ui_color_3
    myrobot_charging.border_color      = ui_color_3
    myrobot_docked.border_color        = ui_color_3
    myrobot_calmpower.border_color     = ui_color_3
    myrobot_gyrox.border_color         = ui_color_4
    myrobot_accelx.border_color        = ui_color_4
    myrobot_cliffdetect.border_color   = ui_color_3
    myrobot_falling.border_color       = ui_color_3
    myrobot_pickup.border_color        = ui_color_3
    myrobot_held.border_color          = ui_color_3
    myrobot_gyroy.border_color         = ui_color_4
    myrobot_accely.border_color        = ui_color_4
    myrobot_touched.border_color       = ui_color_3
    myrobot_button.border_color        = ui_color_3
    myrobot_carrying.border_color      = ui_color_3
    myrobot_docking.border_color       = ui_color_3
    myrobot_gyroz.border_color         = ui_color_4
    myrobot_accelz.border_color        = ui_color_4
    myrobot_pathing.border_color       = ui_color_3
    myrobot_driving.border_color       = ui_color_3
    myrobot_moving.border_color        = ui_color_3
    myrobot_animate.border_color       = ui_color_3
    myrobot_headangle.border_color     = ui_color_3
    myrobot_liftheight.border_color    = ui_color_3
    myrobot_distance.border_color      = ui_color_3
    myrobot_l_wheel.border_color       = ui_color_3
    myrobot_voltage.border_color       = ui_color_3
    myrobot_r_wheel.border_color       = ui_color_3
    robotlog.border_color              = ui_color_5
# sigterm handling
def sigterm_handler(_signo, _stack_frame):
    global program_exit_requested
    log.put_nowait("[errors] Program exit requested by SIGTERM, closing threads")
    if headless:
        print("Program exit requested by SIGTERM, closing threads")
    program_exit_requested = True
signal.signal(signal.SIGTERM, sigterm_handler)
# MQTT publish debug function
def on_publish(client, userdata, mid):
    if MQTT_DEBUG:
        log.put_nowait("[system] MQTT message published")
# --- END OF FUNCTIONS SECTION ---
# --- START OF LAUNCH PREP SECTION ---
# --- In which we connect to the robot and get everything ready to go ---
# was the passive monitoring switch set? If yes disable file logging, discord logging, reanimator, and continuous_cycle
if passive_monitoring_only:
    log.put_nowait("[system] passive monitoring switch is set, file/discord logging, reanimator, and continuous cycles are disabled")
    file_logging                = False
    battery_csv_logging         = False
    discord_logging             = False
    reanimator                  = False
    continuous_cycle            = False
    continuous_cycle_scheduling = False
# clear screen
if not headless:
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')
else:
    print("VecTrix " + str(vt_version) + " started headless, gathering data at refresh rate " + str(refresh_rate) + ", press CTRL+C to exit")
# start UI thread
if not ui_thread_running and not headless:
    try:
        ui_thread_running = True
        Thread(name = "VT-UI", target = ui_thread).start()
    except Exception as e:
        print("[errors] FATAL: Issue starting ui_thread, exiting. E: "+repr(e))
        program_exit_requested = True
# start logging thread
if not logging_thread_running and not program_exit_requested:
    try:
        logging_thread_running = True
        Thread(name = "VT-LOG", target = logging_thread).start()
    except Exception as e:
        print("[errors] FATAL: Issue starting logging_thread, exiting. E: "+repr(e))
        program_exit_requested = True  
# start up input thread
if not input_thread_running and keyboard_control:
    try:
        input_thread_running = True
        Thread(name = "VT-input", target = input_thread).start()
    except Exception as e:
        log.put_nowait("[errors] FATAL: Issue starting thread for input_thread, exiting. E: "+repr(e))
        program_exit_requested = True
if debug_logging and not program_exit_requested:
    log.put_nowait("[system] Initializing and connecting to " + str(vector_name))
# start robot connection thread
while not robot_connected and not program_exit_requested:
    if not robot_connection_thread_running:
        robot_connection_error = False
        try:
            robot_connection_thread_running = True
            Thread(name = "VT-conn", target = robot_connection_thread).start()
        except Exception as e:
            log.put_nowait("[errors] FATAL: Issue starting thread for robot_connection_thread, exiting. E: "+repr(e))
            program_exit_requested = True
    else:
        if debug_logging and not reduced_logging:
            log.put_nowait("[debugs] initial connect: waiting for " + str(vector_name) + " to conn, conn thread running: "+str(robot_connection_thread_running))
        sleep(3)
if program_exit_requested:
    log.put_nowait("[system] exit requested before VecTrix was fully started, attempting to stop threads and exit")
    sleep(0.4)
    program_exit_requested  = True
    input_thread_stop       = True
    logging_thread_stop     = True
    ui_thread_stop          = True
    timeout = 0
    while (input_thread_running or logging_thread_running or ui_thread_running) and timeout < 10:
        if timeout >= 10:
            log.put_nowait("[system] timeout waiting for threads to close")
            break
        timeout = timeout + refresh_rate
        sleep(refresh_rate)
    sys.exit()
# if robot_connected:
    # for item in buttonlist:
        # item.color=ui_color_2
# start the camera feed if configured
if camera_logging:
    try:
        myrobot.camera.init_camera_feed()
    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] issue initializing the camera feed for " + str(vector_name) + ": "+repr(e))
# connect to cube if configured
if connect_to_cube:
    try:
        if not reduced_logging:
            log.put_nowait("[system] connecting to " + str(vector_name) + "'s cube")
        myrobot.world.connect_cube()

    except Exception as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[errors] issue initializing the cube connection: "+repr(e))
# start up data gathering thread
if not robot_sensor_thread_running:
    try:
        robot_sensor_thread_running = True
        Thread(name = "VT-sens", target = robot_sensor_thread).start()
    except Exception as e:
        log.put_nowait("[errors] FATAL: Issue starting thread for robot_sensor_thread, exiting. E: "+repr(e))
        exit()
# start up battery monitoring thread
if not robot_battery_thread_running:
    try:
        robot_battery_thread_running = True
        Thread(name = "VT-batt", target = robot_battery_thread).start()
    except Exception as e:
        log.put_nowait("[errors] FATAL: Issue starting thread for robot_battery_thread, exiting. E: "+repr(e))
        exit()
# start up event thread
if not robot_event_thread_running:
    try:
        robot_event_thread_running = True
        Thread(name = "VT-event", target = robot_event_thread).start()
    except Exception as e:
        log.put_nowait("[errors] FATAL: Issue starting thread for robot_event_thread_running, exiting. E: "+repr(e))
        exit()
# hold for thread readiness
timeout = 0
while (not robot_battery_ready or not robot_sensors_ready or not robot_events_ready) and timeout < 60:
    timeout = timeout+refresh_rate
    sleep(refresh_rate)
    if timeout >= 60:
        log.put_nowait("[system] FATAL: timeout while waiting for battery, sensor, and event threads to report ready")
        exit()
timeout = 0
sleep(1)
# initial accelerometer setup
accelcounter = 0
while accelcounter < 2:
    calibrate_accel_x = calibrate_accel_x + robot_accel_x
    calibrate_accel_y = calibrate_accel_y + robot_accel_y
    calibrate_accel_z = calibrate_accel_z + robot_accel_z
    accelcounter += 1
    sleep(refresh_rate*2)
calibrate_accel_x = calibrate_accel_x/3
calibrate_accel_y = calibrate_accel_y/3
calibrate_accel_z = calibrate_accel_z/3
# csv logging
if battery_csv_logging:
    csvlog="date,time,voltage,20sample_avg,calc_pct,batt_level,is_docked,is_charging"
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    try:
        if datestamp_log_files:
            log_file = open(date+"-"+battery_csv_filename, 'a')
        else:
            log_file = open(battery_csv_filename, 'a')
        log_file.write(csvlog + " \n")
        log_file.close()
    except Exception as e:
        timestamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
        msg = "[errors] issue logging to CSV file " + str(csvlog) + "- E: "+repr(e)
        log.put_nowait(msg) 
# MQTT
if MQTT_logging:
    mqttc = mqtt.Client()
    mqttc.on_publish = on_publish
# --- END OF LAUNCH PREP SECTION ---
# --- START OF MAIN LOOP ---
# -- in which we toil endlessly until told otherwise ---
while (not program_exit_requested and not quit_on_error_request):
    try:
        #are we connected? if not launch a new connection thread
        while not robot_connected and not program_exit_requested:
            if not robot_connection_thread_running:
                robot_connection_error = False
                try:
                    robot_connection_thread_running = True
                    sleep(1)
                    for item in buttonlist:
                        item.color=ui_color_3
                        item.value=100
                    Thread(name = "VT-conn", target = robot_connection_thread).start()
                except Exception as e:
                    log.put_nowait("[errors] FATAL: Issue starting thread for robot_connection_thread, exiting. E: "+repr(e))
                    exit()
            if debug_logging and not reduced_logging:
                log.put_nowait("[debugs] main loop: " + str(vector_name) + " not connected, waiting for connection thread. Conn thread running: " +str(robot_connection_thread_running))
            sleep(5)
        # connected and all is well, get to it
        if robot_connected and not program_exit_requested:
# --- CALCULATED VALUES SECTION ---
# --- In which we turn any gathered telemetry into formatted data for display by the UI thread ---
            # UI value calculations
            if not headless:            
            # UI: BATTERY STATE
                # VOLTAGE BAR CALC
                if battcounter == 20:
                    battcounter = 0
                    robot_voltage_calculated = (robot_voltage_average/20)
                    robot_voltage_average = 0
                    if not robot_docked:
                        for (v, p) in discharge_table.items():
                            if robot_voltage_calculated > v:
                                voltage_display_value = p
                        voltage_display_color = ui_color_1
                        if voltage_display_value > 20:
                            voltage_display_color = ui_color_3
                        if voltage_display_value > 49:
                            voltage_display_color = ui_color_2
                    if robot_docked:
                        for (v, p) in charge_table.items():
                            if robot_voltage_calculated < v:
                                voltage_display_value = p
                        voltage_display_color = ui_color_2
                else:
                    battcounter += 1
                    robot_voltage_average += robot_voltage
                if robot_batlevel != robot_batlevel_old:
                    if robot_batlevel == 1:
                        myrobot_batlevel.value = 33
                        myrobot_batlevel.color = ui_color_1
                        voltage_display_value = 10
                        voltage_display_color =  ui_color_1
                    elif robot_batlevel == 2:
                        myrobot_batlevel.value = 66
                        myrobot_batlevel.color = ui_color_2
                    elif robot_batlevel == 3:
                        myrobot_batlevel.value = 100
                        myrobot_batlevel.color = ui_color_2
                        voltage_display_value = 100 
                    robot_batlevel_old = robot_batlevel
            # charging
                myrobot_charging.value = bool_to_value(robot_charging)
                if robot_charging:
                    myrobot_charging.color = ui_color_2
                else:
                    myrobot_charging.color = ui_color_0
            #docked
                myrobot_docked.value = bool_to_value(robot_docked)
                if robot_docked:
                    myrobot_docked.color = ui_color_2
                    voltage_display_color = ui_color_4
                else:
                    myrobot_docked.color = ui_color_0
            # calmpower/sleep
                myrobot_calmpower.value = bool_to_value(robot_calmpower)
                if robot_calmpower:
                    myrobot_calmpower.color = ui_color_2
                else:
                    myrobot_calmpower.color = ui_color_0
                
                myrobot_voltage.color = voltage_display_color
                myrobot_voltage.value = voltage_display_value
        # UI: SENSORS 
                # cliff values
                myrobot_cliffdetect.value = bool_to_value(robot_cliffdetect)
                if robot_cliffdetect:
                    myrobot_cliffdetect.color = ui_color_2
                else:
                    myrobot_cliffdetect.color = ui_color_0
                # falling values  
                myrobot_falling.value = bool_to_value(robot_falling)
                if robot_falling:
                    myrobot_falling.color = ui_color_2
                else:
                    myrobot_falling.color = ui_color_0
                # pickup values 
                myrobot_pickup.value = bool_to_value(robot_pickup)
                if robot_pickup:
                    myrobot_pickup.color = ui_color_2
                else:
                    myrobot_pickup.color = ui_color_0
                # held values
                myrobot_held.value = bool_to_value(robot_held)
                if robot_held:
                    myrobot_held.color = ui_color_2
                else:
                    myrobot_held.color = ui_color_0
                # touching data
                myrobot_touched.value = bool_to_value(robot_is_being_touched)
                if robot_is_being_touched:
                    myrobot_touched.color = ui_color_2
                else:
                    myrobot_touched.color = ui_color_0
                # button press data
                myrobot_button.value = bool_to_value(robot_button)
                if robot_button:
                    myrobot_button.color = ui_color_2
                else:
                    myrobot_button.color = ui_color_0
        # UI: ACTIONS
                # cube carry
                myrobot_carrying.value = bool_to_value(robot_carrying)
                if robot_carrying:
                    myrobot_carrying.color = ui_color_2
                else:
                    myrobot_carrying.color = ui_color_0
                # docking
                myrobot_docking.value = bool_to_value(robot_docking)
                if robot_docking:
                    myrobot_docking.color = ui_color_2
                else:
                    myrobot_docking.color = ui_color_0
        # UI: MOTION
                # moving data (any motor active)
                myrobot_moving.append(bool_to_value(robot_moving))
                # animating data
                myrobot_animate.append(bool_to_value(robot_animating))
                # pathing data
                myrobot_pathing.append(bool_to_value(robot_pathing))
                # driving data
                myrobot_driving.append(bool_to_value(robot_driving))
        # UI: GYRO
                if robot_gyro_x != robot_gyro_x_old:
                    gyrox = normalize_value(int((robot_gyro_x*10)+50))
                    robot_gyro_x_old = robot_gyro_x
                if robot_gyro_y != robot_gyro_y_old:
                    gyroy = normalize_value(int((robot_gyro_y*10)+50))
                    robot_gyro_y_old = robot_gyro_y
                if robot_gyro_z != robot_gyro_z_old:
                    gyroz = normalize_value(int((robot_gyro_z*10)+50))
                    robot_gyro_z_old = robot_gyro_z
                myrobot_gyrox.append(gyrox)
                myrobot_gyroy.append(gyroy)
                myrobot_gyroz.append(gyroz)
        # UI: ACCELEROMETER
                # ACCELEROMETER CONTINUOUS RECALIBRATION
                if (robot_good_to_go or robot_docked) and acclcalibratecounter >= 50:
                    acclcalibratecounter = 0
                    accelcounter = 0
                    while accelcounter < 2:
                        calibrate_accel_x = calibrate_accel_x + robot_accel_x
                        calibrate_accel_y = calibrate_accel_y + robot_accel_y
                        calibrate_accel_z = calibrate_accel_z + robot_accel_z
                        accelcounter += 1
                    calibrate_accel_x = calibrate_accel_x/3
                    calibrate_accel_y = calibrate_accel_y/3
                    calibrate_accel_z = calibrate_accel_z/3
                else:
                    acclcalibratecounter += 1
                if robot_accel_x != robot_accel_x_old:
                    accelx = normalize_value(int(((calibrate_accel_x-robot_accel_x)/120)+50))
                    robot_accel_x_old = robot_accel_x
                if robot_accel_y != robot_accel_y_old:
                    accely = normalize_value(int(((calibrate_accel_y-robot_accel_y)/120)+50))
                    robot_accel_y_old = robot_accel_y
                if robot_accel_z != robot_accel_z_old:
                    accelz = normalize_value(int(((calibrate_accel_z-robot_accel_z)/120)+50))
                    robot_accel_z_old = robot_accel_z
                myrobot_accelx.append(accelx)
                myrobot_accely.append(accely)
                myrobot_accelz.append(accelz)
        # UI: HEAD ANGLE
                if robot_head_angle_rad != robot_head_angle_rad_old:
                    heada = normalize_value(int(((math.degrees(robot_head_angle_rad))+20)*1.8))
                    robot_head_angle_rad_old = robot_head_angle_rad
                myrobot_headangle.append(heada) 
        # UI: LIFT
                if robot_lift_height_mm != robot_lift_height_mm_old:
                    lifta = normalize_value(int((robot_lift_height_mm-32)*1.5))
                    robot_lift_height_mm_old = robot_lift_height_mm
                myrobot_liftheight.append(lifta)
        # UI: RANGEFINDER
                if robot_distance_mm != robot_distance_mm_old:
                    if not robot_is_lift_in_fov:
                        displaydistance = normalize_value(int((400-robot_distance_mm)/3.4))   
                        myrobot_distance.value = displaydistance
                        robot_distance_mm_old = robot_distance_mm
        # UI: WHEEL SPEED
                lwheelspeed = normalize_value(int((robot_left_wheel_speed_mmps/2.2)+50))
                rwheelspeed = normalize_value(int((robot_right_wheel_speed_mmps/2.2)+50))
                myrobot_l_wheel.append(lwheelspeed)
                myrobot_r_wheel.append(rwheelspeed)
        # Flash borders on max (turn selected graph borders red when hitting 0 or 100)
                if flash_borders_on_max:
                        if gyrox <= 1 or gyrox >= 100:
                            myrobot_gyrox.border_color =  ui_color_1
                        else:
                            myrobot_gyrox.border_color =  ui_color_4
                        if gyroy <= 1 or gyroy >= 100:
                            myrobot_gyroy.border_color =  ui_color_1
                        else:
                            myrobot_gyroy.border_color =  ui_color_4
                        if gyroz <= 1 or gyroz >= 100:
                            myrobot_gyroz.border_color =  ui_color_1
                        else:
                            myrobot_gyroz.border_color =  ui_color_4
                        if accelx == 1 or accelx == 100:
                            myrobot_accelx.border_color =  ui_color_1
                        else:
                            myrobot_accelx.border_color =  ui_color_4
                        if accely == 1 or accely == 100:
                            myrobot_accely.border_color =  ui_color_1
                        else:
                            myrobot_accely.border_color =  ui_color_4
                        if accelz == 1 or accelz == 100:
                            myrobot_accelz.border_color =  ui_color_1
                        else:
                            myrobot_accelz.border_color =  ui_color_4
                        if heada == 1 or heada == 100:
                            myrobot_headangle.border_color =  ui_color_3
                        else:
                            myrobot_headangle.border_color =  ui_color_3
                        if lifta == 1 or lifta == 100:
                            myrobot_liftheight.border_color =  ui_color_3
                        else:
                            myrobot_liftheight.border_color =  ui_color_3
                        if lwheelspeed == 1 or lwheelspeed == 100:
                            myrobot_l_wheel.border_color = ui_color_1
                        else:
                            myrobot_l_wheel.border_color = ui_color_3
                        if rwheelspeed == 1 or rwheelspeed == 100:
                            myrobot_r_wheel.border_color = ui_color_1
                        else:
                            myrobot_r_wheel.border_color = ui_color_3
# --- END OF CALCULATED VALUES SECTION ---
# --- SUBROUTINES SECTION ---
# --- In which we use the gathered data to do fun stuff  ---
# This is also where I suggest you add your own routines. You can read robot state values such as robot_good_to_go, robot_current_control_level, robot_control_blocking, robot_voltage, robot_held, robot_...etc.
# you can also call routines like robot_random_drive(), robot_control_request(control_or_release), robot_roll_cube()
    # CONTINUOUS CYCLE 
            if robot_docked and continuous_cycle_scheduling and (continuous_cycle or cctoggle):
                cctime = datetime.datetime.now().time()
                timestamp = '{:%H:%M}'.format(datetime.datetime.now())
                if (cctime > datetime.time(continuous_cycle_earliest) and cctime < datetime.time(continuous_cycle_latest)):
                    if not ccannounce:
                        if dock_events_logging:
                            log.put_nowait("[cycles] continuous cycle is active, will end at "+str(continuous_cycle_latest)+":00")
                        ccannounce = True
                    continuous_cycle = True
                    cctoggle = False
                else:
                    if ccannounce:
                        if dock_events_logging:
                            log.put_nowait("[cycles] continuous cycle is not active, will start at "+str(continuous_cycle_earliest)+":00")
                        ccannounce = False
                    continuous_cycle = False
                    cctoggle = True
            if robot_docked and continuous_cycle:
                # ADVANCED USE ONLY: if you have a method to detect presence replace my code here
                # this example will only work for my home, I use several Hue sensors and openHAB to come to a consensus on whether a room is occupied
                if use_presence:
                    try:
                        # check every ~10 seconds
                        if presencecounter >= 10:
                            presencecounter = 0
                            # get presence from OpenHAB
                            presencetokenjson = requests.get("http://192.168.0.175:8080/rest/items/MiscHouseData_collect_Housepresencetoken/state")
                            presencetoken = str(presencetokenjson.text)
                            # are we in the study where Vector is? If yes, increase the counter else zero it
                            if presencetoken == "study":
                                presence_ok += 1
                            else:
                                presence_ok = 0
                        else:
                            presencecounter += refresh_rate
                    except Exception as e:
                        # any issue? set it to 0
                        presence_ok = 0
                        presencecounter = 0
                        pass
                else:
                    # if we don't use presence just set it to 12
                    presence_ok = 12
                if robot_docked and not robot_charging and robot_batlevel == 3 and not yeetbot_thread_running and presence_ok >= 12:
                    if debug_logging:
                        log.put_nowait("[debugs] continuous_cycle: launching yeetbot thread")
                    try:
                        yeetbot_thread_running = True
                        Thread(name = "VT-yeet", target = yeetbot).start()
                    except Exception as e:
                        if except_logging and logging_thread_running:
                            log.put_nowait("[errors] continuous_cycle: issue starting thread, continuous cycle inactive. E: "+repr(e))
                        continuous_cycle = False
    # VECTOR REANIMATOR, or how often does Vector sit still during an outing (and can we fix it)(yes we can)
            if not robot_docked and reanimator:
                if (robot_moving or robot_driving) or manual_control or yeetbot_thread_running or robot_performing_action or reanimator_thread_running or recent_wake_word:
                    vector_sit_still_total_time = 0
                    vector_is_idle = False
                if robot_good_to_go:
                #if not robot_cliffdetect and not robot_held and not robot_pickup and not robot_docked and not reanimator_thread_running:
                    if stillswitch and (robot_moving or robot_driving) and not reanimator_thread_running:
                        stillswitch = False
                        if vector_sit_still_total_time == 0:
                            pass
                        else:
                            if debug_logging and not reduced_logging:
                                msg = "[debugs] " + str(vector_name) + " has started moving again, inactivity for "+str("%.2f" % round(vector_sit_still_total_time,2))+" seconds"
                                log.put_nowait(msg)
                            vector_sit_still_total_time = 0
                    if (robot_moving or robot_driving) or manual_control or yeetbot_thread_running or robot_performing_action or reanimator_thread_running:
                        vector_sit_still_total_time = 0
                        vector_is_idle = False
                    if not reanimator_thread_running and not startup and not (robot_moving or robot_driving):
                        vector_sit_still_total_time = vector_sit_still_total_time + refresh_rate
                    if not stillswitch and vector_sit_still_total_time > reanimator_timeout and not reanimator_thread_running:
                        if debug_logging and not reduced_logging:
                            log.put_nowait("[debugs] " + str(vector_name) + " has hit idle threshold at "+str(vector_sit_still_total_time)+ " seconds")
                        if not reanimator_thread_running and not vector_is_idle:
                            vector_is_idle = True
                            vector_sit_still_total_time = 0
                        stillswitch = True
                    if vector_sit_still_total_time > reanimator_timeout and not reanimator_thread_running:
                        vector_is_idle = True
                        vector_sit_still_total_time = 0
                else:
                    vector_sit_still_total_time = 0
                    stillswitch = False
                if endless_reanimator:
                    vector_sit_still_total_time = 0
                    vector_is_idle = True
                if yeetbot_thread_running or robot_control_blocking:
                    vector_is_idle = False
                if vector_is_idle and not reanimator_thread_running and robot_good_to_go:
                    try:
                        reanimator_thread_running = True
                        Thread(name = "VT-ranmtr", target = reanimator_thread).start()
                    except Exception as e:
                        log.put_nowait("[errors] FATAL: Issue starting thread for reanimator_thread, reanimated inactive. E: "+repr(e))
                        reanimator = False
    # volume controls
            if volume_controls and volumechanged:
                if volumelevel == 0:
                    myrobot.audio.set_master_volume(audio.RobotVolumeLevel.LOW)
                    log.put_nowait("[inputs] volume level LOW")
                    volumechanged = False
                if volumelevel == 1:
                    myrobot.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM_LOW)
                    log.put_nowait("[inputs] volume level MEDIUM_LOW")
                    volumechanged = False
                if volumelevel == 2:
                    myrobot.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM)
                    log.put_nowait("[inputs] volume level MEDIUM")
                    volumechanged = False
                if volumelevel == 3:
                    myrobot.audio.set_master_volume(audio.RobotVolumeLevel.MEDIUM_HIGH)
                    log.put_nowait("[inputs] volume level MEDIUM_HIGH")
                    volumechanged = False
                if volumelevel == 4:
                    myrobot.audio.set_master_volume(audio.RobotVolumeLevel.HIGH)
                    log.put_nowait("[inputs] volume level HIGH")
                    volumechanged = False
# --- END OF SUBROUTINES SECTION ---
# --- LOGGING SECTION ---
# --- In which we turn gathered data into log entries ---
    # BATTERY AND DOCK LOGIC
            # log charger state after startup and initial filling of the truth table
            if not startup:
                if not robot_docked:
                    # left dock with full charge
                    # left dock with full charge
                    if fullcharge and docked and not charging:
                        discharge_start_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        if dock_events_logging:
                            log.put_nowait("[action] " + str(vector_name) + " has left the charger with a full battery charge")
                        partial = False
                        if continuous_cycle and dock_events_logging and not reduced_logging:
                            log.put_nowait("[system] continuous cycle is active, current cycle for " + str(vector_name) + " is: " + str(yeetcounter))
                            yeetcounter += 1
                    # left dock but not with full charge 
                    if not fullcharge and docked and charging:
                        charge_stop_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        discharge_start_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        partial = True
                        # dock miss detection
                        if charge_start_time and charge_stop_time:
                            d1 = datetime.datetime.strptime(charge_start_time, "%H:%M:%S")
                            d2 = datetime.datetime.strptime(charge_stop_time, "%H:%M:%S")
                            d3 = datetime.datetime.strptime(str(d2 - d1), "%H:%M:%S")
                            if d3 < datetime.datetime.strptime("00:00:15", "%H:%M:%S") and dock_events_logging and not reduced_logging:
                                log.put_nowait("[chargr] Charger docking attempt miss detected, " + str(vector_name) + " was on charger for less than 15 seconds")
                                partial = True
                            d1 = ""
                            d2 = ""
                            d3 = ""
                        if dock_events_logging:
                            log.put_nowait("[action] " + str(vector_name) + " has left the charger but not with a full battery charge")
                    # not on dock, low power notification
                    if not lowpower and robot_batlevel == 1:
                        #lowpower_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        if dock_events_logging:
                            log.put_nowait("[chargr] " + str(vector_name) + " has a low battery, going to find the charger")  
                if robot_docked:        
                    stuck_warning = False
                    # returned to dock with low battery    
                    if lowpower and robot_charging and not docked and not fullcharge and not charging:
                        discharge_stop_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        if dock_events_logging:
                            log.put_nowait("[action] " + str(vector_name) + " has successfully docked with charger after battery hit low state")
                    # returned to dock, not with low battery
                    if not lowpower and not docked and not charging and robot_charging:
                        discharge_stop_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        partial = True
                        if dock_events_logging:
                            log.put_nowait("[action] " + str(vector_name) + " has successfully docked with charger before battery hit low state")
                    # on dock charging
                    if not charging and robot_charging and not docked:
                        charge_start_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        if dock_events_logging and not reduced_logging:
                            log.put_nowait("[chargr] " + str(vector_name) + "'s battery is charging")
                    # on dock, not charging    
                    if charging and not robot_charging and robot_batlevel == 3 and not fullcharge:
                        charge_stop_time = '{:%H:%M:%S}'.format(datetime.datetime.now())
                        if dock_events_logging and not reduced_logging:
                            log.put_nowait("[chargr] " + str(vector_name) + "'s battery is fully charged")
        # BATT/DOCK TRUTH TABLE UPDATE LOGIC
            if robot_docked:
                if robot_charging:
                    fullcharge = False
                    charging = True
                    docked = True
                    lowpower = False
                    dockcounter = 0
                else:
                    fullcharge = True
                    charging = False
                    docked = True
                    lowpower = False
            if not robot_docked:
                if robot_batlevel == 1:
                    fullcharge = False
                    charging = False
                    docked = False
                    lowpower = True
                else:
                    fullcharge = False
                    charging = False
                    docked = False
                    lowpower = False
        # CHARGE CYCLE LOGGING
            if charge_cycle_logging:
                # first run logic, were we off dock or still charging?
                if startup:
                    # if continuous_cycle_scheduling:
                        # log.put_nowait("[system] continuous_cycle: currently set to: "+str(continuous_cycle)+", scheduled: "+str(continuous_cycle_scheduling)+", starts at "+str(continuous_cycle_earliest)+":00 and ends at "+str(continuous_cycle_latest)+":00")
                    batlvltxt = ""
                    if robot_batlevel == 1:
                        batlvltxt = "low"
                    if robot_batlevel == 2:
                        batlvltxt = "okay"
                    if robot_batlevel == 3:
                        batlvltxt = "full"
                    if robot_docked:
                        if robot_charging and startup:
                            chrgtxt = ""
                            if robot_charging:
                                chrgtxt = "charging"
                            else:
                                chrgtxt = "resting"
                            log.put_nowait("[chargr] When VecTrix was started, " + str(vector_name) + " was "+chrgtxt+" on the charger, battery level was "+batlvltxt)
                    else:
                        log.put_nowait("[chargr] When VecTrix was started, " + str(vector_name) + " was not on the charger, battery level was "+batlvltxt)
                # start/end times for (dis)charge cycles
                # if we have an endtime but not a start time, skip!
                if discharge_stop_time and not discharge_start_time:
                    discharge_stop_time = ""
                    partial = True
                if charge_stop_time and not charge_start_time:
                    charge_stop_time = ""
                    partial = True
                # indicate if we had a partial or full charge/discharge of the battery
                if partial:
                    partialtext = "partial"
                else:
                    partialtext = "full"
                # report on charge/discharge cycle times, I have no idea how datetime works, so this is godawful code but it works
                if discharge_start_time and discharge_stop_time:
                    d1 = datetime.datetime.strptime(discharge_start_time, "%H:%M:%S")
                    d2 = datetime.datetime.strptime(discharge_stop_time, "%H:%M:%S")
                    log.put_nowait("[chargr] " + str(vector_name) + " had a " + partialtext + " battery discharge from " + str(discharge_start_time) + " to " + str(discharge_stop_time) + ", total time: " + str(d2-d1))
                    discharge_start_time = ""
                    discharge_stop_time  = ""
                    d1 = ""
                    d2 = ""
                    partial = False
                    partialtext = ""
                if charge_start_time and charge_stop_time:
                    d1 = datetime.datetime.strptime(charge_start_time, "%H:%M:%S")
                    d2 = datetime.datetime.strptime(charge_stop_time, "%H:%M:%S")
                    log.put_nowait("[chargr] " + str(vector_name) + " had a " + partialtext + " battery charge from " + str(charge_start_time) + " to " + str(charge_stop_time) + ", total time: " + str(d2-d1))           
                    charge_start_time = ""
                    charge_stop_time = ""
                    d1 = ""
                    d2 = ""
                    partial = False
                    partialtext = ""
        # battery logging
            if battery_logging:
                if batlogcounter >= battery_logging_interval:
                    log.put_nowait("[chargr] " + str(vector_name) + " raw voltage: " + str(robot_voltage) + ", 20-sample avg: " + str(robot_voltage_calculated) + ", docked: " + str(robot_docked) + ", charging: "+str(robot_charging)+ ", batlevel: " + str(robot_batlevel))
                    batlogcounter = 0
                else:
                    batlogcounter += refresh_rate
        # object logging only on low battery
            if object_logging_while_low_bat:
                if robot_batlevel == 1 and not robot_docked and not object_logging and not lowbat_objloggingtoggle:
                    object_logging = 1
                    myrobot.events.subscribe(on_robot_object_disappeared, Events.object_disappeared, evt)
                    myrobot.events.subscribe(on_robot_object_moved, Events.object_moved, evt)
                    myrobot.events.subscribe(on_robot_object_stopped_moving, Events.object_stopped_moving, evt)
                    myrobot.events.subscribe(on_robot_object_appeared, Events.object_appeared, evt)
                    myrobot.events.subscribe(on_robot_object_observed, Events.object_observed, evt)
                    lowbat_objloggingtoggle = True
                if robot_docked and not object_logging and lowbat_objloggingtoggle:
                    object_logging = 0
                    myrobot.events.unsubscribe(on_robot_object_disappeared, Events.object_disappeared)
                    myrobot.events.unsubscribe(on_robot_object_moved, Events.object_moved)
                    myrobot.events.unsubscribe(on_robot_object_stopped_moving, Events.object_stopped_moving)
                    myrobot.events.unsubscribe(on_robot_object_appeared, Events.object_appeared)
                    myrobot.events.unsubscribe(on_robot_object_observed, Events.object_observed)
                    lowbat_objloggingtoggle = False
        # robot is stuck and went to sleep while waiting for rescue
            if robot_calmpower and not robot_docked and (robot_pickup or robot_held or robot_cliffdetect) and not stuck_warning:
                stuck_warning = True
                log.put_nowait("[action] " + str(vector_name) + " is in trouble and waits for your rescue")
            if not robot_docked and not (robot_pickup or robot_held or robot_cliffdetect) and not robot_calmpower:
                stuck_warning = False
        # sensors logging 
            if sensors_logging:
                if robot_cliffdetect and not cliffswitch and not recent_cliff:
                    log.put_nowait("[sensor] " + str(vector_name) + " senses a cliff")
                    recent_cliff = True
                    cliffswitch = True
                if not robot_cliffdetect and cliffswitch:
                    log.put_nowait("[sensor] " + str(vector_name) + " no longer senses a cliff")
                    cliffswitch = False
                if robot_falling and not fallswitch:
                    log.put_nowait("[sensor] " + str(vector_name) + " is falling, aaah!")
                    fallswitch = True
                if not robot_falling and fallswitch:
                    log.put_nowait("[sensor] " + str(vector_name) + " is no longer falling")
                    fallswitch = False
                if robot_pickup and not pickupswitch and not recent_pickup:
                    recent_pickup = True
                    if not reduced_logging:
                        log.put_nowait("[sensor] " + str(vector_name) + " senses being picked up")
                    pickupswitch = True
                if not robot_pickup and pickupswitch:
                    if not reduced_logging:
                        log.put_nowait("[sensor] " + str(vector_name) + " no longer senses being picked up")
                    pickupswitch = False
                if robot_held and not heldswitch and not recent_pickup:
                    recent_pickup = True
                    if not reduced_logging:
                        log.put_nowait("[sensor] " + str(vector_name) + " senses being held")
                    heldswitch = True
                if not robot_held and heldswitch:
                    if not reduced_logging:
                        log.put_nowait("[sensor] " + str(vector_name) + " no longer senses being held")
                    heldswitch = False
                if robot_is_being_touched and not petswitch and not recent_touch:
                    recent_touch = True
                    log.put_nowait("[sensor] " + str(vector_name) + " is being petted. Aw yiss!")
                    petswitch = True
                if not robot_is_being_touched and petswitch:
                    petswitch = False
                if robot_button and not buttonswitch:
                    log.put_nowait("[sensor] " + str(vector_name) + " senses a button press")
                    buttonswitch = True
                if not robot_button and buttonswitch:
                    buttonswitch = False
        # actions logging
            # calmpower/sleep logging
            if actions_logging:
                if robot_docked:
                    if robot_calmpower and not calmpowertoggle:
                        log.put_nowait("[action] " + str(vector_name) + " is asleep")
                        calmpowertoggle = True
                    if not robot_calmpower and calmpowertoggle:
                        if leavechargerrequest or yeetbot_thread_running:
                            log.put_nowait("[action] " + str(vector_name) + " is awake")
                        else:
                            log.put_nowait("[action] something woke " + str(vector_name) + "!")
                        calmpowertoggle = False
        # robot dreams
                    if robot_calmpower and robot_moving and dream_delay_counter > 180 and not dreamtoggle:
                        dreaming = random.randint(1, 100)
                        if dreaming > (100-dreamchance):
                            vector_dream = random.choice(dreamlist)
                            log.put_nowait("[action] " + str(vector_name) + " dreams of " + vector_dream)
                        dreamtoggle = True
                        dream_delay_counter = 0
                    if  robot_calmpower and not robot_moving:
                        dream_delay_counter += refresh_rate
                    if dream_delay_counter > 360:
                        dreamtoggle = False
                        dream_delay_counter = 0
        # carrying cube
                if robot_carrying and not carryswitch:
                    log.put_nowait("[action] " + str(vector_name) + " is carrying a cube")
                    carryswitch = True
                if not robot_carrying and carryswitch:
                    log.put_nowait("[action] " + str(vector_name) + " has put down a cube")
                    carryswitch = False
                if robot_docking and not dockswitch:
                    dockswitch = True
                    if robot_batlevel == 1 and not reduced_logging:
                        log.put_nowait("[action] " + str(vector_name) + " is attempting to get on the charger")
                        docking = 1
                        dockcounter += 1
                        if dockcounter > 1 and not reduced_logging:
                            log.put_nowait("[chargr] " + str(vector_name) + " has failed to get on the charger " + str(dockcounter) + " times")
                            if dockcounter == 4:
                                log.put_nowait("[chargr] WARNING: " + str(vector_name) + " has problems with getting on the charger, is the ambient light bright enough for Vector to see the charger? Are the tracks and wheels clean?")
                    else:
                        if not reduced_logging:
                            log.put_nowait("[action] " + str(vector_name) + " is attempting to dock with cube or charger")
                if not robot_docking and dockswitch:        
                    dockswitch = False
        # motion logging
            if motion_logging:
                if robot_moving and not movingswitch and not reduced_logging:
                    movingswitch = True
                    log.put_nowait("[motion] " + str(vector_name) + " is in motion (any motor)")
                if not robot_moving and movingswitch and not reduced_logging:
                    log.put_nowait("[motion] " + str(vector_name) + " is no longer in motion (any motor)")
                    movingswitch = False
                if robot_animating and not animatingswitch and not reduced_logging:
                    animatingswitch = True
                    log.put_nowait("[motion] " + str(vector_name) + " is animating")
                if not robot_animating and animatingswitch and not reduced_logging:
                    animatingswitch = False
                    log.put_nowait("[motion] " + str(vector_name) + " is no longer animating")
                if robot_pathing and not pathswitch:
                    log.put_nowait("[motion] " + str(vector_name) + " is pathing somewhere")
                    pathswitch = True
                if not robot_pathing and pathswitch:
                    pathswitch = False
                    log.put_nowait("[motion] " + str(vector_name) + " is no longer pathing")
                if robot_driving and not drivingswitch and not reduced_logging:
                    log.put_nowait("[motion] " + str(vector_name) + "'s wheels are moving")
                    drivingswitch = True
                if not robot_driving and drivingswitch and not reduced_logging:
                    log.put_nowait("[motion] " + str(vector_name) + "'s wheels are no longer moving")
                    drivingswitch = False
        # accel/gyro logging
            if accelgyro_logging:
                if accelgyrocounter >= accelgyro_logging_interval:
                    accelgyrocounter = 0
                    log.put_nowait("[sensor] " + str(vector_name) + " raw accel: " + str(robot_accel_x) + "," + str(robot_accel_y) + "," + str(robot_accel_z))
                    log.put_nowait("[sensor] " + str(vector_name) + " cal accel: " + str(calibrate_accel_x) + "," + str(calibrate_accel_y) + "," + str(calibrate_accel_z))
                    log.put_nowait("[sensor] " + str(vector_name) + " gyro," + str(robot_gyro_x) + "," + str(robot_gyro_y) + "," + str(robot_gyro_z))
                else:
                    accelgyrocounter += refresh_rate
        # rangefinder logging
            if rangefinder_logging:
                if rangecounter >= rangefinder_logging_interval:
                    log.put_nowait("[sensor] " + str(vector_name) + " rangefinder: " + str(robot_distance_mm) + ", signal quality: " + str(robot_signal_quality))
                    rangecounter = 0
                else: 
                    rangecounter += refresh_rate
        # debug logging 
            if debug_logging and debug_logging_interval > 0:
                    if tickcounter >= debug_logging_interval:
                        log.put_nowait("[debugs] " + str(vector_name) + " ticks: "+str(programticks)+", fullcharge:"+str(fullcharge)+", charging:"+str(charging)+", docked:"+str(docked)+", lowpower:"+str(lowpower)+ ", connected:"+str(robot_connected)+", error:"+str(robot_connection_error)+", idle:"+str(round(vector_sit_still_total_time,2))+", last event:"+str(round(last_event_received,2)))
                        log.put_nowait("[debugs] " + str(vector_name) + " UI:"+str(ui_thread_running)+", conn:"+str(robot_connection_thread_running)+", batt:"+str(robot_battery_thread_running)+", sensor:"+str(robot_sensor_thread_running)+", events:"+str(robot_event_thread_running)+", reanim:"+str(reanimator_thread_running)+", yeet:"+str(yeetbot_thread_running)+", CC: "+str(continuous_cycle)+", CCS: "+str(continuous_cycle_scheduling)+", GTG :"+str(robot_good_to_go))
                        log.put_nowait("[debugs] " + str(vector_name) + " char: "+str(robot_charging)+", dock:"+str(robot_docked)+", calm:"+str(robot_calmpower)+", clif:"+str(robot_cliffdetect)+", fall:"+str(robot_falling)+ ", pick:"+str(robot_pickup)+", held:"+str(robot_held)+", butt:"+str(robot_button)+", carr:"+str(robot_carrying))
                        log.put_nowait("[debugs] " + str(vector_name) + " control: "+str(robot_current_control_level)+", dock: "+str(robot_docking)+", move:"+str(robot_moving)+", anim:"+str(robot_animating)+", path:"+str(robot_pathing)+", driv:"+str(robot_driving)+ ", volt:"+str(round(robot_voltage,2))+", blvl:"+str(robot_batlevel))
                        tickcounter = 0
                        threadlist = ""
                        if not reduced_logging:
                            for t in threading.enumerate():
                                threadlist = threadlist + str(t.getName())+", "
                            log.put_nowait("[debugs] " + str(vector_name) + " threads: "+str(threadlist))
                    else:
                        tickcounter += refresh_rate
                    programticks += 1
                    
        # RECENCY: remembering stuff that just happened so we don't spam the log (initial writeup, this can be more efficient)
            if recency:
                if robot_carrying:
                    recent_carry = True
                    recent_carry_timer = 0
                if robot_is_being_touched:
                    recent_touch = True
                    recent_touch_timer = 0
                if robot_cliffdetect:
                    recent_cliff = True
                    recent_cliff_timer = 0
                if robot_held or robot_pickup:
                    recent_pickup = True
                    recent_pickup_timer = 0
                recent_known_face_seen_timer += refresh_rate
                recent_face_seen_timer += refresh_rate
                recent_cube_tapped_timer += refresh_rate
                recent_cube_rotated_timer += refresh_rate
                recent_wake_word_timer += refresh_rate
                recent_cube_available_timer += refresh_rate 
                recent_carry_timer += refresh_rate
                recent_touch_timer = recent_touch_timer + refresh_rate
                recent_cliff_timer += refresh_rate
                recent_pickup_timer += refresh_rate
                # recency expiry
                if  recent_cube_tapped_timer > 60:
                    recent_cube_tapped = False
                    recent_cube_tapped_timer = 0
                if  recent_cube_rotated_timer > 5:
                    recent_cube_rotated_timer = 0
                    recent_cube_rotated = False
                if  recent_wake_word_timer > 15:
                    recent_wake_word_timer = 0
                    recent_wake_word = False
                if  recent_cube_available_timer > 180:
                    recent_cube_available_timer = 0
                    recent_cube_available = False
                if  recent_face_seen_timer > 60:
                    recent_face_seen_timer = 0
                    recent_face_seen = False
                if  recent_known_face_seen_timer > 30:
                    recent_known_face_seen_timer = 0
                    recent_known_face_seen = False
                if recent_carry and recent_carry_timer > 10 and not robot_carrying:
                    recent_carry_timer = 0
                    recent_carry = False
                if recent_touch and recent_touch_timer > 3 and not robot_is_being_touched:
                    recent_touch_timer = 0
                    recent_touch = False
                if recent_cliff and recent_cliff_timer > 10 and not robot_cliffdetect:
                    recent_cliff_timer = 0
                    recent_cliff = False
                if recent_pickup and recent_pickup_timer > 7 and not (robot_pickup or robot_held):
                    recent_pickup_timer = 0
                    recent_pickup = False
# --- END OF LOGGING SECTION ---
        if startup:
            vector_sit_still_total_time = 0
            startup = False
        # sleep for refresh_rate and go back to the start of the main loop
        sleep(refresh_rate)
# --- END OF MAIN LOOP ---
# --- EXCEPTION SECTION ---
# --- In which we deal with keyboard interrupt and any error states in the main loop
    except KeyboardInterrupt as e:
        program_exit_requested = True
    except anki_vector.exceptions.VectorNotFoundException as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[connct] main_loop: " + str(vector_name) + " not found exception. Error: " + repr(e))
        robot_connected = False
        robot_connection_error = False
        if quit_on_error:
            quit_on_error_request = True
    except anki_vector.exceptions.VectorUnavailableException as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[connct] main_loop: " + str(vector_name) + " unavailable error. Error: " + repr(e))
        robot_connected = False
        robot_connection_error = True
        if quit_on_error:
            quit_on_error_request = True
    except anki_vector.exceptions.VectorConnectionException as e:
        if except_logging and logging_thread_running:
            log.put_nowait("[connct] main_loop: A general connection error occurred: " + repr(e))
        robot_connection_error = True
        robot_connected = False
        if quit_on_error:
            quit_on_error_request = True
    except anki_vector.exceptions.VectorAsyncException as e:
        if except_logging and not reduced_logging and logging_thread_running:
            log.put_nowait("[errors] main_loop: Invalid asynchronous action attempted: " +repr(e))
    except anki_vector.exceptions.VectorBehaviorControlException as e:
        if except_logging and not reduced_logging and logging_thread_running:
            log.put_nowait("[errors] main_loop: Invalid behavior control action attempted: " +repr(e))
    except anki_vector.exceptions.VectorCameraFeedException as e:
        if except_logging and not reduced_logging and logging_thread_running:
            log.put_nowait("[errors] main_loop: The camera feed is not open: " +repr(e))    
    except Exception as e:
        if except_logging and logging_thread_running:
            if logging_thread_running:
                log.put_nowait("[errors] main_loop exception: " +repr(e))
            else:
                print("[errors] main_loop exception: " +repr(e))
    except BaseException as e:
        if except_logging and logging_thread_running:
            if logging_thread_running:
                log.put_nowait("[errors] main_loop base exception: " +repr(e))
            else:
                print("[errors] main_loop base exception: " +repr(e))
# --- END OF EXCEPTION SECTION ---
# --- START OF SHUTDOWN SECTION ---
# In which we clean up any dangling threads and exit the program
if debug_logging and logging_thread_running:
    log.put_nowait("[system] broke out of main loop")
program_is_stopping = True
msg = "[system] Program exit requested, stopping threads, wait"
if headless:
    print(msg)
else:
    if logging_thread_running:
        log.put_nowait(msg)
program_exit_requested = True
if connect_to_cube and myrobot.world.connected_light_cube:
    try:
        myrobot.world.disconnect_cube()
    except:
        if not reduced_logging and logging_thread_running:
            log.put_nowait("[errors] issue disconnecting from " + str(vector_name) + "'s cube")
while reanimator_thread_running:
    sleep(refresh_rate)
while yeetbot_thread_running:
    sleep(refresh_rate)
if debug_logging and logging_thread_running:
    log.put_nowait("[system] reanimator and yeetbot threads stopped")
robot_battery_thread_stop = True
robot_sensor_thread_stop = True
robot_event_thread_stop = True
timeout = 0
while (robot_battery_thread_running or robot_sensor_thread_running or robot_event_thread_running) and timeout < 10:
    timeout = timeout + refresh_rate
    if timeout >= 10:
        if debug_logging and not reduced_logging and logging_thread_running:
            log.put_nowait("[system] waiting for robot monitor threads to close timed out")
        break
    sleep(refresh_rate)
if debug_logging and logging_thread_running:
    log.put_nowait("[system] Threads stopped, closing connection to " + str(vector_name))
robot_connection_thread_stop = True
timeout = 0
while robot_connection_thread_running and timeout < 10:
    sleep(refresh_rate)
    timeout = timeout + refresh_rate
    if timeout >= 10:
        if debug_logging and not reduced_logging and logging_thread_running:
            log.put_nowait("[system] waiting for robot connection thread to close timed out")
        break
msg = "[system] connections closed, stopping log and UI threads. Goodbye!"
if headless:
    print(msg)
else:
    if logging_thread_running:
        log.put_nowait(msg)
sleep(0.5)
logging_thread_stop = True
timeout = 0
while logging_thread_running and timeout < 5:
    sleep(refresh_rate)
    timeout = timeout + refresh_rate
    if timeout >= 5:
        break
if not headless:
    ui_thread_stop = True
timeout = 0
while ui_thread_running and timeout < 5:
    sleep(refresh_rate)
    timeout = timeout + refresh_rate
    if timeout >= 5:
        break
sys.exit()
# --- END OF SHUTDOWN SECTION ---