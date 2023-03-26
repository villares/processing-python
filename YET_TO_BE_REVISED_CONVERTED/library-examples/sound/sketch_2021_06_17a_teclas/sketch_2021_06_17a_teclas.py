add_library('sound')

# Times and levels for the ASR envelope
attack_time = 0.001
sustain_time = 0.1
sustain_level = 0.3
release_time = 0.3

# This is an octave in MIDI notes.
midi_sequence = {'0': 60, '1': 61, '2': 62, '3': 63, '4': 64, '5': 65, '6': 66,
                 '7': 67, '8': 68, '9': 69, 'x': 70, 'c': 71, 'v': 72
                 }
nota = None


def setup():
    global tri_osc, env
    size(640, 360)
    background(255)
    # Create triangle wave and start it
    tri_osc = TriOsc(this)
    # Create the envelope
    env = Env(this)


def draw():
    global nota
    if nota is not None:
        # midiToFreq transforms the MIDI value into a frequency in Hz which we use to
        # control the triangle oscillator with an amplitute of 0.5
        tri_osc.play(midi_to_freq(midi_sequence[nota]), 0.5)
        # The envelope gets triggered with the oscillator as input and the times and
        # levels we defined earlier
        env.play(
            tri_osc,
            attack_time,
            sustain_time,
            sustain_level,
            release_time)
        nota = None


def key_pressed():
    global nota
    if str(key) in "0123456789xcv":
        nota = key

# This helper functiopm calculates the respective frequency of a MIDI note


def midi_to_freq(midi_notation):
    return (2 ** ((midi_notation-69)/12.0)) * 440
