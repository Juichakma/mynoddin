# mynoddin
Volume Control using Hand Gesture

For hand gesture recognition and volume control, this Python software makes use of the MediaPipe and PyCaw libraries, respectively. It enables webcam-based master volume management of the system by recognising hand movements.

Dependencies:

1.OpenCV (cv2)

2.MediaPipe (mediapipe)

3.PyCaw (pycaw)

4.NumPy (numpy)

5.comtypes (comtypes)

6.Install these dependencies using pip:

7.pip install opencv-python mediapipe pycaw numpy comtypes

Application

Take a copy of this repository locally.

Verify that your system has a webcam attached to it.

Execute the hand_gesture_volume_control.py script.

To adjust the volume, make the following hand gestures:

To adjust the volume, spread your thumb and index finger apart.

To turn down the volume, bring your thumb and index finger closer together.

To end the session and release the webcam resource, hit Q.

How it Works

The script captures frames from the webcam and processes them using MediaPipe to detect hand landmarks. It identifies the positions of the thumb and index finger landmarks to calculate the distance between them. Based on the distance between these landmarks, it adjusts the system's master volume using PyCaw. A graphical volume bar is displayed on the screen to visualize the current volume level.

Customization

You can adjust the smoothing factor (smoothing_factor) to control the responsiveness of volume changes based on hand movements. Modify the min_detection_confidence and min_tracking_confidence parameters in the Hands class initialization for hand detection confidence level adjustments. Customize the volume range (minVol, maxVol) and the length range ([50, 220]) in the np.interp() function to suit your preference.

Acknowledgments

This script utilizes the MediaPipe and PyCaw libraries for hand gesture recognition and volume control, respectively. MediaPipe is an open-source library developed by Google Research for building cross-platform multimodal applied ML pipelines. PyCaw is a Python library for controlling the Windows Audio Session API (WASAPI), developed by AndreMiras.
