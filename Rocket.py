# Fill me in!
# use a movement to keep moving the satellite and see how it  loses it's parts
# draw black rectangle to be used in rotating of satellite
rb=Rect(196,209,10,16)

# background
Rect(0,0,400,400,fill=rgb(100,150,245))
re1=Rect(0,0,400,400,fill='black',opacity=10)
app.showLaber = False

# draw the stars that has small opacity
b=Star(200,200,4,5,fill="white",opacity=2)
b1=Star(120,210,4,5,fill="white",opacity=2)
b2=Star(180,210,4,5,fill="white",opacity=2)
b3=Star(230,310,4,5,fill="white",opacity=2)
b4=Star(257,110,4,5,fill="white",opacity=2)
b5=Star(200,210,4,5,fill="white",opacity=2)
b6=Star(100,310,4,5,fill="white",opacity=2)
b7=Star(200,80,4,5,fill="white",opacity=2)
b8=Star(305,210,4,5,fill="white",opacity=2)
b9=Star(350,210,4,5,fill="white",opacity=2)
b10=Star(210,240,4,5,fill="white",opacity=2)
b11=Star(204,20,4,5,fill="white",opacity=2)
b12=Star(120,10,4,5,fill="white",opacity=2)
b13=Star(123,230,4,5,fill="white",opacity=2)
b14=Star(34,230,4,5,fill="white",opacity=2)
b15=Star(65,230,4,5,fill="white",opacity=2)
b16=Star(100,100,4,5,fill="white",opacity=2)
b17=Star(360,30,4,5,fill="white",opacity=2)
b18=Star(23,50,4,5,fill="white",opacity=2)
b19=Star(340,230,4,5,fill="white",opacity=2)
b20=Star(12,340,4,5,fill="white",opacity=2)
b21=Star(124,360,4,5,fill="white",opacity=2)
b22=Star(110,300,4,5,fill="white",opacity=2)
b23=Star(30,350,4,5,fill="white",opacity=2)
b24=Star(350,380,4,5,fill="white",opacity=2)
b25=Star(125,390,4,5,fill="white",opacity=2)
b26=Star(10,330,4,5,fill="white",opacity=2)
b27=Star(123,-1,4,5,fill="white",opacity=2)
b28=Star(350,-1,4,5,fill="white",opacity=2)
b29=Star(10,-1,4,5,fill="white",opacity=2)
b30=Star(20,-1,4,5,fill="white",opacity=2)

# draw the Earth and its shadow with small radius
cs=Circle(5,455,55,fill="blue",opacity=50)
ca=Circle(5,450,50,fill="blue")

# draw the engine of the forth part
sh=Polygon(197,269,203,269,203,271,201,275,199,275,197,271,fill=gradient("white","grey"))
sh1=Rect(197,274,7,8,fill=gradient("orange","yellow","orange",start="left"))
sh2=Oval(200,282,6,14,fill=gradient("orange","yellow","orange",start="left"))


# draw the engine of the third stage
c1=Oval(200,318,20,7,fill=gradient(rgb(255,207,190),rgb(95,95,95),"white",start="left"))
sg=Polygon(197,320,203,320,203,326,201,330,199,330,197,326,fill=gradient("white","grey"))
sg1=Rect(196,268,8,12,fill=gradient("orange","yellow","orange",start="left"))
sg2=Oval(200,278,6,18,fill=gradient("orange","yellow","orange",start="left"))

# draw the engine of the second stage
ce=Oval(200,368,20,7,fill=gradient(rgb(255,207,190),rgb(95,95,95),"white",start="left"))
sf=Polygon(197,370,203,370,203,376,201,380,199,380,197,376,fill=gradient("white","grey"))
sf1=Rect(196,315,8,12,fill=gradient("orange","yellow","orange",start="left"))
sf2=Oval(200,324,6,18,fill=gradient("orange","yellow","orange",start="left"))


