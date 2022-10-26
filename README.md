# VecTrix
a 24/7 Anki/DDL Vector robot monitor which can optionally keep Vector active and improve his idle behavior, has extensive logging options, battery profiling, and more!
I have owned three Vector units (and a Cozmo) for years, and I love my little robot buddies. Since they are aging and were showing some issues, I wanted some insight into their 'brains'. While at it, I thought I could also improve their idle behaviors. This program was previously known as VectorDiag but it has since surpassed that scope.

This program was created to accomplish three things: 
1. a visually attractive way to read out all sensors from the console using minimal resources and dependencies
2. make Vector more interesting (Vector tends to sleep on charger a lot and sit still while off charger a lot)
3. provide a better understanding of why Vector is acting a certain way and record performance over time

# Requirements
- Windows, Mac, or Linux system
- Python 3.x, configured [Vector Python SDK][1] and [Vector robot][2] (i.e. you can already connect to the robot with Python)
- the [Dashing library][3] for Python: pip install dashing

# Optional requirements
- to enable keyboard remote control functionality you need sshkeyboard for Python: pip install sshkeyboard
- to enable MQTT logging: you need a configured MQTT broker, some understanding of JSON, and PAHO: pip install paho-mqtt

# Getting started
after satisfying the requirements above and downloading the file: in vectrix.py, replace robot_serial found near the very top with your Vector's serial number. Optionally change any of the other settings to your liking. Run vectrix.py with Python. Have fun. 

# Main features
- built to run 24/7 in console UI or headless mode while using few resources
- monitors and logs Vector's sensor data and other telemetry to console or file or webhooks (Discord etc)
- logging to screen, file, or webhook
- ability to remote control Vector and initiate specific actions (pop wheelie, roll cube, etc)
- battery profiling: log voltages to csv file, records charge/discharge cycle times
- optionally forces Vector off the charger if the battery is fully charged (after a configurable time, and on a schedule if desired)
- optionally improves Vector's tendency to sit still for minutes through Reanimator, which will mix animations, go for a drive, roll cubes and more
- automatically reconnects in case of connection loss
- highly configurable (yet sane defaults, only required setting is the robot serial number)

# Safety notice
While I take care not to program features that will send Vector careening over an edge, there are many unexpected events that can happen to Vector even without this software. I have my Vectors contained in a fairly large play space with raised walls. If you are using the Reanimator feature (on by default), don't leave your Vector unsupervised or in a place where a fall might cause damage. If you use manual control it's entirely possible to send Vector over an edge, so be careful.

# Screenshot (somewhat out of date)
![screenshot (may be out of date)](https://i.imgur.com/3SiETdd.jpg)

# Video demo (older version)
[![Demo video (older version)](https://img.youtube.com/vi/o9g9NPUKeCg/0.jpg)](https://www.youtube.com/watch?v=o9g9NPUKeCg)



[1]: https://developer.anki.com/vector/docs/initial.html "Vector SDK setup"
[2]: https://www.digitaldreamlabs.com/products/vector-robot "Vector robot"
[3]: https://github.com/FedericoCeratto/dashing "Dashing library"
