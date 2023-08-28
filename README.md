# td_recorda
A TouchDesigner-based production tool for real-time video / LTC striping, burn-in, and recording.  **Recorda** records video, audio, and LTC and supports striping of production audio with LTC and LTC burn-in.  Files are encoded in real-time to lightweight H.265 files for archive or production needs.

# Hardware
**Recorda** expects 3 audio channels embedded on the video input:
1. PGM audio Left
2. PGM audio Right
3. LTC

Analog LTC can be embedded into SDI with the Blackmagic Design Audio -> SDI Mini Converter.

Blackmagic Design video capture and playback hardware is required.  This has been tested on a Decklink 8K Pro and Ultrastudio Mini 4K.  Playback support is optional and only required when an output with LTC burn-in is desired.  

# Menus
## Operation
All functions necessary for production operation are on this page.
### Record
Toggles on and off.  Recording will continue as long as the button is left on.  In on state the button will turn red and a red border will appear around the viewer window.
### Snapshot
Take a single frame capture of the current frame and saves to output folder.  The snapshot does not include LTC or TOD burn-in.
### Description
User input field for the description of the current recording.  Example: 'Rehearsal', 'Test', etc.
### Angle
The camera angle being recorded.  The default value is 'PGM' as this system typically only records the PGM feed.
### Take
The current take.  This value automatically upticks every time a recording is finished.
### Take+
Increases the take counter by 1
### Take-
Decreases the take counter by 1
### Take Reset
Resets the take counter to 1

## Project
This page contains all project-level settings.
### Project Name
The project name for file naming purposes.
### Record Location
The directory where files will be saved.  It is recommended to leave this at the default value (the 'capture' folder in project directory.)
### Save Project
Press to save the current project configuration.

## Input
This page contains all **Input** settings.
### Video Input Device
Select the video input device to use for the input feed.
### Audio Input Device
Select the audio input device to use for the input feed.  This is usually the same device as the Video Input Device.
### LTC Source
Choose between LTC input and generated LTC.  LTC generation starts at project launch and is mostly useful for test recordings or output.
### Legalize
This parameter has 3 modes related to video signal legalization.  User can set a full-to-limited or limited-to-full LUT or bypass legalization.
### Poll Input Devices
When clicked this button will regenerate the menu options for video and audio input devices.  Press this whenever you experience a hardware change.

## Output
This page contains all **Output** settings.
### Bars and Tone
Generates SMPTE bars and 440Hz tone in left and right audio channels.  Useful for testing and proving signal paths.
### Audio Mix
Choose between clean PGM feed and PGM / LTC stripe mix for recordings / output.
### Audio Output Level
Adjust the audio output gain.
### Audio Monitor
Enable or disable the audio monitor.  The audio monitor defaults to the system default audio output device.
### Audio Monitor Level
Adjust the audio monitor gain.
### Video Output
Enable or disable the live video output with LTC burn-in.
### Video Output Device
Select the video output device to use for the output feed.
### Signal Format
Select the signal format for video output.  This is typically 1920x1080.
### Poll Output Devices
When clicked this button will regenerate the menu options for video and audio output devices.  Press this whenever you experience a hardware change.