#the first part which becames the last stage of falling down and its engine showed by letter O
# first draw satellite called A as it is close
ro2=Polygon(196,249,206,249,206,257,203,260,198,260,196,257,fill="red")
ro3=Rect(199,247,4,2,fill="grey")
ro4=Oval(201,243,14,8,fill=gradient("white","grey"))
ro5=Rect(194,53,15,16,fill=gradient("grey","white",start="top"),visible=False)
# draw invisible opened satellite
lp=Line(190,210,210,205,fill="darkBlue",lineWidth=20,opacity=0)
lp4=Line(157,219,147,209,fill="white",lineWidth=1,opacity=0)
lp5=Line(157,219,147,229,fill="White",lineWidth=1,opacity=0)
lp6=Line(157,219,160,204,fill="White",lineWidth=1,opacity=0)
lp7=Line(157,219,167,229,fill="White",lineWidth=1,opacity=0)
lp8=Line(147,209,154,208,fill="white",lineWidth=1,opacity=0)
lp9=Line(160,204,154,208,fill="White",lineWidth=1,opacity=0)
lp10=Line(147,209,149,215,fill="white",lineWidth=1,opacity=0)
lp11=Line(147,229,149,215,fill="white",lineWidth=1,opacity=0)
lp12=Line(147,229,158,225,fill="white",lineWidth=1,opacity=0)
lp13=Line(167,229,158,225,fill="white",lineWidth=1,opacity=0)
cp4=Circle(158,217,9,fill=gradient("white","grey",start="left"),opacity=0)
cp3=Circle(164,217,8,fill="white",opacity=0)
cp2=Circle(167,216,8,fill="darkgray",opacity=0)
lp3=Line(160,217,157,219,fill="grey",opacity=0)
lp1=Line(190,210,163,217,fill=gradient(rgb(50,50,50),"white",start="top"),opacity=0,lineWidth=10)
lp2=Line(162,212,188,205,fill=rgb(60,60,60),opacity=0)
cp=Circle(190,210,15,fill=gradient(rgb(50,50,50),"white",start="left"),opacity=0)
cp1=Circle(198,210,3,fill=gradient("grey",'white',start="left"),opacity=0)
lp14=Line(155,221,167,216,fill="darkblue",lineWidth=15,opacity=0)
lp15=Line(155,221,167,216,fill="white",lineWidth=1,opacity=0)


# second draw it's cover and engine
p=Polygon(197,225,199,225,200,263,186,263,186,237,fill=gradient(rgb(95,95,95),"white",start="left"))
p30=Polygon(199,225,202,225,213,237,213,263,200,263,fill=gradient(rgb(95,95,95),"white",start="right"))
r=Rect(186,238,27,25,fill=gradient(rgb(95,95,95),"white",start="left"),visible=True)
co=Oval(200,263,26,7,fill=gradient(rgb(255,207,190),rgb(95,95,95),"white",start="left"))
ro=Rect(198,260,5,5,fill=rgb(50,50,50))
ro1=RegularPolygon(200,266,6,3,fill=rgb(50,50,50))
 
 #draw an invisibles rectangles,line and ovals(circles) to be apeared in last stage
pb=Polygon(194,76,197,80,200,71,198,69,fill="yellow",visible=False)
pb1=Polygon(190,66,204,68,204,74,196,74,fill=gradient("grey","white"),visible=False)
lb=Line(204,74,209,58,fill="blue",visible=False)

# rectangle that cover the satellite to make it disappeared at time
rb1=Rect(165,50,47,80,opacity=2)

# second part which will be on the third  stage
c2=Oval(200,268,27,7,fill=None,border=rgb(80,80,80),borderWidth=1)
r1=Rect(189,268,21,25,fill=gradient(rgb(40,40,40),rgb(100,50,100),start="left"))
l1=Line(208,268,209,266,fill=rgb(30,30,30),lineWidth=1)
l2=Line(193,268,190,266,fill=rgb(30,30,30),lineWidth=1)
r2=Rect(189,293,21,25,fill=gradient("grey","white",start="left"))


# third part which becames the second stage
r3=Rect(189,318,21,25,fill=gradient(rgb(40,40,40),rgb(100,50,100),start="left"))
r4=Rect(189,343,21,25,fill=gradient(rgb(255,207,190),"white",start="left"))



# the forth part which will the first stage to fall down
r5=Rect(189,368,21,25,fill=gradient(rgb(255,207,190),"white","grey",start="bottom"))
r6=Rect(189,393,21,7,fill=gradient(rgb(40,40,40),rgb(255,207,190),rgb(100,50,100),start="left"))
p26=Polygon(189,400,210,400,213,406,186,406,fill=gradient(rgb(40,40,40),rgb(255,207,190),rgb(100,50,100),start="left"))

# solid rocket boosters
# left
p1=Polygon(184,367,182,367,180,372,180,404,187,404,187,372,fill=gradient("grey",rgb(255,207,190),"white",start="left"))
p2=Polygon(189,366,187,366,184,370,184,402,191,402,191,370,fill=gradient("grey",rgb(255,207,190),"white",start="left"))

