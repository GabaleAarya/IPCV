import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter

# (a) Find the sampling rate used by the recorder.
file_path = 'path/to/your/audio/file.wav'  # Replace with the actual file path
sampling_rate, audio_data = wavfile.read(file_path)

# (b) Find the length of the recorded signal and segment it from length 0 to 64.
signal_length = len(audio_data)
segment_length = 64

# Ensure that the signal length is greater than the desired segment length.
if signal_length < segment_length:
    print("Signal length is less than the desired segment length.")
    # Handle the case appropriately.

# Segment the signal from 0 to 64.
segment = audio_data[:segment_length]

# (c) Generate noisy signal by adding zero-mean uniformly distributed random noise in [-0.5, 0.5].
noise = np.random.uniform(-0.5, 0.5, segment_length)
noisy_signal = segment + noise

# (d) Determine and plot the filtered output signal by FIR Filter.
# Choose appropriate filter parameters.
filter_order = 30
cutoff_frequency = 1000  # Adjust according to your requirements.

# Design the FIR filter using firwin function from scipy.
fir_filter = firwin(filter_order, cutoff_frequency, fs=sampling_rate)

# Apply the FIR filter to the noisy signal.
filtered_output = lfilter(fir_filter, 1.0, noisy_signal)

# Plot the results for comparison.
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(segment)
plt.title('Original Segment')

plt.subplot(3, 1, 2)
plt.plot(noisy_signal)
plt.title('Noisy Signal')

plt.subplot(3, 1, 3)
plt.plot(filtered_output)
plt.title('Filtered Output Signal')

plt.tight_layout()
plt.show()
