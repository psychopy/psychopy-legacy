-------------------------------
PatchComponent
-------------------------------
An event class for presenting image-based stimuli

Categories:
    Stimuli
Works in:
    PsychoPy

Parameters
-------------------------------

Basic
===============================

Name
    Name of this Component (alphanumeric or _, no spaces)

Start type
    How do you want to define your start point?
    
    Options:
    - time (s)
    - frame N
    - condition

Stop type
    How do you want to define your end point?
    
    Options:
    - duration (s)
    - duration (frames)
    - time (s)
    - frame N
    - condition

Start
    When does the Component start?

Stop
    When does the Component end? (blank is endless)

Expected start (s)
    (Optional) expected start (s), purely for representing in the timeline

Expected duration (s)
    (Optional) expected duration (s), purely for representing in the timeline

Image/tex
    The image to be displayed - 'sin','sqr'... or a filename (including path)

Data
===============================

Save onset/offset times
    Store the onset/offset times in the data file (as well as in the log file).

Sync timing with screen refresh
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Testing
===============================

Disable Component
    Disable this Component

Validate with...
    Name of validator Component/Routine to use to check the timing of this stimulus.

    Options are generated live, so will vary according to your setup.

Layout
===============================

Spatial units
    Units of dimensions for this stimulus
    
    Options:
    - from exp settings
    - deg
    - cm
    - pix
    - norm
    - height
    - degFlatPos
    - degFlat

Position [x,y]
    Position of this stimulus (e.g. [1,2] )

Size [w,h]
    Size of this stimulus (either a single value or x,y pair, e.g. 2.5, [1,2] 

Orientation
    Orientation of this stimulus (in deg)
    
    Options:
    - -360
    - 360

Appearance
===============================

Foreground color
    Foreground color of this stimulus (e.g. $[1,1,0], red )

Color space
    In what format (color space) have you specified the colors? (rgb, dkl, lms, hsv)
    
    Options:
    - rgb
    - dkl
    - lms
    - hsv

Fill color
    Fill color of this stimulus (e.g. $[1,1,0], red )

Border color
    Border color of this stimulus (e.g. $[1,1,0], red )

Opacity
    Opacity of the stimulus (1=opaque, 0=fully transparent, 0.5=translucent). Leave blank for each color to have its own opacity (recommended if any color is None).

Contrast
    Contrast of the stimulus (1.0=unchanged contrast, 0.5=decrease contrast, 0.0=uniform/no contrast, -0.5=slightly inverted, -1.0=totally inverted)

Texture
===============================

Mask
    An image to define the alpha mask (ie shape)- gauss, circle... or a filename (including path)

Spatial frequency
    Spatial frequency of image repeats across the patch, e.g. 4 or [2,3]

Phase (in cycles)
    Spatial positioning of the image on the patch (in range 0-1.0)

Texture resolution
    Resolution of the texture for standard ones such as sin, sqr etc. For most cases a value of 256 pixels will suffice
    
    Options:
    - 32
    - 64
    - 128
    - 256
    - 512

Interpolate
    How should the image be interpolated if/when rescaled
    
    Options:
    - linear
    - nearest