# right and center
p4=Polygon(215,367,217,367,221,372,221,403,213,403,213,372,fill=gradient("grey",rgb(255,207,190),"white",start="left"))
p3=Polygon(210,366,212,366,214,372,214,403,208,403,208,372,fill=gradient("grey",rgb(255,207,190),"white",start="left"))
p5=Polygon(199,384,201,384,203,389,203,407,199,407,197,389,fill=gradient("grey",rgb(255,207,190),"white",start="left"))

# first part(draw indian flag and its decoration after):
l6=Line(200,238,200,258,fill="White",lineWidth=1)
l7=Line(200,258,199,264,fill="white",lineWidth=1)
l8=Line(200,236,200,230,fill="white",lineWidth=1)
l3=Line(195,240,204,240,fill=rgb(212,92,17))
l4=Line(195,245,204,245,fill="blue")
c7=Circle(200,242.5,1,fill=None, border="black",borderWidth=1)
l5=Line(204,253,204,258,fill="indianred",lineWidth=6,dashes=(1,0.5))
l9=Line(196,253,190,253,fill="Salmon",lineWidth=5)
l10=Line(211,254,211,259,fill="black",lineWidth=3,dashes=(1,1))
l11=Line(197,293,197,318,fill="white",lineWidth=1)
l12=Line(197,343,197,366,fill="white",lineWidth=1)
l13=Line(187,380,187,404,dashes=(1,2))
l14=Line(212,380,212,404,dashes=(1,2))

# label the words
la=Label("P",200,298,size=6)
la1=Label("S",200,304,size=6)
la2=Label("L",200,309,size=6)
la3=Label("V",200,313,size=5)
la4=Label("c13",203,315,size=6)

# INDIA
la5=Label("I",200,347,size=8)
la6=Label("N",200,355,size=8)
la7=Label("D",200,363,size=8)
la8=Label("I",200,371,size=8)
la9=Label("A",200,379,size=8)

# draw an ingines with the with their light
# ingine of first stage
r10=Polygon(197,405,203,405,203,411,201,415,199,415,197,411,fill=gradient("white","grey"))
f=Rect(196,415,8,12,fill=gradient("orange","yellow","orange",start="left"))
sbr2=Oval(200,427,6,18,fill=gradient("orange","yellow","orange",start="left"))

