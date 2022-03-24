#!/usr/bin/env python

from pynput import keyboard
from PyQt5.QtCore import QThread, pyqtSignal

import qt_debugger


class KeyGrabber(QThread):
    play_pause_pressed = pyqtSignal()


    def run(self):
        # The event listener will be running in this block
        qt_debugger.debug_this_thread()
        with keyboard.Events() as events:
            for event in events:
                if isinstance(event, keyboard.Events.Press) is False:
                    continue
                if event.key == keyboard.Key.media_play_pause:
                    self.play_pause_pressed.emit()
