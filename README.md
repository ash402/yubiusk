# yubiusk

>Where is Yu'biusk?
>>*Yu'biusk is far away. Beyond the icelands to the north, beyond the mountains to the west, beyond the oceans to the south and the deserts to the east. But it is also close. Wherever goblins fight in the name of the Big High War God and their blood spills on the ground, Yu'biusk is close. My predecessor told me that no living goblin has ever gone to Yu'biusk. If no living goblin can go there, then perhaps the dead can.*

>What's it like being dead?
>>*I had thought perhaps I would go to Yu'biusk, to fight in endless battles for the Big High War God. Instead, there is only endless sleep...good luck in your quest, human.*

**Yubiusk** is a program for converting a Kismet [JSORK](https://github.com/kenwalker/jsork) citizens report into a human-readable summary of citizens and near-citizens. Currently, this only functions for chapters within the Kingdom of the Rising Winds, using the "Rising Winds Voting" [report](https://kenwalker.github.io/jsork/rwVoting.html) "Copy to CSV" text output.

### Inputs:
JSORK citizen report (text file)

### Outputs:
List of citizens
List of players who are nearly citizens
* Players who meet attendance and time-in-game requirements, but not dues and waiver
* Players who meet all requirements except time-in-game
* Players who meet attendance requirements, but not time-in-game nor dues and waiver

## Example usage
You should have python3 installed. I happen to be using Python 3.10.7 right now.

1. Go to JSORK and run a citizens list for your park
2. Click "Copy to CSV" and paste the text into notepad. Save the file with a name you will remember in the same directory as this program.
3. Open the command prompt and navigate to the base directory.
4. Run the program from the command line, i.e. `python3 cit.py -i report.jsork -o details.txt`
5. Open file explorer, navigate to the base directory, and click on `details.txt` to read it.

### Arguments
| Argument | Meaning |
| ------------- |:-------------:|
| -i    | Input file name     |
| -o    | Output file name     |
| -v    | Verbose output (print to screen)|

Example: `python3 cit.py -i report.jsork -o details.txt` will parse data from the file `report.jsork` to a new file `details.txt` without printing verbose information to the screen.

## Planned Future Features
* GUI
* Compiled executable
* Multikingdom support

## Unlikely Features
* Direct JSORK API access (I do not know JS)

#### What is Yu'Biusk?
Yu'Biusk is the ancestral land of the of goblins, where they lived before the Big High War God brought them to Gielinor to make war on the other Gods. One day, **citizens** of all twelve **goblin** tribes might return to live in peace in Yu'Biusk.