#   draw smoke of first stage
s=Circle(199,415,5,fill="grey",opacity=5)
s1=Circle(199,420,5,fill="grey",opacity=5)
s2=Circle(199,430,5,fill="grey",opacity=5)
s3=Circle(200,415,5,fill="grey",opacity=5)
s4=Circle(201,410,5,fill="grey",opacity=5)
s5=Circle(198,419,5,fill="grey",opacity=5)
s6=Circle(203,423,5,fill="grey",opacity=20)
s7=Circle(1198,416,5,fill="grey",opacity=5)
s8=Circle(198,417,5,fill="grey",opacity=20)
s9=Circle(199,416,5,fill="grey",opacity=20)
s10=Circle(199,417,5,fill="grey",opacity=5)
s11=Circle(203,419,5,fill="grey",opacity=5)
s12=Circle(203,420,5,fill="grey",opacity=20)
s13=Circle(203,415,5,fill="grey",opacity=5)
s14=Circle(198,419,5,fill="grey",opacity=20)
s15=Circle(196,419,5,fill="grey",opacity=5)
s16=Circle(197,419,5,fill="grey",opacity=20)
s17=Circle(197,423,5,fill="grey",opacity=20)
s18=Circle(199,425,5,fill="grey",opacity=20)
s19=Circle(197,427,5,fill="grey",opacity=5)
s20=Circle(198,427,5,fill="grey",opacity=5)
s21=Circle(198,428,5,fill="grey",opacity=20)
s22=Circle(197,428,5,fill="grey",opacity=20)
s23=Circle(196,427,5,fill="grey",opacity=20)
s24=Circle(199,427,5,fill="grey",opacity=20)
s25=Circle(200,427,5,fill="grey",opacity=20)
s26=Circle(203,427,5,fill="grey",opacity=20)
s27=Circle(202,430,5,fill="grey",opacity=50)
#  smoke of boostes and their engines starting from left
sbl=Polygon(181,404,184,404,184,406,183,408,182,408,181,406,fill="orange")
sbl1=Polygon(185,402,188,402,188,404,187,406,186,406,185,404,fill="orange")
# smoke of boosters and their engines of right side
sbr=Polygon(210,402,213,402,213,404,212,406,211,406,210,404,fill="orange")
sbr1=Polygon(214,403,217,403,217,405,216,407,215,407,214,405,fill="orange")
# final words which will explation of teh satellite 
word=Label("satellite defination",200,420,size=20,fill="Teal")
Linedefination=Line(100,445,300,445,fill="teal")
massege1=Label("an artificial body placed in orbit around the earth or moon or",200,460,size=13,fill="grey")
massege2=Label("another planet inorder to collect information or for communication.",200,480,size=13,fill="grey")
massege3=Label(" This satellite has launched by indian.",200,495,fill="grey")
massege4=Label("The indian remote Sensing satellites(IRS)are a series of",200,530,fill="grey")
massege5=Label("Earth observation satellites,built,lounched and maintained by",200,545,fill="grey")
massege6=Label("ISRO. The IRS series provides remote sensing service to the",200,560,fill="grey")
massege7=Label("country and is the largest. collection of remote sensing",200,575,fill="grey")
massege8=Label("satellite for civilian use in operation today in the world.",200,590,fill="grey")
massege9=Label("the first country that has more number of military satellites is",200,620,fill="grey")
massege10=Label("united states.",200,635,fill="teal")
massege11=Label("from those that has the military satellite also indian is included.",200,650,fill="grey")
massege12=Label("India has launched 239 satellites for 28 different countries as of",200,665,fill="grey")
massege13=Label("October,2018. commercial lauches for foreign nations are negotiated ",200,680,fill="grey")
massege14=Label("through Antix,the commercial arm of Indian Space Research Organisation ",200,695,fill="grey")
massege15=Label("(ISRO).",200,710,size=15,fill="teal")
# creation of the helper functions
# for  smoke funtion of first stage and for first stage 
def allstageUp(d):
    r5.centerY=r5.centerY-d
    r6.centerY=r6.centerY-d
    p26.centerY=p26.centerY-d
    p1.centerY=p1.centerY-d
    p2.centerY=p2.centerY-d
    p4.centerY=p4.centerY-d
    p3.centerY=p3.centerY-d
    p5.centerY=p5.centerY-d
    l13.centerY=l13.centerY-d
    l14.centerY=l14.centerY-d
    la8.centerY=la8.centerY-d
    la9.centerY=la9.centerY-d
    r10.centerY=r10.centerY-d
    f.centerY=f.centerY-d
    s.centerY=s.centerY-d
    s1.centerY=s1.centerY-d
    s2.centerY=s2.centerY-d
    s3.centerY=s3.centerY-d
    s4.centerY=s4.centerY-d
    s5.centerY=s5.centerY-d
    s6.centerY=s6.centerY-d
    s7.centerY=s7.centerY-d
    s8.centerY=s8.centerY-d
    s9.centerY=s9.centerY-d
    s10.centerY=s10.centerY-d
    s11.centerY=s11.centerY-d
    s12.centerY=s12.centerY-d
    s13.centerY=s13.centerY-d
    s14.centerY=s14.centerY-d
    s15.centerY=s15.centerY-d
    s16.centerY=s16.centerY-d
    s17.centerY=s17.centerY-d
    s18.centerY=s18.centerY-d
    s19.centerY=s19.centerY-d
    s20.centerY=s20.centerY-d
    s21.centerY=s21.centerY-d
    s22.centerY=s22.centerY-d
    s23.centerY=s23.centerY-d
    s24.centerY=s24.centerY-d
    s25.centerY=s25.centerY-d
    s26.centerY=s26.centerY-d
    s27.centerY=s27.centerY-d
    sbl.centerY=sbl.centerY-d
    sbl1.centerY=sbl1.centerY-d
    sbr.centerY=sbr.centerY-d
    sbr1.centerY=sbr1.centerY-d
    sbr2.centerY=sbr2.centerY-d
# helper funtion of condition that will helps to fall the first stage and fire to dispear
        # and rotate its booster
