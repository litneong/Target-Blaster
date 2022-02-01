import pygame
import math
import random

pygame.init()

#values
if True:
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
      msl = 0
      msls = []
      msl_mspd = 5
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
      do_break = False
    #targets
    if True:
      reset = False
      collide = False
      r = random.randint(0,100)
      r2 = random.randint(0,1000)
      t_x = random.randrange(15,585)
      t_y = random.randrange(15,385)
      targ_timer = 0
      do_targ_timer = False
      targ_timer_end = 0
    #misc.
    if True:
      o_p = False
      p_p = False
      paused = -1
      pause_timer = 0
      done = False
      page = 1
      var_reset = False
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
      DARKGRAY = (100,100,100)
      RED = (255,0,0)
      GREEN = (0,255,0)
      BLUE = (0,0,255)
      YELLOW = (255,255,0)
      PURPLE = (175,0,200)
      LILAC = (220,70,255)
      ORANGE = (255,150,0)
      SKYBLUE = (0,150,255)
      BROWN = (150,100,0)
      DARKGREEN = (0,200,0)
      INVIS = (255,255,255,0)
      PINK = (255,150,150)
      MAROON = (100,0,0)
      fadeblack = [10,10,10,0]
      fadewhite = [255,255,255,0]
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
      screen = pygame.display.set_mode((600,400),pygame.SRCALPHA)
      pygame.display.set_caption("Target Blaster")
      clock = pygame.time.Clock()
      pygame.event.set_blocked(pygame.MOUSEMOTION)
      current_screen = "menu"
      prev_screen = ""
      dif = "med"
    #fonts
    if True:
      tinyfont = pygame.font.SysFont("Comic Sans MS",20)
      smallfont2 = pygame.font.SysFont("Comic Sans MS",22)
      smallfont = pygame.font.SysFont("Comic Sans MS",30)
      medsmlfont2 = pygame.font.SysFont("Comic Sans MS",40)
      medsmlfont = pygame.font.SysFont("Comic Sans MS",45)
      medfont = pygame.font.SysFont("Comic Sans MS",65)
      medbigfont = pygame.font.SysFont("Comic Sans MS",80)
      bigfont = pygame.font.SysFont("Comic Sans MS",100)
    #surfaces/images
    if True:
      hud = pygame.Surface([600,400],pygame.SRCALPHA)
      gmovsurf = pygame.Surface([600,400],pygame.SRCALPHA)
      gmovsubsurf = bigfont.render("Game Over",True,RED)
      resurf = medfont.render("Play again?",True,GRAY)
      winsurf = pygame.Surface([600,400],pygame.SRCALPHA)
      winsubsurf = bigfont.render("You win!",True,YELLOW)
      pausesurf = medfont.render("Paused",True,WHITE)
      logo = bigfont.render("Target Blaster",True,RED)
      statsurf = pygame.Surface([400,400],pygame.SRCALPHA)
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
          rtdescsub1_2 = smallfont2.render("60/50/40/22%",True,WHITE)
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
          rtdesc.blit(rtdescsub3_2,(10,162.5))
          rtdesc.blit(spctxt,(10,180))
          rtdesc.blit(rtdescsub4,(25,200))
          pygame.draw.line(rtdesc,BLACK,(99,0),(99,250))
        #purple
        if True:
          ptdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          ptdescsub1 = medsmlfont.render("Purple",True,PURPLE)
          ptdescsub1_2 = smallfont2.render("15/25/35/50%",True,WHITE)
          ptdescsub2 = smallfont.render("Points: -5",True,WHITE)
          ptdescsub3 = smallfont.render("Time:",True,WHITE)
          ptdescsub3_2 = smallfont2.render("2/3.2/4/10s",True,WHITE)
          ptdescsub4 = smallfont.render("-1 Health",True,WHITE)
          ptdesc.fill(INVIS)
          ptdesc.blit(ptdescsub1,(1,0))
          ptdesc.blit(ptdescsub1_2,(5,35))
          pygame.draw.circle(ptdesc,PURPLE,(50,85),30)
          pygame.draw.circle(ptdesc,WHITE,(50,85),20)
          pygame.draw.circle(ptdesc,PURPLE,(50,85),10)
          ptdesc.blit(ptdescsub2,(3,120))
          ptdesc.blit(ptdescsub3,(20,140))
          ptdesc.blit(ptdescsub3_2,(10,162.5))
          ptdesc.blit(spctxt,(10,180))
          ptdesc.blit(ptdescsub4,(4,200))
          pygame.draw.line(ptdesc,BLACK,(99,0),(99,250))
        #orange
        if True:
          otdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          otdescsub1 = medsmlfont.render("Ornge",True,ORANGE)
          otdescsub1_2 = smallfont2.render("10/8/6/3%",True,WHITE)
          otdescsub2 = smallfont.render("Points: 1",True,WHITE)
          otdescsub3 = smallfont.render("Time:",True,WHITE)
          otdescsub3_2 = smallfont2.render("12/8.5/5/2s",True,WHITE)
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
          otdesc.blit(otdescsub3_2,(10,162.5))
          otdesc.blit(spctxt,(10,180))
          otdesc.blit(otdescsub4,(5,200))
          otdesc.blit(otdescsub5,(10,220))
          pygame.draw.line(otdesc,BLACK,(99,0),(99,250))
        #green
        if True:
          gtdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          gtdescsub1 = medsmlfont.render("Green",True,DARKGREEN)
          gtdescsub1_2 = smallfont2.render("10/7/6/3%",True,WHITE)
          gtdescsub2 = smallfont.render("Points: 1",True,WHITE)
          gtdescsub3 = smallfont.render("Time:",True,WHITE)
          gtdescsub3_2 = smallfont2.render("12/8.5/5/2s",True,WHITE)
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
          gtdesc.blit(gtdescsub3_2,(10,162.5))
          gtdesc.blit(spctxt,(10,180))
          gtdesc.blit(gtdescsub4,(17,200))
          gtdesc.blit(gtdescsub5,(8,220))
          pygame.draw.line(gtdesc,BLACK,(99,0),(99,250))
        #black
        if True:
          btdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          btdescsub1 = medsmlfont.render("Black",True,BLACK)
          btdescsub1_2 = smallfont2.render("2/5/10/20%",True,WHITE)
          btdescsub2 = smallfont.render("Points: -5",True,WHITE)
          btdescsub3 = smallfont.render("Time:",True,WHITE)
          btdescsub3_2 = smallfont2.render("2/3/3.9/9.5s",True,WHITE)
          btdescsub4 = smallfont.render("+5 walls",True,WHITE)
          btdesc.fill(INVIS)
          btdesc.blit(btdescsub1,(7,0))
          btdesc.blit(btdescsub1_2,(15,35))
          pygame.draw.circle(btdesc,BLACK,(50,85),30)
          pygame.draw.circle(btdesc,WHITE,(50,85),20)
          pygame.draw.circle(btdesc,BLACK,(50,85),10)
          btdesc.blit(btdescsub2,(3,120))
          btdesc.blit(btdescsub3,(20,140))
          btdesc.blit(btdescsub3_2,(10,162.5))
          btdesc.blit(spctxt,(10,180))
          btdesc.blit(btdescsub4,(10,200))
          pygame.draw.line(btdesc,BLACK,(99,0),(99,250))
        #yellow
        if True:
          ytdesc = pygame.Surface([100,250],pygame.SRCALPHA)
          ytdescsub1 = medsmlfont.render("Yellow",True,YELLOW)
          ytdescsub1_2 = smallfont2.render("8/5/3/1%",True,WHITE)
          ytdescsub2 = smallfont.render("Points: 10",True,WHITE)
          ytdescsub3 = smallfont.render("Time:",True,WHITE)
          ytdescsub3_2 = smallfont2.render("5/3.5/2.5/1s",True,WHITE)
          ytdescsub4 = smallfont.render("+1 Max",True,WHITE)
          ytdescsub5 = smallfont.render("Health",True,WHITE)
          ytdesc.fill(INVIS)
          ytdesc.blit(ytdescsub1,(2,0))
          ytdesc.blit(ytdescsub1_2,(25,35))
          pygame.draw.circle(ytdesc,YELLOW,(50,85),30)
          pygame.draw.circle(ytdesc,WHITE,(50,85),20)
          pygame.draw.circle(ytdesc,YELLOW,(50,85),10)
          ytdesc.blit(ytdescsub2,(1,120))
          ytdesc.blit(ytdescsub3,(20,140))
          ytdesc.blit(ytdescsub3_2,(10,162.5))
          ytdesc.blit(spctxt,(10,180))
          ytdesc.blit(ytdescsub4,(13,200))
          ytdesc.blit(ytdescsub5,(20,220))
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
        #health2
        if True:
          h2tdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          h2tdescsub1 = medsmlfont.render("Light",True,LILAC)
          h2tdescsub1_2 = medsmlfont.render("Purple",True,LILAC)
          h2tdescsub2 = medsmlfont.render("Health2",True,WHITE)
          h2tdescsub3 = smallfont2.render("12/20/30/50%",True,WHITE)
          h2tdescsub4 = smallfont.render("Health -1",True,WHITE)
          h2tdescsub5 = smallfont.render("(must be on",True,WHITE)
          h2tdescsub6 = smallfont2.render("purple primary)",True,WHITE)
          h2tdesc.fill(INVIS)
          h2tdesc.blit(h2tdescsub1,(22,0))
          h2tdesc.blit(h2tdescsub1_2,(11,30))
          h2tdesc.blit(h2tdescsub2,(0,60))
          h2tdesc.blit(h2tdescsub3,(15,90))
          pygame.draw.circle(h2tdesc,PURPLE,(60,140),30)
          pygame.draw.circle(h2tdesc,LILAC,(60,140),20)
          pygame.draw.circle(h2tdesc,PURPLE,(60,140),10)
          h2tdesc.blit(h2tdescsub4,(15,175))
          h2tdesc.blit(h2tdescsub5,(2,195))
          h2tdesc.blit(h2tdescsub6,(3,215))
          pygame.draw.line(h2tdesc,BLACK,(119,0),(119,250))
        #missle
        if True:
          mtdesc = pygame.Surface([120,250],pygame.SRCALPHA)
          mtdescsub1 = medsmlfont.render("Light",True,LIGHTGRAY)
          mtdescsub1_2 = medsmlfont.render("Gray",True,LIGHTGRAY)
          mtdescsub2 = medsmlfont.render("Missile",True,WHITE)
          mtdescsub3 = smallfont2.render("25/15/8/2%",True,WHITE)
          mtdescsub4 = smallfont.render("Missile",True,WHITE)
          mtdescsub5 = smallfont.render("count +",True,WHITE)
          mtdescsub6 = smallfont.render("refill rate",True,WHITE)
          mtdesc.fill(INVIS)
          mtdesc.blit(mtdescsub1,(22,0))
          mtdesc.blit(mtdescsub1_2,(25,30))
          mtdesc.blit(mtdescsub2,(6,60))
          mtdesc.blit(mtdescsub3,(20,90))
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
          m2tdescsub1 = medsmlfont.render("Gray",True,DARKGRAY)
          m2tdescsub2 = medsmlfont.render("Missile2",True,WHITE)
          m2tdescsub3 = smallfont2.render("5/2/1/0.1%",True,WHITE)
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
          ntdescsub2 = medsmlfont.render("Nothing",True,WHITE)
          ntdescsub3 = smallfont2.render("38.2/58/65.5/68%",True,WHITE)
          ntdescsub4 = smallfont.render("N/A",True,WHITE)
          ntdesc.fill(INVIS)
          ntdesc.blit(ntdescsub1,(18,15))
          ntdesc.blit(ntdescsub2,(3,60))
          ntdesc.blit(ntdescsub3,(2,90))
          pygame.draw.circle(ntdesc,RED,(60,140),30)
          pygame.draw.circle(ntdesc,WHITE,(60,140),20)
          pygame.draw.circle(ntdesc,RED,(60,140),10)
          ntdesc.blit(ntdescsub4,(40,175))
      #weapons
      if True:
        weapsurf = pygame.Surface([600,300],pygame.SRCALPHA)
        weaptxt = medfont.render("Weapons",True,WHITE)
        weapsurf.fill(INVIS)
        pygame.draw.lines(weapsurf,BLACK,False,[(20,83),(20,63),(48,63)],9)
        #pygame.draw.lines(screen,BLACK,False,[(x+10,y+7),(x+10,y+2),(x+17,y+2)],3)
        weapsubgun = medsmlfont.render("Gun",True,WHITE)
        weapsub1 = smallfont.render("",True,WHITE)
        weapsurf.blit(weaptxt,(200,0))
      #help screen
      if True:
        hsubsurf1 = smallfont.render("Shoot the targets. Use WASD to move and the arrow keys to",True,WHITE)
        hsubsurf2 = smallfont.render("aim. Fire with Enter or the Spacebar. Use Shift to go fast and",True,WHITE)
        hsubsurf3 = smallfont.render("Ctrl to go slow. Q locks you in fast. Press Esc to pause/",True,WHITE)
        hsubsurf4 = smallfont.render("unpause. Press E to see your stats. Use the number keys to",True,WHITE)
        hsubsurf5 = smallfont.render("switch between weapons. 1 is gun, 2 is missile launcher.",True,WHITE)
        hsubsurf6 = smallfont.render("Get 150/250/500/2000 points to win.",True,WHITE)
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

      screen.blit(logo,(50,100))
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
      screen.fill(GRAY)

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
        screen.blit(h2tdesc,(120,80))
        screen.blit(mtdesc,(240,80))
        screen.blit(m2tdesc,(360,80))
        screen.blit(ntdesc,(480,80))
      elif page == 4:
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
              if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT and s_lock != 1:
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
                score += 250
              if event.key == pygame.K_j:
                count += 25
              if event.key == pygame.K_h:
                hlth += 5
                max_hlth += 5
          #weapon keys
          if paused != 1:
            if event.key == pygame.K_1:
              weapon = "gun"
            if event.key == pygame.K_2:
              weapon = "launcher"
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
              firing = True
              fire_timer_g = TICK
              fire_timer_m = TICK
            if event.key == pygame.K_UP:
              if facing == "r":
                facing = "ru"
              if facing == "rd":
                facing = "r"
              if facing == "l":
                facing = "lu"
              if facing == "ld":
                facing = "l"
            if event.key == pygame.K_DOWN:
              if facing == "r":
                facing = "rd"
              if facing == "ru":
                facing = "r"
              if facing == "l":
                facing = "ld"
              if facing == "lu":
                facing = "l"
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
          if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            firing = False
          if event.key == pygame.K_o:
            o_p = False
          if event.key == pygame.K_p:
            p_p = False
    
    if score >= ptrq:
      current_screen = "win"
      show_stats = True
    if hlth <= 0:
      current_screen = "game over"

    #constant update variables
    if True:
      if paused == -1:
        pygame.mouse.set_visible(False)
      elif paused == 1:
        pygame.mouse.set_visible(True)
      move_speed = round(speed*speed_mod,1)
      if s_lock == 1:
        move_speed *= 2
      scoresurf = smallfont.render("Points: "+str(score),True,BLACK)
      mslsurf = smallfont.render("Missles: "+str(msl),True,BLACK)
      spdsurf = smallfont.render("Speed: "+str(round(move_speed*TICK))+"p/s",True,BLACK)
      bmssurf = smallfont.render("Bullet movement speed: "+str(round(blt_mspd*TICK))+"p/s",True,BLACK)
      bfssurf = smallfont.render("Bullet fire rate: "+str(blt_fspd)+"/s",True,BLACK)
      mmssurf = smallfont.render("Missile movement speed: "+str(round(msl_mspd*TICK))+"p/s",True,BLACK)
      mfssurf = smallfont.render("Missile fire rate: "+str(msl_fspd)+"/s",True,BLACK)
      mrfsurf = smallfont.render("Missile refill per target: "+str(msl_rf),True,BLACK)
      countsurf = smallfont.render("Targets until next wall: "+str(5-count),True,BLACK)
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
        statsurf.blit(spdsurf,(254,0))
        statsurf.blit(bmssurf,(84,20))
        statsurf.blit(bfssurf,(175,40))
        statsurf.blit(mmssurf,(71,60))
        statsurf.blit(mfssurf,(162,80))
        statsurf.blit(mrfsurf,(92,100))
        statsurf.blit(countsurf,(97,120))
        if dif == "impos":
          statsurf.blit(difsurf,(188,140))
        else:
          statsurf.blit(difsurf,(223,140))
      #hud
      if True:
        hud.fill(INVIS)
        #health
        hlth_offset = 30*((max_hlth//17)+1)
        for i in range(5,max_hlth*35+1,35):
          if i in range(0,630):
            pygame.draw.polygon(hud,GRAY,[(i,12.5),(i+15,27.5),(i+30,12.5),(i+27.25,7.75),(i+22.5,5),(i+17.75,7.75),(i+15,10),(i+12.25,7.75),(i+7.5,5),(i+2.75,7.75)])
            pygame.draw.arc(hud,GRAY,[i,3.5,16,18],0,pi,50)
            pygame.draw.arc(hud,GRAY,[i+15,3.5,16,18],0,pi,50)
          elif i in range(630,1225):
            pygame.draw.polygon(hud,GRAY,[(i-630,42.5),(i+15-630,57.5),(i+30-630,42.5),(i+27.25-630,37.75),(i+22.5-630,35),(i+17.75-630,37.75),(i+15-630,40),(i+12.25-630,37.75),(i+7.5-630,35),(i+2.75-630,37.75)])
            pygame.draw.arc(hud,GRAY,[i-630,33.5,16,18],0,pi,50)
            pygame.draw.arc(hud,GRAY,[i+15-630,33.5,16,18],0,pi,50)
          elif i in range(1225,1820):
            pygame.draw.polygon(hud,GRAY,[(i-1225,72.5),(i+15-1225,87.5),(i+30-1225,72.5),(i+27.25-1225,67.75),(i+22.5-1225,65),(i+17.75-1225,67.75),(i+15-1225,70),(i+12.25-1225,67.75),(i+7.5-1225,65),(i+2.75-1225,67.75)])
            pygame.draw.arc(hud,GRAY,[i-1225,63.5,16,18],0,pi,50)
            pygame.draw.arc(hud,GRAY,[i+15-1225,63.5,16,18],0,pi,50)
          elif i in range(1820,2415):
            pygame.draw.polygon(hud,GRAY,[(i-1820,102.5),(i+15-1820,117.5),(i+30-1820,102.5),(i+27.25-1820,97.75),(i+22.5-1820,95),(i+17.75-1820,97.75),(i+15-1820,100),(i+12.25-1820,97.75),(i+7.5-1820,95),(i+2.75-1820,97.75)])
            pygame.draw.arc(hud,GRAY,[i-1820,93.5,16,18],0,pi,50)
            pygame.draw.arc(hud,GRAY,[i+15-1820,93.5,16,18],0,pi,50)
        for i in range(5,hlth*35+1,35):
          if i in range(0,630):
            pygame.draw.polygon(hud,RED,[(i,12.5),(i+15,27.5),(i+30,12.5),(i+27.25,7.75),(i+22.5,5),(i+17.75,7.75),(i+15,10),(i+12.25,7.75),(i+7.5,5),(i+2.75,7.75)])
            pygame.draw.arc(hud,RED,[i,3.5,16,18],0,pi,50)
            pygame.draw.arc(hud,RED,[i+15,3.5,16,18],0,pi,50)
          elif i in range(630,1225):
            pygame.draw.polygon(hud,RED,[(i-630,42.5),(i+15-630,57.5),(i+30-630,42.5),(i+27.25-630,37.75),(i+22.5-630,35),(i+17.75-630,37.75),(i+15-630,40),(i+12.25-630,37.75),(i+7.5-630,35),(i+2.75-630,37.75)])
            pygame.draw.arc(hud,RED,[i-630,33.5,16,18],0,pi,50)
            pygame.draw.arc(hud,RED,[i+15-630,33.5,16,18],0,pi,50)
          elif i in range(1225,1820):
            pygame.draw.polygon(hud,RED,[(i-1225,72.5),(i+15-1225,87.5),(i+30-1225,72.5),(i+27.25-1225,67.75),(i+22.5-1225,65),(i+17.75-1225,67.75),(i+15-1225,70),(i+12.25-1225,67.75),(i+7.5-1225,65),(i+2.75-1225,67.75)])
            pygame.draw.arc(hud,RED,[i-1225,63.5,16,18],0,pi,50)
            pygame.draw.arc(hud,RED,[i+15-1225,63.5,16,18],0,pi,50)
          elif i in range(1820,2415):
            pygame.draw.polygon(hud,RED,[(i-1820,102.5),(i+15-1820,117.5),(i+30-1820,102.5),(i+27.25-1820,97.75),(i+22.5-1820,95),(i+17.75-1820,97.75),(i+15-1820,100),(i+12.25-1820,97.75),(i+7.5-1820,95),(i+2.75-1820,97.75)])
            pygame.draw.arc(hud,RED,[i-1820,93.5,16,18],0,pi,50)
            pygame.draw.arc(hud,RED,[i+15-1820,93.5,16,18],0,pi,50)
        hud.blit(scoresurf,(5,hlth_offset))
        hud.blit(mslsurf,(5,hlth_offset+20))
        #stats
        if show_stats == 1:
          hud.blit(statsurf,(200,hlth_offset))

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

    if score >= ptrq:
      current_screen = "win"
    if hlth <= 0:
      current_screen = "game over"

    #screen updates
    if True:
      screen.fill(GREEN)

      #body
      if True:
        pygame.draw.circle(screen,BLACK,[x,y-5],5)
        pygame.draw.line(screen,BLACK,[x,y],[x,y+20])
        pygame.draw.line(screen,BLACK,[x,y+20],[x+5,y+35])
        pygame.draw.line(screen,BLACK,[x,y+20],[x-5,y+35])
        #right arm
        if True:
          if facing == "ru":
            pygame.draw.line(screen,BLACK,[x,y+5],[x+(10/ANG),y+5-(10/ANG)],2)
          elif facing == "rd":
            pygame.draw.line(screen,BLACK,[x,y+6],[x+(10/ANG),y+6+(10/ANG)],2)
          else:
            pygame.draw.line(screen,BLACK,[x,y+5],[x+10,y+5])
        #left arm
        if True:
          if facing == "lu":
            pygame.draw.line(screen,BLACK,[x-1,y+5],[x-1-(10/ANG),y+5-(10/ANG)],2)
          elif facing == "ld":
            pygame.draw.line(screen,BLACK,[x,y+5],[x-(10/ANG),y+5+(10/ANG)],2)
          else:
            pygame.draw.line(screen,BLACK,[x,y+5],[x-10,y+5])

      #targets
      if True:
        #type
        if True:
          #red
          if (dif == "easy" and r in range(0,61)) or (dif == "med" and r in range(0,51)) or (dif == "hard" and r in range(0,41)) or (dif == "impos" and r in range(0,23)):
            t_type = "r"
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
          elif (dif == "easy" and r in range(61,71)) or (dif == "med" and r in range(51,76)) or (dif == "hard" and r in range(41,76)) or (dif == "impos" and r in range(23,73)):
            t_type = "p"
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 2
            elif dif == "med":
              targ_timer_end = 3.3
            elif dif == "hard":
              targ_timer_end = 4
            elif dif == "impos":
              targ_timer_end = 10
          #orange
          elif (dif == "easy" and r in range(71,81)) or (dif == "med" and r in range(76,84)) or (dif == "hard" and r in range(76,82)) or (dif == "impos" and r in range(73,76)):
            t_type = "o"
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 12
            elif dif == "med":
              targ_timer_end = 8.5
            elif dif == "hard":
              targ_timer_end = 5
            elif dif == "impos":
              targ_timer_end = 2
          #green
          elif (dif == "easy" and r in range(81,91)) or (dif == "med" and r in range(84,91)) or (dif == "hard" and r in range(82,88)) or (dif == "impos" and r in range(76,79)):
            t_type = "g"
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 12
            elif dif == "med":
              targ_timer_end = 8.5
            elif dif == "hard":
              targ_timer_end = 5
            elif dif == "impos":
              targ_timer_end = 2
          #black
          elif (dif == "easy" and r in range(91,93)) or (dif == "med" and r in range(91,96)) or (dif == "hard" and r in range(88,98)) or (dif == "impos" and r in range(79,100)):
            t_type = "b"
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 2
            elif dif == "med":
              targ_timer_end = 3
            elif dif == "hard":
              targ_timer_end = 3.9
            elif dif == "impos":
              targ_timer_end = 9.5
          #yellow
          elif (dif == "easy" and r in range(93,101)) or (dif == "med" and r in range(96,101)) or (dif == "hard" and r in range(98,101)) or (dif == "impos" and r in range(100,101)):
            t_type = "y"
            do_targ_timer = True
            if dif == "easy":
              targ_timer_end = 5
            elif dif == "med":
              targ_timer_end = 3.5
            elif dif == "hard":
              targ_timer_end = 2.5
            elif dif == "impos":
              targ_timer_end = 1
          if t_type != "p" and ((dif == "easy" and r2/10 in range(0,31)) or (dif == "med" and r2/10 in range(0,21)) or (dif == "hard" and r2/10 in range(0,16)) or (dif == "impos" and r2/10 in range(0,6))):
            t_type2 = "h"
          elif t_type == "p" and ((dif == "easy" and r2/10 in range(31,43)) or (dif == "med" and r2/10 in range(21,41)) or (dif == "hard" and r2/10 in range(16,46)) or (dif == "impos" and r2/10 in range(6,56))):
            t_type2 = "h2"
          elif (dif == "easy" and r2/10 in range(43,68)) or (dif == "med" and r2/10 in range(41,56)) or (dif == "hard" and r2/10 in range(46,54)) or (dif == "impos" and r2/10 in range(56,57)):
            t_type2 = "m"
          elif (dif == "easy" and r2/10 in range(68,73)) or (dif == "med" and r2/10 in range(56,58)) or (dif == "hard" and r2/10 in range(54,55)) or (dif == "impos" and r2 in range(570,571)):
            t_type2 = "m2"
          else:
            t_type2 = "n"
        #draw
        if True:
          if t_type == "r":
            pygame.draw.circle(screen,RED,[t_x,t_y],15)
            if t_type2 == "h":
              pygame.draw.circle(screen,PINK,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,RED,[t_x,t_y],5)
          elif t_type == "p":
            pygame.draw.circle(screen,PURPLE,[t_x,t_y],15)
            if t_type2 == "h2":
              pygame.draw.circle(screen,LILAC,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,PURPLE,[t_x,t_y],5)
          elif t_type == "g":
            pygame.draw.circle(screen,DARKGREEN,[t_x,t_y],15)
            if t_type2 == "h":
              pygame.draw.circle(screen,PINK,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,DARKGREEN,[t_x,t_y],5)
          elif t_type == "o":
            pygame.draw.circle(screen,ORANGE,[t_x,t_y],15)
            if t_type2 == "h":
              pygame.draw.circle(screen,PINK,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,ORANGE,[t_x,t_y],5)
          elif t_type == "b":
            pygame.draw.circle(screen,BLACK,[t_x,t_y],15)
            if t_type2 == "h":
              pygame.draw.circle(screen,PINK,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,BLACK,[t_x,t_y],5)
          elif t_type == "y":
            pygame.draw.circle(screen,YELLOW,[t_x,t_y],15)
            if t_type2 == "h":
              pygame.draw.circle(screen,PINK,[t_x,t_y],10)
            elif t_type2 == "m":
              pygame.draw.circle(screen,LIGHTGRAY,[t_x,t_y],10)
            elif t_type2 == "m2":
              pygame.draw.circle(screen,GRAY,[t_x,t_y],10)
            elif t_type2 == "n":
              pygame.draw.circle(screen,WHITE,[t_x,t_y],10)
            pygame.draw.circle(screen,YELLOW,[t_x,t_y],5)
        #properties
        if collide == True:
          if t_type == "r":
            score += 2
            count += 1
          elif t_type == "p":
            hlth -= 1
            screen.fill(RED)
            pygame.display.flip()
            pygame.time.wait(100)
            score -= 5
          elif t_type == "o":
            blt_mspd += 0.1
            blt_fspd += 1
            msl_mspd += 0.1
            count += 1
            score += 1
          elif t_type == "g":
            speed += 0.2
            count += 1
            score += 1
          elif t_type == "b":
            count += 25
            score -= 5
          elif t_type == "y":
            score += 10
            count += 1
            max_hlth += 1
          if t_type2 == "h":
            if t_type == "p":
              hlth -= 1
            else:
              hlth += 1
          elif t_type2 == "m":
            msl += msl_rf
          elif t_type2 == "m2":
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
          t_y = random.randrange(15,385)
          reset = False
        #timer
        if do_targ_timer == True and paused != 1:
          targ_timer += 1
          if targ_timer == (targ_timer_end * TICK):
            do_targ_timer = False
            targ_timer = 0
            targ_timer_end = 0
            reset = True

      #gun
      if weapon == "gun":
        if facing == "r":
          pygame.draw.lines(screen,BLACK,False,[(x+10,y+7),(x+10,y+2),(x+17,y+2)],3)
          guntip = [x+17,y+2]
        elif facing == "l":
          pygame.draw.lines(screen,BLACK,False,[(x-10,y+7),(x-10,y+2),(x-17,y+2)],3)
          guntip = [x-17,y+2]
        elif facing == "ru":
          pygame.draw.lines(screen,BLACK,False,[(x+2+(10/ANG),y+7-(10/ANG)),(x+2+(5/ANG),y+7-(15/ANG)),(x+2+(12/ANG),y+7-(22/ANG))],4)
          guntip = [x+2+(12/ANG),y+7-(22/ANG)]
        elif facing == "rd":
          pygame.draw.lines(screen,BLACK,False,[(x+2+(10/ANG),y+7+(10/ANG)),(x+2+(15/ANG),y+7+(5/ANG)),(x+2+(22/ANG),y+7+(12/ANG))],4)
          guntip = [x+2+(22/ANG),y+7+(12/ANG)]
        elif facing == "lu":
          pygame.draw.lines(screen,BLACK,False,[(x-2-(10/ANG),y+7-(10/ANG)),(x-2-(5/ANG),y+7-(15/ANG)),(x-2-(12/ANG),y+7-(22/ANG))],4)
          guntip = [x-2-(12/ANG),y+7-(22/ANG)]
        elif facing == "ld":
          pygame.draw.lines(screen,BLACK,False,[(x-2-(10/ANG),y+7+(10/ANG)),(x-2-(15/ANG),y+7+(5/ANG)),(x-2-(22/ANG),y+7+(12/ANG))],4)
          guntip = [x-2-(22/ANG),y+7+(12/ANG)]

      #bullets
      if True:
        #cooldown
        if paused != 1 and weapon == "gun":
          fire_timer_g += blt_fspd
          if fire_timer_g >= TICK:
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
        #management
        for i in range(len(blts)):
          pygame.draw.circle(screen,RED,[blts[i][0],blts[i][1]],1)
          if paused != 1:
            blts[i][0]+=blts[i][2]
            blts[i][1]+=blts[i][3]
          if blts[i][0] < 0 or blts[i][0] > 600:
            del blts[i]
            break
          if blts[i][0] <= (t_x+15) and blts[i][0] >= (t_x-15) and blts[i][1] <= (t_y+15) and blts[i][1] >= (t_y-15):
            collide = True
            del blts[i]
            break

      #missile launcher
      if weapon == "launcher":
        if facing == "r":
          pygame.draw.polygon(screen,BLACK,[(x+5,y+4),(x+10,y+3),(x+20,y+2),(x+20,y+8),(x+10,y+7),(x+5,y+6)])
          guntip = [x+20,y+5]
        elif facing == "l":
          pygame.draw.polygon(screen,BLACK,[(x-5,y+4),(x-10,y+3),(x-20,y+2),(x-20,y+8),(x-10,y+7),(x-5,y+6)])
          guntip = [x-20,y+5]
        elif facing == "ru":
          pygame.draw.polygon(screen,BLACK,[(x+(5/ANG),y+4-(5/ANG)),(x+(9/ANG),y+3-(9/ANG)),(x-1+(19/ANG),y+2-(17/ANG)),(x+2+(21/ANG),y+12-(26/ANG)),(x+(9/ANG),y+8-(9/ANG)),(x+2+(5/ANG),y+6-(5/ANG))])
          guntip = [x+(20/ANG),y+7-(22/ANG)]
        elif facing == "rd":
          pygame.draw.polygon(screen,BLACK,[(x+(5/ANG),y+6+(5/ANG)),(x+(9/ANG),y+7+(9/ANG)),(x-1+(19/ANG),y+8+(17/ANG)),(x+2+(21/ANG),y-2+(26/ANG)),(x+(9/ANG),y+2+(9/ANG)),(x+2+(5/ANG),y+4+(5/ANG))])
          guntip = [x+(20/ANG),y+3+(22/ANG)]
        elif facing == "lu":
          pygame.draw.polygon(screen,BLACK,[(x-(5/ANG),y+4-(5/ANG)),(x-(9/ANG),y+3-(9/ANG)),(x+1-(19/ANG),y+2-(17/ANG)),(x-2-(21/ANG),y+12-(26/ANG)),(x-(9/ANG),y+8-(9/ANG)),(x-(5/ANG),y+7-(5/ANG))])
          guntip = [x-(20/ANG),y+7-(22/ANG)]
        elif facing == "ld":
          pygame.draw.polygon(screen,BLACK,[(x-(5/ANG),y+6+(5/ANG)),(x-(9/ANG),y+7+(9/ANG)),(x+1-(19/ANG),y+8+(17/ANG)),(x-2-(21/ANG),y-2+(26/ANG)),(x-(9/ANG),y+2+(9/ANG)),(x-2-(5/ANG),y+4+(5/ANG))])
          guntip = [x-(20/ANG),y+3+(22/ANG)]

      #missles
      if True:
        #cooldown
        if paused != 1 and weapon == "launcher":
          fire_timer_m += msl_fspd
          if fire_timer_m >= TICK:
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
        #management
        for i in range(len(msls)):
          if facing == "r":
            pygame.draw.rect(screen,GRAY,[msls[i][0]-6,msls[i][1]-2,13,5])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+7,msls[i][1]-2),(msls[i][0]+7,msls[i][1]+2),(msls[i][0]+6+(2.5*math.sqrt(3)),msls[i][1])])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-6,msls[i][1]-3),(msls[i][0]-2,msls[i][1]-3),(msls[i][0]-5,msls[i][1]-5),(msls[i][0]-8,msls[i][1]-5)])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-6,msls[i][1]+3),(msls[i][0]-2,msls[i][1]+3),(msls[i][0]-5,msls[i][1]+5),(msls[i][0]-8,msls[i][1]+5)])
          elif facing == "l":
            pygame.draw.rect(screen,GRAY,[msls[i][0]-6,msls[i][1]-2,13,5])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-7,msls[i][1]-2),(msls[i][0]-7,msls[i][1]+2),(msls[i][0]-6-(2.5*math.sqrt(3)),msls[i][1])])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+6,msls[i][1]-3),(msls[i][0]+2,msls[i][1]-3),(msls[i][0]+5,msls[i][1]-5),(msls[i][0]+8,msls[i][1]-5)])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+6,msls[i][1]+3),(msls[i][0]+2,msls[i][1]+3),(msls[i][0]+5,msls[i][1]+5),(msls[i][0]+8,msls[i][1]+5)])
          elif facing == "ru":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]-(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]+(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)),msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-2,msls[i][1]-(8/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(8/ANG),msls[i][1]+(3/ANG)),(msls[i][0]-(5/ANG),msls[i][1]-(1/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(1/ANG)),(msls[i][0]-(12/ANG),msls[i][1]+(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(3/ANG),msls[i][1]+(9/ANG)),(msls[i][0]+(1/ANG),msls[i][1]+(5/ANG)),(msls[i][0],msls[i][1]+(8/ANG)),(msls[i][0]-(3/ANG),msls[i][1]+(12/ANG))])
          elif facing == "rd":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12)),msls[i][1]+(8/ANG)-(5*-math.sin(pi/12))),(msls[i][0]+(4/ANG)-(5*-math.cos(pi/12))-2,msls[i][1]+(8/ANG)-(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(8/ANG),msls[i][1]-(3/ANG)),(msls[i][0]-(5/ANG),msls[i][1]+(1/ANG)),(msls[i][0]-(8/ANG),msls[i][1]+(1/ANG)),(msls[i][0]-(12/ANG),msls[i][1]-(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(3/ANG),msls[i][1]-(9/ANG)),(msls[i][0]+(1/ANG),msls[i][1]-(5/ANG)),(msls[i][0],msls[i][1]-(8/ANG)),(msls[i][0]-(3/ANG),msls[i][1]-(12/ANG))])
          elif facing == "lu":
            pygame.draw.polygon(screen,GRAY,[(msls[i][0]+(8/ANG),msls[i][1]+(4/ANG)),(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]+(4/ANG),msls[i][1]+(8/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]-(4/ANG),msls[i][1]-(8/ANG)),(msls[i][0]-(8/ANG),msls[i][1]-(4/ANG)),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12)),msls[i][1]-(8/ANG)+(5*-math.sin(pi/12))),(msls[i][0]-(4/ANG)+(5*-math.cos(pi/12))+2,msls[i][1]-(8/ANG)+(5*-math.sin(pi/12)))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(8/ANG),msls[i][1]+(3/ANG)),(msls[i][0]+(5/ANG),msls[i][1]-(1/ANG)),(msls[i][0]+(8/ANG),msls[i][1]-(1/ANG)),(msls[i][0]+(12/ANG),msls[i][1]+(3/ANG))])
            pygame.draw.polygon(screen,RED,[(msls[i][0]+(3/ANG),msls[i][1]+(9/ANG)),(msls[i][0]-(1/ANG),msls[i][1]+(5/ANG)),(msls[i][0]-(1/ANG),msls[i][1]+(8/ANG)),(msls[i][0]+(3/ANG),msls[i][1]+(12/ANG))])
          elif facing == "ld":
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
          if msls[i][0] <= (t_x+15) and msls[i][0] >= (t_x-15) and msls[i][1] <= (t_y+15) and msls[i][1] >= (t_y-15):
            collide = True
            del msls[i]
            break

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
          pygame.draw.line(screen,BLACK,(walls[i][0],walls[i][1]-15),(walls[i][0],walls[i][1]+15),3)
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
        pause_timer += 1
        if pause_timer > 45:
          pause_timer = -35
        if pause_timer > 0:
          screen.blit(pausesurf,(220,150))
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
      fadewhite[3] += 0.5
    winsurf.fill(fadewhite)
    winsurf.blit(hud,(0,0))
    winsurf.blit(winsubsurf,(150,150))
    winsurf.blit(resurf,(190,220))
    winsurf.blit(yessurf,(100,275))
    winsurf.blit(nosurf,(400,275))
    screen.blit(winsurf,(0,0))
    pygame.display.flip()

  #game over
  if hlth <= 0:
    pygame.mouse.set_visible(True)
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[0] in range(100,200) and event.pos[1] in range(275,325):
            current_screen = "game"
            var_reset = True
          elif event.pos[0] in range(400,500) and event.pos[1] in range(275,325):
            current_screen = "menu"
    if fadeblack[3] < 250 :
      fadeblack[3] += 0.5
    gmovsurf.fill(fadeblack)
    gmovsurf.blit(hud,(0,0))
    gmovsurf.blit(gmovsubsurf,(100,150))
    gmovsurf.blit(resurf,(190,220))
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
    firing = False
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
    show_stats = -1
    hlth = 3
    max_hlth = 4
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
    do_targ_timer = False
    targ_timer_end = 0
    o_p = False
    p_p = False
    paused = -1
    pause_timer = 0
    done = False
    page = 1
    var_reset = False
    fadeblack = [10,10,10,0]
    fadewhite = [255,255,255,0]

  clock.tick(TICK)

pygame.quit()