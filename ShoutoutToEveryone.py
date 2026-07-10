import win32com.client as wincl

# Initialize the speaker engine
speaker = wincl.Dispatch("SAPI.SpVoice")

voices = speaker.getVoices()

voice = 1

speaker.Voice = voices.item(voice)

# 1. Create your list of names (the multiple "passages")
names = ["Harry", "Naman", "Rohan", "Sandeep", "Anjali"]

# 2. Loop through each name to deliver individual shoutouts
for name in names:
    # Construct the personal shoutout string dynamically
    shoutout = f"Shoutout to {name}"
    
    print(shoutout)        # Prints it on your console
    speaker.Speak(shoutout)  # Speaks it out loud
