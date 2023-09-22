
keep_going = "1"

while keep_going == "1":

    # inputs
    root = input("Enter root note: ").upper()
    note2 = input("Enter second note: ").upper()
    note3 = input("Enter third note: ").upper()

    # Lists
    all_notesS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    #all_notesF = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

    # nfr = "notes from root"
    nfr = [
        root,
        all_notesS[(all_notesS.index(root) + 1) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 2) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 3) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 4) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 5) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 6) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 7) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 8) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 9) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 10) % (len(all_notesS))],
        all_notesS[(all_notesS.index(root) + 11) % (len(all_notesS))],
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
            return root + " diminished chord"
        elif nfr.index(note2) == 3 and nfr.index(note3) == 7:
            return root + " minor chord"
        else:
            return "Not recognized"

    keep_going = "1"

    # Run functions

    if root in nfr:
        print(triad_identity())
    else:
        print("Error")
        
    keep_going = input("Type 1 to run again: ")
