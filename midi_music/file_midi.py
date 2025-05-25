from mido import MidiFile, MidiTrack, Message
import os

"""
Author: John Brittain
Date: May 24, 2025

Contains classes and functions to write MIDI data and files
MidiFileWriter: Writes MIDI data into a file in specified location ~midi-music-tool/midi-files/example.mid
MidiFileReader: Reads MIDI data from a file in specified location ~midi-music-tool/midi-files/example.mid
"""

class MidiFileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.tracks = []

    def add_track(self, messages):
        """Add a track to the MIDI file.

        Args:
            messages (list): List of MIDI messages to add to the track.
        """
        self.tracks.append(messages)

    def save(self):
        """Save the MIDI file to the specified location.
        The file will be saved in the 'midi-files' directory within the current working directory.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        midi_dir = os.path.join(base_dir, 'midi-files')
        os.makedirs(midi_dir, exist_ok=True)

        full_path = os.path.join(midi_dir, self.filename)
        midi = MidiFile()

        for track_messages in self.tracks:
            track = MidiTrack()
            for msg_type, kwargs in track_messages:
                track.append(Message(msg_type, **kwargs))
            midi.tracks.append(track)

        midi.save(full_path)
        print(f"MIDI file saved to {full_path}")


class MidiFileReader:
    def __init__(self, filename):
        self.filename = filename
        self.midi = MidiFile(filename)

    """TODO: Add a function to read the MIDI file and return the messages"""