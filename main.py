import pygame
import math
import random

pygame.init()

#values
if True:
  #constants
  if True:
    TICK = 60
    ANG = math.sqrt(2)
    pi = math.pi
    #colors
    if True:
      BLACK = (0,0,0)
      WHITE = (255,255,255)
      GRAY = (125,125,125)
      LIGHTGRAY = (200,200,200)
      DARKGRAY = (75,75,75)
      RED = (255,0,0)
      MAROON = (100,0,0)
      PINK = (255,150,150)
      GREEN = (0,255,0)
      DARKGREEN = (0,200,0)
      BLUE = (0,0,255)
      DARKBLUE = (0,0,100)
      YELLOW = (255,255,0)
      PURPLE = (175,0,200)
      LILAC = (220,70,255)
      ORANGE = (255,150,0)
      SKYBLUE = (0,150,255)
      BROWN = (120,70,0)
      INVIS = (255,255,255,0)
      fadeblack = [10,10,10,0]
      fadewhite = [255,255,255,0]
  #variables
  if True:
    #movement
    if True:
      x = 300
      y = 200
      move_up = "no"
      move_down = "no"
      move_right = "no"
      move_left = "no"
      facing = "r"
      speed = 1
      speed_mod = 1
      s_lock = -1
    #weapons
    if True:
      firing = False
      fire_timer_g = 0
      blts = []
      blt_mspd = 3
      blt_fspd = 10
      hblts = [10,30,50,70]
      msl = 0
      msls = []
      msl_mspd = 6
      msl_fspd = 1
      msl_rf = 1
      fire_timer_m = 0
      weapon = "gun"
      guntip = [x+17,y+2]
    #hud
    if True:
      score = 0
      show_stats = -1
      hlth = 3
      max_hlth = 4
      hlth_offset = 30
    #walls
    if True:
      count = 0
      walls = []
    #targets
    if True:
      reset = False
      collide = False
      r = random.randint(0,100)
      r2 = random.randint(0,1000)
      t_x = random.randrange(15,585)
      t_y = random.randrange(15,380)
      targ_timer = 0
      do_targ_timer = False
      targ_timer_end = 0
      t_type = "Red"
      t_type2 = "None"
      gt = []
    #misc.
    if True:
      o_p = False
      p_p = False
      en_p = False
      sp_p = False
      paused = -1
      pause_timer = 0
      done = False
      page = 1
      var_reset = False
      bclr = BLACK
      hrttmr = 0
      do_hrttmr = False
      shake = 0
      do_break = False
  #misc.
  if True:
    #game
    if True:
      #icon
      if True:
        icon = pygame.Surface([31,31],pygame.SRCALPHA)
        icon.fill(INVIS)
        pygame.draw.circle(icon,RED,(15,15),15)
        pygame.draw.circle(icon,WHITE,(15,15),10)
        pygame.draw.circle(icon,RED,(15,15),5)
        pygame.display.set_icon(icon)
      flags = pygame.SRCALPHA|pygame.RESIZABLE|pygame.SCALED
      display = pygame.display.set_mode((600,400),flags)
      screen = pygame.Surface([600,400],pygame.SRCALPHA)
      pygame.display.set_caption("Target Blaster")
      clock = pygame.time.Clock()
      pygame.event.set_blocked(pygame.MOUSEMOTION)
      current_screen = "menu"
      prev_screen = ""
      dif = "med"
    #fonts
    if True:
      tinyfont = pygame.font.SysFont("freesansbold",20)
      smallfont2 = pygame.font.SysFont("freesansbold",22)
      smallfont = pygame.font.SysFont("freesansbold",30)
      medsmlfont2 = pygame.font.SysFont("freesansbold",40)
      medsmlfont = pygame.font.SysFont("freesansbold",45)
      medfont = pygame.font.SysFont("freesansbold",65)
      medbigfont = pygame.font.SysFont("freesansbold",80)
      bigfont = pygame.font.SysFont("freesansbold",100)
    #surfaces/images
    if True:
      hud = pygame.Surface([600,400],pygame.SRCALPHA)
      hud.set_alpha(230)
      gmovsurf = pygame.Surface([600,400],pygame.SRCALPHA)
      gmovsubsurf = bigfont.render("Game Over",True,RED)
      resurf = medsmlfont.render("Play again with these settings?",True,DARKGRAY)
      winsurf = pygame.Surface([600,400],pygame.SRCALPHA)
      winsubsurf = bigfont.render("You win!",True,YELLOW)
      pausetxt = medfont.render("Paused",True,WHITE)
      pausesurf = pygame.Surface([600,400],pygame.SRCALPHA)
      pausesurf.fill([0,0,0,50])
      logo = bigfont.render("Target Blaster",True,RED)
      statsurf = pygame.Surface([400,400],pygame.SRCALPHA)
      stattxt = smallfont.render("Press E to show stats",True,BLACK)
      stattxt.set_alpha(150)
      instrtxt = medfont.render("Instructions",True,WHITE)
      keytxt = medfont.render("Target Key",True,WHITE)
      prmtxt = medsmlfont.render("Primary Color",True,WHITE)
      scdtxt = medsmlfont.render("Secondary Color",True,WHITE)
      diftxt = medbigfont.render("Select Difficulty",True,BLACK)
      #expressions
      if True:
        exprtxt = medfont.render("Expressions",True,WHITE)
        p_s_txt = smallfont.render("p/s: pixels per second",True,WHITE)
        divtxt = smallfont.render("#/#/#/#: easy/normal/hard/impossible (difficulty)",True,WHITE)
      #buttons
      if True:
        #yes
        if True:
          yessurf = pygame.Surface([100,50])
          yestxt = medfont.render("YES",True,BLACK)
          yessurf.fill(BLACK)
          pygame.draw.rect(yessurf,WHITE,[5,5,90,40])
          yessurf.blit(yestxt,(6,5))
        #no
        if True:
          nosurf = pygame.Surface([100,50])
          notxt = medfont.render("NO",True,BLACK)
          nosurf.fill(BLACK)
          pygame.draw.rect(nosurf,WHITE,[5,5,90,40])
          nosurf.blit(notxt,(17,5))
        #play
        if True:
          playsurf = pygame.Surface([140,50])
          playtxt = medfont.render("PLAY",True,BLACK)
          playsurf.fill(BLACK)
          pygame.draw.rect(playsurf,WHITE,[5,5,130,40])
          playsurf.blit(playtxt,(12,5))
        #help
        if True:
          helpsurf = pygame.Surface([140,50])
          helptxt = medfont.render("HELP",True,BLACK)
          helpsurf.fill(BLACK)
          pygame.draw.rect(helpsurf,WHITE,[5,5,130,40])
          helpsurf.blit(helptxt,(12,5))
        #menu
        if True:
          menusurf = pygame.Surface([140,50])
          menutxt = medfont.render("MENU",True,BLACK)
          menusurf.fill(BLACK)
          pygame.draw.rect(menusurf,WHITE,[5,5,130,40])
          menusurf.blit(menutxt,(5,5))
        #back
        if True:
          backsurf = pygame.Surface([140,50])
          backtxt = medfont.render("BACK",True,BLACK)
          backsurf.fill(BLACK)
          pygame.draw.rect(backsurf,WHITE,[5,5,130,40])
          backsurf.blit(backtxt,(5,5))
        #next
        if True:
          nextsurf = pygame.Surface([140,50])
          nexttxt = medfont.render("NEXT",True,BLACK)
          nextsurf.fill(BLACK)
          pygame.draw.rect(nextsurf,WHITE,[5,5,130,40])
          nextsurf.blit(nexttxt,(8,5))
        #prev
        if True:
          prevsurf = pygame.Surface([140,50])
          prevtxt = medfont.render("PREV",True,BLACK)
          prevsurf.fill(BLACK)
          pygame.draw.rect(prevsurf,WHITE,[5,5,130,40])
          prevsurf.blit(prevtxt,(5,5))
        #difficulty
        if True:
          #easy
          if True:
            easysurf = pygame.Surface([200,50])
            easytxt = medfont.render("EASY",True,BLACK)
            easysurf.fill(BLACK)
            pygame.draw.rect(easysurf,DARKGREEN,[5,5,190,40])
            easysurf.blit(easytxt,(37,5))
          #normal/medium
          if True:
            medsurf = pygame.Surface([200,50])
            medtxt = medfont.render("NORMAL",True,BLACK)
            medsurf.fill(BLACK)
            pygame.draw.rect(medsurf,YELLOW,[5,5,190,40])
            medsurf.blit(medtxt,(5,5))
          #hard
          if True:
            hardsurf = pygame.Surface([200,50])
            hardtxt = medfont.render("HARD",True,BLACK)
            hardsurf.fill(BLACK)
            pygame.draw.rect(hardsurf,RED,[5,5,190,40])
            hardsurf.blit(hardtxt,(35,5))
          #impossible
          if True:
            impossurf = pygame.Surface([290,50])
            impostxt = medfont.render("IMPOSSIBLE",True,BLACK)
            impossurf.fill(BLACK)
            pygame.draw.rect(impossurf,MAROON,[5,5,280,40])
            impossurf.blit(impostxt,(8,5))
      #target descriptions
      if True:
        spctxt = smallfont.render("Special:",True,WHITE)
        #red
        if True:
          rtdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          rtdescsub1 = medsmlfont.render("Red",True,RED)
          rtdescsub1_2 = smallfont2.render("60/50/43/32%",True,WHITE)
          rtdescsub2 = smallfont.render("Points: 2",True,WHITE)
          rtdescsub3 = smallfont.render("Time:",True,WHITE)
          rtdescsub3_2 = smallfont2.render("45/30/20/5s",True,WHITE)
          rtdescsub4 = smallfont.render("None",True,WHITE)
          rtdesc.fill(INVIS)
          rtdesc.blit(rtdescsub1,(20,0))
          rtdesc.blit(rtdescsub1_2,(5,35))
          pygame.draw.circle(rtdesc,RED,(50,85),30)
          pygame.draw.circle(rtdesc,WHITE,(50,85),20)
          pygame.draw.circle(rtdesc,RED,(50,85),10)
          rtdesc.blit(rtdescsub2,(5,120))
          rtdesc.blit(rtdescsub3,(20,140))
          rtdesc.blit(rtdescsub3_2,(10,160))
          rtdesc.blit(spctxt,(10,175))
          rtdesc.blit(rtdescsub4,(25,195))
          pygame.draw.line(rtdesc,BLACK,(99,0),(99,250))
        #purple
        if True:
          ptdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          ptdescsub1 = medsmlfont.render("Purple",True,PURPLE)
          ptdescsub1_2 = smallfont2.render("15/25/32/40%",True,WHITE)
          ptdescsub2 = smallfont.render("Points: -5",True,WHITE)
          ptdescsub3 = smallfont.render("Time:",True,WHITE)
          ptdescsub3_2 = smallfont2.render("2/3.3/4/4.5s",True,WHITE)
          ptdescsub4 = smallfont.render("-1 Health",True,WHITE)
          ptdesc.fill(INVIS)
          ptdesc.blit(ptdescsub1,(1,0))
          ptdesc.blit(ptdescsub1_2,(5,35))
          pygame.draw.circle(ptdesc,PURPLE,(50,85),30)
          pygame.draw.circle(ptdesc,WHITE,(50,85),20)
          pygame.draw.circle(ptdesc,PURPLE,(50,85),10)
          ptdesc.blit(ptdescsub2,(3,120))
          ptdesc.blit(ptdescsub3,(20,140))
          ptdesc.blit(ptdescsub3_2,(2,160))
          ptdesc.blit(spctxt,(10,175))
          ptdesc.blit(ptdescsub4,(4,195))
          pygame.draw.line(ptdesc,BLACK,(99,0),(99,250))
        #orange
        if True:
          otdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          otdescsub1 = medsmlfont.render("Ornge",True,ORANGE)
          otdescsub1_2 = smallfont2.render("10/8/6/3%",True,WHITE)
          otdescsub2 = smallfont.render("Points: 1",True,WHITE)
          otdescsub3 = smallfont.render("Time:",True,WHITE)
          otdescsub3_2 = smallfont2.render("12/8.5/5/2.5s",True,WHITE)
          otdescsub4 = smallfont.render("Weapons",True,WHITE)
          otdescsub5 = smallfont.render("(see P4)",True,WHITE)
          otdesc.fill(INVIS)
          otdesc.blit(otdescsub1,(3,0))
          otdesc.blit(otdescsub1_2,(15,35))
          pygame.draw.circle(otdesc,ORANGE,(50,85),30)
          pygame.draw.circle(otdesc,WHITE,(50,85),20)
          pygame.draw.circle(otdesc,ORANGE,(50,85),10)
          otdesc.blit(otdescsub2,(5,120))
          otdesc.blit(otdescsub3,(20,140))
          otdesc.blit(otdescsub3_2,(7,160))
          otdesc.blit(spctxt,(10,175))
          otdesc.blit(otdescsub4,(5,195))
          otdesc.blit(otdescsub5,(10,215))
          pygame.draw.line(otdesc,BLACK,(99,0),(99,250))
        #green
        if True:
          gtdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          gtdescsub1 = medsmlfont.render("Green",True,DARKGREEN)
          gtdescsub1_2 = smallfont2.render("10/7/6/3%",True,WHITE)
          gtdescsub2 = smallfont.render("Points: 1",True,WHITE)
          gtdescsub3 = smallfont.render("Time:",True,WHITE)
          gtdescsub3_2 = smallfont2.render("12/8.5/5/2.5s",True,WHITE)
          gtdescsub4 = smallfont.render("Speed",True,WHITE)
          gtdescsub5 = smallfont.render("+12 (p/s)",True,WHITE)
          gtdesc.fill(INVIS)
          gtdesc.blit(gtdescsub1,(5,0))
          gtdesc.blit(gtdescsub1_2,(15,35))
          pygame.draw.circle(gtdesc,DARKGREEN,(50,85),30)
          pygame.draw.circle(gtdesc,WHITE,(50,85),20)
          pygame.draw.circle(gtdesc,DARKGREEN,(50,85),10)
          gtdesc.blit(gtdescsub2,(5,120))
          gtdesc.blit(gtdescsub3,(20,140))
          gtdesc.blit(gtdescsub3_2,(7,160))
          gtdesc.blit(spctxt,(10,175))
          gtdesc.blit(gtdescsub4,(17,195))
          gtdesc.blit(gtdescsub5,(8,215))
          pygame.draw.line(gtdesc,BLACK,(99,0),(99,250))
        #black
        if True:
          btdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          btdescsub1 = medsmlfont.render("Black",True,BLACK)
          btdescsub1_2 = smallfont2.render("2/5/10/20%",True,WHITE)
          btdescsub2 = smallfont.render("Points: -5",True,WHITE)
          btdescsub3 = smallfont.render("Time:",True,WHITE)
          btdescsub3_2 = smallfont2.render("2/3/3.4/4s",True,WHITE)
          btdescsub4 = smallfont.render("+5 walls",True,WHITE)
          btdesc.fill(INVIS)
          btdesc.blit(btdescsub1,(7,0))
          btdesc.blit(btdescsub1_2,(15,35))
          pygame.draw.circle(btdesc,BLACK,(50,85),30)
          pygame.draw.circle(btdesc,WHITE,(50,85),20)
          pygame.draw.circle(btdesc,BLACK,(50,85),10)
          btdesc.blit(btdescsub2,(3,120))
          btdesc.blit(btdescsub3,(20,140))
          btdesc.blit(btdescsub3_2,(12,160))
          btdesc.blit(spctxt,(10,175))
          btdesc.blit(btdescsub4,(9,195))
          pygame.draw.line(btdesc,BLACK,(99,0),(99,250))
        #yellow
        if True:
          ytdesc = pygame.Surface([100,270],pygame.SRCALPHA)
          ytdescsub1 = medsmlfont.render("Yellow",True,YELLOW)
          ytdescsub1_2 = smallfont2.render("8/5/3/1%",True,WHITE)
          ytdescsub2 = smallfont.render("Points: 10",True,WHITE)
          ytdescsub3 = smallfont.render("Time:",True,WHITE)
          ytdescsub3_2 = smallfont2.render("7/3.5/2.5/1.5s",True,WHITE)
          ytdescsub4 = smallfont.render("+1 Health",True,WHITE)
          ytdescsub5 = smallfont.render("and Max",True,WHITE)
          ytdescsub6 = smallfont.render("Health",True,WHITE)
          ytdesc.fill(INVIS)
          ytdesc.blit(ytdescsub1,(2,0))
          ytdesc.blit(ytdescsub1_2,(25,35))
          pygame.draw.circle(ytdesc,YELLOW,(50,85),30)
          pygame.draw.circle(ytdesc,WHITE,(50,85),20)
          pygame.draw.circle(ytdesc,YELLOW,(50,85),10)
          ytdesc.blit(ytdescsub2,(1,120))
          ytdesc.blit(ytdescsub3,(20,140))
          ytdesc.blit(ytdescsub3_2,(1,160))
          ytdesc.blit(spctxt,(10,175))
          ytdesc.blit(ytdescsub4,(3,195))
          ytdesc.blit(ytdescsub5,(10,215))
          ytdesc.blit(ytdescsub6,(20,235))
        #health
        if True:
          htdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          htdescsub1 = medsmlfont.render("Pink",True,PINK)
          htdescsub2 = medsmlfont.render("Health",True,WHITE)
          htdescsub3 = smallfont2.render("30/20/15/5%",True,WHITE)
          htdescsub4 = smallfont.render("Health +1",True,WHITE)
          htdescsub5 = smallfont.render("(can't be on",True,WHITE)
          htdescsub6 = smallfont2.render("purple primary)",True,WHITE)
          htdesc.fill(INVIS)
          htdesc.blit(htdescsub1,(25,15))
          htdesc.blit(htdescsub2,(11,60))
          htdesc.blit(htdescsub3,(20,90))
          pygame.draw.circle(htdesc,RED,(60,140),30)
          pygame.draw.circle(htdesc,PINK,(60,140),20)
          pygame.draw.circle(htdesc,RED,(60,140),10)
          htdesc.blit(htdescsub4,(15,175))
          htdesc.blit(htdescsub5,(2,195))
          htdesc.blit(htdescsub6,(3,215))
          pygame.draw.line(htdesc,BLACK,(119,0),(119,250))
        #damage
        if True:
          dtdesc = pygame.Surface([120,270],pygame.SRCALPHA)
          dtdescsub1 = medsmlfont.render("Light",True,LILAC)
          dtdescsub1_2 = medsmlfont.render("Purple",True,LILAC)
          dtdescsub2 = medsmlfont.render("Damage",True,WHITE)
          dtdescsub3 = smallfont2.render("2/5/10/20%",True,WHITE)
          dtdescsub4 = smallfont.render("Health -1",True,WHITE)
          dtdescsub5 = smallfont.render("(must be on",True,WHITE)
          dtdescsub6 = smallfont2.render("purple primary)",True,WHITE)
          dtdesc.fill(INVIS)
          dtdesc.blit(dtdescsub1,(22,0))
          dtdesc.blit(dtdescsub1_2,(11,30))
          dtdesc.blit(dtdescsub2,(0,60))
          dtdesc.blit(dtdescsub3,(22,90))
          pygame.draw.circle(dtdesc,PURPLE,(60,140),30)
          pygame.draw.circle(dtdesc,LILAC,(60,140),20)
          pygame.draw.circle(dtdesc,PURPLE,(60,140),10)
          dtdesc.blit(dtdescsub4,(15,175))
          dtdesc.blit(dtdescsub5,(2,195))
          dtdesc.blit(dtdescsub6,(3,215))
          pygame.draw.line(dtdesc,BLACK,(119,0),(119,250))
        #missle
        if True:
          mtdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          mtdescsub1 = medsmlfont.render("Light",True,LIGHTGRAY)
          mtdescsub1_2 = medsmlfont.render("Gray",True,LIGHTGRAY)
          mtdescsub2 = medsmlfont.render("Missile",True,WHITE)
          mtdescsub3 = smallfont2.render("25/15/10/5%",True,WHITE)
          mtdescsub4 = smallfont.render("Missile",True,WHITE)
          mtdescsub5 = smallfont.render("count +",True,WHITE)
          mtdescsub6 = smallfont.render("refill rate",True,WHITE)
          mtdesc.fill(INVIS)
          mtdesc.blit(mtdescsub1,(22,0))
          mtdesc.blit(mtdescsub1_2,(25,30))
          mtdesc.blit(mtdescsub2,(6,60))
          mtdesc.blit(mtdescsub3,(17,90))
          pygame.draw.circle(mtdesc,RED,(60,140),30)
          pygame.draw.circle(mtdesc,LIGHTGRAY,(60,140),20)
          pygame.draw.circle(mtdesc,RED,(60,140),10)
          mtdesc.blit(mtdescsub4,(22,175))
          mtdesc.blit(mtdescsub5,(22,195))
          mtdesc.blit(mtdescsub6,(15,215))
          pygame.draw.line(mtdesc,BLACK,(119,0),(119,250))
        #missle2
        if True:
          m2tdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          m2tdescsub1 = medsmlfont.render("Gray",True,GRAY)
          m2tdescsub2 = medsmlfont.render("Missile2",True,WHITE)
          m2tdescsub3 = smallfont2.render("5/2/1/0.5%",True,WHITE)
          m2tdescsub4 = smallfont.render("Missile",True,WHITE)
          m2tdescsub5 = smallfont.render("Refill Rate",True,WHITE)
          m2tdescsub6 = smallfont.render("+1",True,WHITE)
          m2tdesc.fill(INVIS)
          m2tdesc.blit(m2tdescsub1,(25,15))
          m2tdesc.blit(m2tdescsub2,(0,60))
          m2tdesc.blit(m2tdescsub3,(25,90))
          pygame.draw.circle(m2tdesc,RED,(60,140),30)
          pygame.draw.circle(m2tdesc,GRAY,(60,140),20)
          pygame.draw.circle(m2tdesc,RED,(60,140),10)
          m2tdesc.blit(m2tdescsub4,(22,175))
          m2tdesc.blit(m2tdescsub5,(10,195))
          m2tdesc.blit(m2tdescsub6,(50,215))
          pygame.draw.line(m2tdesc,BLACK,(119,0),(119,250))
        #none
        if True:
          ntdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          ntdescsub1 = medsmlfont.render("White",True,WHITE)
          ntdescsub2 = medsmlfont.render("None",True,WHITE)
          ntdescsub3 = smallfont2.render("38/58/64/69.5%",True,WHITE)
          ntdescsub4 = smallfont.render("No added",True,WHITE)
          ntdescsub5 = smallfont.render("effects",True,WHITE)
          ntdesc.fill(INVIS)
          ntdesc.blit(ntdescsub1,(18,15))
          ntdesc.blit(ntdescsub2,(23,60))
          ntdesc.blit(ntdescsub3,(7,90))
          pygame.draw.circle(ntdesc,RED,(60,140),30)
          pygame.draw.circle(ntdesc,WHITE,(60,140),20)
          pygame.draw.circle(ntdesc,RED,(60,140),10)
          ntdesc.blit(ntdescsub4,(15,175))
          ntdesc.blit(ntdescsub5,(30,195))
      #weapons
      if True:
        weapsurf = pygame.Surface([600,400],pygame.SRCALPHA)
        weaptxt = medfont.render("Weapons",True,WHITE)
        #gun
        if True:
          gunsurf = pygame.Surface([600,55],pygame.SRCALPHA)
          gunsurf.fill(INVIS)
          pygame.draw.lines(gunsurf,BLACK,False,[(25,38),(25,18),(53,18)],9)
          gunsub1 = medsmlfont.render("Gun",True,WHITE)
          gunsub2 = smallfont.render("Fires bullets. Fast fire rate. Button: 1",True,WHITE)
          gunsurf.blit(gunsub1,(80,5))
          gunsurf.blit(gunsub2,(80,33))
        #missile launcher
        if True:
          mslnsurf = pygame.Surface([600,55],pygame.SRCALPHA)
          mslnsurf.fill(INVIS)
          pygame.draw.polygon(mslnsurf,BLACK,[(6,26),(26,24),(28,20),(66,18),(66,42),(28,40),(26,36),(6,34)])
          mslnsub1 = medsmlfont.render("Missile Launcher",True,WHITE)
          mslnsub2 = smallfont.render("Fires missiles. Slow fire rate. Button: 2",True,WHITE)
          mslnsurf.blit(mslnsub1,(80,5))
          mslnsurf.blit(mslnsub2,(80,33))
        #bullets
        if True:
          bltsurf = pygame.Surface([600,55],pygame.SRCALPHA)
          bltssurf = pygame.Surface([80,55],pygame.SRCALPHA)
          bltsurf.fill(INVIS)
          bltsub1 = medsmlfont.render("Bullets",True,WHITE)
          bltsub2 = smallfont.render("Unlimited. Low speed. Cannot go through walls.",True,WHITE)
        #missiles
        if True:
          mslssurf = pygame.Surface([600,55],pygame.SRCALPHA)
          mslssurf.fill(INVIS)
          pygame.draw.rect(mslssurf,GRAY,[35-24,25-8,49,17])
          pygame.draw.polygon(mslssurf,RED,[(35+25,25-8),(35+25,25+8),(35+24+(10*math.sqrt(3)),25)])
          pygame.draw.polygon(mslssurf,RED,[(35-24,25-9),(35-8,25-9),(35-20,25-17),(35-32,25-17)])
          pygame.draw.polygon(mslssurf,RED,[(35-24,25+9),(35-8,25+9),(35-20,25+17),(35-32,25+17)])
          mslssub1 = medsmlfont.render("Missile",True,WHITE)
          mslssub2 = smallfont.render("Limited supply. High speed. Will destroy walls.",True,WHITE)
          mslssurf.blit(mslssub1,(80,5))
          mslssurf.blit(mslssub2,(80,33))
        stinsurf1 = smallfont.render("Orange targets increase gun fire rate by 1 bullet per second,",True,WHITE)
        stinsurf2 = smallfont.render("bullet movement speed by 6p/s, missile movement speed",True,WHITE)
        stinsurf3 = smallfont.render("by 12 p/s, and missile fire rate by 0.1 missles per second.",True,WHITE)
      #help screen
      if True:
        hsubsurf1 = smallfont.render("Shoot the targets. Use WASD to move and the arrow keys to",True,WHITE)
        hsubsurf2 = smallfont.render("aim. Fire with Enter or the Spacebar. Use Shift to go fast and",True,WHITE)
        hsubsurf3 = smallfont.render("Ctrl to go slow. Q locks you in fast. Press Esc to pause/",True,WHITE)
        hsubsurf4 = smallfont.render("unpause. Press E to see your stats. Use the number keys to",True,WHITE)
        hsubsurf5 = smallfont.render("switch between weapons. 1 is gun, 2 is missile launcher.",True,WHITE)
        hsubsurf6 = smallfont.render("Get 150/250/500/1000 points to win.",True,WHITE)
        hsurf = pygame.Surface((600,200),pygame.SRCALPHA)
        hsurf.fill(INVIS)
        hsurf.blit(hsubsurf1,(10,0))
        hsurf.blit(hsubsurf2,(5,25))
        hsurf.blit(hsubsurf3,(30,50))
        hsurf.blit(hsubsurf4,(10,75))
        hsurf.blit(hsubsurf5,(20,100))
        hsurf.blit(hsubsurf6,(125,125))





