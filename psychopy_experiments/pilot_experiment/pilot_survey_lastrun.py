#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on maart 27, 2023, at 14:51
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
expName = 'pilot_survey'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\jooss004\\Documents\\traineeship_project\\word_norms_survey\\psychopy_experiments\\pilot\\pilot_survey_lastrun.py',
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

# --- Initialize components for Routine "block_selector" ---
# Run 'Begin Experiment' code from code
# I don't know how to do this yet, but, for every
# trials file that I load, I have to select only 
# the 16 trials that accord to each participant's
# assigned number

p_num = int(expInfo['participant'])


row_start = (p_num-1) * 16
row_end = ((p_num-1) * 16) + 16
trial_rows = str(row_start) + ':' + str(row_end)

# --- Initialize components for Routine "general_introduction" ---
general_introduction_text = visual.TextStim(win=win, name='general_introduction_text',
    text="Welkom bij ons experiment. Om door te gaan moet je toestemming geven dat we je data kunnen opslaan en gebruiken voor verdere analyse. Klik hiervoor op de 'IK GEEF TOESTEMMING' knop onderaan de pagina. Enkel als je toestemming gegeven hebt kan je door naar de rest van het experiment. Indien je geen toestemming geeft kan je de survey afsluiten door op de 'escape' knop te klikken en terug te gaan naar de onderzoeker.\n\nVoor verdere vragen over het onderzoek, mail: a.y.joosse@uu.nl",
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=1.7, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_button_gen_intro = visual.ButtonStim(win, 
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
    name='next_button_gen_intro'
)
next_button_gen_intro.buttonClock = core.Clock()
box1 = visual.Rect(
    win=win, name='box1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-.5, -.3), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
checkbox_mouse = event.Mouse(win=win)
x, y = [None, None]
checkbox_mouse.mouseClock = core.Clock()
consent_text = visual.TextStim(win=win, name='consent_text',
    text='IK GEEF TOESTEMMING',
    font='Open Sans',
    pos=(-0.16, -0.2935), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "pause_tenthsecond" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "example_trial_instructions" ---
example_trial_instruction_text = visual.TextStim(win=win, name='example_trial_instruction_text',
    text='In deze survey zal je drie blokken met elk 16 vragen te zien krijgen, met tussendoor een pauze. Elke individuele vraag betreft vier woorden of namen waaruit je één minst en één meest passende optie moet kiezen voor een willekeurige associatie. Let dus goed op bij iedere nieuwe vraag welke associatie willekeurig gekozen is.\n\nOp de volgende pagina zal er een voorbeeld gepresenteerd worden, waarbij je de verschillende knoppen uit kan proberen om te zien hoe het precies werkt. Hierna volgen er instructies voor de echte vragenlijst.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.7, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_button_example_trial_instructions = visual.ButtonStim(win, 
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
    name='next_button_example_trial_instructions'
)
next_button_example_trial_instructions.buttonClock = core.Clock()
ex_trial_inst_mouse = event.Mouse(win=win)
x, y = [None, None]
ex_trial_inst_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "pause_tenthsecond" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "example_trial" ---
radio_left_ex = visual.Slider(win=win, name='radio_left_ex',
    startValue=None, size=[0.3, 0.05], pos=[-0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=270.0, depth=0, readOnly=False)
radio_right_ex = visual.Slider(win=win, name='radio_right_ex',
    startValue=None, size=[0.3, 0.05], pos=[0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=270.0, depth=-1, readOnly=False)
next_button_trials_ex = visual.ButtonStim(win, 
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
    name='next_button_trials_ex'
)
next_button_trials_ex.buttonClock = core.Clock()
instruction_text_ex = visual.TextStim(win=win, name='instruction_text_ex',
    text='Welke van de vier                   associeer je het MINSTE \nen het MEESTE met                           ',
    font='Open Sans',
    pos=[0, 0.35], height=0.05, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
wordtype_var_text_ex = visual.TextBox2(
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
     name='wordtype_var_text_ex',
     autoLog=False,
)
association_var_text_ex = visual.TextBox2(
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
     name='association_var_text_ex',
     autoLog=False,
)
line_below_ex = visual.Line(
    win=win, name='line_below_ex',
    start=(-[1.3, 0.2][0]/2.0, 0), end=(+[1.3, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-8.0, interpolate=True)
line_above_ex = visual.Line(
    win=win, name='line_above_ex',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-9.0, interpolate=True)
line_above_2_ex = visual.Line(
    win=win, name='line_above_2_ex',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-10.0, interpolate=True)
line_above_3_ex = visual.Line(
    win=win, name='line_above_3_ex',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-11.0, interpolate=True)
line_above_4_ex = visual.Line(
    win=win, name='line_above_4_ex',
    start=(-[0.7, 0.2][0]/2.0, 0), end=(+[0.7, 0.2][0]/2.0, 0),
    ori=0.0, pos=(-0.7, -0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0] ,
    opacity=1.0, depth=-12.0, interpolate=True)
minst_text_ex = visual.TextBox2(
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
     name='minst_text_ex',
     autoLog=False,
)
meest_text_ex = visual.TextBox2(
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
     name='meest_text_ex',
     autoLog=False,
)
word1_var_text_ex = visual.TextStim(win=win, name='word1_var_text_ex',
    text='',
    font='Open Sans',
    pos=(0, -.04), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
word2_var_text_ex = visual.TextStim(win=win, name='word2_var_text_ex',
    text='',
    font='Open Sans',
    pos=(0, -0.14), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
word3_var_text_ex = visual.TextStim(win=win, name='word3_var_text_ex',
    text='',
    font='Open Sans',
    pos=(0, -.24), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
word4_var_text_ex = visual.TextStim(win=win, name='word4_var_text_ex',
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

# --- Initialize components for Routine "selftimed_pause" ---
selftimed_pause_text = visual.TextStim(win=win, name='selftimed_pause_text',
    text="Soms kan een survey invullen erg vermoeiend werken. Om vermoeidheid tegen te gaan bieden we hier de mogelijkheid om een pauze te nemen. Deze pauze kan zo lang duren als je zelf wilt. \n\nHet is voor dit experiment toegestaan om tijdens deze pauzes je telefoon er bij te pakken. \n\nOm door te gaan naar de rest van het experiment, klik op de 'volgende'-knop.",
    font='Open Sans',
    pos=(0, 0.06), height=0.05, wrapWidth=1.7, ori=0.0, 
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
selftimed_pause_mouse = event.Mouse(win=win)
x, y = [None, None]
selftimed_pause_mouse.mouseClock = core.Clock()

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
    text='Je krijgt straks 16 verschillende sets van 4                               te zien. Verder geldt er voor iedere individuele set een specifieke, willekeurig gekozen associatie. Voor iedere set van 4                                  vragen we je om aan te geven welke je hiervan het MEESTE en het MINSTE vind passen bij de associatie. \n\nLet op: de associaties worden willekeurig gekozen, lees deze dus goed voor het beantwoorden van de vragen.',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=1.7, ori=0.0, 
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
     pos=(0.130, 0.3413),     letterHeight=0.05,
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
     pos=(-.07, 0.2033),     letterHeight=0.05,
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
block_instr_mouse = event.Mouse(win=win)
x, y = [None, None]
block_instr_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "bestworst_trial" ---
radio_left = visual.Slider(win=win, name='radio_left',
    startValue=None, size=[0.3, 0.05], pos=[-0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=270.0, depth=0, readOnly=False)
radio_right = visual.Slider(win=win, name='radio_right',
    startValue=None, size=[0.3, 0.05], pos=[0.5, -0.2], units=None,
    labels=(1, 2, 3, 4), ticks=(1, 2, 3, 4), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.0000, 0.0000, 0.0000], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=270.0, depth=-1, readOnly=False)
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
    pos=(0, -.34), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
word2_var_text = visual.TextStim(win=win, name='word2_var_text',
    text='',
    font='Open Sans',
    pos=(0, -0.24), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
word3_var_text = visual.TextStim(win=win, name='word3_var_text',
    text='',
    font='Open Sans',
    pos=(0, -.14), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
word4_var_text = visual.TextStim(win=win, name='word4_var_text',
    text='',
    font='Open Sans',
    pos=(0, -.04), height=0.05, wrapWidth=None, ori=0.0, 
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

# --- Initialize components for Routine "thanks_and_bye" ---
thanks_and_bye_text = visual.TextStim(win=win, name='thanks_and_bye_text',
    text="Je hebt het einde bereikt van het experiment! Dankjewel voor je deelname aan het onderzoek. Je kan onderaan de pagina klikken op 'AFSLUITEN' en terug gaan naar de onderzoeker, die je deelname zal registreren en je credits toe zal kennen. \n\nNog een fijne dag gewenst!",
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=1.7, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
finish_button = visual.ButtonStim(win, 
    text='Afsluiten', font='Arvo',
    pos=[0.77, -0.44],
    letterHeight=0.025,
    size=[0.2, 0.1], borderWidth=0.0,
    fillColor=[0.12, 0.45, -0.14], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='finish_button'
)
finish_button.buttonClock = core.Clock()
thanks_bye_mouse = event.Mouse(win=win)
x, y = [None, None]
thanks_bye_mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "block_selector" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
block_selectorComponents = []
for thisComponent in block_selectorComponents:
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

# --- Run Routine "block_selector" ---
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
    for thisComponent in block_selectorComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "block_selector" ---
for thisComponent in block_selectorComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "block_selector" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "general_introduction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from nextbutton_and_concent_gen_intro_code
next_button_clicked = False
consent = False

next_button_gen_intro.fillColor = (0.55, 0.55, 0.55)
next_button_gen_intro.updateColors()

checkboxes = [box1]
clicked = []
mouseDown = False
for box in checkboxes:
    box.color = "white"
# setup some python lists for storing info about the checkbox_mouse
checkbox_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
general_introductionComponents = [general_introduction_text, next_button_gen_intro, box1, checkbox_mouse, consent_text]
for thisComponent in general_introductionComponents:
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

# --- Run Routine "general_introduction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_introduction_text* updates
    if general_introduction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_introduction_text.frameNStart = frameN  # exact frame index
        general_introduction_text.tStart = t  # local t and not account for scr refresh
        general_introduction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_introduction_text, 'tStartRefresh')  # time at next scr refresh
        general_introduction_text.setAutoDraw(True)
    
    # *next_button_gen_intro* updates
    if next_button_gen_intro.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        next_button_gen_intro.frameNStart = frameN  # exact frame index
        next_button_gen_intro.tStart = t  # local t and not account for scr refresh
        next_button_gen_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_button_gen_intro, 'tStartRefresh')  # time at next scr refresh
        next_button_gen_intro.setAutoDraw(True)
    if next_button_gen_intro.status == STARTED:
        # check whether next_button_gen_intro has been pressed
        if next_button_gen_intro.isClicked:
            if not next_button_gen_intro.wasClicked:
                next_button_gen_intro.timesOn.append(next_button_gen_intro.buttonClock.getTime()) # store time of first click
                next_button_gen_intro.timesOff.append(next_button_gen_intro.buttonClock.getTime()) # store time clicked until
            else:
                next_button_gen_intro.timesOff[-1] = next_button_gen_intro.buttonClock.getTime() # update time clicked until
            if not next_button_gen_intro.wasClicked:
                if consent == True:
                    continueRoutine = False
            next_button_gen_intro.wasClicked = True  # if next_button_gen_intro is still clicked next frame, it is not a new click
        else:
            next_button_gen_intro.wasClicked = False  # if next_button_gen_intro is clicked next frame, it is a new click
    else:
        next_button_gen_intro.wasClicked = False  # if next_button_gen_intro is clicked next frame, it is a new click
    # Run 'Each Frame' code from nextbutton_and_concent_gen_intro_code
    # make button standard color be grey, turn green 
    # when both radio buttons have an answer
    
    if checkbox_mouse.getPressed()[0] == 0:
        mouseDown = False
        
    for box in checkboxes:   
        if checkbox_mouse.isPressedIn(box) and box.name not in clicked and not mouseDown:
            box.color = "black"
            clicked.append(box.name)
            consent = True
            mouseDown = True  
        elif checkbox_mouse.isPressedIn(box) and box.name in clicked and not mouseDown:
            box.color = "white"
            consent = False
            clicked.remove(box.name)
            mouseDown = True
    
    
    if consent == True:
        next_button_gen_intro.fillColor = (0.12, 0.45, -0.14)
        next_button_gen_intro.updateColors()
    else:
        next_button_gen_intro.fillColor = (0.55, 0.55, 0.55)
        next_button_gen_intro.updateColors()
    
    # *box1* updates
    if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box1.frameNStart = frameN  # exact frame index
        box1.tStart = t  # local t and not account for scr refresh
        box1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
        box1.setAutoDraw(True)
    # *checkbox_mouse* updates
    if checkbox_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        checkbox_mouse.frameNStart = frameN  # exact frame index
        checkbox_mouse.tStart = t  # local t and not account for scr refresh
        checkbox_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(checkbox_mouse, 'tStartRefresh')  # time at next scr refresh
        checkbox_mouse.status = STARTED
        checkbox_mouse.mouseClock.reset()
        prevButtonState = checkbox_mouse.getPressed()  # if button is down already this ISN'T a new click
    
    # *consent_text* updates
    if consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_text.frameNStart = frameN  # exact frame index
        consent_text.tStart = t  # local t and not account for scr refresh
        consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
        consent_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "general_introduction" ---
for thisComponent in general_introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from nextbutton_and_concent_gen_intro_code
next_button_clicked = False

if consent == True:
    thisExp.addData('consent', True)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "general_introduction" was not non-slip safe, so reset the non-slip timer
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
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
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

# --- Prepare to start Routine "example_trial_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from ex_trial_inst_code
if ex_trial_inst_mouse.getPressed()[0] == 1:
    next_button_example_trial_instructions.fillColor = (0.55, 0.55, 0.55)
    next_button_example_trial_instructions.updateColors()
    ability_to_click_next = False

# setup some python lists for storing info about the ex_trial_inst_mouse
ex_trial_inst_mouse.x = []
ex_trial_inst_mouse.y = []
ex_trial_inst_mouse.leftButton = []
ex_trial_inst_mouse.midButton = []
ex_trial_inst_mouse.rightButton = []
ex_trial_inst_mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
example_trial_instructionsComponents = [example_trial_instruction_text, next_button_example_trial_instructions, ex_trial_inst_mouse]
for thisComponent in example_trial_instructionsComponents:
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

# --- Run Routine "example_trial_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_trial_instruction_text* updates
    if example_trial_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_trial_instruction_text.frameNStart = frameN  # exact frame index
        example_trial_instruction_text.tStart = t  # local t and not account for scr refresh
        example_trial_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_trial_instruction_text, 'tStartRefresh')  # time at next scr refresh
        example_trial_instruction_text.setAutoDraw(True)
    
    # *next_button_example_trial_instructions* updates
    if next_button_example_trial_instructions.status == NOT_STARTED and tThisFlip >= 0.01-frameTolerance:
        # keep track of start time/frame for later
        next_button_example_trial_instructions.frameNStart = frameN  # exact frame index
        next_button_example_trial_instructions.tStart = t  # local t and not account for scr refresh
        next_button_example_trial_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_button_example_trial_instructions, 'tStartRefresh')  # time at next scr refresh
        next_button_example_trial_instructions.setAutoDraw(True)
    if next_button_example_trial_instructions.status == STARTED:
        # check whether next_button_example_trial_instructions has been pressed
        if next_button_example_trial_instructions.isClicked:
            if not next_button_example_trial_instructions.wasClicked:
                next_button_example_trial_instructions.timesOn.append(next_button_example_trial_instructions.buttonClock.getTime()) # store time of first click
                next_button_example_trial_instructions.timesOff.append(next_button_example_trial_instructions.buttonClock.getTime()) # store time clicked until
            else:
                next_button_example_trial_instructions.timesOff[-1] = next_button_example_trial_instructions.buttonClock.getTime() # update time clicked until
            if not next_button_example_trial_instructions.wasClicked:
                if ability_to_click_next == True: 
                 continueRoutine = False
            next_button_example_trial_instructions.wasClicked = True  # if next_button_example_trial_instructions is still clicked next frame, it is not a new click
        else:
            next_button_example_trial_instructions.wasClicked = False  # if next_button_example_trial_instructions is clicked next frame, it is a new click
    else:
        next_button_example_trial_instructions.wasClicked = False  # if next_button_example_trial_instructions is clicked next frame, it is a new click
    # Run 'Each Frame' code from ex_trial_inst_code
    if ex_trial_inst_mouse.getPressed()[0] == 0:
        next_button_example_trial_instructions.fillColor = (0.12, 0.45, -0.14)
        next_button_example_trial_instructions.updateColors()
        ability_to_click_next = True
    # *ex_trial_inst_mouse* updates
    if ex_trial_inst_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ex_trial_inst_mouse.frameNStart = frameN  # exact frame index
        ex_trial_inst_mouse.tStart = t  # local t and not account for scr refresh
        ex_trial_inst_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ex_trial_inst_mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('ex_trial_inst_mouse.started', t)
        ex_trial_inst_mouse.status = STARTED
        ex_trial_inst_mouse.mouseClock.reset()
        prevButtonState = ex_trial_inst_mouse.getPressed()  # if button is down already this ISN'T a new click
    if ex_trial_inst_mouse.status == STARTED:  # only update if started and not finished!
        buttons = ex_trial_inst_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = ex_trial_inst_mouse.getPos()
                ex_trial_inst_mouse.x.append(x)
                ex_trial_inst_mouse.y.append(y)
                buttons = ex_trial_inst_mouse.getPressed()
                ex_trial_inst_mouse.leftButton.append(buttons[0])
                ex_trial_inst_mouse.midButton.append(buttons[1])
                ex_trial_inst_mouse.rightButton.append(buttons[2])
                ex_trial_inst_mouse.time.append(ex_trial_inst_mouse.mouseClock.getTime())
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_trial_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "example_trial_instructions" ---
for thisComponent in example_trial_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('next_button_example_trial_instructions.numClicks', next_button_example_trial_instructions.numClicks)
if next_button_example_trial_instructions.numClicks:
   thisExp.addData('next_button_example_trial_instructions.timesOn', next_button_example_trial_instructions.timesOn)
   thisExp.addData('next_button_example_trial_instructions.timesOff', next_button_example_trial_instructions.timesOff)
else:
   thisExp.addData('next_button_example_trial_instructions.timesOn', "")
   thisExp.addData('next_button_example_trial_instructions.timesOff', "")
# store data for thisExp (ExperimentHandler)
thisExp.addData('ex_trial_inst_mouse.x', ex_trial_inst_mouse.x)
thisExp.addData('ex_trial_inst_mouse.y', ex_trial_inst_mouse.y)
thisExp.addData('ex_trial_inst_mouse.leftButton', ex_trial_inst_mouse.leftButton)
thisExp.addData('ex_trial_inst_mouse.midButton', ex_trial_inst_mouse.midButton)
thisExp.addData('ex_trial_inst_mouse.rightButton', ex_trial_inst_mouse.rightButton)
thisExp.addData('ex_trial_inst_mouse.time', ex_trial_inst_mouse.time)
thisExp.nextEntry()
# the Routine "example_trial_instructions" was not non-slip safe, so reset the non-slip timer
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
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
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

# --- Prepare to start Routine "example_trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
radio_left_ex.reset()
radio_right_ex.reset()
# Run 'Begin Routine' code from nextbutton_trials_code_ex
next_button_clicked = False

next_button_trials_ex.fillColor = (0.55, 0.55, 0.55)
next_button_trials_ex.updateColors()
wordtype_var_text_ex.reset()
wordtype_var_text_ex.setText('woorden')
association_var_text_ex.reset()
association_var_text_ex.setText('kwaadaardigheid')
minst_text_ex.reset()
meest_text_ex.reset()
word1_var_text_ex.setText('oorlog')
word2_var_text_ex.setText('boterham')
word3_var_text_ex.setText('vrede')
word4_var_text_ex.setText('straatlantaarn')
# keep track of which components have finished
example_trialComponents = [radio_left_ex, radio_right_ex, next_button_trials_ex, instruction_text_ex, wordtype_var_text_ex, association_var_text_ex, line_below_ex, line_above_ex, line_above_2_ex, line_above_3_ex, line_above_4_ex, minst_text_ex, meest_text_ex, word1_var_text_ex, word2_var_text_ex, word3_var_text_ex, word4_var_text_ex]
for thisComponent in example_trialComponents:
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

# --- Run Routine "example_trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *radio_left_ex* updates
    if radio_left_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        radio_left_ex.frameNStart = frameN  # exact frame index
        radio_left_ex.tStart = t  # local t and not account for scr refresh
        radio_left_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radio_left_ex, 'tStartRefresh')  # time at next scr refresh
        radio_left_ex.setAutoDraw(True)
    
    # *radio_right_ex* updates
    if radio_right_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        radio_right_ex.frameNStart = frameN  # exact frame index
        radio_right_ex.tStart = t  # local t and not account for scr refresh
        radio_right_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radio_right_ex, 'tStartRefresh')  # time at next scr refresh
        radio_right_ex.setAutoDraw(True)
    # Run 'Each Frame' code from linking_sliders_code_ex
    left_slider_choice = radio_left_ex.getRating()
    right_slider_choice = radio_right_ex.getRating()
    
    if len(radio_left_ex.getHistory()) > 0 and len(radio_right_ex.getHistory()) > 0:
        left_last_choice_time = radio_left_ex.getHistory()[-1][1]
        right_last_choice_time = radio_right_ex.getHistory()[-1][1]
    
        if left_slider_choice == right_slider_choice:
            # check whether right radio was interacted with last
            if right_last_choice_time > left_last_choice_time:
                radio_left_ex.reset()
                radio_right_ex.reset()
                radio_right_ex.recordRating(right_slider_choice)
            else:
                radio_right_ex.reset()
                radio_left_ex.reset()
                radio_left_ex.recordRating(left_slider_choice)
    
    # *next_button_trials_ex* updates
    if next_button_trials_ex.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        next_button_trials_ex.frameNStart = frameN  # exact frame index
        next_button_trials_ex.tStart = t  # local t and not account for scr refresh
        next_button_trials_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_button_trials_ex, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'next_button_trials_ex.started')
        next_button_trials_ex.setAutoDraw(True)
    if next_button_trials_ex.status == STARTED:
        # check whether next_button_trials_ex has been pressed
        if next_button_trials_ex.isClicked:
            if not next_button_trials_ex.wasClicked:
                next_button_trials_ex.timesOn.append(next_button_trials_ex.buttonClock.getTime()) # store time of first click
                next_button_trials_ex.timesOff.append(next_button_trials_ex.buttonClock.getTime()) # store time clicked until
            else:
                next_button_trials_ex.timesOff[-1] = next_button_trials_ex.buttonClock.getTime() # update time clicked until
            if not next_button_trials_ex.wasClicked:
                if radio_right_ex.getRating() and radio_left_ex.getRating():
                     next_button_clicked = True
            next_button_trials_ex.wasClicked = True  # if next_button_trials_ex is still clicked next frame, it is not a new click
        else:
            next_button_trials_ex.wasClicked = False  # if next_button_trials_ex is clicked next frame, it is a new click
    else:
        next_button_trials_ex.wasClicked = False  # if next_button_trials_ex is clicked next frame, it is a new click
    # Run 'Each Frame' code from nextbutton_trials_code_ex
    # make button standard color be grey, turn green 
    # when both radio buttons have an answer
    
    if radio_right_ex.getRating() and radio_left_ex.getRating():
        next_button_trials_ex.fillColor = (0.12, 0.45, -0.14)
        next_button_trials_ex.updateColors()
        if next_button_clicked == True:
            continueRoutine = False
        else:
            pass
    else:
        next_button_trials_ex.fillColor = (0.55, 0.55, 0.55)
        next_button_trials_ex.updateColors()
    
    # *instruction_text_ex* updates
    if instruction_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_ex.frameNStart = frameN  # exact frame index
        instruction_text_ex.tStart = t  # local t and not account for scr refresh
        instruction_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_ex, 'tStartRefresh')  # time at next scr refresh
        instruction_text_ex.setAutoDraw(True)
    
    # *wordtype_var_text_ex* updates
    if wordtype_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wordtype_var_text_ex.frameNStart = frameN  # exact frame index
        wordtype_var_text_ex.tStart = t  # local t and not account for scr refresh
        wordtype_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wordtype_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        wordtype_var_text_ex.setAutoDraw(True)
    
    # *association_var_text_ex* updates
    if association_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        association_var_text_ex.frameNStart = frameN  # exact frame index
        association_var_text_ex.tStart = t  # local t and not account for scr refresh
        association_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(association_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        association_var_text_ex.setAutoDraw(True)
    
    # *line_below_ex* updates
    if line_below_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line_below_ex.frameNStart = frameN  # exact frame index
        line_below_ex.tStart = t  # local t and not account for scr refresh
        line_below_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line_below_ex, 'tStartRefresh')  # time at next scr refresh
        line_below_ex.setAutoDraw(True)
    
    # *line_above_ex* updates
    if line_above_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line_above_ex.frameNStart = frameN  # exact frame index
        line_above_ex.tStart = t  # local t and not account for scr refresh
        line_above_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line_above_ex, 'tStartRefresh')  # time at next scr refresh
        line_above_ex.setAutoDraw(True)
    
    # *line_above_2_ex* updates
    if line_above_2_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line_above_2_ex.frameNStart = frameN  # exact frame index
        line_above_2_ex.tStart = t  # local t and not account for scr refresh
        line_above_2_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line_above_2_ex, 'tStartRefresh')  # time at next scr refresh
        line_above_2_ex.setAutoDraw(True)
    
    # *line_above_3_ex* updates
    if line_above_3_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line_above_3_ex.frameNStart = frameN  # exact frame index
        line_above_3_ex.tStart = t  # local t and not account for scr refresh
        line_above_3_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line_above_3_ex, 'tStartRefresh')  # time at next scr refresh
        line_above_3_ex.setAutoDraw(True)
    
    # *line_above_4_ex* updates
    if line_above_4_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line_above_4_ex.frameNStart = frameN  # exact frame index
        line_above_4_ex.tStart = t  # local t and not account for scr refresh
        line_above_4_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line_above_4_ex, 'tStartRefresh')  # time at next scr refresh
        line_above_4_ex.setAutoDraw(True)
    
    # *minst_text_ex* updates
    if minst_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        minst_text_ex.frameNStart = frameN  # exact frame index
        minst_text_ex.tStart = t  # local t and not account for scr refresh
        minst_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(minst_text_ex, 'tStartRefresh')  # time at next scr refresh
        minst_text_ex.setAutoDraw(True)
    
    # *meest_text_ex* updates
    if meest_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        meest_text_ex.frameNStart = frameN  # exact frame index
        meest_text_ex.tStart = t  # local t and not account for scr refresh
        meest_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(meest_text_ex, 'tStartRefresh')  # time at next scr refresh
        meest_text_ex.setAutoDraw(True)
    
    # *word1_var_text_ex* updates
    if word1_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word1_var_text_ex.frameNStart = frameN  # exact frame index
        word1_var_text_ex.tStart = t  # local t and not account for scr refresh
        word1_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word1_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        word1_var_text_ex.setAutoDraw(True)
    
    # *word2_var_text_ex* updates
    if word2_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word2_var_text_ex.frameNStart = frameN  # exact frame index
        word2_var_text_ex.tStart = t  # local t and not account for scr refresh
        word2_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word2_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        word2_var_text_ex.setAutoDraw(True)
    
    # *word3_var_text_ex* updates
    if word3_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word3_var_text_ex.frameNStart = frameN  # exact frame index
        word3_var_text_ex.tStart = t  # local t and not account for scr refresh
        word3_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word3_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        word3_var_text_ex.setAutoDraw(True)
    
    # *word4_var_text_ex* updates
    if word4_var_text_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word4_var_text_ex.frameNStart = frameN  # exact frame index
        word4_var_text_ex.tStart = t  # local t and not account for scr refresh
        word4_var_text_ex.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word4_var_text_ex, 'tStartRefresh')  # time at next scr refresh
        word4_var_text_ex.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "example_trial" ---
for thisComponent in example_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('radio_left_ex.response', radio_left_ex.getRating())
thisExp.addData('radio_right_ex.response', radio_right_ex.getRating())
thisExp.addData('next_button_trials_ex.numClicks', next_button_trials_ex.numClicks)
if next_button_trials_ex.numClicks:
   thisExp.addData('next_button_trials_ex.timesOn', next_button_trials_ex.timesOn)
   thisExp.addData('next_button_trials_ex.timesOff', next_button_trials_ex.timesOff)
else:
   thisExp.addData('next_button_trials_ex.timesOn', "")
   thisExp.addData('next_button_trials_ex.timesOff', "")
# Run 'End Routine' code from nextbutton_trials_code_ex
next_button_clicked = False

# the Routine "example_trial" was not non-slip safe, so reset the non-slip timer
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
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
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

# set up handler to look after randomisation of conditions etc
wordtype_block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pilot_trials_blocks.xlsx'),
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
        
    if selftimed_pause_mouse.getPressed()[0] == 1:
        next_button_selftimed_pause.fillColor = (0.55, 0.55, 0.55)
        next_button_selftimed_pause.updateColors()
        ability_to_click_next = False
    
    # setup some python lists for storing info about the selftimed_pause_mouse
    selftimed_pause_mouse.x = []
    selftimed_pause_mouse.y = []
    selftimed_pause_mouse.leftButton = []
    selftimed_pause_mouse.midButton = []
    selftimed_pause_mouse.rightButton = []
    selftimed_pause_mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    selftimed_pauseComponents = [selftimed_pause_text, next_button_selftimed_pause, selftimed_pause_mouse]
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
        # Run 'Each Frame' code from selftimed_pause_code
        if selftimed_pause_mouse.getPressed()[0] == 0:
            next_button_selftimed_pause.fillColor = (0.12, 0.45, -0.14)
            next_button_selftimed_pause.updateColors()
            ability_to_click_next = True
        
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
                if not next_button_selftimed_pause.wasClicked:
                    if ability_to_click_next == True: 
                     continueRoutine = False
                next_button_selftimed_pause.wasClicked = True  # if next_button_selftimed_pause is still clicked next frame, it is not a new click
            else:
                next_button_selftimed_pause.wasClicked = False  # if next_button_selftimed_pause is clicked next frame, it is a new click
        else:
            next_button_selftimed_pause.wasClicked = False  # if next_button_selftimed_pause is clicked next frame, it is a new click
        # *selftimed_pause_mouse* updates
        if selftimed_pause_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            selftimed_pause_mouse.frameNStart = frameN  # exact frame index
            selftimed_pause_mouse.tStart = t  # local t and not account for scr refresh
            selftimed_pause_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(selftimed_pause_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('selftimed_pause_mouse.started', t)
            selftimed_pause_mouse.status = STARTED
            selftimed_pause_mouse.mouseClock.reset()
            prevButtonState = selftimed_pause_mouse.getPressed()  # if button is down already this ISN'T a new click
        if selftimed_pause_mouse.status == STARTED:  # only update if started and not finished!
            buttons = selftimed_pause_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = selftimed_pause_mouse.getPos()
                    selftimed_pause_mouse.x.append(x)
                    selftimed_pause_mouse.y.append(y)
                    buttons = selftimed_pause_mouse.getPressed()
                    selftimed_pause_mouse.leftButton.append(buttons[0])
                    selftimed_pause_mouse.midButton.append(buttons[1])
                    selftimed_pause_mouse.rightButton.append(buttons[2])
                    selftimed_pause_mouse.time.append(selftimed_pause_mouse.mouseClock.getTime())
        
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
    # store data for wordtype_block (TrialHandler)
    wordtype_block.addData('selftimed_pause_mouse.x', selftimed_pause_mouse.x)
    wordtype_block.addData('selftimed_pause_mouse.y', selftimed_pause_mouse.y)
    wordtype_block.addData('selftimed_pause_mouse.leftButton', selftimed_pause_mouse.leftButton)
    wordtype_block.addData('selftimed_pause_mouse.midButton', selftimed_pause_mouse.midButton)
    wordtype_block.addData('selftimed_pause_mouse.rightButton', selftimed_pause_mouse.rightButton)
    wordtype_block.addData('selftimed_pause_mouse.time', selftimed_pause_mouse.time)
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
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
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
    # setup some python lists for storing info about the block_instr_mouse
    block_instr_mouse.x = []
    block_instr_mouse.y = []
    block_instr_mouse.leftButton = []
    block_instr_mouse.midButton = []
    block_instr_mouse.rightButton = []
    block_instr_mouse.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from block_instr_code
    if block_instr_mouse.getPressed()[0] == 1:
        next_button_block_instructions.fillColor = (0.55, 0.55, 0.55)
        next_button_block_instructions.updateColors()
        ability_to_click_next = False
    
    # keep track of which components have finished
    block_instructionsComponents = [block_instruction_text, next_button_block_instructions, wordtype_textbox_instruction_block_1, wordtype_textbox_instruction_block_2, block_instr_mouse]
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
                    if ability_to_click_next == True: 
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
        # *block_instr_mouse* updates
        if block_instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_instr_mouse.frameNStart = frameN  # exact frame index
            block_instr_mouse.tStart = t  # local t and not account for scr refresh
            block_instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_instr_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('block_instr_mouse.started', t)
            block_instr_mouse.status = STARTED
            block_instr_mouse.mouseClock.reset()
            prevButtonState = block_instr_mouse.getPressed()  # if button is down already this ISN'T a new click
        if block_instr_mouse.status == STARTED:  # only update if started and not finished!
            buttons = block_instr_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = block_instr_mouse.getPos()
                    block_instr_mouse.x.append(x)
                    block_instr_mouse.y.append(y)
                    buttons = block_instr_mouse.getPressed()
                    block_instr_mouse.leftButton.append(buttons[0])
                    block_instr_mouse.midButton.append(buttons[1])
                    block_instr_mouse.rightButton.append(buttons[2])
                    block_instr_mouse.time.append(block_instr_mouse.mouseClock.getTime())
        # Run 'Each Frame' code from block_instr_code
        if block_instr_mouse.getPressed()[0] == 0:
            next_button_block_instructions.fillColor = (0.12, 0.45, -0.14)
            next_button_block_instructions.updateColors()
            ability_to_click_next = True
        
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
    # store data for wordtype_block (TrialHandler)
    wordtype_block.addData('block_instr_mouse.x', block_instr_mouse.x)
    wordtype_block.addData('block_instr_mouse.y', block_instr_mouse.y)
    wordtype_block.addData('block_instr_mouse.leftButton', block_instr_mouse.leftButton)
    wordtype_block.addData('block_instr_mouse.midButton', block_instr_mouse.midButton)
    wordtype_block.addData('block_instr_mouse.rightButton', block_instr_mouse.rightButton)
    wordtype_block.addData('block_instr_mouse.time', block_instr_mouse.time)
    # the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    within_block_trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blocks, selection=trial_rows),
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
        word1_var_text.setText(option1)
        word2_var_text.setText(option2)
        word3_var_text.setText(option3)
        word4_var_text.setText(option4)
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
                    if not next_button_trials.wasClicked:
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
        
        # Run 'End Routine' code from saving_variables_code
        # creating a word list with the four trial words
        word_list = [option1, option2, option3, option4]
        
        # acquiring the best and worst words using the 
        # ratings from the radio buttons (-1 because the
        # radio buttons count from 1)
        worst = word_list[int(radio_left.getRating() - 1)]
        best = word_list[int(radio_right.getRating() - 1)]
        
        # add data to the excel sheet
        thisExp.addData('worst', worst)
        thisExp.addData('best', best)
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
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
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
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
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


# --- Prepare to start Routine "thanks_and_bye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the thanks_bye_mouse
thanks_bye_mouse.x = []
thanks_bye_mouse.y = []
thanks_bye_mouse.leftButton = []
thanks_bye_mouse.midButton = []
thanks_bye_mouse.rightButton = []
thanks_bye_mouse.time = []
gotValidClick = False  # until a click is received
# Run 'Begin Routine' code from thanks_bye_code
if thanks_bye_mouse.getPressed()[0] == 1:
    finish_button.fillColor = (0.55, 0.55, 0.55)
    finish_button.updateColors()
    ability_to_click_next = False

# keep track of which components have finished
thanks_and_byeComponents = [thanks_and_bye_text, finish_button, thanks_bye_mouse]
for thisComponent in thanks_and_byeComponents:
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

# --- Run Routine "thanks_and_bye" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_and_bye_text* updates
    if thanks_and_bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_and_bye_text.frameNStart = frameN  # exact frame index
        thanks_and_bye_text.tStart = t  # local t and not account for scr refresh
        thanks_and_bye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_and_bye_text, 'tStartRefresh')  # time at next scr refresh
        thanks_and_bye_text.setAutoDraw(True)
    
    # *finish_button* updates
    if finish_button.status == NOT_STARTED and tThisFlip >= 0.01-frameTolerance:
        # keep track of start time/frame for later
        finish_button.frameNStart = frameN  # exact frame index
        finish_button.tStart = t  # local t and not account for scr refresh
        finish_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_button, 'tStartRefresh')  # time at next scr refresh
        finish_button.setAutoDraw(True)
    if finish_button.status == STARTED:
        # check whether finish_button has been pressed
        if finish_button.isClicked:
            if not finish_button.wasClicked:
                finish_button.timesOn.append(finish_button.buttonClock.getTime()) # store time of first click
                finish_button.timesOff.append(finish_button.buttonClock.getTime()) # store time clicked until
            else:
                finish_button.timesOff[-1] = finish_button.buttonClock.getTime() # update time clicked until
            if ability_to_click_next == True: 
             continueRoutine = False
            finish_button.wasClicked = True  # if finish_button is still clicked next frame, it is not a new click
        else:
            finish_button.wasClicked = False  # if finish_button is clicked next frame, it is a new click
    else:
        finish_button.wasClicked = False  # if finish_button is clicked next frame, it is a new click
    # *thanks_bye_mouse* updates
    if thanks_bye_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_bye_mouse.frameNStart = frameN  # exact frame index
        thanks_bye_mouse.tStart = t  # local t and not account for scr refresh
        thanks_bye_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_bye_mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('thanks_bye_mouse.started', t)
        thanks_bye_mouse.status = STARTED
        thanks_bye_mouse.mouseClock.reset()
        prevButtonState = thanks_bye_mouse.getPressed()  # if button is down already this ISN'T a new click
    if thanks_bye_mouse.status == STARTED:  # only update if started and not finished!
        buttons = thanks_bye_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = thanks_bye_mouse.getPos()
                thanks_bye_mouse.x.append(x)
                thanks_bye_mouse.y.append(y)
                buttons = thanks_bye_mouse.getPressed()
                thanks_bye_mouse.leftButton.append(buttons[0])
                thanks_bye_mouse.midButton.append(buttons[1])
                thanks_bye_mouse.rightButton.append(buttons[2])
                thanks_bye_mouse.time.append(thanks_bye_mouse.mouseClock.getTime())
    # Run 'Each Frame' code from thanks_bye_code
    if thanks_bye_mouse.getPressed()[0] == 0:
        finish_button.fillColor = (0.12, 0.45, -0.14)
        finish_button.updateColors()
        ability_to_click_next = True
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanks_and_byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks_and_bye" ---
for thisComponent in thanks_and_byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finish_button.numClicks', finish_button.numClicks)
if finish_button.numClicks:
   thisExp.addData('finish_button.timesOn', finish_button.timesOn)
   thisExp.addData('finish_button.timesOff', finish_button.timesOff)
else:
   thisExp.addData('finish_button.timesOn', "")
   thisExp.addData('finish_button.timesOff', "")
# store data for thisExp (ExperimentHandler)
thisExp.addData('thanks_bye_mouse.x', thanks_bye_mouse.x)
thisExp.addData('thanks_bye_mouse.y', thanks_bye_mouse.y)
thisExp.addData('thanks_bye_mouse.leftButton', thanks_bye_mouse.leftButton)
thisExp.addData('thanks_bye_mouse.midButton', thanks_bye_mouse.midButton)
thisExp.addData('thanks_bye_mouse.rightButton', thanks_bye_mouse.rightButton)
thisExp.addData('thanks_bye_mouse.time', thanks_bye_mouse.time)
thisExp.nextEntry()
# the Routine "thanks_and_bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
