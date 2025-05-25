from mido import MidiFile, MidiTrack, Message

import os

"""
This python class contains functions to generate MIDI data and files
"""

def create_midi_file(filename, tracks_data):
    """
    Create a MIDI file from a list of midi tracks.

    :param filename: Output filename
    :param tracks_data: List of track messages (each element is a list of (msg_type, kwargs))
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MIDI_DIR = os.path.join(BASE_DIR, 'midi-files')
    os.makedirs(MIDI_DIR, exist_ok=True)

    MIDI_FILE_PATH = os.path.join(MIDI_DIR, filename)
    midi_file = MidiFile()

    for track_messages in tracks_data:
        track = MidiTrack()
        for msg_type, kwargs in track_messages:
            track.append(Message(msg_type, **kwargs))
        midi_file.tracks.append(track)

    midi_file.save(MIDI_FILE_PATH)
    print(f"MIDI file saved to {MIDI_FILE_PATH}")

"""
Functions to generate different types of MIDI messages
for more information on MIDI messages, refer to
https://www.mathworks.com/help/audio/ug/midi-device-interface.html


SUPPORTED MIDI MESSAGES:
- note_on
- note_off
- control_change
- program_change
- pitch_bend

UNSUPPORTED MIDI MESSAGES:
- Polyphonic key pressure(Aftertouch)
- Channel pressure(Aftertouch)
- All Sound Off
- Reset all controllers
- Local control
- All notes off
- Omni Mode Off
- Omni Mode On
- Mono Mode On(Poly Off)
- Poly Mode On(Poly On)
- System Exclusive
- MIDI Time Code Quarter Frame
- Song Position Pointer
- Song Select
- Tune Request
- End of Exclusive
- Timing Clock
- Start
- Continue
- Stop
- Active Sensing
- Reset
"""

def generate_note_on(channel=0, note=60, velocity=64, duration=480):
    """
    Generate a MIDI note on message

    :param channel: MIDI channel (default is 0)
    :param note: MIDI note number (default is 60, which is Middle C)
    :param velocity: Note velocity (default is 64)
    :param duration: Duration of the note in ticks (default is 480)
    :return: List of MIDI messages
    """
    return [
        ('note_on', {'note': note, 'velocity': velocity, 'time': duration, 'channel': channel})
    ]
def generate_note_off(channel=0, note=60, velocity=64):
    """
    Generate a MIDI note off message

    :param channel: MIDI channel (default is 0)
    :param note: MIDI note number (default is 60, which is Middle C)
    :param velocity: Note velocity (default is 64)
    :return: List of MIDI messages
    """
    return [
        ('note_off', {'note': note, 'velocity': velocity, 'time': 0, 'channel': channel})
    ]

def generate_midi_note(channel=0, note=60, velocity=64, duration=480):
    """
    Generate a MIDI note message with note on and note off

    :param channel: MIDI channel (default is 0)
    :param note: MIDI note number (default is 60, which is Middle C)
    :param velocity: Note velocity (default is 64)
    :param duration: Duration of the note in ticks (default is 480)
    :return: List of MIDI messages
    """
    return [
        ('note_on', {'note': note, 'velocity': velocity, 'time': 0, 'channel': channel}),
        ('note_off', {'note': note, 'velocity': 0, 'time': duration, 'channel': channel})
    ]

def generate_control_change(channel=0, CCNumber=0, CCValue=0):
    """
    Generate a MIDI control change message

    :param channel: MIDI channel (default is 0)
    :param CCNumber: Control Change number (0-127)
    :param CCValue: Control Change value (0-127)
    :return: List of MIDI messages
    """
    return [
        ('control_change', {'channel': channel, 'control': CCNumber, 'value': CCValue})
    ]   

def generate_program_change(channel=0, Program=0):
    """
    Generate a MIDI program change message

    :param channel: MIDI channel (default is 0)
    :param Program: Program number (0-127)
    :return: List of MIDI messages
    """
    return [
        ('program_change', {'channel': channel, 'program': Program})
    ]

def generate_pitch_bend(channel=0, pitch_bend_value=8192):
    """
    Generate a MIDI pitch bend message

    :param channel: MIDI channel (default is 0)
    :param pitch_bend_value: Pitch bend value (0-16383)
    :return: List of MIDI messages
    """
    return [
        ('pitchwheel', {'channel': channel, 'pitch': pitch_bend_value})
    ]
                            