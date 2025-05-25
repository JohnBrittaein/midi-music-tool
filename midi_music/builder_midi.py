"""
Author: John Brittain
Date: May 24, 2025

Contains MidiTrackBuilder class to build a lsit of MIDI messages into a track
"""

class MidiTrackBuilder:
    def __init__(self):
        self.messages = []

    def add(self, midi_messages):
        self.messages.extend(midi_messages)
        return self

    def build(self):
        return self.messages
