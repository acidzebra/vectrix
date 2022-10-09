Changelog

note: earlier versions of Vectix (named VectorDiag) are available here: gist.github.com/acidzebra/74d7b288b267d7fcea8c33358d4c2e78

0.9.5 
- (minor) new switch rainbow_eyes - will turn eyes blue when VecTrix is active, yellow in case of error (color will revert to normal when Vectrix is not active)
- (minor) new routines for driving to random pose and looking around
- (minor) reanimator cleanup

0.9.4 
- (minor) moved logging function to its own thread and implemented logging queue
- (minor) new config option to log battery voltage to separate CSV file for battery performance profiling
- (minor) cube powersaver will disconnect from cube whenever it connects (about every 2 mins when Vector is in freeplay) (this doesn't really work I think)
- (minor) cleanup, fixes, and cosmetics

0.9.3 
- (minor) UI buttons now indicate Vector connection status when not connected, orange=connecting, red=error
- (minor) moar switches and config options
- (minor) reanimator: control/release requests now in separate function (minor) fixes and cleanup

0.9.2
- (minor) refactored reanimator, split off animate/drive/cube code into functions
- (minor) improved calculated value/UI code
- (minor) additional thread safety measures
- (minor) cleanup, cosmetics, fixes
- (minor) cube events now working correctly (requires powered cube)

0.9.1 
- (minor) added scheduling function to continuous cycle
- (minor) touch detection fix
- (minor) added roll cube action to reanimator
- (minor) (dis)connect resilience and speed improvements
- (minor) moved all calculations and variable declarations out of UI thread (minor) cleanup, cosmetics, fixes

0.9.0
- (major) REANIMATOR will mix random animations when Vector has been idle off-charger (major) added wheel speed graphs to UI (major) implemented full threading for VecTrix, significant performance improvement
- (major) added headless mode, disables UI but runs all other functions
- (major) VecTrix now uses passive event monitoring to get telemetry reducing active calls to robot
- (major) startup resilience and graceful exit improvements (minor) UI color schemes
- (minor) cleanup, fixes, and cosmetic improvements throughout
- (minor) re-licensed to MIT

0.8.0
- (major) reduced number of calls to robot for data gathering by ~50%
- (major) reorganized code into more well-defined sections (prep for asyncio/future implementation)
- (minor) small fixes and cosmetics throughout

0.7.6
- (minor) I am DONE with drive_off_charger and DONE with yeetbot() ,I will just tell the robot to roll forward using set_wheel_motors. I give up. drive_off_charger is unreliable, sometimes it won't execute no matter the priority level, sometimes it will hang forever, who knows.

0.7.5
- (minor) improvements to accel/gyro and logging of same
- (minor) more work on yeetbot()... drive_off_charger seems to be reliable only 70% of the time :(

0.7.4
- (minor) clean up of accel/gyro/head/lift code
- (minor) cleanup and cosmetic fixes
- (minor) did I say I was done with yeetbot()? I lied. (minor) new dock miss detection

0.7.3
- (minor) okay, think I'm done tinkering with yeetrobot(), not perfect but it'll do... for now

0.7.2
- (minor) continued tinkering with yeetrobot()
- (minor) fixes and safety rails

0.7.1
- (minor) fiddling with yeetrobot() to make continuous_cycle more robust (still crappy)
- (minor) cosmetic fixes
- (minor) battery display improvements

0.7.0
- (major) continuous accelerometer recalibration (when robot is still)
- (minor) consistency & cosmetic fixes
- (minor) bugfixes on counters and battery display

0.6.2
- (minor) file logging is now on by default it's quite useful in long runs
- (minor) switch naming consistency
- (minor) added motion_logging and bundled all motion-related stuff there
- (minor) small bugfixes

0.6.1
- (minor) moar switches and config options
- (minor) some cleanup & cosmetic stuff

0.6.0
- (major) rewrote continuous_cycle to use threads - this still fails sometimes but at least doesn't hang the whole program (but leaves some fun threads hanging)
- (major) exciting new switches! (minor) added categories to log entries

0.5.4
- (minor) added calmpower/sleep to logging
- (minor) disabled new dock miss detection due to false positives

0.5.3
- (minor) restructured program sections to be more cohesive/consistent, added comments

0.5.2
- (minor) additional charger dock attempt miss detection
- (minor) re-grouped and expanded switches
- (minor) raw accelerometer/gyro logging
- (minor) configurable offset for accelerometer

0.5.1
- (minor) cosmetic cleanup
- (minor) some additional exception handling

0.5.0
- (major) rewrote logging as a function because things were getting out of hand
- (major) added failed docking attempt detection
- (minor) more fiddling with gyro and accelerometer graphs

0.4.2
- (minor) log improvements

0.4.1
- (minor) extra info on program exit
- (minor) pedantic case changes while going through code
- (minor) voltage graph minor improvements, still crappy
- (minor) small cosmetic stuff and touchups

0.4.0
- (major) UI design changes, reorganized bar layout. path/drive/move/anim moved to same bar and changed to a graph instead of button, swapped some buttons

0.3.3
- (minor) still tinkering with accell graphs
- (minor) added detection for starting Vectrix off dock
- (minor) moar code comments
- (minor) reduced log time precision, don't need microsecond precision

0.3.2
- (minor) small fixes and cosmetics throughout
- (minor) improved accel/gyro/head/lift graphs a little. accelx seems a bit off with the same calculations used for accely and accelz, I wonder if that is just my Vector? I adjusted it so I hope it's all Vectors lol

0.3.1
- (minor) logging fixes

0.3.0
- (major) crappy charging meter implemented
- (major) new switches implemented
- (major) attempting to reduce logspam
- (minor) more detailed object logging
- (minor) work on faceID/names

0.2.0
- (major) added charge/discharge cycle times to logging
- (major) some new optional switches

0.1.0
- (major) initial release, hurray!