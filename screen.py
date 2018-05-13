import cv2
import mss
import numpy as np


class Screen:

    def __init__(self):
        self.screen = mss.mss()
        self.screen_dimensions = {'top': 0, 'left': 0, 'width': 1000, 'height': 600}
        self.current_frame = None
        self.last_frame = None
        self.update_frames()

    def update_frames(self):
        self.last_frame = self.current_frame
        raw_frame = np.array(self.screen.grab(self.screen_dimensions))
        processed_frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2GRAY)
        self.current_frame = processed_frame

    def template_match(self, template, threshold=None, frame=None):
        if threshold is None:
            threshold = .35
        if frame is None:
            frame = self.current_frame
        res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        return not (len(loc[0]) == 0 and len(loc[1]) == 0)

    def show(self, frame=None):
        if frame is None:
            frame = self.current_frame
        cv2.imshow("Current frame", frame)
