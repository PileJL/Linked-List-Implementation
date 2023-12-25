import random, os, time, pygame, playsound2, sys
from pygame import mixer
from gtts import gTTS

b = "\033[1;30;0m" 
r = "\033[1;91;1m"
w = "\033[0;97;1m"
g = "\033[32m"
y = "\33[93m"
wh = "\33[7m"
bh = "\33[40m"
reset = '\033[0m'
bl = "\033[1;40m" 
o = "\033[33m"
s = f"\t\t\t\t\t\t" # indention for guides
ln = f"{r}──────────" * 2 + f"{w}──────────"*2 # lay down
v = "━" 
FLIPPED_CARD = f"""\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘"""
tab_spaces = "\t" * 11

def display_guide():
    tab = "\t" *9   
    s = f"\t\t\t"                
    instruction = [
            f"\n{s}{r}{tab}  █▀▀  {w}█░█  {w}█  {w}█▀▄ {r}█▀▀{w} █▀  \n",
            f"{s}{r}{tab}  █▄█  {w}█▄█  {r}█  {w}█▄▀ {r}██▄{w} ▄█ \n\n",
            f"{s}{w}          {w}{v*75}{r}{v*75}\n\n",
            f"{s}\t        {r}[1] {w}Once the game starts after selecting a card design, one card from the 52-card deck will be the monkey card until the end of the game.\n\n",
            f"{s}\t        {r}[2] {w}The program will then shuffle and randomly distribute the 51 cards between the user and the computer.\n\n",
            f"{s}\t        {r}[3] {w}Next, the program will pair the respective cards of the players and remove those paired cards from the players' decks to start the draw.\n\n",
            f"{s}\t        {r}[4] {w}Then, the program will ask the user to choose between 'Heads' or 'Tails', as the winner will pick a card first from the opposing deck.\n\n",
            f"{s}\t        {r}[5] {w}Afterwards, the loser's deck will shuffle. If the chosen card has a pair from the picker's deck, display all paired cards.\n\n",
            f"{s}\t        {r}[6] {w}The player shall correctly choose the paired cards to remove. Otherwise, {r}GAME OVER.\n\n",
            f"{s}\t        {r}[7] {w}If there are no pairs, the program will add the chosen card to the picker's deck then the game shall proceed with the alternate draws\n",
            f"{s}\t        {r}    {w}between the players until there is one card left.\n\n",
            f"{s}\t        {r}[8] {w}The first player to have zero cards is the winner of the Match N' Monkey game.\n\n",
            f"{s}\t        {r}[9] {w}Lastly, the program will pair the last card to the monkey card and label the other player as the monkey of the game.\n\n",
            f"{s}{w}          {r}{v*75}{w}{v*75}\n\n"]
    for char in instruction:
        sys.stdout.write(char)
        time.sleep(0.5)
    while True:
        os.system("cls")
        print("".join(instruction))
        print(f"{w}   [0] Back to Main Menu".center(226),end="\n\n")
        guide_choice = input(f"{tab}\t\t\t\t{r} ➤  {w}")
        if guide_choice =="0":
            return

def display_cardTheme_choices():
    print(f"\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t{r}█▀▀ ▄▀█ █▀█ █▀▄  {w} ▀█▀ █░█ █▀▀ █▀▄▀█ █▀▀".center(251), f"{w}\t\t█▄▄ █▀█ █▀▄ █▄▀   ░█░ {r}█▀█ ██▄ █░▀░█ ██▄".center(237))
    print(f"""
{s}{w}           {w}{v*55}{r}{v*55}\n\n\n
\t\t\t\t\t\t       {r}┌─────────┐───┐{reset}          {wh}┌─────────┐───┐{reset}           {r}┌─────────┐───┐{reset}            {r}┌─────────┐───┐{reset}           {w}┌─────────┐───┐{reset}                
\t\t\t\t\t\t       {r}│A        │   │{reset}          {wh}│A        │   │{reset}           {r}│A        │   │{reset}            {r}│A        │   │{reset}           {w}│A        │   │{reset} 
\t\t\t\t\t\t       {r}│         │   │{reset}          {wh}│         │   │{reset}           {r}│         │   │{reset}            {r}│         │   │{reset}           {w}│         │   │{reset}  
\t\t\t\t\t\t       {r}│    ♥    │   │{reset}          {wh}│    ♥    │   │{reset}           {r}│    ♥    │   │{reset}            {y}│    ♥    │   │{reset}           {w}│    {r}♥{w}    │   │{reset}            
\t\t\t\t\t\t       {r}│         │   │{reset}          {wh}│         │   │{reset}           {w}│         │   │{reset}            {y}│         │   │{reset}           {w}│         │   │{reset}  
\t\t\t\t\t\t       {r}│        A│  A│{reset}          {wh}│        A│  A│{reset}           {w}│        A│  A│{reset}            {y}│        A│  A│{reset}           {w}│        A│  A│{reset}  
\t\t\t\t\t\t       {r}└─────────┘───┘{reset}          {wh}└─────────┘───┘{reset}           {w}└─────────┘───┘{reset}            {y}└─────────┘───┘{reset}           {w}└─────────┘───┘{reset}  
\t\t\t\t\t\t                
\t\t\t\t\t\t     {y}[1]{r} Full-Red Deck {reset}       {y}[2]{w} Full White Deck{reset}        {y}[3] {r}Gradient{w} Deck{reset}        {y}[4]{r} Red n' {y}Yellow Deck{reset}      {y}[5]{w} Standard{r} Deck{reset}  \n
\n{s}{w}           {r}{v*55}{w}{v*55}\n\n
                                                                                                        {y}[0] {w}Back to Main Menu\n""")
    while True: 
        try: 
            card_theme_choice1 = int(input(f"\t\t\t\t\t\t\t\t\t\t\t\t\t        {w}➤   {y}"))
            if card_theme_choice1 in range(6):
                return card_theme_choice1
        except:
            pass

def colorText(text, lis):
    for color in lis:
        text = text.replace("[[" + color + "]]", lis[color])
    return text