def firstStagedown(d):
    r5.centerY=r5.centerY+d
    r6.centerY=r6.centerY+d
    p26.centerY=p26.centerY+d
    p1.rotateAngle+=3
    p1.centerY=p1.centerY+4
    p1.centerX=p1.centerX-2
    p2.centerY=p2.centerY+6
    p2.centerX=p2.centerX-1
    p2.rotateAngle+=2
    p3.centerY=p3.centerY+6
    p3.centerX=p3.centerX+1
    p3.rotateAngle-=2
    p4.centerY=p4.centerY+4
    p4.centerX=p4.centerX+2
    p4.rotateAngle-=3
    p5.centerY=p5.centerY+3
    p5.centerX=p5.centerX
    p5.rotateAngle+=4
    l13.centerY=p2.centerY+6
    l13.centerX=p2.centerX-1
    l13.rotateAngle+=2
    l14.centerY=p3.centerY+6
    l14.centerX=p3.centerX+1
    l14.rotateAngle-=2
    la8.centerY=la8.centerY+d
    la9.centerY=la9.centerY+d
    r10.centerY=r10.centerY+d
    f.centerY=f.centerY+d
    s.centerY=s.centerY+d
    s1.centerY=s1.centerY+d
    s2.centerY=s2.centerY+d
    s3.centerY=s3.centerY+d
    s4.centerY=s4.centerY+d
    s5.centerY=s5.centerY+d
    s6.centerY=s6.centerY+d
    s7.centerY=s7.centerY+d
    s8.centerY=s8.centerY+d
    s9.centerY=s9.centerY+d
    s10.centerY=s10.centerY+d
    s11.centerY=s11.centerY+d
    s12.centerY=s12.centerY+d
    s13.centerY=s13.centerY+d
    s14.centerY=s14.centerY+d
    s15.centerY=s15.centerY+d
    s16.centerY=s16.centerY+d
    s17.centerY=s17.centerY+d
    s18.centerY=s18.centerY+d
    s19.centerY=s19.centerY+d
    s20.centerY=s20.centerY+d
    s21.centerY=s21.centerY+d
    s22.centerY=s22.centerY+d
    s23.centerY=s23.centerY+d
    s24.centerY=s24.centerY+d
    s25.centerY=s25.centerY+d
    s26.centerY=s26.centerY+d
    s27.centerY=s27.centerY+d
    # disapear the fire
    sbl.visible=False
    sbl1.visible=False
    sbr.visible=False
    sbr1.visible=False
    sbr2.visible=False
    f.visible=False
   # move the fire of the second stage or use ather engine
    
    sf1.centerY=sf1.centerY-d
    sf2.centerY=sf2.centerY-d
    sg1.centerY=sg1.centerY-d
    sg2.centerY=sg2.centerY-d
# second stage funtion move it up
def secondStageup(d):
    r3.centerY=r3.centerY-d
    r4.centerY=r4.centerY-d
    la5.centerY=la5.centerY-d
    la6.centerY=la6.centerY-d
    la7.centerY=la7.centerY-d
    l12.centerY=l12.centerY-d
    ce.centerY=ce.centerY-d
    sf.centerY=sf.centerY-d
# second stage funtion of falling it down
def secondStagedown(d):
    r3.centerY=r3.centerY+d
    r4.centerY=r4.centerY+d
    la5.centerY=la5.centerY+d
    la6.centerY=la6.centerY+d
    la7.centerY=la7.centerY+d
    l12.centerY=l12.centerY+d
    ce.centerY=ce.centerY+d
    sf.centerY=sf.centerY+d
    sf1.visible=False
    sf2.visible=False
#  the function that keep moving the third stage up
def thirdStageUp(d):
    c2.centerY=c2.centerY-d 
    r1.centerY=r1.centerY-d
    l1.centerY=l1.centerY-d
    l2.centerY=l2.centerY-d 
    r2.centerY=r2.centerY-d
    l11.centerY=l11.centerY-d
    la.centerY=la.centerY-d
    la1.centerY=la1.centerY-d
    la2.centerY=la2.centerY-d
    la3.centerY=la3.centerY-d
    la4.centerY=la4.centerY-d
    c1.centerY=c1.centerY-d 
    sg.centerY=sg.centerY-d
# the function that will fall down the third stage
def thirdStageDown(d):
    c2.centerY=c2.centerY+d 
    r1.centerY=r1.centerY+d
    l1.centerY=l1.centerY+d
    l2.centerY=l2.centerY+d 
    r2.centerY=r2.centerY+d
    l11.centerY=l11.centerY+d
    la.centerY=la.centerY+d
    la1.centerY=la1.centerY+d
    la2.centerY=la2.centerY+d
    la3.centerY=la3.centerY+d
    la4.centerY=la4.centerY+d
    c1.centerY=c1.centerY+d 
    sg.centerY=sg.centerY+d
    sg1.visible=False
    sg2.visible=False
