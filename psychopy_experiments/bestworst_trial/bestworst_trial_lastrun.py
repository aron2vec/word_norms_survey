#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on maart 09, 2023, at 12:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'bestworst_trial'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jooss004\\Documents\\traineeship_project\\survey\\psychopy_survey\\bestworst_trial_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "stimuli_loader" ---

# --- Initialize components for Routine "stimuli_block_creator" ---

# --- Initialize components for Routine "selftimed_pause" ---
selftimed_pause_text = visual.TextStim(win=win, name='selftimed_pause_text',
    text="Soms kan een survey invullen erg vermoeiend werken. Om vermoeidheid tegen te gaan bieden we hier de mogelijkheid om een pauze te nemen. Deze pauze kan zo lang duren als je zelf wilt en het is voor dit experiment toegestaan om tijdens deze pauzes je telefoon er bij te pakken. \n\nOm door te gaan naar de rest van het experiment, klik op de 'volgende'-knop.",
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
next_button_selftimed_pause = visual.ButtonStim(win, 
    text='Volgende >>', font='Arvo',
    pos=[0.77, -0.44],
    letterHeight=0.025,
    size=[0.2, 0.1], borderWidth=0.0,
    fillColor=[0.12, 0.45, -0.14], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='next_button_selftimed_pause'
)
next_button_selftimed_pause.buttonClock = core.Clock()

# --- Initialize components for Routine "pause_tenthsecond" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "block_instructions" ---
block_instruction_text = visual.TextStim(win=win, name='block_instruction_text',
    text='Je krijgt straks [hoeveelheid] sets van 4                              te zien. Verder is er aan iedere set een specifieke associatie verbonden. Voor iedere set van 4                              vragen we je om aan te geven welke je hiervan het MEESTE en het MINSTE vind passen bij de associatie. \n\nOp de volgende pagina zal er een voorbeeld gepresenteerd worden, waarbij je de verschillende knoppen uit kan proberen om te zien hoe het precies werkt. Hierna volgen de echte vragen die bij het experiment horen.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_button_block_instructions = visual.ButtonStim(win, 
    text='Volgende >>', font='Arvo',
    pos=[0.77, -0.44],
    letterHeight=0.025,
    size=[0.2, 0.1], borderWidth=0.0,
    fillColor=[0.12, 0.45, -0.14], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='next_button_block_instructions'
)
next_button_block_instructions.buttonClock = core.Clock()
wordtype_textbox_instruction_block_1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0.182, 0.309),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center-left',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='wordtype_textbox_instruction_block_1',
     autoLog=False,
)
wordtype_textbox_instruction_block_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.208, 0.172),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center-left',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='wordtype_textbox_instruction_block_2',
     autoLog=False,
)

