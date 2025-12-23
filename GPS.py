initialstate=["red disk on pole","blue disk on pole","green disk on pole","green disk on top"]
finalstate=["green disk on pole","blue disk on pole","red disk on pole","red disk on top"]
disk_ops=[
    {
        "action":"Move geen disk from pole to table",
        "preconds":["green disk on pole","green disk on top"],
        "add":["green disk on table"],
        "delete":["green disk on pole"]
    },
    {
        "action": "Move blue disk from pole to green disk",
        "preconds": ["blue disk on pole", "green disk on table"],
        "add": ["disk disk on green disk"],
        "delete": ["blue disk on pole"]
    },
    {
        "action": "Move red disk from pole to blue disk",
        "preconds": ["red disk on pole", "blue disk on green disk"],
        "add": ["red disk on blue disk","red disk on top"],
        "delete": ["red disk on pole"]
    }


]

