from psychopy.experiment.components.movie import MovieComponent
from psychopy.experiment.components import getInitVals
from psychopy.localization import _translate
from pathlib import Path


class OpenCVMovieComponent(MovieComponent):
    iconFile = Path(__file__).parent / 'OpenCVMovieComponent.png'
    iconSVG = Path(__file__).parent / 'OpenCVMovieComponent.svg'
    tooltip = _translate('Play movies via the OpenCV movie backend')

    def writeInitCode(self, buff):
        # get init vals
        inits = getInitVals()
        # get depth in Routine
        inits['depth'] = -self.getPosInRoutine()
        # write
        code = (
            "%(name)s = visual.MovieStim2(\n"
            "    win=win, \n"
            "    name='%(name)s', \n"
            "    units=%(units)s, \n"
            "    noAudio=%(No audio)s, \n"
            "    filename=%(movie)s, \n"
            "    ori=%(ori)s, \n",
            "    pos=%(pos)s, \n"
            "    opacity=%(opacity)s,\n"
            "    loop=%(loop)s, \n"
            "    anchor=%(anchor)s, \n"
            "    size=%(size)s, \n"
            "    depth=%(depth)s, \n"
            ")\n"
        )
        buff.writeIndentedLines(code % inits)