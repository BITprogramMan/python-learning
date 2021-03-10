from game import main
from turtle_recorder import Recorder
import os
with Recorder(main, fps=30) as peg:
    peg.to_video('./media/demo.mp4')
    os.system("ffmpeg -i ./media/demo.mp4 ./media/demo.gif")