import os
import pytest
from backend.tools import change_mp4_speed

@pytest.mark.parametrize("input_mp4_path", ["mp4/plan_plot.mp4"])
@pytest.mark.parametrize("output_mp4_path", ["mp4/plan_plot_speed_3.mp4"])
@pytest.mark.parametrize("speed", [3])
def test_change_mp4_speed(input_mp4_path, output_mp4_path, speed):
    change_mp4_speed(input_mp4_path, output_mp4_path, speed)
    assert os.path.exists(output_mp4_path)
    