# the function of the forth stage that keep moving it up
def forthStageUp(d):
    p.centerY=p.centerY-d 
    r.centerY=r.centerY-d 
    co.centerY=co.centerY-d 
    ro.centerY=ro.centerY-d 
    ro1.centerY=ro1.centerY-d 
    ro2.centerY=ro2.centerY-d 
    ro3.centerY=ro3.centerY-d 
    ro4.centerY=ro4.centerY-d 
    l6.centerY=l6.centerY-d
    l7.centerY=l7.centerY-d
    l8.centerY=l8.centerY-d
    l3.centerY=l3.centerY-d
    l4.centerY=l4.centerY-d
    c7.centerY=c7.centerY-d
    l5.centerY=l5.centerY-d
    l9.centerY=l9.centerY-d
    l10.centerY=l10.centerY-d
    p30.centerY=p30.centerY-d
    sh.centerY=sh.centerY-d
    sh1.centerY=sh1.centerY-d
    sh2.centerY=sh2.centerY-d 
# make the funtion that moves the forth stage down of that covers of the 
# satellite
def forthStageDown(d):
    r.visible=False
    co.visible=False
    p.centerY=p.centerY+2
    p.centerX=p.centerX-1
    p.rotateAngle-=1
    p30.centerY=p30.centerY+2
    p30.centerX=p30.centerX+1
    p30.rotateAngle+=1
    l5.centerY=p30.centerY+2
    l5.centerX=p30.centerX+1
    l10.centerY=p30.centerY+4
    l10.centerX=p30.centerX+4
    l9.centerY=p.centerY+2
    l9.centerX=p.centerX-1
    l6.visible=False
    l7.visible=False
    l8.visible=False
    l3.visible=False
    l4.visible=False
    c7.visible=False
    sh.centerY=100
    sh1.centerY=108
    sh2.centerY=114
# function that will show the appearance of the stars
# when the background is becaming dark
def Staropac():
    b.opacity+=1
    b1.opacity+=1
    b2.opacity+=1
    b3.opacity+=1
    b4.opacity+=1
    b5.opacity+=1
    b6.opacity+=1
    b7.opacity+=1
    b8.opacity+=1
    b9.opacity+=1
    b10.opacity+=1
    b11.opacity+=1
    b12.opacity+=1
    b13.opacity+=1
    b14.opacity+=1
    b15.opacity+=1
    b16.opacity+=1
    b17.opacity+=1
    b19.opacity+=1
    b20.opacity+=1
    b21.opacity+=1
    b22.opacity+=1
    b23.opacity+=1
    b24.opacity+=1
    b25.opacity+=1
    b26.opacity+=1
    b27.opacity+=1 
    b28.opacity+=1
    b29.opacity+=1
    b30.opacity+=1
# funtion that helps the stars to not be more than 100 opacity 
    # to be at 40 opacity as maximum
def StarOpacMax():
    b.opacity-=1
    b1.opacity-=1
    b2.opacity-=1
    b3.opacity-=1
    b4.opacity-=1
    b5.opacity-=1
    b6.opacity-=1
    b7.opacity-=1
    b8.opacity-=1
    b9.opacity-=1
    b10.opacity-=1
    b11.opacity-=1
    b12.opacity-=1
    b13.opacity-=1
    b14.opacity-=1
    b15.opacity-=1
    b16.opacity-=1
    b17.opacity-=1
    b19.opacity-=1
    b20.opacity-=1
    b21.opacity-=1
    b22.opacity-=1
    b23.opacity-=1
    b24.opacity-=1
    b25.opacity-=1
    b26.opacity-=1
    b27.opacity-=1 
    b28.opacity-=1
    b29.opacity-=1
    b30.opacity-=1
# funtion that moves the star according to the star called b at the 
# center
def StarMove(c):
    b.centerY=b.centerY+c
    b1.centerY=b1.centerY+c
    b2.centerY=b2.centerY+c
    b2.centerY=b2.centerY+c
    b3.centerY=b3.centerY+c
    b4.centerY=b4.centerY+c
    b5.centerY=b5.centerY+c
    # b6.centerY=b6.centerY+c
    b7.centerY=b7.centerY+c
    b8.centerY=b8.centerY+c
    b9.centerY=b9.centerY+c
    b10.centerY=b10.centerY+c
    b11.centerY=b11.centerY+c
    b24.centerY=b24.centerY+c
    b13.centerY=b13.centerY+c
    b14.centerY=b14.centerY+c
    b15.centerY=b15.centerY+c
    b16.centerY=b16.centerY+c
    b17.centerY=b17.centerY+c
    b18.centerY=b18.centerY+c
    b19.centerY=b19.centerY+c
    b20.centerY=b20.centerY+c
    b21.centerY=b21.centerY+c
    b22.centerY=b22.centerY+c
    b23.centerY=b23.centerY+c
    b25.centerY=b25.centerY+c
