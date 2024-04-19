-------------------------------
RatingScaleComponent
-------------------------------
A class for presenting a rating scale as a builder Component


Categories:
    Responses
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

Category choices
    A list of categories (non-numeric alternatives) to present, space or comma-separated; these take precedence over a numeric scale

Scale description
    Brief instructions, such as a description of the scale numbers as seen by the subject.

Force end of Routine
    Should accepting a rating cause the end of the Routine (e.g. trial)?

Data
===============================

Save onset/offset times
    Store the onset/offset times in the data file (as well as in the log file).

Sync timing with screen refresh
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Visual analog scale
    Show a continuous visual analog scale; returns 0.00 to 1.00; takes precedence over numeric scale or categorical choices

Lowest value
    Lowest rating (low end of the scale); not used for categories.

Highest value
    Highest rating (top end of the scale); not used for categories.

Labels
    Labels for the ends of the scale, separated by commas

Marker start
    initial position for the marker

Store rating
    store the rating

Store rating time
    store the time taken to make the choice (in seconds)

Store history
    store the history of (selection, time)

Testing
===============================

Disable Component
    Disable this Component

Interface
===============================

Marker type
    Style for the marker: triangle, circle, glow, slider, hover
    
    Options:
    - triangle
    - circle
    - glow
    - slider
    - hover

Single click
    Should clicking the line accept that rating (without needing to confirm via 'accept')?

Disappear
    Hide the scale when a rating has been accepted; False to remain on-screen

Show accept
    Should the accept button by visible?

Tick height
    height of tick marks (1 is upward, 0 is hidden, -1 is downward)

Custom
===============================

Customize everything :
    Use this text to create the rating scale as you would in a code Component; overrides all dialog settings except time parameters, forceEndRoutine, storeRatingTime, storeRating

Layout
===============================

Size
    Size of this stimulus (either a single value or x,y pair, e.g. 2.5, [1,2] 

Position [x,y]
    Position of this stimulus (e.g. [1,2] )

