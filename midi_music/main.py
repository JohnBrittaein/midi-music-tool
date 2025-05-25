from generate_midi import MidiMessageGenerator

from file_midi import MidiFileWriter, MidiFileReader

from builder_midi import MidiTrackBuilder

from utils import print_midi_message, print_midi_track, print_midi_file

OUTPUT_FILENAME = 'example2.mid'

def main():
    """Example usage of the midi-music-tool"""

    message_generator = MidiMessageGenerator()
    track_builder = MidiTrackBuilder()

    """Generate MIDI messages"""
    tracks = []
    for i in range(5):
        note_on = message_generator.generate_note_on(channel=0, note=60+i, velocity=64, duration=480)
        note_off = message_generator.generate_note_off(channel=0, note=60+i, velocity=64)
        midi_note = message_generator.generate_midi_note(channel=0, note=60+i, velocity=64, duration=480)
        cc = message_generator.generate_control_change(channel=0, CCNumber=i, CCValue=i*10)
        program = message_generator.generate_program_change(channel=0, Program=i)
        track = track_builder.add(note_on).add(note_off).add(midi_note).add(cc).add(program).build()
        tracks.append(track)    
        
    # Create a MidiFileWriter instance
    file_writer = MidiFileWriter(filename=OUTPUT_FILENAME)

    for track in tracks:
        file_writer.add_track(track)

    file_writer.save()

    print_midi_file(file_writer)

if __name__ == "__main__":
    main()