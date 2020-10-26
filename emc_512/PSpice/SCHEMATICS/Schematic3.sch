*version 9.1 1047460068
u 39
V? 2
R? 4
U? 2
T? 2
? 4
@libraries
@analysis
.TRAN 1 0 0 0
+0 0
+1 500e-6
+3 100ns
.OP 0 
@targets
@attributes
@translators
a 0 u 13 0 0 0 hln 100 PCBOARDS=PCB
a 0 u 13 0 0 0 hln 100 PSPICE=PSPICE
a 0 u 13 0 0 0 hln 100 XILINX=XILINX
@setup
unconnectedPins 0
connectViaLabel 0
connectViaLocalLabels 0
NoStim4ExtIFPortsWarnings 1
AutoGenStim4ExtIFPorts 1
@index
pageloc 1 0 2864 
@status
n 0 119:00:17:16:02:22;1547737342 e 
s 2832 119:00:17:16:02:25;1547737345 e 
*page 1 0 970 720 iA
@ports
port 32 GND_ANALOG 310 340 h
port 34 GND_ANALOG 500 320 h
@parts
part 7 T 380 280 h
a 0 sp 0 0 0 10 hlb 100 PART=T
a 0 a 0:13 0 0 0 hln 100 PKGREF=T1
a 0 ap 9 0 20 10 hln 100 REFDES=T1
a 0 u 0 0 0 0 hln 100 Z0=100
a 0 u 0 0 0 0 hln 100 TD=10e-6
part 2 VDC 250 280 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 24 7 hcn 100 REFDES=V1
a 1 u 13 0 -11 18 hcn 100 DC=10V
part 3 r 290 260 h
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
a 0 u 13 0 15 25 hln 100 VALUE=10
part 5 r 520 320 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R3
a 0 ap 9 0 15 0 hln 100 REFDES=R3
a 0 u 13 0 15 25 hln 100 VALUE=500
part 6 Sw_tClose 330 250 h
a 0 sp 0 0 0 24 hln 100 PART=Sw_tClose
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 0 20 hln 100 REFDES=U1
a 0 u 13 13 -2 -4 hln 100 tClose=1
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 36 nodeMarker 290 260 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 37 nodeMarker 380 260 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 38 nodeMarker 520 270 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
@conn
w 17
a 0 up 0:33 0 0 0 hln 100 V=
s 250 320 250 340 16
s 250 340 310 340 18
s 380 340 380 300 20
s 310 340 380 340 33
a 0 up 33 0 345 339 hct 100 V=
w 23
a 0 up 0:33 0 0 0 hln 100 V=
s 480 300 480 320 22
s 480 320 500 320 24
s 500 320 520 320 35
a 0 up 33 0 510 319 hct 100 V=
w 13
a 0 up 0:33 0 0 0 hln 100 V=
s 290 260 250 260 12
a 0 up 33 0 270 259 hct 100 V=
s 250 260 250 280 14
w 9
a 0 up 0:33 0 0 0 hln 100 V=
s 380 280 380 260 8
a 0 up 33 0 382 270 hlt 100 V=
s 380 260 370 260 10
w 27
a 0 up 0:33 0 0 0 hln 100 V=
s 480 280 480 270 26
s 480 270 520 270 28
a 0 up 33 0 500 269 hct 100 V=
s 520 270 520 280 30
@junction
j 330 260
+ p 6 1
+ p 3 2
j 380 280
+ p 7 A+
+ w 9
j 370 260
+ p 6 2
+ w 9
j 290 260
+ p 3 1
+ w 13
j 250 280
+ p 2 +
+ w 13
j 250 320
+ p 2 -
+ w 17
j 380 300
+ p 7 A-
+ w 17
j 480 300
+ p 7 B-
+ w 23
j 520 320
+ p 5 1
+ w 23
j 480 280
+ p 7 B+
+ w 27
j 520 280
+ p 5 2
+ w 27
j 310 340
+ s 32
+ w 17
j 500 320
+ s 34
+ w 23
j 290 260
+ p 36 pin1
+ p 3 1
j 290 260
+ p 36 pin1
+ w 13
j 380 260
+ p 37 pin1
+ w 9
j 520 270
+ p 38 pin1
+ w 27
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
