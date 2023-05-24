# inputs
root = input("Enter root note: ")
note2 = input("Enter second note: ")
note3 = input("Enter third note: ")

# Lists
all_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
# nfr = "notes from root"
nfr = [
    root,
    all_notes[(all_notes.index(root) + 1) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 2) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 3) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 4) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 5) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 6) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 7) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 8) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 9) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 10) % (len(all_notes))],
    all_notes[(all_notes.index(root) + 11) % (len(all_notes))],
    root]


# Functions that identify triads
def triad_identity():
    if nfr.index(note2) == 4 and nfr.index(note3) == 7:
        return root + " major chord"
    elif nfr.index(note2) == nfr.index(root) + 2 and nfr.index(note3) == nfr.index(root) + 7:
        return root + " sus2 chord"
    elif nfr.index(note2) == nfr.index(root) + 5 and nfr.index(note3) == nfr.index(root) + 7:
        return root + " sus4 chord"
    elif nfr.index(note2) == nfr.index(root) + 4 and nfr.index(note3) == nfr.index(root) + 8:
        return root + " augmented chord"
    elif nfr.index(note2) == 3 and nfr.index(note3) == 6:
        return root + " diminished triad"
    elif nfr.index(note2) == 3 and nfr.index(note3) == 7:
        return root + " minor triad"
    else:
        return "Not recognized"


# Run functions
if root in nfr:
    print(triad_identity())
else:
    print("Error")
