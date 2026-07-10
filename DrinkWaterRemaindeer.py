import win32com.client as wincl
import time

speaker_number = 1
message = '''hey, naman it is the time to drink water take a break and drink 1 glass of water
'''
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)

for i in range(24):
    spk.Speak(message)
    time.sleep(3600)