# --- Initialize components for Routine "bestworst_trial" ---
radio_left = visual.Slider(win=win, name='radio_left',
    startValue=None, size=[0.3, 0.05], pos=[-0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=270.0, depth=0, readOnly=False)
radio_right = visual.Slider(win=win, name='radio_right',
    startValue=None, size=[0.3, 0.05], pos=[0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=270.0, depth=-1, readOnly=False)
next_button_trials = visual.ButtonStim(win, 
    text='Volgende >>', font='Arvo',
    pos=[0.77, -0.44],
    letterHeight=0.025,
    size=[0.2, 0.1], borderWidth=0.0,
    fillColor=[0.55, 0.55, 0.55], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='next_button_trials'
)
next_button_trials.buttonClock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text='Welke van de vier                   associeer je het MINSTE \nen het MEESTE met                           ',
    font='Open Sans',
    pos=[0, 0.35], height=0.05, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
wordtype_var_text = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=[-0.18, 0.385],     letterHeight=0.05,
     size=[0.1, 0.1], borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center-left',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='wordtype_var_text',
     autoLog=False,
)
association_var_text = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=[0.07, 0.316],     letterHeight=0.05,
     size=[0.3], borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center-left',
     anchor='center-left',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='association_var_text',
     autoLog=False,
)
line_below = visual.Line(
    win=win, name='line_below',
    start=(-[1.3, 0.2][0]/2.0, 0), end=(+[1.3, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-8.0, interpolate=True)
line_above = visual.Line(
    win=win, name='line_above',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-9.0, interpolate=True)
line_above_2 = visual.Line(
    win=win, name='line_above_2',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-10.0, interpolate=True)
line_above_3 = visual.Line(
    win=win, name='line_above_3',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-11.0, interpolate=True)
line_above_4 = visual.Line(
    win=win, name='line_above_4',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-12.0, interpolate=True)
minst_text = visual.TextBox2(
     win, text='Minste', font='Open Sans',
     pos=(-0.5, 0.05),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='minst_text',
     autoLog=False,
)
meest_text = visual.TextBox2(
     win, text='Meeste', font='Open Sans',
     pos=(0.5, 0.05),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='meest_text',
     autoLog=False,
)
word1_var_text = visual.TextStim(win=win, name='word1_var_text',
    text='',
    font='Open Sans',
    pos=(0, -.04), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
word2_var_text = visual.TextStim(win=win, name='word2_var_text',
    text='',
    font='Open Sans',
    pos=(0, -0.14), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
word3_var_text = visual.TextStim(win=win, name='word3_var_text',
    text='',
    font='Open Sans',
    pos=(0, -.24), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
word4_var_text = visual.TextStim(win=win, name='word4_var_text',
    text='',
    font='Open Sans',
    pos=(0, -.34), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# --- Initialize components for Routine "pause_tenthsecond" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pause_tenthsecond" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "stimuli_loader" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
stimuli_loaderComponents = []
for thisComponent in stimuli_loaderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "stimuli_loader" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stimuli_loaderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "stimuli_loader" ---
for thisComponent in stimuli_loaderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stimuli_loader" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "stimuli_block_creator" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
stimuli_block_creatorComponents = []
for thisComponent in stimuli_block_creatorComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "stimuli_block_creator" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stimuli_block_creatorComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "stimuli_block_creator" ---
for thisComponent in stimuli_block_creatorComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "stimuli_block_creator" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wordtype_block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bestworst_example_trials_blocks.xlsx'),
    seed=None, name='wordtype_block')
thisExp.addLoop(wordtype_block)  # add the loop to the experiment
thisWordtype_block = wordtype_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWordtype_block.rgb)
if thisWordtype_block != None:
    for paramName in thisWordtype_block:
        exec('{} = thisWordtype_block[paramName]'.format(paramName))

for thisWordtype_block in wordtype_block:
    currentLoop = wordtype_block
    # abbreviate parameter names if possible (e.g. rgb = thisWordtype_block.rgb)
    if thisWordtype_block != None:
        for paramName in thisWordtype_block:
            exec('{} = thisWordtype_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selftimed_pause" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selftimed_pause_code
    if wordtype_instructions == 'voornamen':
        continueRoutine = False
    else:
        pass
    # keep track of which components have finished
    selftimed_pauseComponents = [selftimed_pause_text, next_button_selftimed_pause]
    for thisComponent in selftimed_pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "selftimed_pause" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *selftimed_pause_text* updates
        if selftimed_pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            selftimed_pause_text.frameNStart = frameN  # exact frame index
            selftimed_pause_text.tStart = t  # local t and not account for scr refresh
            selftimed_pause_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(selftimed_pause_text, 'tStartRefresh')  # time at next scr refresh
            selftimed_pause_text.setAutoDraw(True)
        
        # *next_button_selftimed_pause* updates
        if next_button_selftimed_pause.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_button_selftimed_pause.frameNStart = frameN  # exact frame index
            next_button_selftimed_pause.tStart = t  # local t and not account for scr refresh
            next_button_selftimed_pause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button_selftimed_pause, 'tStartRefresh')  # time at next scr refresh
            next_button_selftimed_pause.setAutoDraw(True)
        if next_button_selftimed_pause.status == STARTED:
            # check whether next_button_selftimed_pause has been pressed
            if next_button_selftimed_pause.isClicked:
                if not next_button_selftimed_pause.wasClicked:
                    next_button_selftimed_pause.timesOn.append(next_button_selftimed_pause.buttonClock.getTime()) # store time of first click
                    next_button_selftimed_pause.timesOff.append(next_button_selftimed_pause.buttonClock.getTime()) # store time clicked until
                else:
                    next_button_selftimed_pause.timesOff[-1] = next_button_selftimed_pause.buttonClock.getTime() # update time clicked until
                continueRoutine = False
                next_button_selftimed_pause.wasClicked = True  # if next_button_selftimed_pause is still clicked next frame, it is not a new click
            else:
                next_button_selftimed_pause.wasClicked = False  # if next_button_selftimed_pause is clicked next frame, it is a new click
        else:
            next_button_selftimed_pause.wasClicked = False  # if next_button_selftimed_pause is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selftimed_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selftimed_pause" ---
    for thisComponent in selftimed_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selftimed_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "pause_tenthsecond" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    pause_tenthsecondComponents = [text]
    for thisComponent in pause_tenthsecondComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_tenthsecond" ---
    while continueRoutine and routineTimer.getTime() < 0.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_tenthsecondComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_tenthsecond" ---
    for thisComponent in pause_tenthsecondComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.100000)
    
    # --- Prepare to start Routine "block_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wordtype_textbox_instruction_block_1.reset()
    wordtype_textbox_instruction_block_1.setText(wordtype_instructions)
    wordtype_textbox_instruction_block_2.reset()
    wordtype_textbox_instruction_block_2.setText(wordtype_instructions)
    # keep track of which components have finished
    block_instructionsComponents = [block_instruction_text, next_button_block_instructions, wordtype_textbox_instruction_block_1, wordtype_textbox_instruction_block_2]
    for thisComponent in block_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_instruction_text* updates
        if block_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_instruction_text.frameNStart = frameN  # exact frame index
            block_instruction_text.tStart = t  # local t and not account for scr refresh
            block_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_instruction_text, 'tStartRefresh')  # time at next scr refresh
            block_instruction_text.setAutoDraw(True)
        
        # *next_button_block_instructions* updates
        if next_button_block_instructions.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            next_button_block_instructions.frameNStart = frameN  # exact frame index
            next_button_block_instructions.tStart = t  # local t and not account for scr refresh
            next_button_block_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button_block_instructions, 'tStartRefresh')  # time at next scr refresh
            next_button_block_instructions.setAutoDraw(True)
        if next_button_block_instructions.status == STARTED:
            # check whether next_button_block_instructions has been pressed
            if next_button_block_instructions.isClicked:
                if not next_button_block_instructions.wasClicked:
                    next_button_block_instructions.timesOn.append(next_button_block_instructions.buttonClock.getTime()) # store time of first click
                    next_button_block_instructions.timesOff.append(next_button_block_instructions.buttonClock.getTime()) # store time clicked until
                else:
                    next_button_block_instructions.timesOff[-1] = next_button_block_instructions.buttonClock.getTime() # update time clicked until
                if not next_button_block_instructions.wasClicked:
                    continueRoutine = False
                next_button_block_instructions.wasClicked = True  # if next_button_block_instructions is still clicked next frame, it is not a new click
            else:
                next_button_block_instructions.wasClicked = False  # if next_button_block_instructions is clicked next frame, it is a new click
        else:
            next_button_block_instructions.wasClicked = False  # if next_button_block_instructions is clicked next frame, it is a new click
        
        # *wordtype_textbox_instruction_block_1* updates
        if wordtype_textbox_instruction_block_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wordtype_textbox_instruction_block_1.frameNStart = frameN  # exact frame index
            wordtype_textbox_instruction_block_1.tStart = t  # local t and not account for scr refresh
            wordtype_textbox_instruction_block_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordtype_textbox_instruction_block_1, 'tStartRefresh')  # time at next scr refresh
            wordtype_textbox_instruction_block_1.setAutoDraw(True)
        
        # *wordtype_textbox_instruction_block_2* updates
        if wordtype_textbox_instruction_block_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wordtype_textbox_instruction_block_2.frameNStart = frameN  # exact frame index
            wordtype_textbox_instruction_block_2.tStart = t  # local t and not account for scr refresh
            wordtype_textbox_instruction_block_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordtype_textbox_instruction_block_2, 'tStartRefresh')  # time at next scr refresh
            wordtype_textbox_instruction_block_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_instructions" ---
    for thisComponent in block_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    within_block_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blocks),
        seed=None, name='within_block_trials')
    thisExp.addLoop(within_block_trials)  # add the loop to the experiment
    thisWithin_block_trial = within_block_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWithin_block_trial.rgb)
    if thisWithin_block_trial != None:
        for paramName in thisWithin_block_trial:
            exec('{} = thisWithin_block_trial[paramName]'.format(paramName))
    
    for thisWithin_block_trial in within_block_trials:
        currentLoop = within_block_trials
        # abbreviate parameter names if possible (e.g. rgb = thisWithin_block_trial.rgb)
        if thisWithin_block_trial != None:
            for paramName in thisWithin_block_trial:
                exec('{} = thisWithin_block_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "bestworst_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        radio_left.reset()
        radio_right.reset()
        # Run 'Begin Routine' code from nextbutton_trials_code
        next_button_clicked = False
        
        next_button_trials.fillColor = (0.55, 0.55, 0.55)
        next_button_trials.updateColors()
        wordtype_var_text.reset()
        wordtype_var_text.setText(wordtype)
        association_var_text.reset()
        association_var_text.setText(association)
        minst_text.reset()
        meest_text.reset()
        word1_var_text.setText(word1)
        word2_var_text.setText(word2)
        word3_var_text.setText(word3)
        word4_var_text.setText(word4)
        # keep track of which components have finished
        bestworst_trialComponents = [radio_left, radio_right, next_button_trials, instruction_text, wordtype_var_text, association_var_text, line_below, line_above, line_above_2, line_above_3, line_above_4, minst_text, meest_text, word1_var_text, word2_var_text, word3_var_text, word4_var_text]
        for thisComponent in bestworst_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "bestworst_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *radio_left* updates
            if radio_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                radio_left.frameNStart = frameN  # exact frame index
                radio_left.tStart = t  # local t and not account for scr refresh
                radio_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(radio_left, 'tStartRefresh')  # time at next scr refresh
                radio_left.setAutoDraw(True)
            
            # *radio_right* updates
            if radio_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                radio_right.frameNStart = frameN  # exact frame index
                radio_right.tStart = t  # local t and not account for scr refresh
                radio_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(radio_right, 'tStartRefresh')  # time at next scr refresh
                radio_right.setAutoDraw(True)
            # Run 'Each Frame' code from linking_sliders_code
            left_slider_choice = radio_left.getRating()
            right_slider_choice = radio_right.getRating()
            
            if len(radio_left.getHistory()) > 0 and len(radio_right.getHistory()) > 0:
                left_last_choice_time = radio_left.getHistory()[-1][1]
                right_last_choice_time = radio_right.getHistory()[-1][1]
            
                if left_slider_choice == right_slider_choice:
                    # check whether right radio was interacted with last
                    if right_last_choice_time > left_last_choice_time:
                        radio_left.reset()
                        radio_right.reset()
                        radio_right.recordRating(right_slider_choice)
                    else:
                        radio_right.reset()
                        radio_left.reset()
                        radio_left.recordRating(left_slider_choice)
            
            # *next_button_trials* updates
            if next_button_trials.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                next_button_trials.frameNStart = frameN  # exact frame index
                next_button_trials.tStart = t  # local t and not account for scr refresh
                next_button_trials.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next_button_trials, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'next_button_trials.started')
                next_button_trials.setAutoDraw(True)
            if next_button_trials.status == STARTED:
                # check whether next_button_trials has been pressed
                if next_button_trials.isClicked:
                    if not next_button_trials.wasClicked:
                        next_button_trials.timesOn.append(next_button_trials.buttonClock.getTime()) # store time of first click
                        next_button_trials.timesOff.append(next_button_trials.buttonClock.getTime()) # store time clicked until
                    else:
                        next_button_trials.timesOff[-1] = next_button_trials.buttonClock.getTime() # update time clicked until
                    if radio_right.getRating() and radio_left.getRating():
                         next_button_clicked = True
                    next_button_trials.wasClicked = True  # if next_button_trials is still clicked next frame, it is not a new click
                else:
                    next_button_trials.wasClicked = False  # if next_button_trials is clicked next frame, it is a new click
            else:
                next_button_trials.wasClicked = False  # if next_button_trials is clicked next frame, it is a new click
            # Run 'Each Frame' code from nextbutton_trials_code
            # make button standard color be grey, turn green 
            # when both radio buttons have an answer
            
            if radio_right.getRating() and radio_left.getRating():
                next_button_trials.fillColor = (0.12, 0.45, -0.14)
                next_button_trials.updateColors()
                if next_button_clicked == True:
                    continueRoutine = False
                else:
                    pass
            else:
                next_button_trials.fillColor = (0.55, 0.55, 0.55)
                next_button_trials.updateColors()
            
            # *instruction_text* updates
            if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instruction_text.frameNStart = frameN  # exact frame index
                instruction_text.tStart = t  # local t and not account for scr refresh
                instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
                instruction_text.setAutoDraw(True)
            
            # *wordtype_var_text* updates
            if wordtype_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wordtype_var_text.frameNStart = frameN  # exact frame index
                wordtype_var_text.tStart = t  # local t and not account for scr refresh
                wordtype_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wordtype_var_text, 'tStartRefresh')  # time at next scr refresh
                wordtype_var_text.setAutoDraw(True)
            
            # *association_var_text* updates
            if association_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                association_var_text.frameNStart = frameN  # exact frame index
                association_var_text.tStart = t  # local t and not account for scr refresh
                association_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(association_var_text, 'tStartRefresh')  # time at next scr refresh
                association_var_text.setAutoDraw(True)
            
            # *line_below* updates
            if line_below.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                line_below.frameNStart = frameN  # exact frame index
                line_below.tStart = t  # local t and not account for scr refresh
                line_below.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line_below, 'tStartRefresh')  # time at next scr refresh
                line_below.setAutoDraw(True)
            
            # *line_above* updates
            if line_above.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                line_above.frameNStart = frameN  # exact frame index
                line_above.tStart = t  # local t and not account for scr refresh
                line_above.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line_above, 'tStartRefresh')  # time at next scr refresh
                line_above.setAutoDraw(True)
            
            # *line_above_2* updates
            if line_above_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                line_above_2.frameNStart = frameN  # exact frame index
                line_above_2.tStart = t  # local t and not account for scr refresh
                line_above_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line_above_2, 'tStartRefresh')  # time at next scr refresh
                line_above_2.setAutoDraw(True)
            
            # *line_above_3* updates
            if line_above_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                line_above_3.frameNStart = frameN  # exact frame index
                line_above_3.tStart = t  # local t and not account for scr refresh
                line_above_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line_above_3, 'tStartRefresh')  # time at next scr refresh
                line_above_3.setAutoDraw(True)
            
            # *line_above_4* updates
            if line_above_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                line_above_4.frameNStart = frameN  # exact frame index
                line_above_4.tStart = t  # local t and not account for scr refresh
                line_above_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(line_above_4, 'tStartRefresh')  # time at next scr refresh
                line_above_4.setAutoDraw(True)
            
            # *minst_text* updates
            if minst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                minst_text.frameNStart = frameN  # exact frame index
                minst_text.tStart = t  # local t and not account for scr refresh
                minst_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(minst_text, 'tStartRefresh')  # time at next scr refresh
                minst_text.setAutoDraw(True)
            
            # *meest_text* updates
            if meest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                meest_text.frameNStart = frameN  # exact frame index
                meest_text.tStart = t  # local t and not account for scr refresh
                meest_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(meest_text, 'tStartRefresh')  # time at next scr refresh
                meest_text.setAutoDraw(True)
            
            # *word1_var_text* updates
            if word1_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word1_var_text.frameNStart = frameN  # exact frame index
                word1_var_text.tStart = t  # local t and not account for scr refresh
                word1_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word1_var_text, 'tStartRefresh')  # time at next scr refresh
                word1_var_text.setAutoDraw(True)
            
            # *word2_var_text* updates
            if word2_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word2_var_text.frameNStart = frameN  # exact frame index
                word2_var_text.tStart = t  # local t and not account for scr refresh
                word2_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word2_var_text, 'tStartRefresh')  # time at next scr refresh
                word2_var_text.setAutoDraw(True)
            
            # *word3_var_text* updates
            if word3_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word3_var_text.frameNStart = frameN  # exact frame index
                word3_var_text.tStart = t  # local t and not account for scr refresh
                word3_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word3_var_text, 'tStartRefresh')  # time at next scr refresh
                word3_var_text.setAutoDraw(True)
            
            # *word4_var_text* updates
            if word4_var_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word4_var_text.frameNStart = frameN  # exact frame index
                word4_var_text.tStart = t  # local t and not account for scr refresh
                word4_var_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word4_var_text, 'tStartRefresh')  # time at next scr refresh
                word4_var_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in bestworst_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "bestworst_trial" ---
        for thisComponent in bestworst_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        within_block_trials.addData('radio_left.response', radio_left.getRating())
        within_block_trials.addData('radio_right.response', radio_right.getRating())
        within_block_trials.addData('next_button_trials.numClicks', next_button_trials.numClicks)
        if next_button_trials.numClicks:
           within_block_trials.addData('next_button_trials.timesOn', next_button_trials.timesOn)
           within_block_trials.addData('next_button_trials.timesOff', next_button_trials.timesOff)
        else:
           within_block_trials.addData('next_button_trials.timesOn', "")
           within_block_trials.addData('next_button_trials.timesOff', "")
        # Run 'End Routine' code from nextbutton_trials_code
        next_button_clicked = False
        
        # the Routine "bestworst_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause_tenthsecond" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        pause_tenthsecondComponents = [text]
        for thisComponent in pause_tenthsecondComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause_tenthsecond" ---
        while continueRoutine and routineTimer.getTime() < 0.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause_tenthsecondComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_tenthsecond" ---
        for thisComponent in pause_tenthsecondComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.100000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'within_block_trials'
    
    
    # --- Prepare to start Routine "pause_tenthsecond" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    pause_tenthsecondComponents = [text]
    for thisComponent in pause_tenthsecondComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pause_tenthsecond" ---
    while continueRoutine and routineTimer.getTime() < 0.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_tenthsecondComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause_tenthsecond" ---
    for thisComponent in pause_tenthsecondComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.100000)
# completed 1.0 repeats of 'wordtype_block'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
