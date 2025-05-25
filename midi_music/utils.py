"""
Author: John Brittain
Date: May 25, 2025

Contains utility functions for MIDI generation.
"""

def print_midi_message(message):
    """Print a MIDI message in a readable format.

    Args:
        message: MIDI message to print.
    """
    print(message)


def print_midi_track(track):
    """Print a MIDI track in a readable format.

    Args:
        track: MIDI track to print.
    """
    for message in track:
        print_midi_message(message)
    print("End of track")
    print("===================================")


def print_midi_file(midi_file):
    """Print a MIDI file in a readable format.

    Args:
        midi_file: MIDI file object to print.
    """
    print("MIDI file:")
    print(f"File name: {midi_file.filename}")
    print(f"Number of tracks: {len(midi_file.tracks)}")
    print("===================================")
    for i, track in enumerate(midi_file.tracks):
        print(f"Track {i + 1}:")
        print_midi_track(track)
    print("===================================")
    print("End of MIDI file")