#main loop
while done == False:
  display.blit(screen,(0,0))
  
  #menu
  if current_screen == "menu":
    #event management
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(230,370) and event.pos[1] in range(230,280):
            current_screen = "difslct"
            prev_screen = "menu"
            var_reset = True
          elif event.pos[0] in range(230,370) and event.pos[1] in range(300,350):
            current_screen = "help"
            prev_screen = "menu"
            page = 1
    #screen updates
    if True:
      screen.fill(GREEN)

      screen.blit(logo,(65,100))
      screen.blit(playsurf,(230,230))
      screen.blit(helpsurf,(230,300))

      pygame.display.flip()
  
  #help
  if current_screen == "help":
    #event management
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(230,370) and event.pos[1] in range(350,400):
            current_screen = prev_screen
          elif event.pos[0] in range(460,600) and event.pos[1] in range(350,400) and page <= 3:
            page += 1
          elif event.pos[0] in range(0,140) and event.pos[1] in range(350,400) and page > 1:
            page -= 1
    #screen updates
    if True:
      screen.fill(DARKBLUE)

      screen.blit(tinyfont.render("P"+str(page),True,WHITE),(0,0))
      screen.blit(backsurf,(230,350))
      if page <= 3:
        screen.blit(nextsurf,(460,350))
      if page > 1:
        screen.blit(prevsurf,(0,350))
      if page == 1:
        screen.blit(instrtxt,(175,5))
        screen.blit(hsurf,(0,50))
        screen.blit(exprtxt,(180,200))
        screen.blit(p_s_txt,(15,255))
        screen.blit(divtxt,(15,280))
      elif page == 2:
        screen.blit(keytxt,(190,5))
        screen.blit(prmtxt,(205,50))
        screen.blit(rtdesc,(0,80))
        screen.blit(ptdesc,(100,80))
        screen.blit(otdesc,(200,80))
        screen.blit(gtdesc,(300,80))
        screen.blit(btdesc,(400,80))
        screen.blit(ytdesc,(500,80))
      elif page == 3:
        screen.blit(keytxt,(190,5))
        screen.blit(scdtxt,(185,50))
        screen.blit(htdesc,(0,80))
        screen.blit(dtdesc,(120,80))
        screen.blit(mtdesc,(240,80))
        screen.blit(m2tdesc,(360,80))
        screen.blit(ntdesc,(480,80))
      elif page == 4:
        bltssurf.fill(INVIS)
        for i in range(len(hblts)):
          hblts[i] += 2
          if hblts[i] > 80:
            hblts[i] -= 80
          pygame.draw.circle(bltssurf,RED,[hblts[i],25],4)
        bltsurf.fill(INVIS)
        bltsurf.blit(bltsub1,(80,5))
        bltsurf.blit(bltsub2,(80,33))
        bltsurf.blit(bltssurf,(-5,0))
        weapsurf.fill(INVIS)
        weapsurf.blit(weaptxt,(200,0))
        weapsurf.blit(gunsurf,(0,50))
        weapsurf.blit(mslnsurf,(0,100))
        weapsurf.blit(bltsurf,(0,165))
        weapsurf.blit(mslssurf,(0,215))
        weapsurf.blit(stinsurf1,(10,280))
        weapsurf.blit(stinsurf2,(10,300))
        weapsurf.blit(stinsurf3,(10,320))
        screen.blit(weapsurf,(0,0))

      pygame.display.flip()
  
  #difficulty
  if current_screen == "difslct":
    #event management
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(200,400) and event.pos[1] in range(60,110):
            dif = "easy"
            ptrq = 150
            current_screen = "game"
          elif event.pos[0] in range(200,400) and event.pos[1] in range(130,180):
            dif = "med"
            ptrq = 250
            current_screen = "game"
          elif event.pos[0] in range(200,400) and event.pos[1] in range(200,250):
            dif = "hard"
            ptrq = 500
            current_screen = "game"
          elif event.pos[0] in range(155,445) and event.pos[1] in range(270,320):
            dif = "impos"
            ptrq = 1000
            current_screen = "game"
          elif event.pos[0] in range(230,370) and event.pos[1] in range(350,400):
            current_screen = prev_screen
    #screen updates
    if True:
      screen.fill(GREEN)

      screen.blit(diftxt,(90,5))
      screen.blit(easysurf,(200,60))
      screen.blit(medsurf,(200,130))
      screen.blit(hardsurf,(200,200))
      screen.blit(impossurf,(155,270))
      screen.blit(backsurf,(230,350))

      pygame.display.flip()

  #game
  if current_screen == "game":
    #event management
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.WINDOWFOCUSLOST:
        paused = 1
      #mouse
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if paused == 1:
            if event.pos[0] in range(230,370) and event.pos[1] in range(210,260):
              current_screen = "menu"
              var_reset = True
            elif event.pos[0] in range(230,370) and event.pos[1] in range(280,330):
              current_screen = "help"
              prev_screen = "game"
              page = 1
      #keyboard functions
      if True:
        #key press
        if event.type == pygame.KEYDOWN:
          #movement keys
          if paused != 1:
            if event.key == pygame.K_w:
              move_up = "yes"
            if event.key == pygame.K_s:
              move_down = "yes"
            if event.key == pygame.K_d:
              move_right = "yes"
            if event.key == pygame.K_a:
              move_left = "yes"
            #speed modifying keys
            if True:
              if event.key == pygame.K_q:
                s_lock *= -1
              if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                if s_lock == 1:
                  speed_mod = 0.25
                else:
                  speed_mod = 0.5
              if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT and s_lock == -1:
                speed_mod = 2
          #cheat keys
          if True:
            if event.key == pygame.K_o:
              o_p = True
            if event.key == pygame.K_p:
              p_p = True
            if o_p == True and p_p == True:
              if event.key == pygame.K_m:
                speed += 10
              if event.key == pygame.K_n:
                speed -= 10
              if event.key == pygame.K_k:
                hlth = 0
              if event.key == pygame.K_b:
                blt_mspd += 3
                blt_fspd += 10
                msl_mspd += 2
              if event.key == pygame.K_v:
                blt_mspd -= 3
                blt_fspd -= 10
              if event.key == pygame.K_i:
                score += ptrq
              if event.key == pygame.K_j:
                count += 25
              if event.key == pygame.K_u:
                msl += 5
              if event.key == pygame.K_h:
                hlth += 5
                max_hlth += 5
          #weapon keys
          if paused != 1:
            if event.key == pygame.K_1:
              weapon = "gun"
            if event.key == pygame.K_2:
              weapon = "launcher"
            if event.key == pygame.K_RETURN:
              firing = True
              en_p = True
            if event.key == pygame.K_SPACE:
              firing = True
              sp_p = True
            if event.key == pygame.K_UP:
              if facing == "r" or facing == "rd":
                facing = "ru"
              if facing == "l" or facing == "ld":
                facing = "lu"
            if event.key == pygame.K_DOWN:
              if facing == "r" or facing == "ru":
                facing = "rd"
              if facing == "l" or facing == "lu":
                facing = "ld"
            if event.key == pygame.K_RIGHT:
              if facing == "lu":
                facing = "ru"
              elif facing == "ld":
                facing = "rd"
              else:
                facing = "r"
            if event.key == pygame.K_LEFT:
              if facing == "ru":
                facing = "lu"
              elif facing == "rd":
                facing = "ld"
              else:
                facing = "l"
          #misc. keys
          if True:
            if event.key == pygame.K_e:
              show_stats *= -1
            if event.key == pygame.K_ESCAPE:
              paused *= -1
              pause_timer = 0
        #key release
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_w:
            move_up = "no"
          if event.key == pygame.K_s:
            move_down = "no"
          if event.key == pygame.K_d:
            move_right = "no"
          if event.key == pygame.K_a:
            move_left = "no"
          if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
            speed_mod = 1
          if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            speed_mod = 1
          if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
            speed_mod = 1
          if event.key == pygame.K_RETURN:
            en_p = False
            if sp_p == False:
              firing = False
          if event.key == pygame.K_SPACE:
            sp_p = False
            if en_p == False:
              firing = False
          if event.key == pygame.K_o:
            o_p = False
          if event.key == pygame.K_p:
            p_p = False
    
    if score >= ptrq:
      current_screen = "win"
      show_stats = 0
    if hlth <= 0:
      current_screen = "game over"
      show_stats = 0

    #constant update variables
    if True:
      if paused == -1:
        pygame.mouse.set_visible(False)
      elif paused == 1:
        pygame.mouse.set_visible(True)
      move_speed = round(speed*speed_mod,1)
      if s_lock == 1:
        move_speed *= 2
      atick = round(clock.get_fps(),1)
      scoresurf = smallfont.render("Points: "+str(score),True,BLACK)
      mslsurf = smallfont.render("Missles: "+str(msl),True,BLACK)
      spdsurf = smallfont.render("Speed: "+str(round(move_speed*TICK))+"p/s",True,BLACK)
      if s_lock == 1:
        slcksurf = smallfont.render("Speed lock: On",True,BLACK)
      elif s_lock == -1:
        slcksurf = smallfont.render("Speed lock: Off",True,BLACK)
      bmssurf = smallfont.render("Bullet movement speed: "+str(round(blt_mspd*TICK))+"p/s",True,BLACK)
      bfssurf = smallfont.render("Bullet fire rate: "+str(blt_fspd*(TICK/60))+"/s",True,BLACK)
      mmssurf = smallfont.render("Missile movement speed: "+str(round(msl_mspd*TICK))+"p/s",True,BLACK)
      mfssurf = smallfont.render("Missile fire rate: "+str(round(msl_fspd,1)*(TICK/60))+"/s",True,BLACK)
      mrfsurf = smallfont.render("Missile refill per target: "+str(msl_rf),True,BLACK)
      countsurf = smallfont.render("Targets until next wall: "+str(5-count),True,BLACK)
      targsurf = smallfont.render("Current target types: "+t_type+","+t_type2,True,BLACK)
      tartmsurf = smallfont.render("Time left for target: "+str(round(((targ_timer_end*TICK)-targ_timer)/TICK,1))+"s",True,BLACK)
      mfpssurf = smallfont.render("Optimal framerate: "+str(TICK)+"fps",True,BLACK)
      afpssurf = smallfont.render("Current framerate: "+str(atick)+"("+str(round((atick/TICK)*100,1))+"%)fps",True,BLACK)
      if dif == "med":
        difsurf = smallfont.render("Difficulty: normal",True,BLACK)
      elif dif == "impos":
        difsurf = smallfont.render("Difficulty: impossible",True,BLACK)
      else:
        difsurf = smallfont.render("Difficulty: "+dif,True,BLACK)
      if hlth > max_hlth:
        hlth -=1
      #stats
      if True:
        statsurf.fill(INVIS)
        statsurf.set_alpha(150)
        statsurf.blit(spdsurf,(254,0))
        statsurf.blit(slcksurf,(208,20))
        statsurf.blit(bmssurf,(84,40))
        statsurf.blit(bfssurf,(175,60))
        statsurf.blit(mmssurf,(71,80))
        statsurf.blit(mfssurf,(162,100))
        statsurf.blit(mrfsurf,(92,120))
        statsurf.blit(countsurf,(97,140))
        if dif == "impos":
          statsurf.blit(difsurf,(188,160))
        else:
          statsurf.blit(difsurf,(223,160))
        statsurf.blit(tartmsurf,(132,180))
        if t_type2 == "Light Purple":
          statsurf.blit(targsurf,(0,200)) 
        elif t_type2 == "Light Gray":
          statsurf.blit(targsurf,(15,200))
        else:
          statsurf.blit(targsurf,(47,200))
        statsurf.blit(mfpssurf,(132,355-hlth_offset))
        statsurf.blit(afpssurf,(60,375-hlth_offset))
      #hud
      if True:
        hud.set_alpha(230)
        hud.fill(INVIS)
        #health
        hlth_offset = 30*((max_hlth//17)+1)
        h_ox = 5
        h_oy = 0
        for i in range(max_hlth):
          pygame.draw.polygon(hud,GRAY,[(h_ox,12.5+h_oy),(h_ox+15,27.5+h_oy),(h_ox+30,12.5+h_oy),(h_ox+27.25,7.75+h_oy),(h_ox+22.5,5+h_oy),(h_ox+17.75,7.75+h_oy),(h_ox+15,10+h_oy),(h_ox+12.25,7.75+h_oy),(h_ox+7.5,5+h_oy),(h_ox+2.75,7.75+h_oy)])
          pygame.draw.arc(hud,GRAY,[h_ox,3.5+h_oy,16,18],0,pi,50)
          pygame.draw.arc(hud,GRAY,[h_ox+15,3.5+h_oy,16,18],0,pi,50)
          h_ox += 35
          if h_ox > 595:
            h_ox = 5
            h_oy += 30
        h_ox = 5
        h_oy = 0
        for i in range(hlth):
          pygame.draw.polygon(hud,RED,[(h_ox,12.5+h_oy),(h_ox+15,27.5+h_oy),(h_ox+30,12.5+h_oy),(h_ox+27.25,7.75+h_oy),(h_ox+22.5,5+h_oy),(h_ox+17.75,7.75+h_oy),(h_ox+15,10+h_oy),(h_ox+12.25,7.75+h_oy),(h_ox+7.5,5+h_oy),(h_ox+2.75,7.75+h_oy)])
          pygame.draw.arc(hud,RED,[h_ox,3.5+h_oy,16,18],0,pi,50)
          pygame.draw.arc(hud,RED,[h_ox+15,3.5+h_oy,16,18],0,pi,50)
          h_ox += 35
          if h_ox > 595:
            h_ox = 5
            h_oy += 30
        hud.blit(scoresurf,(5,hlth_offset))
        hud.blit(mslsurf,(5,hlth_offset+20))
        #stats
        if show_stats == 1:
          hud.blit(statsurf,(200,hlth_offset))
        elif show_stats == -1:
          hud.blit(stattxt,(380,hlth_offset))

    #movement
    if True:
      #boundaries
      if True:
        if y < 12:
          move_up = "no"
        if y > 365:
          move_down = "no"
        if x < 10:
          move_left = "no"
        if x > 590:
          move_right = "no"
      #movement
      if True:
        if move_up == "yes":
          y-=move_speed
        if move_down == "yes":
          y+=move_speed
        if move_right == "yes":
          x+=move_speed
        if move_left == "yes":
          x-=move_speed

    #screen updates
    if True:
      screen.fill(GREEN)

      #health backing
      if True:
        h_ox = 5
        h_oy = 0
        for i in range(max_hlth):
          pygame.draw.polygon(screen,WHITE,[(h_ox,12.5+h_oy),(h_ox+15,27.5+h_oy),(h_ox+30,12.5+h_oy),(h_ox+27.25,7.75+h_oy),(h_ox+22.5,5+h_oy),(h_ox+17.75,7.75+h_oy),(h_ox+15,10+h_oy),(h_ox+12.25,7.75+h_oy),(h_ox+7.5,5+h_oy),(h_ox+2.75,7.75+h_oy)])
          pygame.draw.arc(screen,WHITE,[h_ox,3.5+h_oy,16,18],0,pi,50)
          pygame.draw.arc(screen,WHITE,[h_ox+15,3.5+h_oy,16,18],0,pi,50)
          h_ox += 35
          if h_ox > 595:
            h_ox = 5
            h_oy += 30

      #body
      if True:
        pygame.draw.circle(screen,bclr,[x+shake,y-5],5)
        pygame.draw.line(screen,bclr,[x+shake,y],[x+shake,y+20])
        pygame.draw.line(screen,bclr,[x+shake,y+20],[x+shake+5,y+35])
        pygame.draw.line(screen,bclr,[x+shake,y+20],[x+shake-5,y+35])
        #right arm
        if True:
          if facing == "ru":
            pygame.draw.line(screen,bclr,[x+shake,y+5],[x+shake+(10/ANG),y+5-(10/ANG)],2)
          elif facing == "rd":
            pygame.draw.line(screen,bclr,[x+shake,y+6],[x+shake+(10/ANG),y+6+(10/ANG)],2)
          else:
            pygame.draw.line(screen,bclr,[x+shake,y+5],[x+shake+10,y+5])
        #left arm
        if True:
          if facing == "lu":
            pygame.draw.line(screen,bclr,[x+shake-1,y+5],[x+shake-1-(10/ANG),y+5-(10/ANG)],2)
          elif facing == "ld":
            pygame.draw.line(screen,bclr,[x+shake-1,y+4],[x+shake-1-(10/ANG),y+4+(10/ANG)],2)
          else:
            pygame.draw.line(screen,bclr,[x+shake,y+5],[x+shake-10,y+5])

      #targets
      if True:
        #type
        if True:
          #red
          if (dif == "easy" and r in range(0,61)) or (dif == "med" and r in range(0,51)) or (dif == "hard" and r in range(0,44)) or (dif == "impos" and r in range(0,33)):
            t_type = "Red"
            t_c = RED
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 45
            elif dif == "med":
              targ_timer_end = 30
            elif dif == "hard":
              targ_timer_end = 20
            elif dif == "impos":
              targ_timer_end = 5
          #purple
          elif (dif == "easy" and r in range(61,71)) or (dif == "med" and r in range(51,76)) or (dif == "hard" and r in range(44,76)) or (dif == "impos" and r in range(33,73)):
            t_type = "Purple"
            t_c = PURPLE
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 2
            elif dif == "med":
              targ_timer_end = 3.3
            elif dif == "hard":
              targ_timer_end = 4
            elif dif == "impos":
              targ_timer_end = 4.5
          #orange
          elif (dif == "easy" and r in range(71,81)) or (dif == "med" and r in range(76,84)) or (dif == "hard" and r in range(76,82)) or (dif == "impos" and r in range(73,76)):
            t_type = "Orange"
            t_c = ORANGE
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 12
            elif dif == "med":
              targ_timer_end = 8.5
            elif dif == "hard":
              targ_timer_end = 5
            elif dif == "impos":
              targ_timer_end = 2.5
          #green
          elif (dif == "easy" and r in range(81,91)) or (dif == "med" and r in range(84,91)) or (dif == "hard" and r in range(82,88)) or (dif == "impos" and r in range(76,79)):
            t_type = "Green"
            t_c = DARKGREEN
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 12
            elif dif == "med":
              targ_timer_end = 8.5
            elif dif == "hard":
              targ_timer_end = 5
            elif dif == "impos":
              targ_timer_end = 2.5
          #black
          elif (dif == "easy" and r in range(91,93)) or (dif == "med" and r in range(91,96)) or (dif == "hard" and r in range(88,98)) or (dif == "impos" and r in range(79,100)):
            t_type = "Black"
            t_c = BLACK
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 2
            elif dif == "med":
              targ_timer_end = 3
            elif dif == "hard":
              targ_timer_end = 3.4
            elif dif == "impos":
              targ_timer_end = 4
          #yellow
          elif (dif == "easy" and r in range(93,101)) or (dif == "med" and r in range(96,101)) or (dif == "hard" and r in range(98,101)) or (dif == "impos" and r in range(100,101)):
            t_type = "Yellow"
            t_c = YELLOW
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 7
            elif dif == "med":
              targ_timer_end = 3.5
            elif dif == "hard":
              targ_timer_end = 2.5
            elif dif == "impos":
              targ_timer_end = 1.5
          #health
          if t_type != "Purple" and ((dif == "easy" and r2 in range(0,354)) or (dif == "med" and r2 in range(0,268)) or (dif == "hard" and r2 in range(0,222)) or (dif == "impos" and r2 in range(0,84))):
            t_type2 = "Pink"
            t_c2 = PINK
          #damage
          elif t_type == "Purple" and ((dif == "easy" and r2 in range(354,487)) or (dif == "med" and r2 in range(268,468)) or (dif == "hard" and r2 in range(222,535)) or (dif == "impos" and r2 in range(84,584))):
            t_type2 = "Light Purple"
            t_c2 = LILAC
          #missile
          elif (dif == "easy" and r2 in range(487,737)) or (dif == "med" and r2 in range(468,618)) or (dif == "hard" and r2 in range(535,635)) or (dif == "impos" and r2 in range(584,634)):
            t_type2 = "Light Gray"
            t_c2 = LIGHTGRAY
          #missile2
          elif (dif == "easy" and r2 in range(737,787)) or (dif == "med" and r2 in range(618,638)) or (dif == "hard" and r2 in range(635,645)) or (dif == "impos" and r2 in range(634,639)):
            t_type2 = "Gray"
            t_c2 = GRAY
          #none
          else:
            t_type2 = "White"
            t_c2 = WHITE
        #draw
        if True:
          pygame.draw.circle(screen,t_c,[t_x,t_y],15)
          pygame.draw.circle(screen,t_c2,[t_x,t_y],10)
          pygame.draw.circle(screen,t_c,[t_x,t_y],5)
        #properties
        if collide == True:
          if t_type == "Red":
            score += 2
            count += 1
          elif t_type == "Purple":
            hlth -= 1
            bclr = RED
            do_hrttmr = True
            score -= 5
          elif t_type == "Orange":
            blt_mspd += 0.1
            blt_fspd += 1
            msl_mspd += 0.2
            msl_fspd += 0.1
            count += 1
            score += 1
          elif t_type == "Green":
            speed += 0.1
            count += 1
            score += 1
          elif t_type == "Black":
            count += 25
            score -= 5
          elif t_type == "Yellow":
            score += 10
            count += 1
            max_hlth += 1
            hlth += 1
          if t_type2 == "Pink":
            hlth += 1
          elif t_type2 == "Light Purple":
            hlth -= 1
          elif t_type2 == "Light Gray":
            msl += msl_rf
          elif t_type2 == "Gray":
            msl_rf += 1
          reset = True
          collide = False
          do_targ_timer = False
          targ_timer = 0
        #new values
        if reset == True:
          r = random.randint(0,100)
          r2 = random.randint(0,1000)
          t_x = random.randrange(15,585)
          t_y = random.randrange(15,380)
          reset = False
        #timers
        if paused != 1:
          #target timer
          if do_targ_timer == True:
            targ_timer += 1
            if targ_timer == (targ_timer_end * TICK):
              do_targ_timer = False
              targ_timer = 0
              targ_timer_end = 0
              reset = True
          #damage timer
          if do_hrttmr == True:
            hrttmr += 1
            if hrttmr % 2 == 0:
              shake = -1
            elif hrttmr % 2 == 1:
              shake = 1
            if hrttmr == 15:
              do_hrttmr = False
              hrttmr = 0
              bclr = BLACK
              shake = 0
          #target residue
          for i in range(len(gt)):
            if gt[i][3] == "Purple":
              pygame.draw.circle(screen,[255,0,0,10],[gt[i][0],gt[i][1]],15)
            else:
              pygame.draw.circle(screen,[0,240,0,200],[gt[i][0],gt[i][1]],15)
            gt[i][2] += 1
            if gt[i][2] == 7:
              del(gt[i])
              break

      #gun
      if weapon == "gun":
        if facing == "r":
          pygame.draw.polygon(screen,BLACK,[(x+9,y+7),(x+9,y+1),(x+17,y),(x+17,y+3),(x+11,y+3),(x+11,y+7)])
          guntip = [x+17,y+2]
        elif facing == "l":
          pygame.draw.polygon(screen,BLACK,[(x-9,y+7),(x-9,y+1),(x-17,y),(x-17,y+3),(x-11,y+3),(x-11,y+7)])
          guntip = [x-17,y+2]
        elif facing == "ru":
          pygame.draw.polygon(screen,BLACK,[(x+2+(9/ANG),y+7-(9/ANG)),(x+1+(5/ANG),y+7-(15/ANG)),(x+2+(11/ANG),y+7-(23/ANG)),(x+2+(13/ANG),y+7-(21/ANG)),(x+4+(5/ANG),y+7-(15/ANG)),(x+2+(11/ANG),y+7-(12/ANG))])
          guntip = [x+2+(12/ANG),y+7-(22/ANG)]
        elif facing == "rd":
          pygame.draw.polygon(screen,BLACK,[(x+(9/ANG),y+7+(9/ANG)),(x+(15/ANG),y+6+(5/ANG)),(x+(23/ANG),y+7+(11/ANG)),(x+(21/ANG),y+7+(13/ANG)),(x+(15/ANG),y+9+(5/ANG)),(x+(11/ANG),y+7+(12/ANG))])
          guntip = [x+(22/ANG),y+7+(12/ANG)]
        elif facing == "lu":
          pygame.draw.polygon(screen,BLACK,[(x-2-(9/ANG),y+7-(9/ANG)),(x-1-(5/ANG),y+7-(15/ANG)),(x-2-(11/ANG),y+7-(23/ANG)),(x-2-(13/ANG),y+7-(21/ANG)),(x-4-(5/ANG),y+7-(15/ANG)),(x-2-(11/ANG),y+7-(12/ANG))])
          guntip = [x-2-(12/ANG),y+7-(22/ANG)]
        elif facing == "ld":
          pygame.draw.polygon(screen,BLACK,[(x-(9/ANG),y+7+(9/ANG)),(x-(15/ANG),y+6+(5/ANG)),(x-(23/ANG),y+7+(11/ANG)),(x-(21/ANG),y+7+(13/ANG)),(x-(15/ANG),y+9+(5/ANG)),(x-(11/ANG),y+7+(12/ANG))])
          guntip = [x-(22/ANG),y+7+(12/ANG)]

      #bullets
      if True:
        #cooldown
        if paused == -1:
          if fire_timer_g > 0:
            fire_timer_g -= blt_fspd
          if fire_timer_g < 0:
            fire_timer_g = 0
        #values
        if firing == True and fire_timer_g == 0 and weapon == "gun":
          bx = guntip[0]
          by = guntip[1]
          if facing == "r":
            dofx = blt_mspd
            dofy = 0
          elif facing == "l":
            dofx = -blt_mspd
            dofy = 0
          elif facing == "ru":
            dofx = (blt_mspd/ANG)
            dofy = -(blt_mspd/ANG)
          elif facing == "rd":
            dofx = (blt_mspd/ANG)
            dofy = (blt_mspd/ANG)
          elif facing == "lu":
            dofx = -(blt_mspd/ANG)
            dofy = -(blt_mspd/ANG)
          elif facing == "ld":
            dofx = -(blt_mspd/ANG)
            dofy = (blt_mspd/ANG)
          blts.append([bx,by,dofx,dofy])
          fire_timer_g = 60
        #management
        for i in range(len(blts)):
          pygame.draw.circle(screen,RED,[blts[i][0],blts[i][1]],1)
          if paused != 1:
            blts[i][0]+=blts[i][2]
            blts[i][1]+=blts[i][3]
          if blts[i][0] < 0 or blts[i][0] > 600:
            del blts[i]
            break
          if blts[i][0] >= t_x-15 and blts[i][0] <= t_x+15 and blts[i][1] >= t_y-15 and blts[i][1] <= t_y+15:
            collide = True
            del blts[i]
            gt.append([t_x,t_y,0,t_type])
            break

      #missles
      if True:
        #cooldown
        if paused == -1:
          if fire_timer_m > 0:
            fire_timer_m -= msl_fspd
          if fire_timer_m < 0:
            fire_timer_m = 0
        #values
        if firing == True and fire_timer_m == 0 and weapon == "launcher" and msl > 0:
          mx = guntip[0]
          my = guntip[1]
          if facing == "r":
            dofx = msl_mspd
            dofy = 0
          elif facing == "l":
            dofx = -msl_mspd
            dofy = 0
          elif facing == "ru":
            dofx = (msl_mspd/ANG)
            dofy = -(msl_mspd/ANG)
          elif facing == "rd":
            dofx = (msl_mspd/ANG)
            dofy = (msl_mspd/ANG)
          elif facing == "lu":
            dofx = -(msl_mspd/ANG)
            dofy = -(msl_mspd/ANG)
          elif facing == "ld":
            dofx = -(msl_mspd/ANG)
            dofy = (msl_mspd/ANG)
          msls.append([mx,my,dofx,dofy,facing])
          msl -= 1
          fire_timer_m = 60
        #management
        for i in range(len(msls)):
          if msls[i][4] == "r":
            pygame.draw.rect(screen,GRAY,[msls[i][0]-6,msls[i][1]-2,13,5])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+7,msls[i][1]-2),(msls[i][0]+7,msls[i][1]+2),(msls[i][0]+6+(2.5*math.sqrt(3)),msls[i][1])])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-6,msls[i][1]-3),(msls[i][0]-2,msls[i][1]-3),(msls[i][0]-5,msls[i][1]-5),(msls[i][0]-8,msls[i][1]-5)])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-6,msls[i][1]+3),(msls[i][0]-2,msls[i][1]+3),(msls[i][0]-5,msls[i][1]+5),(msls[i][0]-8,msls[i][1]+5)])
          elif msls[i][4] == "l":
            pygame.draw.rect(screen,GRAY,[msls[i][0]-6,msls[i][1]-2,13,5])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-7,msls[i][1]-2),(msls[i][0]-7,msls[i][1]+2),(msls[i][0]-6-(2.5*math.sqrt(3)),msls[i][1])])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+6,msls[i][1]-3),(msls[i][0]+2,msls[i][1]-3),(msls[i][0]+5,msls[i][1]-5),(msls[i][0]+8,msls[i][1]-5)])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+6,msls[i][1]+3),(msls[i][0]+2,msls[i][1]+3),(msls[i][0]+5,msls[i][1]+5),(msls[i][0]+8,msls[i][1]+5)])
          elif msls[i][4] == "ru":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]-(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]+(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)),msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-2,msls[i][1]-(8/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(8/ANG),msls[i][1]+(3/ANG)),(msls[i][0]-(5/ANG),msls[i][1]-(1/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(1/ANG)),(msls[i][0]-(12/ANG),msls[i][1]+(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(3/ANG),msls[i][1]+(9/ANG)),(msls[i][0]+(1/ANG),msls[i][1]+(5/ANG)),(msls[i][0],msls[i][1]+(8/ANG)),(msls[i][0]-(3/ANG),msls[i][1]+(12/ANG))])
          elif msls[i][4] == "rd":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)),msls[i][1]+(8/ANG)-(5*-math.sin(pi/12))),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-2,msls[i][1]+(8/ANG)-(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(8/ANG),msls[i][1]-(3/ANG)),(msls[i][0]-(5/ANG),msls[i][1]+(1/ANG)),(msls[i][0]-(8/ANG),msls[i][1]+(1/ANG)),(msls[i][0]-(12/ANG),msls[i][1]-(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(3/ANG),msls[i][1]-(9/ANG)),(msls[i][0]+(1/ANG),msls[i][1]-(5/ANG)),(msls[i][0],msls[i][1]-(8/ANG)),(msls[i][0]-(3/ANG),msls[i][1]-(12/ANG))])
          elif msls[i][4] == "lu":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12)),msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12))+2,msls[i][1]-(8/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(8/ANG),msls[i][1]+(3/ANG)),(msls[i][0]+(5/ANG),msls[i][1]-(1/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(1/ANG)),(msls[i][0]+(12/ANG),msls[i][1]+(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(3/ANG),msls[i][1]+(9/ANG)),(msls[i][0]-(1/ANG),msls[i][1]+(5/ANG)),(msls[i][0]-(1/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(3/ANG),msls[i][1]+(12/ANG))])
          elif msls[i][4] == "ld":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]+(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]-(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12)),msls[i][1]+(8/ANG)-(5*-math.sin(pi/12))),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12))+2,msls[i][1]+(8/ANG)-(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(8/ANG),msls[i][1]-(3/ANG)),(msls[i][0]+(5/ANG),msls[i][1]+(1/ANG)),(msls[i][0]+(8/ANG),msls[i][1]+(1/ANG)),(msls[i][0]+(12/ANG),msls[i][1]-(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(3/ANG),msls[i][1]-(9/ANG)),(msls[i][0]-(1/ANG),msls[i][1]-(5/ANG)),(msls[i][0]-(1/ANG),msls[i][1]-(8/ANG)),(msls[i][0]+(3/ANG),msls[i][1]-(12/ANG))])
          if paused != 1:
            msls[i][0]+=msls[i][2]
            msls[i][1]+=msls[i][3]
          if msls[i][0] < 0 or msls[i][0] > 600:
            del msls[i]
            break
          if msls[i][4] == "r":
            for j in range(round(msls[i][0]-6),round(msls[i][0]+12)):
              for k in range(round(msls[i][1]-2),round(msls[i][1]+3)):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          elif msls[i][4] == "l":
            for j in range(round(msls[i][0]-12),round(msls[i][0]+6)):
              for k in range(round(msls[i][1]-2),round(msls[i][1]+3)):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          elif msls[i][4] == "ru":
            for j in range(round(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-(msl_mspd+1)),round(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)))):
              for k in range(round(msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),round(msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))+(msl_mspd+1))):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          elif msls[i][4] == "rd":
            for j in range(round(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-(msl_mspd+1)),round(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)))):
              for k in range(round(msls[i][1]+(8/ANG)+(5*-math.sin(pi/12))-(msl_mspd+1)),round(msls[i][1]+(8/ANG)+(5*-math.sin(pi/12)))):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          elif msls[i][4] == "lu":
            for j in range(round(msls[i][0]-(4/ANG)-(5*-math.cos(pi/12))),round(msls[i][0]-(4/ANG)-(5*-math.cos(pi/12))+(msl_mspd+1))):
              for k in range(round(msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),round(msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))+(msl_mspd+1))):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          elif msls[i][4] == "ld":
            for j in range(round(msls[i][0]-(4/ANG)-(5*-math.cos(pi/12))),round(msls[i][0]-(4/ANG)-(5*-math.cos(pi/12))+(msl_mspd+1))):
              for k in range(round(msls[i][1]+(8/ANG)+(5*-math.sin(pi/12))-(msl_mspd+1)),round(msls[i][1]+(8/ANG)+(5*-math.sin(pi/12)))):
                if j in range(t_x-15,t_x+16) and k in range(t_y-15,t_y+16):
                  collide = True
                  del(msls[i])
                  gt.append([t_x,t_y,0,t_type])
                  do_break = True
                  break
              if do_break == True:
                break
          if do_break == True:
            do_break = False
            break

      #missile launcher
      if weapon == "launcher":
        if facing == "r":
          pygame.draw.polygon(screen,BLACK,[(x+5,y+4),(x+10,y+3),(x+20,y+2),(x+20,y+8),(x+10,y+7),(x+5,y+6)])
          guntip = [x+15,y+5]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x+21,y+3),(x+21,y+7),(x+20+(2.5*math.sqrt(3)),y+5)])
            pygame.draw.polygon(screen,RED,[(x+9,y+2),(x+13,y+2),(x+10,y),(x+7,y)])
            pygame.draw.polygon(screen,RED,[(x+9,y+8),(x+13,y+8),(x+10,y+10),(x+7,y+10)])
        elif facing == "l":
          pygame.draw.polygon(screen,BLACK,[(x-5,y+4),(x-10,y+3),(x-20,y+2),(x-20,y+8),(x-10,y+7),(x-5,y+6)])
          guntip = [x-15,y+5]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x-21,y+3),(x-21,y+7),(x-20-(2.5*math.sqrt(3)),y+5)])
            pygame.draw.polygon(screen,RED,[(x-9,y+2),(x-13,y+2),(x-10,y),(x-7,y)])
            pygame.draw.polygon(screen,RED,[(x-9,y+8),(x-13,y+8),(x-10,y+10),(x-7,y+10)])
        elif facing == "ru":
          pygame.draw.polygon(screen,BLACK,[(x+(5/ANG),y+4-(5/ANG)),(x+(9/ANG),y+3-(9/ANG)),(x-1+(19/ANG),y+2-(17/ANG)),(x+2+(21/ANG),y+12-(26/ANG)),(x+(12/ANG),y+8-(9/ANG)),(x+(12/ANG),y+8-(12/ANG)),(x+2+(5/ANG),y+6-(5/ANG))])
          guntip = [x+(16/ANG),y+7-(18/ANG)]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x+1+(19/ANG),y+6-(23/ANG)),(x+1+(23/ANG),y+6-(19/ANG)),(x+1+(19/ANG)-(5*-math.cos(pi/12)),y+6-(23/ANG)+(5*-math.sin(pi/12))),(x-1+(19/ANG)-(5*-math.cos(pi/12)),y+6-(23/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(x+1+(7/ANG),y+5-(12/ANG)),(x+1+(10/ANG),y+5-(16/ANG)),(x+1+(7/ANG),y+5-(16/ANG)),(x+1+(3/ANG),y+5-(12/ANG))])
            pygame.draw.polygon(screen,RED,[(x+1+(12/ANG),y+6-(6/ANG)),(x+1+(16/ANG),y+6-(10/ANG)),(x+1+(15/ANG),y+6-(7/ANG)),(x+1+(12/ANG),y+6-(3/ANG))])
        elif facing == "rd":
          pygame.draw.polygon(screen,BLACK,[(x+(5/ANG),y+6+(5/ANG)),(x+(9/ANG),y+7+(9/ANG)),(x-1+(19/ANG),y+8+(17/ANG)),(x+2+(21/ANG),y-2+(26/ANG)),(x+(14/ANG),y+2+(12/ANG)),(x+(12/ANG),y+2+(12/ANG)),(x+2+(5/ANG),y+4+(5/ANG))])
          guntip = [x+(16/ANG),y+3+(18/ANG)]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x+(19/ANG),y+5+(23/ANG)),(x+(23/ANG),y+5+(19/ANG)),(x+(19/ANG)-(5*-math.cos(pi/12)),y+5+(23/ANG)-(5*-math.sin(pi/12))),(x-2+(19/ANG)-(5*-math.cos(pi/12)),y+5+(23/ANG)-(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(x+1+(7/ANG),y+6+(12/ANG)),(x+1+(10/ANG),y+6+(16/ANG)),(x+1+(7/ANG),y+6+(16/ANG)),(x+1+(3/ANG),y+6+(12/ANG))])
            pygame.draw.polygon(screen,RED,[(x+1+(12/ANG),y+5+(6/ANG)),(x+1+(16/ANG),y+5+(10/ANG)),(x+1+(15/ANG),y+5+(7/ANG)),(x+1+(12/ANG),y+5+(3/ANG))])
        elif facing == "lu":
          pygame.draw.polygon(screen,BLACK,[(x-(5/ANG),y+4-(5/ANG)),(x-(9/ANG),y+3-(9/ANG)),(x+1-(19/ANG),y+2-(17/ANG)),(x-2-(21/ANG),y+12-(26/ANG)),(x-(12/ANG),y+8-(9/ANG)),(x-(12/ANG),y+8-(12/ANG)),(x-2-(5/ANG),y+6-(5/ANG))])
          guntip = [x-(16/ANG),y+7-(18/ANG)]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x-1-(19/ANG),y+6-(23/ANG)),(x-1-(23/ANG),y+6-(19/ANG)),(x-1-(19/ANG)+(5*-math.cos(pi/12)),y+6-(23/ANG)+(5*-math.sin(pi/12))),(x+1-(19/ANG)+(5*-math.cos(pi/12)),y+6-(23/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(x-1-(7/ANG),y+5-(12/ANG)),(x-1-(10/ANG),y+5-(16/ANG)),(x-1-(7/ANG),y+5-(16/ANG)),(x-1-(3/ANG),y+5-(12/ANG))])
            pygame.draw.polygon(screen,RED,[(x-1-(12/ANG),y+6-(6/ANG)),(x-1-(16/ANG),y+6-(10/ANG)),(x-1-(15/ANG),y+6-(7/ANG)),(x-1-(12/ANG),y+6-(3/ANG))])
        elif facing == "ld":
          pygame.draw.polygon(screen,BLACK,[(x-(5/ANG),y+6+(5/ANG)),(x-(9/ANG),y+7+(9/ANG)),(x+1-(19/ANG),y+8+(17/ANG)),(x-2-(21/ANG),y-2+(26/ANG)),(x-(14/ANG),y+2+(12/ANG)),(x-(12/ANG),y+2+(12/ANG)),(x-2-(5/ANG),y+4+(5/ANG))])
          guntip = [x-(16/ANG),y+3+(18/ANG)]
          if fire_timer_m == 0 and msl > 0:
            pygame.draw.polygon(screen,RED,[(x-(19/ANG),y+5+(23/ANG)),(x-(23/ANG),y+5+(19/ANG)),(x-(19/ANG)+(5*-math.cos(pi/12)),y+5+(23/ANG)-(5*-math.sin(pi/12))),(x+2-(19/ANG)+(5*-math.cos(pi/12)),y+5+(23/ANG)-(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(x-1-(7/ANG),y+6+(12/ANG)),(x-1-(10/ANG),y+6+(16/ANG)),(x-1-(7/ANG),y+6+(16/ANG)),(x-1-(3/ANG),y+6+(12/ANG))])
            pygame.draw.polygon(screen,RED,[(x-1-(12/ANG),y+5+(6/ANG)),(x-1-(16/ANG),y+5+(10/ANG)),(x-1-(15/ANG),y+5+(7/ANG)),(x-1-(12/ANG),y+5+(3/ANG))])

      #walls
      if True:
        #values
        if count >= 5:
          count -= 5
          wx=random.randrange(25,575)
          wy=random.randrange(40,350)
          walls.append([wx,wy])
        #management
        for i in range(len(walls)):
          pygame.draw.line(screen,[50,50,50],(walls[i][0],walls[i][1]-15),(walls[i][0],walls[i][1]+15),3)
          for j in range(len(blts)):
            if blts[j][0]>=(walls[i][0]-(blt_mspd/2)) and blts[j][0]<=(walls[i][0]+(blt_mspd/2)) and blts[j][1]>=(walls[i][1]-15) and blts[j][1]<=(walls[i][1]+15):
              del(blts[j])
              break
          for j in range(len(msls)):
            if msls[j][4] == "r":
              for k in range(round(msls[j][0]-6),round(msls[j][0]+12)):
                for l in range(round(msls[j][1]-2),round(msls[j][1]+3)):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            elif msls[j][4] == "l":
              for k in range(round(msls[j][0]-12),round(msls[j][0]+6)):
                for l in range(round(msls[j][1]-2),round(msls[j][1]+3)):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            elif msls[j][4] == "ru":
              for k in range(round(msls[j][0]+(4/ANG)-(5*-math.cos(pi/12))-(msl_mspd+1)),round(msls[j][0]+(4/ANG)-(5*-math.cos(pi/12)))):
                for l in range(round(msls[j][1]-(8/ANG)+(5*-math.sin(pi/12))),round(msls[j][1]-(8/ANG)+(5*-math.sin(pi/12))+(msl_mspd+1))):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            elif msls[j][4] == "rd":
              for k in range(round(msls[j][0]+(4/ANG)-(5*-math.cos(pi/12))-(msl_mspd+1)),round(msls[j][0]+(4/ANG)-(5*-math.cos(pi/12)))):
                for l in range(round(msls[j][1]+(8/ANG)+(5*-math.sin(pi/12))-(msl_mspd+1)),round(msls[j][1]+(8/ANG)+(5*-math.sin(pi/12)))):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            elif msls[j][4] == "lu":
              for k in range(round(msls[j][0]-(4/ANG)-(5*-math.cos(pi/12))),round(msls[j][0]-(4/ANG)-(5*-math.cos(pi/12))+(msl_mspd+1))):
                for l in range(round(msls[j][1]-(8/ANG)+(5*-math.sin(pi/12))),round(msls[j][1]-(8/ANG)+(5*-math.sin(pi/12))+(msl_mspd+1))):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            elif msls[j][4] == "ld":
              for k in range(round(msls[j][0]-(4/ANG)-(5*-math.cos(pi/12))),round(msls[j][0]-(4/ANG)-(5*-math.cos(pi/12))+(msl_mspd+1))):
                for l in range(round(msls[j][1]+(8/ANG)+(5*-math.sin(pi/12))-(msl_mspd+1)),round(msls[j][1]+(8/ANG)+(5*-math.sin(pi/12)))):
                  if k in range(walls[i][0]-1,walls[i][0]+2) and l in range(walls[i][1]-15,walls[i][1]+16):
                    del(msls[j])
                    do_break = True
                    break
                if do_break == True:
                  break
            if do_break == True:
              break
          if do_break == True:
            del(walls[i])
            do_break = False
            break

      screen.blit(hud,(0,0))

      #pause
      if paused == 1:
        screen.blit(pausesurf,(0,0))
        pause_timer += 1
        if pause_timer > 45:
          pause_timer = -45
        if pause_timer > 0:
          screen.blit(pausetxt,(220,150))
        screen.blit(menusurf,(230,210))
        screen.blit(helpsurf,(230,280))

      pygame.display.flip()
  
  #win
  if current_screen == "win":
    pygame.mouse.set_visible(True)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(100,200) and event.pos[1] in range(275,325):
            current_screen = "game"
            var_reset = True
          elif event.pos[0] in range(400,500) and event.pos[1] in range(275,325):
            current_screen = "menu"
    if fadewhite[3] < 250 :
      fadewhite[3] += 2
    winsurf.fill(fadewhite)
    winsurf.blit(hud,(0,0))
    if dif == "impos":
      winsurf.blit(difsurf,(388,hlth_offset))
    else:
      winsurf.blit(difsurf,(423,hlth_offset))
    winsurf.blit(winsubsurf,(150,150))
    winsurf.blit(resurf,(70,225))
    winsurf.blit(yessurf,(100,275))
    winsurf.blit(nosurf,(400,275))
    screen.blit(winsurf,(0,0))
    pygame.display.flip()

  #game over
  if current_screen == "game over":
    pygame.mouse.set_visible(True)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(100,200) and event.pos[1] in range(275,325):
            current_screen = "game"
            var_reset = True
          elif event.pos[0] in range(400,500) and event.pos[1] in range(275,325):
            current_screen = "menu"
    if fadeblack[3] < 250 :
      fadeblack[3] += 5
    screen.fill(RED)
    gmovsurf.fill(fadeblack)
    gmovsurf.blit(hud,(0,0))
    if dif == "impos":
      gmovsurf.blit(difsurf,(388,hlth_offset))
    else:
      gmovsurf.blit(difsurf,(423,hlth_offset))
    gmovsurf.blit(gmovsubsurf,(100,150))
    gmovsurf.blit(resurf,(70,225))
    gmovsurf.blit(yessurf,(100,275))
    gmovsurf.blit(nosurf,(400,275))
    screen.blit(gmovsurf,(0,0))
    pygame.display.flip()

  if var_reset == True:
    x = 300
    y = 200
    move_up = "no"
    move_down = "no"
    move_right = "no"
    move_left = "no"
    facing = "r"
    speed = 1
    speed_mod = 1
    s_lock = -1
    fire_timer_g = 0
    blts = []
    blt_mspd = 3
    blt_fspd = 10
    msl = 0
    msls = []
    msl_mspd = 5
    msl_fspd = 1
    msl_rf = 1
    fire_timer_m = 0
    weapon = "gun"
    guntip = [x+17,y+2]
    score = 0
    hlth = 3
    max_hlth = 4
    show_stats = -1
    count = 0
    walls = []
    do_break = False
    reset = False
    collide = False
    r = random.randint(0,100)
    r2 = random.randint(0,1000)
    t_x = random.randrange(15,585)
    t_y = random.randrange(15,385)
    targ_timer = 0
    o_p = False
    p_p = False
    paused = -1
    pause_timer = 0
    page = 1
    var_reset = False
    fadeblack = [10,10,10,0]
    fadewhite = [255,255,255,0]
    bclr = BLACK
    hrttmr = 0 
    do_hrttmr = False

  clock.tick(TICK)

pygame.quit()