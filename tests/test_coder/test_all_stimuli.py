import sys, os, copy
from pathlib import Path

from psychopy import visual, monitors, prefs, constants
from psychopy.visual import filters
from psychopy.tools.coordinatetools import pol2cart
from psychopy.tests import utils
import numpy
import pytest
import shutil
from tempfile import mkdtemp

"""Each test class creates a context subclasses _basePluginTest to run a series
of tests on a single graphics context (e.g. pyglet with shaders)

To add a new stimulus test use _base so that it gets tested in all contexts

"""

from psychopy.tests import skip_under_vm, requires_plugin
from psychopy.tools import systemtools

class _basePluginTest():
    @classmethod
    def setup_class(self):#run once for each test class (window)
        self.win=None
        self.contextName
        raise NotImplementedError

    @classmethod
    def teardown_class(self):#run once for each test class (window)
        self.win.close()#shutil.rmtree(self.temp_dir)

    def setup_method(self):#this is run for each test individually
        #make sure we start with a clean window
        self.win.flip()
    
    def test_rating_scale(self):
        if self.win.winType=='pygame':
            pytest.skip("RatingScale not available on pygame")
        # try to avoid text; avoid default / 'triangle' because it does not display on win XP
        win = self.win
        win.flip()
        rs = visual.RatingScale(win, low=0, high=1, precision=100, size=3, pos=(0,-.4),
                        labels=[' ', ' '], scale=' ',
                        marker='glow', markerStart=0.7, markerColor='darkBlue', autoLog=False)
        "{}".format(rs) #check that str(xxx) is working
        rs.draw()
        utils.compareScreenshot('ratingscale1_%s.png' %(self.contextName), win, crit=40.0)
        win.flip()#AFTER compare screenshot

class TestPygletNorm(_basePluginTest):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128,128], winType='pyglet', pos=[50,50],
                                 allowStencil=True, autoLog=False)
        self.contextName='norm'
        self.scaleFactor=1#applied to size/pos values

class TestPygletHexColor(_basePluginTest):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128,128], winType='pyglet', pos=[50,50],
                                 color="#FF0099",
                                 allowStencil=True, autoLog=False)
        self.contextName='normHexbackground'
        self.scaleFactor=1#applied to size/pos values

if not systemtools.isVM_CI():
    class TestPygletBlendAdd(_basePluginTest):
        @classmethod
        def setup_class(self):
            self.win = visual.Window([128,128], winType='pyglet', pos=[50,50],
                                     blendMode='add', useFBO=True)
            self.contextName='normAddBlend'
            self.scaleFactor=1#applied to size/pos values


class TestPygletNormFBO(_basePluginTest):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128,128], units="norm", winType='pyglet', pos=[50,50],
                                 allowStencil=True, autoLog=False, useFBO=True)
        self.contextName='norm'
        self.scaleFactor=1#applied to size/pos values


class TestPygletHeight(_basePluginTest):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128,64], units="height", winType='pyglet', pos=[50,50],
                                 allowStencil=False, autoLog=False)
        self.contextName='height'
        self.scaleFactor=1#applied to size/pos values


class TestPygletNormStencil(_basePluginTest):
    @classmethod
    def setup_class(self):
        self.win = visual.Window([128,128], units="norm", monitor='testMonitor',
                                 winType='pyglet', pos=[50,50],
                                 allowStencil=True, autoLog=False)
        self.contextName='stencil'
        self.scaleFactor=1#applied to size/pos values


class TestPygletPix(_basePluginTest):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57)
        mon.setWidth(40.0)
        mon.setSizePix([1024,768])
        self.win = visual.Window([128,128], units="pix", monitor=mon,
                                 winType='pyglet', pos=[50, 50],
                                 allowStencil=True, autoLog=False)
        self.contextName='pix'
        self.scaleFactor=60#applied to size/pos values


class TestPygletCm(_basePluginTest):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57.0)
        mon.setWidth(40.0)
        mon.setSizePix([1024,768])
        self.win = visual.Window([128,128], units="cm", monitor=mon,
                                 winType='pyglet', pos=[50,50],
                                 allowStencil=False, autoLog=False)
        self.contextName='cm'
        self.scaleFactor=2#applied to size/pos values


class TestPygletDeg(_basePluginTest):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(57.0)
        mon.setWidth(40.0)
        mon.setSizePix([1024,768])
        self.win = visual.Window([128,128], units="deg", monitor=mon,
                                 winType='pyglet', pos=[50,50], allowStencil=True,
                                 autoLog=False)
        self.contextName='deg'
        self.scaleFactor=2#applied to size/pos values


class TestPygletDegFlat(_basePluginTest):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(10.0) #exaggerate the effect of flatness by setting the monitor close
        mon.setWidth(40.0)
        mon.setSizePix([1024,768])
        self.win = visual.Window([128,128], units="degFlat", monitor=mon,
                                 winType='pyglet', pos=[50,50],
                                 allowStencil=True, autoLog=False)
        self.contextName='degFlat'
        self.scaleFactor=4#applied to size/pos values


class TestPygletDegFlatPos(_basePluginTest):
    @classmethod
    def setup_class(self):
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(10.0) #exaggerate the effect of flatness by setting the monitor close
        mon.setWidth(40.0)
        mon.setSizePix([1024,768])
        self.win = visual.Window([128,128], units='degFlatPos', monitor=mon,
                                 winType='pyglet', pos=[50,50],
                                 allowStencil=True, autoLog=False)
        self.contextName='degFlatPos'
        self.scaleFactor=4#applied to size/pos values
