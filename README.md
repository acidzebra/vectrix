# vectrix
Vectrix is a 24/7 Anki/DDL Vector console-based robot monitor which can optionally keep Vector active and improve his idle behavior, has extensive logging options, battery profiling, and more!

# Requirements:
- Windows, Mac, or Linux system
- Python 3.x, configured Vector Python SDK and Vector robot (i.e. you can already connect to the robot with Python)
- the Dashing library for Python: pip3 install dashing

# Main features
- built to run 24/7 in console UI or headless mode while using few resources
- monitors and logs Vector's sensor data and other telemetry to console or file
- optionally forces Vector off the charger if the battery is fully charged (after a configurable time)
- optionally improves Vector's idle behavior (sitting still for minutes) by: mixing animations, going for a drive, rolling cubes and more
- battery profiling: log voltages to csv file, records charge/discharge cycle times
- many more options to configure