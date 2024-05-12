# import cv2
# import mediapipe as mp
# import math
# import numpy as np
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # solution APIs
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# # Volume Control Library Usage 
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# volRange = volume.GetVolumeRange()
# minVol , maxVol , volBar, volPer= volRange[0] , volRange[1], 400, 0

# # Webcam Setup
# wCam, hCam = 640, 480
# cam = cv2.VideoCapture(0)
# cam.set(3,wCam)
# cam.set(4,hCam)

# # Mediapipe Hand Landmark Model
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:

#   while cam.isOpened():
#     success, image = cam.read()

#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style()
#             )

#     # multi_hand_landmarks method for Finding postion of Hand landmarks      
#     lmList = []
#     if results.multi_hand_landmarks:
#       myHand = results.multi_hand_landmarks[0]
#       for id, lm in enumerate(myHand.landmark):
#         h, w, c = image.shape
#         cx, cy = int(lm.x * w), int(lm.y * h)
#         lmList.append([id, cx, cy])          

#     # Assigning variables for Thumb and Index finger position
#     if len(lmList) != 0:
#       x1, y1 = lmList[4][1], lmList[4][2]
#       x2, y2 = lmList[8][1], lmList[8][2]

#       # Marking Thumb and Index finger
#       cv2.circle(image, (x1,y1),15,(255,255,255))  
#       cv2.circle(image, (x2,y2),15,(255,255,255))   
#       cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
#       length = math.hypot(x2-x1,y2-y1)
#       if length < 50:
#         cv2.line(image,(x1,y1),(x2,y2),(0,0,255),3)

#       vol = np.interp(length, [50, 220], [minVol, maxVol])
#       volume.SetMasterVolumeLevel(vol, None)
#       volBar = np.interp(length, [50, 220], [400, 150])
#       volPer = np.interp(length, [50, 220], [0, 100])

#       # Volume Bar
#       cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
#       cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
#       cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
#                 1, (0, 0, 0), 3)
    
#     cv2.imshow('handDetector', image) 
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
# cam.release()


# import cv2
# import mediapipe as mp
# import math
# import numpy as np
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # solution APIs
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# # Volume Control Library Usage
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# volRange = volume.GetVolumeRange()
# minVol, maxVol, _, _ = volRange

# # Get the current volume level of the device
# currentVol = volume.GetMasterVolumeLevel()

# # Webcam Setup
# wCam, hCam = 640, 480
# cam = cv2.VideoCapture(0)
# cam.set(3, wCam)
# cam.set(4, hCam)

# # Mediapipe Hand Landmark Model
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:

#     while cam.isOpened():
#         success, image = cam.read()

#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = hands.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     image,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS,
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style()
#                 )

#         # multi_hand_landmarks method for Finding position of Hand landmarks
#         lmList = []
#         if results.multi_hand_landmarks:
#             myHand = results.multi_hand_landmarks[0]
#             for id, lm in enumerate(myHand.landmark):
#                 h, w, c = image.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmList.append([id, cx, cy])

#         # Assigning variables for Thumb and Index finger position
#         if len(lmList) != 0:
#             x1, y1 = lmList[4][1], lmList[4][2]
#             x2, y2 = lmList[8][1], lmList[8][2]

#             # Marking Thumb and Index finger
#             cv2.circle(image, (x1, y1), 15, (255, 255, 255))
#             cv2.circle(image, (x2, y2), 15, (255, 255, 255))
#             cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
#             length = math.hypot(x2 - x1, y2 - y1)
#             if length < 50:
#                 cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

#             # Interpolate volume based on hand length
#             vol = np.interp(length, [50, 220], [minVol, maxVol])

#             # Adjust application volume to match device volume
#             volume.SetMasterVolumeLevel(vol + currentVol, None)

#             # Calculate volume percentage and draw volume bar
#             volBar = np.interp(length, [50, 220], [400, 150])
#             volPer = np.interp(length, [50, 220], [0, 100])

#             # Volume Bar
#             cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
#             cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
#             cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
#                         1, (0, 0, 0), 3)

#         cv2.imshow('handDetector', image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cam.release()