#animations
def get_percentage_loadingAnimation():
        bar, x = "▇", " "
        loading = [f"{w}LOAᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ: {r}%0 {bar}", f"{r}ʟᴏᴀDIɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ: {w}%0 {bar}", f"{w}ʟᴏᴀᴅɪNG Pʟᴇᴀsᴇ ᴡᴀɪᴛ: {r}%5 {bar * 2}",f"{r}ʟᴏᴀᴅɪɴɢ ᴘLEᴀsᴇ ᴡᴀɪᴛ: {w}%10 {bar * 3}",
            f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇASE ᴡᴀɪᴛ: {r}%15 {bar * 4}",f"{r}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ WAɪᴛ:{w} %20 {bar * 5}", f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀIT: {r}%25 {bar * 6}",f"{r}LOAᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ: {w}%30 {bar * 7}", 
            f"{w}ʟᴏᴀDIɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ: %35{r} {bar * 8}",f"{r}ʟᴏᴀᴅɪNG Pʟᴇᴀsᴇ ᴡᴀɪᴛ:{w} %40 {bar * 9}",f"{w}ʟᴏᴀᴅɪɴɢ ᴘLEᴀsᴇ ᴡᴀɪᴛ:{r} %45 {bar * 10}", f"{r}ʟᴏᴀᴅɪɴɢ ᴘʟᴇASE ᴡᴀɪᴛ: {w}%50 {bar * 11}",
            f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ WAɪᴛ:{r} %55 {bar * 12}", f"{r}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀIT:{w} %60 {bar * 13}",f"{w}LOAᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ:{r} %65 {bar * 14}",f"{r}ʟᴏᴀDIɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ:{w} %70 {bar * 15}", 
            f"{w}ʟᴏᴀᴅɪNG Pʟᴇᴀsᴇ ᴡᴀɪᴛ:{r} %75 {bar * 16}",f"{w}ʟᴏᴀᴅɪɴɢ ᴘLEᴀsᴇ ᴡᴀɪᴛ:{r} %80 {bar * 17}", f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇASE ᴡᴀɪᴛ:{w} %85 {bar * 18}",f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ WAɪᴛ:{r} %90 {bar * 19}",
            f"{w}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀIᴛ: {r}%95 {bar * 20}", f"{r}ʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪT: {w}%100 {bar * 21}{reset}", ]
        print(w)
        time.sleep(1)
        for i in range(23):
            print(x * 90, loading[i % len(loading)], end="\r")
            time.sleep(0.2)
        print(f"{w}{x * 90} LOADING COMPLETE!    {r}%100 {bar * 21}{reset}")
        time.sleep(1)
        os.system("cls")

def display_main_menu(for_opening= True):
    os.system("cls")
    title = f'''
{r}\n\n\n
                \t\t\t\t  ███╗   ███╗ █████╗ ████████╗ ██████╗██╗  ██╗    ███╗   ██╗ █   ███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗██╗   ██╗ 
                \t\t\t\t  ████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██║  ██║    ████╗  ██║     ████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
                \t\t\t\t  ██╔████╔██║███████║   ██║   ██║     ███████║    ██╔██╗ ██║     ██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝ {w}
                \t\t\t\t  ██║╚██╔╝██║██╔══██║   ██║   ██║     ██╔══██║    ██║╚██╗██║     ██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝  
                \t\t\t\t  ██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╗██║  ██║    ██║ ╚████║     ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗███████╗   ██║  
                \t\t\t\t  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝  
                \t\t{w}    {v*75}{r}{v*75}
                                                                                                                                                   {o}|| __   ||
                                                                                                                                                   {o}||=\_`\=||
                                                                    {r}\t\t     ░█▀▄▀█ ─█▀▀█ {b}▀█▀ ░█▄─░█ 　 {r}░█▀▄▀█ ░█▀▀▀ {b}░█▄─░█ ░█─░█          {o}|| (__/ ||  
                                                                    {r}\t\t     ░█░█░█ ░█▄▄█ {b}░█─ ░█░█░█ 　 {r}░█░█░█ ░█▀▀▀ {b}░█░█░█ ░█─░█          {r}||  | | :-"""-.      
                                                                    {r}\t\t     ░█──░█ ░█─░█ {b}▄█▄ ░█──▀█ 　 {r}░█──░█ ░█▄▄▄ {b}░█──▀█ ─▀▄▄▀          {r}||==| \/-=-.   \
                                                                                                                           \t\t\t\t\t\t\t\t\t\t           {r}||  |(_|o o/   |_
                                                                                                                                                   {o}||   \/ "  \   ,_)
                                                                                                                                                   {o}||====\ ^  /__/
                                                                                                                                                   {o}||     ;--'  `-.
                        \t\t\t                             {r}_____               {w}▄█    {r}█▀▀  {w}█░█  {w}█  {w}█▀▄ {r}█▀▀                        {r}||    /      .  \                 
                        \t\t\t{r} _____                {o}_____ {r}|6    |              {w}░█    {r}█▄█  {w}█▄█  {r}█  {w}█▄▀ {r}██▄                        {r}||===;        |  |
                        \t\t\t{r}|2    |              {o}|5    |{r}| & & |                          \t\t\t\t           {r}||   |         | |
                        \t\t\t{r}|  &  |{o} _____        {o}| & & |{r}| & & |                                                                {o}|| .-\ '     _/_/
                        \t\t\t{r}|     |{o}|3    |{r} _____ {o}|  &  |{r}| & & |               {w} ▀█{r}   █▀█{w}  █░░ {w} ▄▀█  {r}█▄█                         {o}|:'  _;.    (_  \                            
                        \t\t\t{r}|  &  |{o}| & & |{r}|4    |{o}| & & |{r}|____9|               {w}░█▄   {r}█▀▀  {w}{r}█▄▄  {w}█▀█  {r}░█░                        {o}/  .'  `;\   \\_/  
                        \t\t\t{r}|____Z|{o}|     |{r}| & & |{o}|____S|                                                                      {r}|_ /     |||  |\\     
                        \t\t\t       {o}|  &  |{r}|     |                                                                           {r} /  _)=====|||  | || 
                        \t\t\t       {o}|____E|{r}| & & |                              {w}▀▀█   {r}█▀█ {w} █░█  {w}█  {r}▀█▀                      {r}/  /|      ||/  / //
                        \t\t\t              {r}|____h|                              {w}▄██   {r}▀▀█  {w}█▄█  {r}█  {r}░█░                      {o}\_/||      ( `-/ ||  
                                                                                                                                                 {o} ||======/  /  \\ .-.                                                                                                                           
                    \t\t  {r}{v*60}{w}   ＩＮＰＵＴ {r}Ａ {w}ＮＵＭＢＥＲ   {v*60}\n'''
    if for_opening:
        for line in title:
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(0.001)
    else:
        print(title)

