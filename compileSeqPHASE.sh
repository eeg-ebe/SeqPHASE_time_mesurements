git clone https://github.com/eeg-ebe/SeqPHASE.git
cd SeqPHASE/haxe

haxe -main SeqPhase1 -dce full -cpp seqphase1_dce_full
haxe -main SeqPhase1 -dce std -cpp seqphase1_dce_std
haxe -main SeqPhase1 -dce no -cpp seqphase1_dce_no

haxe -main SeqPhase1 -dce full -lua seqphase1_dce_full.lua
haxe -main SeqPhase1 -dce std -lua seqphase1_dce_std.lua
haxe -main SeqPhase1 -dce no -lua seqphase1_dce_no.lua

haxe -main SeqPhase1 -dce full -neko seqphase1_dce_full.n
haxe -main SeqPhase1 -dce std -neko seqphase1_dce_std.n
haxe -main SeqPhase1 -dce no -neko seqphase1_dce_no.n

haxe -main SeqPhase1 -dce full -python seqphase1_dce_full.py
haxe -main SeqPhase1 -dce std -python seqphase1_dce_std.py
haxe -main SeqPhase1 -dce no -python seqphase1_dce_no.py

haxe -main SeqPhase1 -dce full -js seqphase1_dce_full.py -lib hxnodejs
haxe -main SeqPhase1 -dce std -js seqphase1_dce_std.py -lib hxnodejs
haxe -main SeqPhase1 -dce no -js seqphase1_dce_no.py -lib hxnodejs

haxe -main SeqPhase1 -dce full -java seqphase1_dce_full.jar
haxe -main SeqPhase1 -dce std -java seqphase1_dce_std.jar
haxe -main SeqPhase1 -dce no -java seqphase1_dce_no.jar


haxe -main SeqPhase2 -dce full -cpp seqphase2_dce_full
haxe -main SeqPhase2 -dce std -cpp seqphase2_dce_std
haxe -main SeqPhase2 -dce no -cpp seqphase2_dce_no

haxe -main SeqPhase2 -dce full -lua seqphase2_dce_full.lua
haxe -main SeqPhase2 -dce std -lua seqphase2_dce_std.lua
haxe -main SeqPhase2 -dce no -lua seqphase2_dce_no.lua

haxe -main SeqPhase2 -dce full -neko seqphase2_dce_full.n
haxe -main SeqPhase2 -dce std -neko seqphase2_dce_std.n
haxe -main SeqPhase2 -dce no -neko seqphase2_dce_no.n

haxe -main SeqPhase2 -dce full -python seqphase2_dce_full.py
haxe -main SeqPhase2 -dce std -python seqphase2_dce_std.py
haxe -main SeqPhase2 -dce no -python seqphase2_dce_no.py

haxe -main SeqPhase2 -dce full -js seqphase2_dce_full.py -lib hxnodejs
haxe -main SeqPhase2 -dce std -js seqphase2_dce_std.py -lib hxnodejs
haxe -main SeqPhase2 -dce no -js seqphase2_dce_no.py -lib hxnodejs

haxe -main SeqPhase2 -dce full -java seqphase2_dce_full.jar
haxe -main SeqPhase2 -dce std -java seqphase2_dce_std.jar
haxe -main SeqPhase2 -dce no -java seqphase2_dce_no.jar

