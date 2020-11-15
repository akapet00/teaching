*version 9.1 1226798632
u 42
T? 2
V? 4
U? 2
R? 3
? 4
@libraries
@analysis
.TRAN 1 0 0 0
+0 0s
+1 500e-6s
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
pageloc 1 0 2709 
@status
n 0 117:11:19:14:12:29;1513689149 e 
s 2832 118:11:07:10:30:14;1544175014 e 
*page 1 0 970 720 iA
@ports
port 39 GND_ANALOG 570 190 h
port 41 GND_ANALOG 740 180 h
@parts
part 5 Sw_tClose 580 130 h
a 0 sp 0 0 0 24 hln 100 PART=Sw_tClose
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 0 20 hln 100 REFDES=U1
part 7 r 540 140 h
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R2
a 0 ap 9 0 15 0 hln 100 REFDES=R2
a 0 u 13 0 15 25 hln 100 VALUE=10
part 6 r 760 180 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
a 0 u 13 0 15 25 hln 100 VALUE=500
part 8 VDC 520 150 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V3
a 1 ap 9 0 24 7 hcn 100 REFDES=V3
a 1 u 13 0 -11 18 hcn 100 DC=10V
part 2 T 640 160 h
a 0 sp 0 0 0 10 hlb 100 PART=T
a 0 a 0:13 0 0 0 hln 100 PKGREF=T1
a 0 ap 9 0 20 10 hln 100 REFDES=T1
a 0 u 0 0 0 0 hln 100 TD=10e-6
a 0 u 0 0 0 0 hln 100 Z0=100
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 32 nodeMarker 540 140 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 33 nodeMarker 640 140 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 34 nodeMarker 760 140 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
@conn
w 10
a 0 up 0:33 0 0 0 hln 100 V=
s 520 140 540 140 9
a 0 up 33 0 530 139 hct 100 V=
s 520 150 520 140 11
w 14
a 0 up 0:33 0 0 0 hln 100 V=
s 640 140 620 140 15
s 640 160 640 140 13
a 0 up 33 0 642 150 hlt 100 V=
w 18
a 0 up 0:33 0 0 0 hln 100 V=
s 760 140 740 140 17
s 740 140 740 160 19
a 0 up 33 0 742 150 hlt 100 V=
w 26
a 0 up 0:33 0 0 0 hln 100 V=
s 640 190 570 190 27
a 0 up 33 0 580 189 hct 100 V=
s 640 180 640 190 25
s 570 190 520 190 40
w 22
a 0 up 0:33 0 0 0 hln 100 V=
s 740 180 760 180 23
a 0 up 33 0 750 179 hct 100 V=
@junction
j 580 140
+ p 7 2
+ p 5 1
j 760 140
+ p 6 2
+ w 18
j 760 180
+ p 6 1
+ w 22
j 520 190
+ p 8 -
+ w 26
j 740 180
+ p 2 B-
+ w 22
j 740 160
+ p 2 B+
+ w 18
j 640 180
+ p 2 A-
+ w 26
j 540 140
+ p 7 1
+ w 10
j 520 150
+ p 8 +
+ w 10
j 540 140
+ p 32 pin1
+ p 7 1
j 540 140
+ p 32 pin1
+ w 10
j 760 140
+ p 34 pin1
+ p 6 2
j 760 140
+ p 34 pin1
+ w 18
j 570 190
+ s 39
+ w 26
j 740 180
+ s 41
+ p 2 B-
j 740 180
+ s 41
+ w 22
j 620 140
+ p 5 2
+ w 14
j 640 160
+ p 2 A+
+ w 14
j 640 140
+ p 33 pin1
+ w 14
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