def get_monkey_animation():
    os.system("cls")
    def colorText(text, lis):
        for color in lis:
            text = text.replace("[[" + color + "]]", lis[color])
        return text
        
    filenames = ["monkey 1.txt", "monkey 2.txt", "monkey 3.txt", "monkey 4.txt", "monkey 5.txt"]
    pygame.init()  # initializing for pygame
    mixer.music.load("countdown.mp3")
    mixer.music.play()
    def monkey(filenames, delay=0.5, repeat=10):
        frames = []
        for name in filenames:
           with open(name, "r", encoding="UTF-8") as f:
               frames.append(f.readlines())
        for i in range(repeat):
            for frame in frames:
                ascii = "".join(frame)
                print(colorText(ascii, {"black":"\33[93m","red": "\u001b[31;1m","white":"\u001b[37m",})) 
                time.sleep(delay)
                os.system("cls")
    
    monkey(filenames, delay=0.9, repeat=2)
    monkey(filenames, delay=0.5, repeat=1)
    monkey(filenames, delay=0.3, repeat=2)
    monkey(filenames, delay=0.2, repeat=1)

def get_rocket_animation():
        f= ["Rocket 1.txt", "Rocket 2.txt", "Rocket 3.txt", "Rocket 4.txt"]
        pygame.init()  # initializing for pygame
        mixer.music.load("rocket.mp3")
        mixer.music.play()
        frames = []
        for name in f:
            with open(name, "r", encoding="UTF-8") as f:
                frames.append(f.readlines())
        for frame in frames:
            ascii = "".join(frame)
            print(colorText(ascii, {"white":"\033[1;30;0m","red": "\u001b[31;1m","yellow":"\33[93m"}))
            time.sleep(1)
            os.system("cls")
        os.system("cls")

def get_loading_animation(text="ＬＯＡ", text1= "ＤＩＮＧ",indention = "\t\t\t\t\t\t\t\t\t\t"):
    Loading = [ f"{y}◑    ", f" {y}◒   ", f"{y}  ◐  ", f"{y}   ◓ ", f"{y}    ◑", f"{y}   ◓ ", f"{y}  ◐  ", f"{y} ◒   " ]
    i = 0
    while i != 20:
        print(f'{r}{indention}        {text}{w}{text1}', Loading[i % len(Loading)], end='\r')
        time.sleep(.2)                      
        i += 1
    time.sleep(.2)

def get_shuffling_animation(for_turns = False,shufflingWord_top ="█▀ █░█ █░█ █▀▀ █▀▀ █░░ █ █▄░█ █▀▀", shufflingWord_bottom = "▄█ █▀█ █▄█ █▀░ █▀░ █▄▄ █ █░▀█ █▄█\n\n", \
    shufflingWord_top_4botLabel=f"\n\n{tab_spaces}   █▀ █░█ █░█ █▀▀ █▀▀ █░░ █ █▄░█ █▀▀",shufflingWord_bot_4botLabel= "▄█ █▀█ █▄█ █▀░ █▀░ █▄▄ █ █░▀█ █▄█",\
    card_filler = f"\n{tab_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│", card_filler1 = f"\n{tab_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│"\
    ,card_filler2 = f"\n{tab_spaces}        │░│░░│░░│░░░│░░░░░░░░░│",vertical_spaces = "\n\n\n\n\n\n\n",spaces= tab_spaces, mid_spaces = tab_spaces ):
    
    deck_list = [f"""{vertical_spaces}{r}
{spaces}   {shufflingWord_top}{w}
{spaces}   {shufflingWord_bottom}{reset}
{mid_spaces}     ┌──┌───┌──┌─┌──┌───┌─────────┐
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│{card_filler}{card_filler}
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     └──└───└──└─└──└───└─────────┘{y}
{spaces}   {shufflingWord_top_4botLabel}{w}
{spaces}   {shufflingWord_bot_4botLabel}
""", 
f"""{vertical_spaces}{w}
{spaces}   {shufflingWord_top}{y}
{spaces}   {shufflingWord_bottom}{reset}
{mid_spaces}       ┌──┌─┌──┌──┌───┌─────────┐
{mid_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│{card_filler1}{card_filler1}
{mid_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}       │░░│░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}       └──└─└──└──└───└─────────┘{w}
{spaces}   {shufflingWord_top_4botLabel}{r}
{spaces}   {shufflingWord_bot_4botLabel}
    """,
    f"""{vertical_spaces}{y}
{spaces}   {shufflingWord_top}{w}
{spaces}   {shufflingWord_bottom}{reset}
{mid_spaces}        ┌─┌──┌──┌───┌─────────┐
{mid_spaces}        │░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}        │░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}        │░│░░│░░│░░░│░░░░░░░░░│{card_filler2}{card_filler2}
{mid_spaces}        │░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}        │░│░░│░░│░░░│░░░░░░░░░│
{mid_spaces}        └─└──└──└───└─────────┘{r}
{spaces}   {shufflingWord_top_4botLabel}{w}
{spaces}   {shufflingWord_bot_4botLabel}
    """,
f"""{vertical_spaces}{r}
{spaces}   {shufflingWord_top}{w}
{spaces}   {shufflingWord_bottom}{reset}
{mid_spaces}     ┌──┌───┌──┌─┌──┌───┌─────────┐
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│{card_filler}{card_filler}
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     │░░│░░░│░░│░│░░│░░░│░░░░░░░░░│
{mid_spaces}     └──└───└──└─└──└───└─────────┘{y}
{spaces}   {shufflingWord_top_4botLabel}{w}
{spaces}   {shufflingWord_bot_4botLabel}
"""]
    os.system('cls')
    shuffle_count=4
    while shuffle_count!=-1:
        print(deck_list[shuffle_count-1])
        time.sleep(0.7)
        os.system('cls')
        pygame.init()  # initializing for pygame
        mixer.music.load("shuffle.mp3")
        mixer.music.play(-1)
        shuffle_count-=1
    pygame.mixer.music.stop()    
    if not for_turns:
        time.sleep(1)
        print(f"""\n\n\n\n\n\n\n{w}
        {spaces}  {r}┌┌┌─────────┐
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  │││{w}░░░░░░░░░{r}│
        {spaces}  └└└─────────┘ {reset}""")
        time.sleep(0.3)
        print(f"\n\t\t\t\t\t\t\t\t\t\t{w}ＴＨＥ ＤＥＣＫ ＨＡＳ {r}ＢＥＥＮ ＳＨＵＦＦＬＥＤ{reset}")
        time.sleep(2.5)

