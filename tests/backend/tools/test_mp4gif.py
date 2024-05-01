import os
import pytest
from backend.tools import convert_mp4_to_gif

@pytest.mark.parametrize("input_mp4_path", ["mp4/plan_plot.mp4"])
@pytest.mark.parametrize("gif_path", ["converted/plan_plot.gif"])
@pytest.mark.parametrize("speed", [3])
def test_convert_mp4_to_gif(input_mp4_path, gif_path, speed):
    convert_mp4_to_gif(input_mp4_path, gif_path, speed)
    assert os.path.exists(gif_path)