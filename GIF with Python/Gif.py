from pathlib import Path
import imageio.v3 as iio

base = Path(__file__).resolve().parent

filenames = [base / "team-pic1.png", base / "team-pic2.png"]
images = [iio.imread(str(name)) for name in filenames]

iio.imwrite(base / "team.gif", images, duration=500, loop=0)