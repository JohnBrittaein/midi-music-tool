from generate_midi import MidiMessageGenerator

from file_midi import MidiFileWriter, MidiFileReader

from builder_midi import MidiTrackBuilder

def main():
    """Example usage of the midi-music-tool"""

    MessageGenerator = MidiMessageGenerator()
    TrackBuilder = MidiTrackBuilder()

    """Generate MIDI messages"""
    for i in range(5):
        note_on = MessageGenerator.generate_note_on(channel=0, note=60+i, velocity=64, duration=480)
        note_off = MessageGenerator.generate_note_off(channel=0, note=60+i, velocity=64)
        midi_note = MessageGenerator.generate_midi_note(channel=0, note=60+i, velocity=64, duration=480)
        cc = MessageGenerator.generate_control_change(channel=0, CCNumber=i, CCValue=i*10)
        program = MessageGenerator.generate_program_change(channel=0, Program=i)
        track = TrackBuilder.add(note_on).add(note_off).add(midi_note).add(cc).add(program).build()
        
    print("MIDI messages generated")
    print(track)

    # Create a MidiFileWriter instance
    FileWriter = MidiFileWriter(filename='example2.mid')
    # Add the track to the MidiFileWriter
    FileWriter.add_track(track)
    # Save the MIDI file
    FileWriter.save()

if __name__ == "__main__":
    main()