#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc, os, time, random, codecs

def measureTime(cmd):
    startTime, endTime = 0, 0
    gcEnabled = gc.isenabled()
    try:
        gc.disable()
        startTime = time.time()
        os.system(cmd)
        endTime = time.time()
    finally:
        if gcEnabled:
            gc.enable()
    return endTime - startTime

def measureTimes(cmds, nr):
    result = []
    toExecute = []
    for cmd in cmds:
        for i in range(nr):
            toExecute.append(cmd)
    random.shuffle(toExecute)
    for cmd in toExecute:
        time = measureTime(cmd)
        result.append((cmd, time))
    return result

def saveTime(timeMessurements, filename):
    with codecs.open(filename, "w") as outF:
        outF.write("Time\tCommand\n")
        for timeMes in timeMessurements:
            outF.write("%s\t%s\n" % (timeMes[1], timeMes[0]))

if __name__ == "__main__":
    cmds = []

    # hello world commands
    commands = [
        r"./helloworld/helloworld/HelloWorld",
        r"java -jar helloworld/helloworld.jar/HelloWorld.jar",
        r"nodejs helloworld/helloworld.js",
        r"lua helloworld/helloworld.lua",
        r"neko helloworld/helloworld.n",
        r"python3 helloworld/helloworld.py",
        r"perl helloworld/helloworld.pl",
    ]
    for cmd in commands:
        cmds.append(cmd)

    # commands for step1
    commands = [
        r"./SeqPHASE/haxe/seqphase1_dce_full/SeqPhase1",
        r"./SeqPHASE/haxe/seqphase1_dce_std/SeqPhase1",
        r"./SeqPHASE/haxe/seqphase1_dce_no/SeqPhase1",
        r"java -jar SeqPHASE/haxe/seqphase1_dce_full.jar/SeqPhase1.jar",
        r"java -jar SeqPHASE/haxe/seqphase1_dce_std.jar/SeqPhase1.jar",
        r"java -jar SeqPHASE/haxe/seqphase1_dce_no.jar/SeqPhase1.jar",
        r"nodejs SeqPHASE/haxe/seqphase1_dce_full.js",
        r"nodejs SeqPHASE/haxe/seqphase1_dce_std.js",
        r"nodejs SeqPHASE/haxe/seqphase1_dce_no.js",
        r"lua SeqPHASE/haxe/seqphase1_dce_full.lua",
        r"lua SeqPHASE/haxe/seqphase1_dce_std.lua",
        r"lua SeqPHASE/haxe/seqphase1_dce_no.lua",
        r"neko SeqPHASE/haxe/seqphase1_dce_full.n",
        r"neko SeqPHASE/haxe/seqphase1_dce_std.n",
        r"neko SeqPHASE/haxe/seqphase1_dce_no.n",
        r"python3 SeqPHASE/haxe/seqphase1_dce_full.py",
        r"python3 SeqPHASE/haxe/seqphase1_dce_std.py",
        r"python3 SeqPHASE/haxe/seqphase1_dce_no.py",
        r"perl SeqPHASE/seqphase1.pl"
    ]
    # load all step1 datassets
    step1Datasets = [f for f in os.listdir("datasets/step1")]
    for cmd in commands:
        for ds in step1Datasets:
            cmds.append("%s -1 datasets/step1/%s" % (cmd, ds))

    # commands for step2
    commands = [
        r"./SeqPHASE/haxe/seqphase2_dce_full/SeqPhase2",
        r"./SeqPHASE/haxe/seqphase2_dce_std/SeqPhase2",
        r"./SeqPHASE/haxe/seqphase2_dce_no/SeqPhase2",
        r"java -jar SeqPHASE/haxe/seqphase2_dce_full.jar/SeqPhase2.jar",
        r"java -jar SeqPHASE/haxe/seqphase2_dce_std.jar/SeqPhase2.jar",
        r"java -jar SeqPHASE/haxe/seqphase2_dce_no.jar/SeqPhase2.jar",
        r"nodejs SeqPHASE/haxe/seqphase2_dce_full.js",
        r"nodejs SeqPHASE/haxe/seqphase2_dce_std.js",
        r"nodejs SeqPHASE/haxe/seqphase2_dce_no.js",
        r"lua SeqPHASE/haxe/seqphase2_dce_full.lua",
        r"lua SeqPHASE/haxe/seqphase2_dce_std.lua",
        r"lua SeqPHASE/haxe/seqphase2_dce_no.lua",
        r"neko SeqPHASE/haxe/seqphase2_dce_full.n",
        r"neko SeqPHASE/haxe/seqphase2_dce_std.n",
        r"neko SeqPHASE/haxe/seqphase2_dce_no.n",
        r"python3 SeqPHASE/haxe/seqphase2_dce_full.py",
        r"python3 SeqPHASE/haxe/seqphase2_dce_std.py",
        r"python3 SeqPHASE/haxe/seqphase2_dce_no.py",
        r"perl SeqPHASE/seqphase2.pl"
    ]
    # load all step2 datassets
    step2Datasets = [f for f in os.listdir("datasets/step2")]
    for cmd in commands:
        for ds in step2Datasets:
            if ds.endswith(".out"):
                const = ds[:-4]
                cmds.append("%s -c %s.const -i %s" % (cmd, const, ds))

    mes = measureTimes(cmds, 5)
    saveTime(mes, "times.dat")
