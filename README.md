This repository contains experimental data used for justification of 2.5 encoded frame size multiplier in WebRTC "huge frame" concept.

files:
* data.txt - raw data produced by patched WebRTC standalone video_loopback tool. It contains several lines of data. If the slide change event occured, a line "-1 -1 -1.00" is generated. Then frame is encoded, a line containing frame encoded size, typical frame size (encoder configured bitrate per second, divided by fps), and ratio of frame_size/typical_frame_size.
* process.py - simple script to process raw data. It reads data.txt, outputs minimum encoded frame size for slide change frame, and maximum ecoded frame size for regular frame. It also bruteforces possible multipliers starting from 2.00 to 4.00 with a step of 0.05. Then it outputs false positive and false negative ratio for each checked multiplier.
* processed.txt - output of the process.py. The first line contains minimum encoded size of slide change frame and maximum encoded size of a regular frame. Each next line contains 3 numbers - multiplier in percents, false positive and false negative ratios for slide change detection using corresponded multiplier.

Since it's prefereble to always detect a slide change event, we would want to minimize the false negative ratio first. You can see in processed.txt that miltipliers below 2.55 are suitable for that. Then to have some room for different video data we suggest to take even smaller multiplier of 2.50. making it even smaller will increase a false possitive further, so 2.5 is the most suitable multiplier to use.
