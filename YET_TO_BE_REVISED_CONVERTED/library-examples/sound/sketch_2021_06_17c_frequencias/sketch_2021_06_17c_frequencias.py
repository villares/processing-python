"""
Processing Sound Library, Example 1

Five sine waves are layered to construct a cluster of frequencies.
This method is called additive synthesis. Use the mouse position
inside the display window to detune the cluster.
"""

add_library('sound')    # import processing.sound.*

sine_waves = []  # Array of sines
sine_freq = []  # Array of frequencies
num_sines = 5  # Number of oscillators to use


def setup():
    size(640, 360)
    background(255)

    for i in range(num_sines):
        # Calculate the amplitude for each oscillator
        sine_volume = (1.0 / num_sines) / (i + 1)
        # Create the oscillators
        sine_waves.append(SinOsc(this))
        # Start Oscillators
        sine_waves[i].play()
        # Set the amplitudes for all oscillators
        sine_waves[i].amp(sine_volume)

    sine_freq[:] = [0] * num_sines


def draw():
    background(200)
    line(0, mouse_y, width, mouse_y)
    # Map mouseY from 0 to 1
    yoffset = map(mouse_y, 0, height, 0, 1)
    # Map mouseY logarithmically to 150 - 1150 to create a base frequency range
    frequency = pow(1000, yoffset) + 150
    # Use mouseX mapped from -0.5 to 0.5 as a detune argument
    detune = map(mouse_x, 0, width, -0.5, 0.5)

    for i in range(num_sines):
        sine_freq[i] = frequency * (i + 1 * detune)
        # Set the frequencies for all oscillators
        sine_waves[i].freq(sine_freq[i])
