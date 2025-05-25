"""
Author: John Brittain
Date: May 24, 2025

Contains MidiTrackBuilder class to build a lsit of MIDI messages into a track
"""

class MidiTrackBuilder:
    def __init__(self):
        self.messages = []

    def add(self, midi_messages):
        """Add MIDI messages to the track.
        Args:
            midi_messages (list): List of MIDI messages to add.
        """
        self.messages.extend(midi_messages)
        return self

    def build(self):
        """Build the MIDI track.
        Returns:
            list: List of MIDI messages in the track.
        """
        return self.messages