def get_tossCoin_animation(headsOrTails_answer,delay=0.2, repeat=7,) -> str:
    filenames = ["coin 1.txt", "coin 2.txt", "coin 3.txt", "coin 4.txt"]
    def colorText(text):
        COLORS = { "black":"\33[93m", "white":"\u001b[37m", "yellow": "\33[93m"}
        for color in COLORS:
            text = text.replace("[[" + color + "]]", COLORS[color])
        return text

    coin_heads = (f"""\n\n\n\n\n\n{y}
    {tab_spaces}                 ████████
    {tab_spaces}             ████░░░░░░░░████
    {tab_spaces}           ██░░░░▒▒▒▒▒▒▒▒░░░░██
    {tab_spaces}         ██░░▒▒▒▒░░░░░░░░▒▒▒▒░░██
    {tab_spaces}       ██░░▒▒░░    ░░░░    ░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░    ░░░░    ░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░            ░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░    ░░░░    ░░▒▒░░██
    {tab_spaces}         ██░░▒▒    ░░░░    ▒▒░░██
    {tab_spaces}           ██░░▒▒░░░░░░░░▒▒░░██
    {tab_spaces}             ████▒▒▒▒▒▒▒▒████
    {tab_spaces}                 ████████
    """)
    coin_tails = (f"""\n\n\n\n\n\n{y}
    {tab_spaces}                 ████████
    {tab_spaces}             ████░░░░░░░░████
    {tab_spaces}           ██░░░░▒▒▒▒▒▒▒▒░░░░██
    {tab_spaces}         ██░░▒▒▒▒░░░░░░░░▒▒▒▒░░██
    {tab_spaces}       ██░░▒▒░░            ░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░░░░░    ░░░░░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░░░░░    ░░░░░░▒▒░░██
    {tab_spaces}       ██░░▒▒░░░░░░    ░░░░░░▒▒░░██
    {tab_spaces}         ██░░▒▒░░░░    ░░░░▒▒░░██
    {tab_spaces}           ██░░▒▒░░░░░░░░▒▒░░██
    {tab_spaces}             ████▒▒▒▒▒▒▒▒████
    {tab_spaces}                 ████████
    """)
    pygame.init()  # initializing for pygame
    mixer.music.load("CoinsFlippin.mp3")
    mixer.music.play()
    frames = []
    for name in filenames:
        with open(name, "r", encoding="UTF-8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            ascii = "".join(frame)
            os.system("cls")
            print(colorText(ascii))
            time.sleep(delay)
            os.system("cls")
    random_coin = random.choice((coin_heads,coin_tails))  # Toss coin random
    print(random_coin, reset)
    pygame.mixer.music.stop()
    if (random_coin == coin_heads and headsOrTails_answer == "heads") or (random_coin == coin_tails and headsOrTails_answer == "tails"):
        print(f'''{y}
\t\t\t\t\t\t\t\t\t\t\t    █▄█ █▀█ █░█ █▀█   ▀█▀ █░█ █▀█ █▄░█  {w}
\t\t\t\t\t\t\t\t\t\t\t    ░█░ █▄█ █▄█ █▀▄   ░█░ █▄█ █▀▄ █░▀█  \n\n'''.center(200), reset)
    else:
                print(f'''{w}
\t\t\t\t\t\t\t\t\t\t █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀  ▀█▀ █░█ █▀█ █▄░█  {y}
\t\t\t\t\t\t\t\t\t\t █▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█  ░█░ █▄█ █▀▄ █░▀█  \n\n'''.center(200), reset)
    if random_coin == coin_heads: return "heads"
    return 'tails'

def join_lines(list_):
    lines = [string.splitlines() for string in list_]
    return '\n'.join(''.join(lines) for lines in zip(*lines))

def print_gameOver_text():
    print(f"{r}\n\n",'''
\t\t                                                        ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
\t\t                                                       ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
\t\t                                                       ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
\t\t                                                       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
\t\t                                                       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
\t\t                                                        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝'''.center(200), reset)

def print_youLose_text():
    print(f"{y}\n\n",'''
 \t\t                                                           ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
 \t\t                                                           ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 \t\t                                                            ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
 \t\t                                                             ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
 \t\t                                                              ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
 \t\t                                                              ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝'''.center(200), reset) 

def print_winning_text():
    print(f"{y}\n\n",'''
\t\t                          ██╗   ██╗ ██████╗ ██╗   ██╗     █████╗ ██████╗ ███████╗    ████████╗██╗  ██╗███████╗    ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
\t\t                          ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
\t\t                           ╚████╔╝ ██║   ██║██║   ██║    ███████║██████╔╝█████╗         ██║   ███████║█████╗      ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
\t\t                            ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██╗██╔══╝         ██║   ██╔══██║██╔══╝      ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
\t\t                             ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║███████╗       ██║   ██║  ██║███████╗    ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║
\t\t                             ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝'''.center(200), reset)

def print_yourDeck_text():
    print(f'''\n
{w}█▄█ █▀█ █░█ █▀█   {r}█▀▄ █▀▀ █▀▀ █▄▀ ▀
{r}░█░ █▄█ █▄█ █▀▄  {w} █▄▀ ██▄ █▄▄ █░█ ▄\n{reset}''')

def print_computersDeck_text():
    print(f'''\n
{w}█▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀  {r} █▀▄ █▀▀ █▀▀ █▄▀ ▀
{r}█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█  {w} █▄▀ ██▄ █▄▄ █░█ ▄\n{reset}''')

def print_monkeyCard_text():
    print(f'''\n
{y}█▀▄▀█ █▀█ █▄░█ █▄▀ █▀▀ █▄█ {w}  █▀▀ ▄▀█ █▀█ █▀▄ ▀
{w}█░▀░█ █▄█ █░▀█ █░█ ██▄ ░█░ {y}  █▄▄ █▀█ █▀▄ █▄▀ ▄{w}''')

def print_thankYou_text():
    os.system("cls")
    print(f'''{y}\n\n\n\n\n\n\n{w}
                                    {reset}              ⠀⠀ ⣠⣶⡾⠏⠉⠙⠳⢦⡀{r}⠀⠀ ⢠⠞⠉⠙⠲⡀{reset}⠀
                                                ⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀ ⢳⡀{r}  ⡏⠀⠀⠀  ⢷{reset}
                                                ⠀⠀⢠⣟⣋⡀{w}⢀⣀⣀⡀⠀⣀⡀{reset} ⣧⠀{r}⢸⠀⠀⠀⠀⠀  ⡇{reset}   
                                            ⠀     ⢸⣯⡭⠁{w}⠸⣛⣟⠆⡴⣻⡲{reset} ⣿{r}⠀⣸⠀{w} BYE {r} ⡇{reset}   {y}           ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
                                    {reset}            ⠀ ⣟⣿⡭⠀⠀{w}⠀⠀⠀⢱⠀⠀{reset} ⣿ {r}⢹⠀⠀⠀⠀ ⠀ ⡇ {reset}         {y}    ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
                                    {reset}              ⠙⢿⣯⠄⠀⠀{w}⠀⢀⡀⠀{reset} ⠀⡿ ⠀{r}⡇⠀⠀⠀⠀ ⡼ {reset}       {y}          ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
                                     {reset}           ⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀ {r}⠘⠤⣄⣠⠞⠀ {reset}             {w}     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
                                    {reset}        ⠀⠀⠀⠀  ⠀  ⢸⣷⡦⢤⡤⢤⣞⣁⠀                     {w}       ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
                                         {w}       ⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀                       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝
                                      {w}          ⣼⣿⠍⠉⣿⡭⠉⠙{r}⢺⣇⣼⡏⠀⠀⠀{w}⣄⢸⠀⠀{w}
                                     {y}          ⣿⣿⣧⣀⣿………⣀⣰⣏⣘⣆⣀{reset}⠀⠀

    \n\n''')

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "You Lose Sound Effect.mp3"
    tts.save(filename)
    playsound2.playsound(filename)

def play_enterSound():
    pygame.init() 
    mixer.music.load("enter.mp3")
    mixer.music.play()

def display_youLose_ending():
    print_youLose_text()
    print_yourDeck_text()
    user_deck.print_deck()
    print_monkeyCard_text()
    print(f"\n{y}{deck.monkey_card}")
    playsound2.playsound("lose_sound.wav")
    speak("you lose, you're the monkey")

def display_winning_ending():
    print_winning_text()
    print_computersDeck_text()
    computer_deck.print_deck()
    print_monkeyCard_text()
    print(f"\n{y}{deck.monkey_card}")
    playsound2.playsound("winner.wav")
    speak("Congratulations, you are the winner!, I am the monkey")

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    monkey_card = None
    def __init__(self, head=None):
        def make_card( value, symbol):
            if card_theme_choice==1:
                card = color_theme_choice+"""\
┌─────────┐
│{}       │
│         │
│    {}    │
│         │
│       {}│
└─────────┘
{}""".format(f'{value: <2}', f'{symbol: <2}', f'{value: <2}', reset)
            elif card_theme_choice==2:
                card = color_theme_choice+"""\
┌─────────┐
│{}       │
│         │
│    {}   │
│         │
│       {}│
└─────────┘
{}""".format(f'{value: <2}', f'{symbol: <2}', f'{value: <2}', reset)
            elif card_theme_choice==3:
                card = color_theme_choice + """\
┌─────────┐
│{}       │
│         │
│    {}    │
│         │
│       {}│
└─────────┘
{}""".format(f'{value: <2}', f'{symbol: <2}', f'{value: <2}', reset)
            elif card_theme_choice==4:
                card = color_theme_choice+"""\
┌─────────┐
│{}       │
│         │
│    {}    │{}
│         │
│       {}│
└─────────┘
{}""".format(f'{value: <2}', f'{symbol: <1}', f"{y}", f'{value: <2}', reset)
            else:
                card = """\
┌─────────┐
│{}       │
│         │
│    {}    │
│         │
│       {}│
└─────────┘
{}""".format(f'{value: <2}', f'{symbol: <2}', f'{value: <2}', reset)
            return card

        if card_theme_choice==1: card_types = [f'{r}♥', f'{b}♣{r}', f'{b}♠{r}',f'{r}♦'] 
        elif card_theme_choice in (2,4): card_types = ['♥', '♣', "♠", '♦']
        else: card_types = [f'{reset}{r}♥{reset}', f'{reset}{b}♣{reset}', f"{reset}{b}♠{reset}", f'{reset}{r}♦{reset}']
        self.deck = [make_card("A", card_type) for card_type in card_types]
        for i in range(2,11):
            self.deck += [make_card(str(i), card_type) for card_type in card_types] 
        for card_type1 in ["J", "Q", "K"]:
            self.deck += [make_card(card_type1, card_type) for card_type in card_types]
        self.head = head
    
    def append(self, value):
        if not self.head:
            self.head = Node(value, None)
            return

        curr_node = self.head
        while curr_node.next_node:
            curr_node = curr_node.next_node
        curr_node.next_node = Node(value, None)
    
    def get_elements(self):
        curr_node = self.head
        elements = []
        while curr_node:
            elements.append(curr_node.value)
            curr_node = curr_node.next_node
        return elements

    def get_length(self):
        length = 0
        curr_node = self.head
        while curr_node:
            length+=1
            curr_node = curr_node.next_node
        return length

    def extend(self, values):
        for value in values:
            self.append(value)

    def remove_at(self, index):
        if not index:
            removed_card = self.head.value
            self.head = self.head.next_node
            return removed_card
        curr_node = self.head
        i = 0
        while curr_node:
            if i == index - 1:
                removed_card = curr_node.next_node.value
                curr_node.next_node = curr_node.next_node.next_node
                return removed_card
            i+=1
            curr_node = curr_node.next_node
        
    def shuffle(self):
        cards = self.get_elements()
        random.shuffle(cards)
        self.head = None
        for card in cards:
            self.append(card)

    def print_deck(self, color=""):
        deck = self.get_elements()      
        card_num = self.get_length()
        print(join_lines(deck[:18]), end=color)
        if card_num>=18:print(join_lines(deck[18:36]), end=color)
        if card_num>=36:print(join_lines(deck[36:]), end=color)

    def has(self, value):
        curr_node = self.head
        for _ in range(self.get_length()):
            if curr_node.value == value:
                return True
            curr_node = curr_node.next_node
        return False
        
    def find_paired_cards(self, remove_pairs = True):
        self.paired_cards = LinkedList()
        card_2be_paired = self.head
        while card_2be_paired:
            next_card = card_2be_paired.next_node
            while next_card:
                if card_2be_paired.value[len(color_theme_choice)+13] == next_card.value[len(color_theme_choice)+13] and not self.paired_cards.has(card_2be_paired.value):
                    if remove_pairs:
                        self.remove(card_2be_paired.value)  
                        self.remove(next_card.value)
                    self.paired_cards.append(card_2be_paired.value)
                    self.paired_cards.append(next_card.value)
                    break
                next_card = next_card.next_node
            card_2be_paired = card_2be_paired.next_node

    def remove(self, value):
            temp = self.head
            if temp.value == value:
                self.head = temp.next_node
                temp = None
                return
            while(temp is not None):
                if temp.value == value:
                    break
                prev = temp
                temp = temp.next_node
            if(temp == None):
                return
            prev.next_node = temp.next_node
            temp = None


get_monkey_animation()
pygame.init() 
mixer.music.load("Track.mp3")
mixer.music.play(-1)
display_main_menu()  
os.system("cls")
while True: 
    display_main_menu(False) 
    try:
        main_menu_choice = int(input(f"\t\t\t\t\t\t\t\t\t\t\t\t\t  {r}➤  {w}"))
        if main_menu_choice == 2:
            os.system("cls")
            get_percentage_loadingAnimation()
            card_theme_choice = display_cardTheme_choices()
            if not card_theme_choice: 
                continue
            elif card_theme_choice==1: color_theme_choice=  r
            elif card_theme_choice==2: color_theme_choice= wh
            elif card_theme_choice==3: color_theme_choice = r
            elif card_theme_choice==4: color_theme_choice = r
            else: color_theme_choice = ""
            os.system("cls")
            pygame.mixer.music.stop()
            play_enterSound()
            get_rocket_animation()
            os.system("cls")
            # ------------------------------------------------------------------------------------------------------------------------------------------------game starts here
            #creation of the deck        
            deck = LinkedList()
            deck.extend(deck.deck)
            print(f"""
\t\t\t\t\t\t\t\t\t\t\t {r}█▀▄ █▀▀ █▀▀ █▄▀
\t\t\t\t\t\t\t\t\t\t{w}{deck.get_length()} Cards{reset} {r}█▄▀ ██▄ █▄▄ █░█{w} {deck.get_length()} Cards{reset}\n""")
            deck.print_deck(); print("\n")
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t\t{w}ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()
            os.system("cls")

            #moneky card picking and displaying
            LinkedList.monkey_card = deck.remove_at(random.choice(list(range(0,52))))
            print(f"""{y}
█▀▄▀█ █▀█ █▄░█ █▄▀ █▀▀ █▄█   █▀▀ ▄▀█ █▀█ █▀▄
{b}█░▀░█ █▄█ █░▀█ █░█ ██▄ ░█░   █▄▄ █▀█ █▀▄ █▄▀{reset}""")    
            with open("mkey.txt", "r", encoding="UTF-8") as f:
                a = f.read()
            print(a)
            print(f"\n{y}{deck.monkey_card}")
            Loading = [ f"{y}◑    ", f"{y} ◒   ", f"{y}  ◐  ", f"{y}   ◓ ", f"{y}    ◑", f"{y}   ◓ ", f"{y}  ◐  ", f"{y} ◒   " ]
            i = 0
            while i != 17:
                print(f'\t{y}   ＬＯＡ{w}ＤＩＮＧ',Loading[i % len(Loading)], end='\r')
                time.sleep(.2)
                i += 1
            input(f'    {w}ＥＮＴＥＲ {y}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()

            #deck without Monkey Card
            print(f"""
\t\t\t\t\t\t\t\t\t\t\t {r}█▀▄ █▀▀ █▀▀ █▄▀
\t\t\t\t\t\t\t\t\t\t{w}{deck.get_length()} Cards{reset} {r}█▄▀ ██▄ █▄▄ █░█{w} {deck.get_length()} Cards{reset}\n""")
            deck.print_deck(); print("\n")
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t\t{w}  ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()
            os.system("cls")
            get_shuffling_animation()
            time.sleep(1)

            #shuffled Deck
            os.system("cls")
            print(f"""
\t\t\t\t\t\t\t\t\t {r}█▀ █░█ █░█ █▀▀ █▀▀ █░░ █▀▀ █▀▄   █▀▄ █▀▀ █▀▀ █▄▀
\t\t\t\t\t\t\t\t{w}{deck.get_length()} Cards{reset} {r}▄█ █▀█ █▄█ █▀░ █▀░ █▄▄ ██▄ █▄▀   █▄▀ ██▄ █▄▄ █░█{w} {deck.get_length()} Cards{reset}\n""")
            deck.shuffle()
            deck.print_deck(); print("\n")
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t{w}          ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()
            os.system("cls")

            #both players' deck
            user_deck = LinkedList()
            computer_deck = LinkedList()

            #allocationg & displaying
            player_2give_cards = random.choice((computer_deck, user_deck))
            for card in deck.get_elements():    
                player_2give_cards.append(card)
                if player_2give_cards ==  computer_deck:
                    player_2give_cards = user_deck
                else:
                    player_2give_cards = computer_deck
            #displaying and eliminating computer's paired cards
            print(f"""
\t\t\t\t\t\t\t\t\t {b}█▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀   █▀▄ █▀▀ █▀▀ █▄▀
\t\t\t\t\t\t\t\t{w}{computer_deck.get_length()} Cards{reset} {r}█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█   █▄▀ ██▄ █▄▄ █░█{w} {computer_deck.get_length()} Cards{reset}\n""")
            computer_deck.print_deck()
            computer_deck.find_paired_cards()
            print(f"""
\t\t\t\t\t\t\t    {r}█▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀   █▀█ ▄▀█ █ █▀█ █▀▀ █▀▄  █▀▀ ▄▀█ █▀█ █▀▄ █▀
\t\t\t\t\t\t   {w}{computer_deck.paired_cards.get_length()} Cards{reset}\
 {b}█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█   █▀▀ █▀█ █ █▀▄ ██▄ █▄▀  █▄▄ █▀█ █▀▄ █▄▀ ▄█{w} {computer_deck.paired_cards.get_length()} Cards{reset}\n""")
            computer_deck.paired_cards.print_deck(); print("\n")
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t\t{w} ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()
            #displaying and eliminating user's paired cards
            print(f"""\n\n
\t\t\t\t\t\t\t\t\t        {r}█▄█ █▀█ █░█ █▀█   █▀▄ █▀▀ █▀▀ █▄▀
\t\t\t\t\t\t\t\t       {w}{user_deck.get_length()} Cards{reset} {b}░█░ █▄█ █▄█ █▀▄   █▄▀ ██▄ █▄▄ █░█{w} {user_deck.get_length()} Cards{reset}\n""")
            user_deck.print_deck()
            user_deck.find_paired_cards()
            print(f"""
\t\t\t\t\t\t\t\t    {b}█▄█ █▀█ █░█ █▀█   █▀█ ▄▀█ █ █▀█ █▀▀ █▀▄  █▀▀ ▄▀█ █▀█ █▀▄ █▀
\t\t\t\t\t\t\t   {w}{user_deck.paired_cards.get_length()} Cards{reset} {r}░█░ █▄█ █▄█ █▀▄   █▀▀ █▀█ █ █▀▄ ██▄ █▄▀  █▄▄ █▀█ █▀▄ █▄▀ ▄█{w} {user_deck.paired_cards.get_length()} Cards{reset}\n""")
            user_deck.paired_cards.print_deck(); print("\n")
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t\t{w}    ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
            play_enterSound()

            #both players' remaining cards
            print(f"""\n\n
\t\t\t\t\t\t\t\t\t {b}█▀█ █▀▀ █▀▄▀█ ▄▀█ {r}█ █▄░█ █ █▄░█{b} █▀▀ {r} █▀▀ ▄▀█{b} █▀█ █▀▄ █▀
\t\t\t\t\t\t\t\t\t{w}{b} █▀▄ ██▄ █░▀░█ █▀█ {r}█ █░▀█ █ █░▀█ {b}█▄█ {r} █▄▄ █▀█ {b}█▀▄ █▄▀ ▄█{w} \n\n""")
            print(f"{w}ＣＯＭＰＵＴＥＲ'Ｓ ＤＥＣＫ {r}({computer_deck.get_length()} ＣＡＲＤＳ):\n{reset}")
            computer_deck.print_deck()
            print(f"{r}\nＹＯＵＲ ＤＥＣＫ {w}({user_deck.get_length()} ＣＡＲＤＳ):\n{reset}")
            user_deck.print_deck(); print("\n")
            Loading = [ f"{y}◑    ", f"{y} ◒   ", f"{y}  ◐  ", f"{y}   ◓ ", f"{y}    ◑", f"{y}   ◓ ", f"{y}  ◐  ", f"{y} ◒   " ]
            get_loading_animation()
            input(f'\t\t\t\t\t\t\t\t\t\t{w}     ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')   
            play_enterSound()                                                                           
            os.system("cls")

            # heads or tails
            if user_deck.get_length() and computer_deck.get_length():
                print(f"""\n\n\n\n\n\n
\t\t\t\t\t\t\t\t\t\t    {w}█░█ █▀▀ ▄▀█ █▀▄ █▀  {w} █▀█ █▀█   {y}▀█▀ ▄▀█ █ █░░ █▀
\t\t\t\t\t\t\t\t\t\t    {y}█▀█ ██▄ █▀█ █▄▀ ▄█  {w} █▄█ █▀▄   {w}░█░ █▀█ █ █▄▄ ▄█""")
                while True:
                    headsOrTails_answer = input(f"\n{w}\t\t\t\t\t\t\t\t\t\t\t\t      ➔{y}  ").lower()
                    if headsOrTails_answer in ("tails", "heads"):
                        play_enterSound()
                        coinFlip_result = get_tossCoin_animation(headsOrTails_answer)
                        input(f'\t\t\t\t\t\t\t\t\t\t\t{w}     ＥＮＴＥＲ {y}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
                        play_enterSound()
                        users_turn = headsOrTails_answer == coinFlip_result 
                        break
                    else:
                        print(f"""\t\t\t\t\t\t\t\t\t\t\t{w}   Pʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴇɪᴛʜᴇʀ {y}HEADS {w}ᴏʀ{y} TAILS""", end="")
                game_over = False
                while computer_deck.get_length() and user_deck.get_length():
                    if game_over:
                        break
                    if users_turn:
                        get_shuffling_animation(True,f" {' '*10}█▀ █░█ █░█ █▀▀ █▀▀ █░░ █ █▄░█ █▀▀",f"{' '*7}    ▄█ █▀█ █▄█ █▀░ █▀░ █▄▄ █ █░▀█ █▄█\n",\
                        f"\n   █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀  █▀▄ █▀▀ █▀▀ █▄▀",f"█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█  █▄▀ ██▄ █▄▄ █░█","","","","","", f"{' '*10}")
                        print(f'''\n\n{r}
\t\t █▄█ █▀█ █░█ █▀█   ▀█▀ █░█ █▀█ █▄░█  {w}
\t\t ░█░ █▄█ █▄█ █▀▄   ░█░ █▄█ █▀▄ █░▀█  \n'''.center(200), reset)
                        computer_deck.shuffle()
                        print(f"{r}ＣＯＭＰＵＴＥＲ'Ｓ ＤＥＣＫ {w}({computer_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                        print(join_lines([FLIPPED_CARD for _ in range(computer_deck.get_length())]))
                        print("".join([str(i+1).center(11) for i in range(computer_deck.get_length())]), f"{w}\n\n\t\t  Ｅｎｔｅｒ {r}ｙｏｕｒ {w}ｐｉｃｋ: {r}", end="")
                        while True:
                            try:
                                picked_card = int(input())
                                if picked_card in range(1, computer_deck.get_length()+1):
                                    play_enterSound()
                                    print(f"\n\n{r}ＰＩＣＫＥＤ {y}ＣＡＲＤ:\n{reset}")
                                    actual_picked_card = computer_deck.remove_at(picked_card-1)
                                    user_deck.append(actual_picked_card)
                                    print(actual_picked_card)
                                    if computer_deck.get_length(): print(f"{r}ＣＯＭＰＵＴＥＲ'Ｓ ＤＥＣＫ {w}({computer_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                                    computer_deck.print_deck()
                                    user_deck.find_paired_cards(remove_pairs=False)

                                    if user_deck.paired_cards.get_length():               
                                        print(f"{y}\nＹＯＵＲ ＰＡＩＲＥＤ {r}ＣＡＲＤＳ ({user_deck.paired_cards.get_length()} ＣＡＲＤＳ):\n{reset}")
                                        user_deck.paired_cards.print_deck()   
                                    else:
                                        print(f"{r}\n",f"\t\t\t\t      ＮＯ {y}ＰＡＩＲＥＤ ＣＡＲＤＳ", reset)

                                    print(f"{r}\nＹＯＵＲ ＤＥＣＫ {w}({user_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                                    user_deck.print_deck()
                                    print(r,"".join([str(i+1).center(11) for i in range(user_deck.get_length())]))
                                    print(f'\n   {ln}{r}\n           ＬＡＹ {w}ＤＯＷＮ ＣＡＲＤＳ{w}\n\n          Aꜱᴄᴇɴᴅɪɴɢ {r} Fᴏʀᴍᴀᴛ: 1,2,3...{w}{r}\n\n            ＯＲ {w}"{r}０{w}" ＴＯ ＳＫＩＰ\n   {ln}',reset)
                                    while True:
                                        try:
                                            inputed_cardNumbers_2Discard = tuple(map(int,input(f'\n   {r}ＡＮＳ{w}ＷＥＲ: {y}').split(",")))
                                            if not inputed_cardNumbers_2Discard[0] and len(inputed_cardNumbers_2Discard)==1: # if input is 0/skip
                                                play_enterSound()
                                                break
                                            card_nums = list(range(1, user_deck.get_length()+1))
                                            valid_inputed_cardNumbers_2Discard = True
                                            previous_cardNum = 0 
                                            for card_num in inputed_cardNumbers_2Discard:
                                                if not card_num in card_nums or previous_cardNum > card_num:
                                                    valid_inputed_cardNumbers_2Discard = False
                                                    break
                                                else:
                                                    card_nums.remove(card_num) 
                                                previous_cardNum = card_num
                                            if valid_inputed_cardNumbers_2Discard: # if desired cardNum\s to discrad are\is in the deck
                                                if len(inputed_cardNumbers_2Discard)%2==0 and len(inputed_cardNumbers_2Discard) <= user_deck.paired_cards.get_length():
                                                    play_enterSound()
                                                    #get desired cards numbers to discard
                                                    actual_cardNums_2be_discard = []
                                                    count = 1
                                                    for card_num in inputed_cardNumbers_2Discard:
                                                        actual_cardNums_2be_discard.append(user_deck.remove_at(card_num-count)[13])
                                                        count+=1
                                                    #get paired cards numbers
                                                    pairedCards_nums = [] 
                                                    for i in range(user_deck.paired_cards.get_length()):
                                                        pairedCards_nums.append(user_deck.paired_cards.remove_at(i-i)[13])
                                                    #check if desired cards to discard are in paired cards
                                                    for card_num in actual_cardNums_2be_discard:
                                                        if not card_num in pairedCards_nums:
                                                            print_gameOver_text()
                                                            playsound2.playsound("game over.wav")
                                                            speak("Game Over!")
                                                            game_over = True
                                                            os.system("cls")
                                                            get_percentage_loadingAnimation()
                                                            pygame.init() 
                                                            mixer.music.load("Track.mp3")
                                                            mixer.music.play(-1)
                                                            break
                                                        else:
                                                            pairedCards_nums.remove(card_num)
                                                else:
                                                    print_gameOver_text()
                                                    playsound2.playsound("game over.wav")
                                                    speak("Game Over!")
                                                    game_over = True
                                                    os.system("cls")
                                                    get_percentage_loadingAnimation()
                                                    pygame.init() 
                                                    mixer.music.load("Track.mp3")
                                                    mixer.music.play(-1)
                                                    break
                                                break
                                            else:
                                                print(f'\n   {ln}{r}\n           ＬＡＹ {w}ＤＯＷＮ ＣＡＲＤＳ{w}\n          {y}({w}Aꜱᴄᴇɴᴅɪɴɢ {r} Fᴏʀᴍᴀᴛ: 1,2,3...{y}){y}{r}\n            ＯＲ {w}"{r}０{w}" ＴＯ ＳＫＩＰ\n   {ln}',reset)
                                        except:
                                            print(f'\n   {ln}{r}\n           ＬＡＹ {w}ＤＯＷＮ ＣＡＲＤＳ{w}\n          {y}({w}Aꜱᴄᴇɴᴅɪɴɢ {r} Fᴏʀᴍᴀᴛ: 1,2,3...{y}){y}{r}\n            ＯＲ {w}"{r}０{w}" ＴＯ ＳＫＩＰ\n   {ln}',reset)
                                    users_turn = False
                                    break
                                else:
                                    print(f"\n{w}Ｉｎｖａｌｉｄ{r} ｃａｒｄ {w}ｎｕｍｂｅｒ:{r} ", end="")
                            except:
                                print(f"\n{w}Ｉｎｖａｌｉｄ{r} ｃａｒｄ {w}ｎｕｍｂｅｒ:{r} ", end="")
                    else:
                        get_shuffling_animation(True," █▀ █░█ █░█ █▀▀ █▀▀ █░░ █ █▄░█ █▀▀"," ▄█ █▀█ █▄█ █▀░ █▀░ █▄▄ █ █░▀█ █▄█\n",\
                        "\n   █▄█ █▀█ █░█ █▀█   █▀▄ █▀▀ █▀▀ █▄▀","░█░ █▄█ █▄█ █▀▄   █▄▀ ██▄ █▄▄ █░█","","","","","","")
                        print(f'''\n\n\t{r}
\t█▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█ ▀ █▀  ▀█▀ █░█ █▀█ █▄░█  {w}
\t█▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄ ░ ▄█  ░█░ █▄█ █▀▄ █░▀█ \n'''.center(200), reset)
                        user_deck.shuffle()
                        print(f"{r}\nＹＯＵＲ ＤＥＣＫ {w}({user_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                        user_deck.print_deck()
                        print()
                        Loading = [ f"{y}◑    ", f"{y} ◒   ", f"{y}  ◐  ", f"{y}   ◓ ", f"{y}    ◑", f"{y}   ◓ ", f"{y}  ◐  ", f"{y} ◒   " ]
                        i = 0
                        while i != 17:
                            print(f'\t\t{y}   ＰＩＣＫ{r}ＩＮＧ',Loading[i % len(Loading)], end='\r')
                            time.sleep(.2)
                            i += 1
                        input(f'\t\t    {w}ＥＮＴＥＲ {y}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
                        play_enterSound()
                        print(f"\n{r}\nＰＩＣＫＥＤ {y}ＣＡＲＤ:\n{reset}")
                        actual_picked_card = user_deck.remove_at(random.choice(list(range(1,user_deck.get_length()+1)))-1)
                        computer_deck.append(actual_picked_card)
                        print(actual_picked_card)
                        print(f"{r}ＣＯＭＰＵＴＥＲ'Ｓ ＤＥＣＫ {w}({computer_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                        computer_deck.print_deck()
                        computer_deck.find_paired_cards()
                        if computer_deck.paired_cards.get_length():
                            print(f"{y}\nＣＯＭＰＵＴＥＲ'Ｓ ＰＡＩＲＥＤ {r}({computer_deck.paired_cards.get_length()} ＣＡＲＤＳ):\n{reset}")
                            computer_deck.paired_cards.print_deck()
                        else:
                            print(f"{r}\n",f"\t\t\t\t\tＮＯ {y}ＰＡＩＲＥＤ ＣＡＲＤＳ", reset)
                        if user_deck.get_length(): print(f"{r}\nＹＯＵＲ ＤＥＣＫ {w}({user_deck.get_length()} ＣＡＲＤ/Ｓ):\n{reset}")
                        user_deck.print_deck()
                        users_turn = True
                        input(f'{w}\n\t\t\tＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')  
                        play_enterSound()
                else:
                    if user_deck.get_length():
                        display_youLose_ending()
                    else:
                        display_winning_ending()
                    input(f'\t\t\t\t\t\t\t\t\t\t{w} ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
                    os.system("cls")
                    get_percentage_loadingAnimation()
                    pygame.init() 
                    mixer.music.load("Track.mp3")
                    mixer.music.play(-1)
            else:
                if user_deck.get_length():
                    display_youLose_ending()
                else:
                    display_winning_ending()
                input(f'\t\t\t\t\t\t\t\t\t\t{w} ＥＮＴＥＲ {r}ｔｏ {w}ＣＯＮＴＩＮＵＥ')
                os.system("cls")
                get_percentage_loadingAnimation()
                pygame.init() 
                mixer.music.load("Track.mp3")
                mixer.music.play(-1)
        elif main_menu_choice == 1:
            os.system("cls")
            display_guide()
        elif main_menu_choice ==3:
            print_thankYou_text()
            break
    except:
        pass