# funtion that helps some stars to start when they dispeared
def StarStart(c):
    if(b.centerY>405):
        b.centerY=-1
    if(b4.centerY>405):
        b4.centerY=b4.centerY+c
    if(b10.centerY>405):
        b10.centerY=-1
    if(b11.centerY>405):
        b11.centerY=-1
    if(b12.centerY>405):
        b12.centerY=-1
    if(b13.centerY>405):
        b13.centerY=-1
    if(b14.centerY>405):
        b14.centerY=-1
    if(b15.centerY>405):
        b15.centerY=-1
    if(b16.centerY>405):
        b16.centerY=-1
    if(b17.centerY>405):
        b17.centerY=-1
    if(b18.centerY>405):
        b18.centerY=-1
    if(b19.centerY>405):
        b19.centerY=-1
    if(b20.centerY>405):
        b20.centerY=-1
    if(b21.centerY>405):
        b21.centerY=-1
    if(b22.centerY>405):
        b22.centerY=-1
    if(b23.centerY>405):
        b23.centerY=-1
    if(b24.centerY>405):
        b24.centerY=-1
    if(b25.centerY>405):
        b25.centerY=-1
# funtion that will rotate the satellite to second scene
def SatelliteRotate():
    ro5.centerX=201
    ro5.centerY=61
    ro5.rotateAngle=20
    ro4.centerX=197
    ro4.centerY=72
    ro4.rotateAngle=20
    ro3.centerX=195
    ro3.centerY=76
    ro3.rotateAngle=20
    ro2.centerX=193
    ro2.centerY=82
    ro2.rotateAngle=20
    ro1.centerX=187
    ro1.centerY=92
    ro1.rotateAngle=20
    ro.centerX=189
    ro.centerY=89
    ro.rotateAngle=20
    sh.centerX=185
    sh.centerY=79
    sh.rotateAngle=20
    sh1.centerX=182
    sh1.centerY=73
    sh1.rotateAngle=20
    sh2.centerX=180
    sh2.centerY=72
    sh2.rotateAngle=20
# function which will fall the engine of last stage and disapear the
    # fire
def lastEngine(d,c):
    ro2.centerX=ro2.centerX-d
    ro2.centerY=ro2.centerY+c
    ro.centerX=ro.centerX-d
    ro.centerY=ro.centerY+c
    ro1.centerX=ro1.centerX-d    
    ro1.centerY=ro1.centerY+c
    ro4.visible=False
    pb.visible=True
    pb1.visible=True
    lb.visible=True
    sh1.visible=False
    sh2.visible=False
    sh.visible=False
# funtion that will inrease the opacity of the satellite 
# as the Earth apeared
def satelliteOpacMax(d):
    lp.opacity+=d
    lp4.opacity+=d
    lp5.opacity+=d
    lp6.opacity+=d
    lp7.opacity+=d
    lp8.opacity+=d
    lp9.opacity+=d
    lp10.opacity+=d
    lp11.opacity+=d
    lp12.opacity+=d
    lp13.opacity+=d
    cp4.opacity+=d
    cp3.opacity+=d
    cp2.opacity+=d
    lp3.opacity+=d
    lp1.opacity+=d
    lp2.opacity+=d
    cp.opacity+=d
    cp1.opacity+=d
    lp14.opacity+=d
    lp15.opacity+=d
    lp4.opacity+=d
    lp5.opacity+=d
    lp6.opacity+=d
    lp7.opacity+=d
    lp8.opacity+=d
    lp9.opacity+=d
    lp10.opacity+=d
    lp11.opacity+=d
    lp12.opacity+=d
    lp13.opacity+=d
    cp4.opacity+=d
    cp3.opacity+=d
    cp2.opacity+=d
    lp1.opacity+=d
    lp2.opacity+=d
    cp.opacity+=d
    cp1.opacity+=d
    lp14.opacity+=d
    lp15.opacity+=d
    
# make the funtion that will keep changing the massage of 
# explanation process
app.message = ''
opacit=Label(app.message,200,370,size=15,fill="white",opacity=0)

def message(message):
    opacit.value= message
    if(opacit.opacity>=0)and(opacit.opacity<80):
        opacit.opacity+=2
# funtion which will deal with the final massege about satellite 
# make the funtion movethewords()
def movethewords():
    word.centerY-=1
    Linedefination.centerY-=1
    massege1.centerY-=1
    massege2.centerY-=1
    massege3.centerY-=1
    massege4.centerY-=1
    massege5.centerY-=1
    massege6.centerY-=1
    massege7.centerY-=1
    massege8.centerY-=1
    massege9.centerY-=1
    massege10.centerY-=1
    massege12.centerY-=1
    massege13.centerY-=1
    massege14.centerY-=1
    massege15.centerY-=1
   
