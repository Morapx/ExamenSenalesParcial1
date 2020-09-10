import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#6
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)
#4
frecuencia770_3 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
#6
frecuencia770_2 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1477_2 = SinSignal(freq=1477, amp=1, offset=0)
#2
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

#wave 6
wave_770 = frecuencia770.make_wave(duration=0.5, start=0, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=0, framerate=44100)
#wave4
wave_770_3 = frecuencia770_3.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)
#wave6
wave_770_2 = frecuencia770_2.make_wave(duration=0.5, start=1, framerate=44100)
wave_1477_2 = frecuencia1477_2.make_wave(duration=0.5, start=1, framerate=44100)
#wave2
wave_697 = frecuencia697.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1.5, framerate=44100)

#6 4 6 2
wave_sonido = (wave_770 + wave_1477) + (wave_770_3 + wave_1209) + (wave_770_2 + wave_1477_2) + (wave_697 + wave_1336)

wave_sonido.write("output.wav")

#6462 es el numero
