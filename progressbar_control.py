from progressbar import ProgressBar, Bar, Percentage
from sys import stdout

def setup_progressbar() -> None:
    global bar
    bar = ProgressBar(maxval=100, widgets=[Bar('=', '[', ']'), ' ', Percentage()])

def update_progressbar(iterator: int, denominator: int) -> None:
##    progress = int(iterator/denominator * 100)
    progress = iterator * 100 // denominator
    bar.update(progress)
    stdout.flush()
    if progress == 100:
        print('\r')
