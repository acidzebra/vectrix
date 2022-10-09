# VecTrix
a 24/7 Anki/DDL Vector robot monitor which can optionally keep Vector active and improve his idle behavior, has extensive logging options, battery profiling, and more!
I have owned three Vector units (and a Cozmo) for years, and I love my little robot buddies. This program was previously known as VectorDiag but it surpassed that scope.

This program was created to accomplish three things: 
1. a visually attractive way to read out all sensors from the console using minimal resources and dependencies
2. make Vector more interesting (Vector tends to sleep on charger a lot and sit still while off charger a lot)
3. provide a better understanding of why Vector is acting a certain way and record performance over time

# Requirements
- Windows, Mac, or Linux system
- Python 3.x, configured [Vector Python SDK][1] and [Vector robot][2] (i.e. you can already connect to the robot with Python)
- the [Dashing library][3] for Python: pip3 install dashing

# Main features
- built to run 24/7 in console UI or headless mode while using few resources
- monitors and logs Vector's sensor data and other telemetry to console or file
- optionally forces Vector off the charger if the battery is fully charged (after a configurable time)
- optionally improves Vector's idle behavior (sitting still for minutes) by: mixing animations, going for a drive, rolling cubes and more
- battery profiling: log voltages to csv file, records charge/discharge cycle times
- automatically reconnects in case of connection loss
- highly configurable

# Screenshot (somewhat out of date)
![screenshot (may be out of date)](https://i.imgur.com/3SiETdd.jpg)

# Video demo (older version)
[![Demo video (older version)](https://img.youtube.com/vi/o9g9NPUKeCg/0.jpg)](https://www.youtube.com/watch?v=o9g9NPUKeCg)



[1]: https://developer.anki.com/vector/docs/initial.html "Vector SDK setup"
[2]: https://www.digitaldreamlabs.com/products/vector-robot "Vector robot"
[3]: https://github.com/FedericoCeratto/dashing "Dashing library"
