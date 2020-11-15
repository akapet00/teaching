*version 9.1 921504380
u 42
V? 2
L? 3
R? 4
? 2
C? 3
@libraries
@analysis
.AC 1 3 0
+0 101
+1 10
+2 100.00K
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
pageloc 1 0 2442 
@status
n 0 119:00:18:09:13:47;1547799227 e 
s 2832 119:11:04:10:28:08;1575451688 e 
*page 1 0 970 720 iA
@ports
port 5 GND_ANALOG 160 290 h
@parts
part 2 VAC 160 240 h
a 0 sp 0 0 0 50 hln 100 PART=VAC
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 20 10 hcn 100 REFDES=V1
a 0 u 13 0 -9 23 hcn 100 ACMAG=1V
part 21 c 280 260 v
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C1
a 0 ap 9 0 15 0 hln 100 REFDES=C1
a 0 u 13 0 15 25 hln 100 VALUE=560p
part 22 c 310 210 h
a 0 sp 0 0 0 10 hlb 100 PART=c
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=CK05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=C2
a 0 ap 9 0 15 0 hln 100 REFDES=C2
a 0 u 13 0 15 25 hln 100 VALUE=15n
part 23 r 360 270 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R2
a 0 ap 9 0 15 0 hln 100 REFDES=R2
a 0 u 13 0 15 25 hln 100 VALUE=10k
part 24 r 190 210 h
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R3
a 0 ap 9 0 15 0 hln 100 REFDES=R3
a 0 u 13 0 15 25 hln 100 VALUE=10k
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 20 nodeMarker 360 210 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=C1:2
a 0 a 0 0 4 22 hlb 100 LABEL=1
@conn
w 7
a 0 up 0:33 0 0 0 hln 100 V=
s 160 210 160 240 8
a 0 up 33 0 162 225 hlt 100 V=
s 190 210 160 210 25
w 11
a 0 up 0:33 0 0 0 hln 100 V=
s 160 280 160 290 10
s 280 280 160 280 18
a 0 up 33 0 220 279 hct 100 V=
s 280 280 280 260 29
s 360 280 360 270 37
s 280 280 360 280 39
w 13
a 0 up 0:33 0 0 0 hln 100 V=
s 280 210 280 230 14
s 280 210 230 210 27
a 0 up 33 0 260 209 hct 100 V=
s 310 210 280 210 31
w 34
a 0 up 0:33 0 0 0 hln 100 V=
s 360 210 360 230 33
s 340 210 360 210 35
a 0 up 33 0 350 209 hct 100 V=
@junction
j 160 240
+ p 2 +
+ w 7
j 160 280
+ p 2 -
+ w 11
j 160 290
+ s 5
+ w 11
j 280 230
+ p 21 2
+ w 13
j 190 210
+ p 24 1
+ w 7
j 230 210
+ p 24 2
+ w 13
j 280 260
+ p 21 1
+ w 11
j 310 210
+ p 22 1
+ w 13
j 360 230
+ p 23 2
+ w 34
j 340 210
+ p 22 2
+ w 34
j 360 270
+ p 23 1
+ w 11
j 280 280
+ w 11
+ w 11
j 360 210
+ p 20 pin1
+ w 34
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
