from .ToneGenerator import ToneGenerator

BUZZER_FREQ_DIV = [8, 10, 12, 14, 16, 20, 24, 28]
ENVELOP_STEP_DIV = [16, 20, 24, 28, 16, 20, 24, 28]

SOUND_CLOCK_DIV = 128
ONE_SHOT_PULSE_WIDTH_DIV = [8 * SOUND_CLOCK_DIV, 16 * SOUND_CLOCK_DIV]
ENVELOPE_CYCLE_DIV = [16 * SOUND_CLOCK_DIV, 32 * SOUND_CLOCK_DIV]

SQUARENESS_FACTOR = 5

class E0C6200sound():
    def __init__(self, clock):

        self._system_clock = clock
        self._one_shot_counter = 0
        self._buzzer_freq = clock / BUZZER_FREQ_DIV[0]
        self._envelope_step = 7
        self._envelope_cycle = ENVELOPE_CYCLE_DIV[0]
        self._envelope_counter = 0
        self._envelope_on = False
        self._sound_on = False
        self._cycle_counter = 0

        self._tone_generator = ToneGenerator()

    def clock(self):
        self._cycle_counter += 1
        if (self._one_shot_counter > 0):
            self._one_shot_counter -= 1
            if (self._one_shot_counter <= 0):
                self._tone_generator.stop(self._cycle_counter / self._system_clock)
        if (self._envelope_counter > 0):
            self._envelope_counter -= 1
            if (self._envelope_counter <= 0):
                if (self._envelope_step > 0):
                    self._tone_generator.play(self._buzzer_freq, False, self._envelope_step / 7 * SQUARENESS_FACTOR, self._cycle_counter / self._system_clock)
                    self._envelope_step -= 1
                self._envelope_counter = self._envelope_cycle

    def set_freq(self, value):
        self._buzzer_freq = self._system_clock / BUZZER_FREQ_DIV[value]
        if (self._sound_on):
            self._tone_generator.play(self._buzzer_freq, False, self._envelope_step / 7 * SQUARENESS_FACTOR, self._cycle_counter / self._system_clock)

    def set_envelope_on(self):
        self._envelope_on = True
        self._envelope_step = 7

    def set_envelope_off(self):
        self._envelope_on = False
        self._envelope_step = 7
        self._envelope_counter = 0
        self._tone_generator.stop(self._cycle_counter / self._system_clock)

    def set_envelope_cycle(self, cycle):
        self._envelope_cycle = ENVELOPE_CYCLE_DIV[cycle]

    def reset_envelope(self):
        self._envelope_step = 7

    def one_shot(self, duration):
        if (self._one_shot_counter == 0):
            self._one_shot_counter = ONE_SHOT_PULSE_WIDTH_DIV[duration]
            if (not self._sound_on):
                self._tone_generator.play(self._buzzer_freq, False, self._envelope_step / 7, self._cycle_counter / self._system_clock)

    def set_buzzer_on(self):
        self._sound_on = True
        self._one_shot_counter = 0
        self._tone_generator.play(self._buzzer_freq, False, self._envelope_step / 7, self._cycle_counter / self._system_clock)
        if (self._envelope_on):
            self._envelope_counter = self._envelope_cycle

    def set_buzzer_off(self):
        self._sound_on = False
        self._envelope_counter = 0
        self._one_shot_counter = 0
        self._tone_generator.stop(self._cycle_counter / self._system_clock)

    def is_one_shot_ringing(self):
        return self._one_shot_counter > 0