# import cv2
# import mediapipe as mp
# import math
# import numpy as np
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# # Volume Control Library Usage
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# volRange = volume.GetVolumeRange()

# # Check if volRange contains enough values
# if len(volRange) >= 4:
#     minVol, maxVol, _, _ = volRange
# else:
#     # If volRange doesn't contain enough values, set default minVol and maxVol
#     minVol, maxVol = -63.5, 0.0

# # Get the current volume level of the device
# currentVol = volume.GetMasterVolumeLevel()

# # solution APIs
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# # Webcam Setup
# wCam, hCam = 640, 480
# cam = cv2.VideoCapture(0)
# cam.set(3, wCam)
# cam.set(4, hCam)

# # Mediapipe Hand Landmark Model
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:

#     while cam.isOpened():
#         success, image = cam.read()

#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = hands.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     image,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS,
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style()
#                 )

#         # multi_hand_landmarks method for Finding position of Hand landmarks
#         lmList = []
#         if results.multi_hand_landmarks:
#             myHand = results.multi_hand_landmarks[0]
#             for id, lm in enumerate(myHand.landmark):
#                 h, w, c = image.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmList.append([id, cx, cy])

#         # Assigning variables for Thumb and Index finger position
#         if len(lmList) != 0:
#             x1, y1 = lmList[4][1], lmList[4][2]
#             x2, y2 = lmList[8][1], lmList[8][2]

#             # Marking Thumb and Index finger
#             cv2.circle(image, (x1, y1), 15, (255, 255, 255))
#             cv2.circle(image, (x2, y2), 15, (255, 255, 255))
#             cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
#             length = math.hypot(x2 - x1, y2 - y1)
#             if length < 50:
#                 cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

#             # Interpolate volume based on hand length
#             vol = np.interp(length, [50, 220], [minVol, maxVol])

#             # Adjust application volume to match device volume
#             new_vol = vol + currentVol
#             if new_vol < minVol:
#                 new_vol = minVol
#             elif new_vol > maxVol:
#                 new_vol = maxVol
#             volume.SetMasterVolumeLevel(new_vol, None)
#             # Calculate volume percentage and draw volume bar
#             volBar = np.interp(length, [50, 220], [400, 150])
#             volPer = np.interp(length, [50, 220], [0, 100])

#             # Volume Bar
#             cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
#             cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
#             cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
#                         1, (0, 0, 0), 3)

#         cv2.imshow('handDetector', image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cam.release()

import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# solution APIs
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Volume Control Library Usage 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol , maxVol , volBar, volPer= volRange[0] , volRange[1], 400, 0

# Webcam Setup
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3,wCam)
cam.set(4,hCam)

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

  # Initialize variables for smoothing
  smoothing_factor = 0.5
  prev_length = 0

  while cam.isOpened():
    success, image = cam.read()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
            )

    # multi_hand_landmarks method for Finding postion of Hand landmarks      
    lmList = []
    if results.multi_hand_landmarks:
      myHand = results.multi_hand_landmarks[0]
      for id, lm in enumerate(myHand.landmark):
        h, w, c = image.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        lmList.append([id, cx, cy])          

    # Assigning variables for Thumb and Index finger position
    if len(lmList) != 0:
      x1, y1 = lmList[4][1], lmList[4][2]
      x2, y2 = lmList[8][1], lmList[8][2]

      # Marking Thumb and Index finger
      cv2.circle(image, (x1,y1),15,(255,255,255))  
      cv2.circle(image, (x2,y2),15,(255,255,255))   
      cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
      length = math.hypot(x2-x1,y2-y1)

      # Smoothing the hand movement
      length = smoothing_factor * length + (1 - smoothing_factor) * prev_length
      prev_length = length

      if length < 50:
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),3)

      vol = np.interp(length, [50, 220], [minVol, maxVol])
      volume.SetMasterVolumeLevel(vol, None)
      volBar = np.interp(length, [50, 220], [400, 150])
      volPer = np.interp(length, [50, 220], [0, 100])

      # Volume Bar
      cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
      cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
      cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 0), 3)
    
    cv2.imshow('handDetector', image) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Release webcam resource
cam.release()
cv2.destroyAllWindows()
