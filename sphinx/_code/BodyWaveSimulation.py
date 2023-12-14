from manim import *

class PWavePropagation(Scene):
    CONFIG = {
        "background_color": BLACK,
    }
    
    def construct(self):
        self.p_wave()

    def p_wave(self):
        # Create the axes
        axes = Axes(x_range=[-1, 10], y_range=[-1, 1])
        axes.axis_color = rgb_to_color([141/255, 111/255, 34/255])
        self.add(axes)

        # Create the initial P wave (sine wave representing the P wave equation)
        p_wave = axes.plot(lambda x: np.sin(2 * PI * x), color=rgb_to_color([138/255, 36/255, 59/255]))  # Adjust the frequency and color as needed

        # Animate the propagation of the P wave
        self.play(
            ApplyWave(p_wave, direction=RIGHT, amplitude=0.3, time_width=0.5, run_time=4),
            rate_func=linear,
        )

        self.wait()

class SWavePropagation(Scene):
    CONFIG = {
        "background_color": BLACK,
    }
    
    def construct(self):
        self.s_wave()

    def s_wave(self):
        # Create the axes
        axes = Axes(x_range=[-1, 10], y_range=[-1, 1], color=rgb_to_color([141/255, 111/255, 34/255]))
        self.add(axes)

        # Create the initial S wave (sine wave representing the S wave equation)
        s_wave = axes.plot(lambda x: np.sin(2 * PI * x), color=rgb_to_color([138/255, 36/255, 59/255]))  # Adjust the frequency and color as needed

        # Animate the propagation of the S wave
        self.play(
            ApplyWave(s_wave, direction=UP, amplitude=0.3, time_width=0.5, run_time=4),
            rate_func=linear,
        )

        self.wait()