def onMouseMove(mouseX,mouseY):
    message(app.message)
    
    d=1
    c=2
    rb.centerY=rb.centerY-d
    # first stage move it down and rotate its booster
    #  fist condition helps to move up the first stage and its smoke
    # indicated by letter s
    # call the allstageUp function
    if(r.centerY>190):
        allstageUp(d)
        # condition that will helps to fall the first stage and smoke down
        # and rotate its booster
        # call funtion of  firstStage down 
    if(r.centerY<190): 
        firstStagedown(d)
        # explanation of first stage separation call the funtioin message
    if(r.centerY<190)and (r.centerY>150):
        app.message="First stage of Separation"
     
        # second stage
    # move the stage up 
    # call helper funtion of secondStageup
    if(r.centerY>130):
        secondStageup(d)
        # condition that helps the second stage to fall dawn
        # call of  secondstagedown
    if(r.centerY<130):
        secondStagedown(d)
        # explanation of Second stage separation call the funtioin message
    if(r.centerY<130)and (r.centerY>110):
        app.message="Second stage of Separation"
        # third stage move it up 
        # by calling of thirdstageup funtion
    if(r.centerY>100):
        thirdStageUp(d)
        # condition that helps the third stage to fall dawn
        # call funtion of thirdStageDown
    if(r.centerY<100):
        thirdStageDown(d)
    # explanation of Third stage separation call the funtioin message
    if(r.centerY<100)and (r.centerY>80):
        app.message="Third stage of Separation"
        # forth stage call the funtion forthStageUp(d)
    if(r.centerY>80):
        forthStageUp(d)
        # condition that will call the invisible rectangle 
        # ro5 if the centerY of r equals to 79.5
    if(r.centerY==79.5):
        ro5.visible=True
       # condition that will helps to fall down the forth stage of
       # that part that covers the satellite
       #   then call the forthStageDown(d)
    if(r.centerY<80):
        forthStageDown(d)
    # explanation of Forth stage separation call the funtioin message
    if(r.centerY<80)and (r.centerY>70):
        app.message="fairing Separation"
        # if condition about the change of colors of the background until it get dark
    if(re1.opacity<100):
        re1.opacity+=1
    if(re1.opacity>=100):
        re1.opacity-=1
        
    # draw stars as  the back ground becames dark stars apeared
    # call funtion Staropac()
    if(b.opacity<40):
        Staropac()
    #  condition which helps the stars to not be more than 100 opacity 
    # to be at 40 opacity as maximum
    # call funtion StarOpacMax()
    if(b.opacity>=40):
        StarOpacMax()
# move the stars acording to star at the the center called b.
# call funtion StarMove(c)
    if(b.centerY<406):
       StarMove(c)
    # condition which helps some  stars to restart when they dispeared
    # call funtion StarStart(c)
    StarStart(c)
    # condition that deals with the apearance of the satellite
    if(rb.centerY>-45)and(rb.centerY<-1):
        rb1.opacity+=2
    if(rb.centerY<-45)and(rb.centerY>-80):
        rb1.opacity-=2
    # condition to rotate the satellite and its engine using rectangle
    # rb fills black moving at the top
    # call funtion SatelliteRotate().
    if(rb.centerY==-43):
        SatelliteRotate()
        
    #  condition which will fall the engine of last stage and disapear the
    # fire call funtion lastEngine().
    
    if(rb.centerY<-200):
        lastEngine(d,c)
    #  explanation of Forth stage separation call the funtioin message
    if(rb.centerY<-200)and (rb.centerY>-250):
        app.message="Payload Separation"
    # the end of the explanations
    if(rb.centerY<=-240):
        app.message=""
        # the condition that deal with apearance satellite only
    if(rb.centerY<-250)and(rb.centerY>-290):
        rb1.opacity+=2
   
        # appear the earth by increasing it.
    if(rb.centerY<-315)and(rb.centerY>-464):
        ca.radius+=1
        cs.radius+=1
        # inrease the opacity of the satellite as the Earth apeared
        # call the funtion satelliteOpacMax(d)
    if(rb.centerY<-315)and(rb.centerY>-360):
        satelliteOpacMax(d)
    
        # THE END
    if(rb.centerY<-400)and(rb.centerY>-730):
        print(rb.centerY)
        movethewords()
