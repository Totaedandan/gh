from scamp import *

s = Session()

piano = s.new_part("piano")

pitches = [64, 65, 67, 69, 71, 69, 67, 65]

while True:
    for pitch in pitches:
        piano.play_note(pitch, 1.5, 0.2 )

#for char in text:
#    if char == " ":
#        wait(0.2)
#    elif char.isalnum():
#        piano.play_note(ord(char) - 20, 0.5, 0.06)
#    else:
#        wait(0.2)
#        piano.play_note(ord(char), 0.8, 0.06)
#        wait(0.2)