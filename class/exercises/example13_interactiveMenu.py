#!/usr/bin/python2.3
import sys, os, re, datetime, time, pwd, platform, shutil, string, getopt, traceback
from random import randint
import signal

def signal_handler(signal, frame):
    return 0
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, signal_handler)

font_six= """
|       |  ###  |### ###|  # #  |   #   |###   #|  ##   |  ###  |
|       |  ###  |### ###|  # #  |  #### |# #  # | #  #  |  ###  |
|       |  ###  | #   # |#######| # #   |### #  |  ##   |   #   |
|       |   #   | #   # |  # #  | ##### |   #   | ###   |   #   |
|       |       |       |#######|   #  #|  # ###|#   # #|       |
|       |  ###  |       |  # #  | ##### | #  # #|#    # |       |
|       |  ###  |       |  # #  |   #   |#   ###| #### #|       |
-----------------------------------------------------------------
|   #   |   #   |       |       |       |       |       |      #|
|  #    |    #  | #   # |   #   |       |       |       |     # |
| #     |     # |  # #  |   #   |       |       |       |    #  |
| #     |     # |#######| ##### |  ###  | ##### |       |   #   |
| #     |     # |  # #  |   #   |  ###  |       |  ###  |  #    |
|  #    |    #  | #   # |   #   |   #   |       |  ###  | #     |
|   #   |   #   |       |       |  #    |       |  ###  |#      |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
|   ##  |   #   |  #### | ##### |    ## | ######|  #### | ######|
|  #  # | ###   | #    #|      #|   # # | #     | #     |     # |
| #  # #|   #   |    ## |  #### |  #  # | ##### | # ### |    #  |
| # #  #|   #   |  ##   |      #| ######|      #| ##   #|   #   |
|  #  # |   #   | #     |      #|     # | #    #| #    #|  #    |
|   ##  | ##### | ######| ##### |     # |  #### |  #### |  #    |
-----------------------------------------------------------------
|       |       |   #   |  ###  |    #  |       |  #    |       |
|  #### |  #### |  ###  |  ###  |   #   |       |   #   |  #### |
| #    #| #    #|   #   |       |  #    | ##### |    #  | #    #|
|  #### | #    #|       |  ###  | #     |       |     # |    ## |
| #    #|  #####|   #   |  ###  |  #    | ##### |    #  |   #   |
| #    #|      #|  ###  |   #   |   #   |       |   #   |       |
|  #### |  #### |   #   |  #    |    #  |       |  #    |   #   |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
|  #### |   ##  | ##### |  #### | ##### | ######| ######|  #### |
| #    #|  #  # | #    #| #    #| #    #| #     | #     | #    #|
| # ## #| #    #| ##### | #     | #    #| ##### | ##### | #     |
| # ####| ######| #    #| #     | #    #| #     | #     | #  ###|
| #     | #    #| #    #| #    #| #    #| #     | #     | #    #|
|  #### | #    #| ##### |  #### | ##### | ######| #     |  #### |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
| #    #|    #  |      #| #    #| #     | #    #| #    #|  #### |
| #    #|    #  |      #| #   # | #     | ##  ##| ##   #| #    #|
| #    #|    #  |      #| ####  | #     | # ## #| # #  #| #    #|
| ######|    #  |      #| #  #  | #     | #    #| #  # #| #    #|
| #    #|    #  | #    #| #   # | #     | #    #| #   ##| #    #|
| #    #|    #  |  #### | #    #| ######| #    #| #    #|  #### |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
| ##### |  #### | ##### |  #### |  #####| #    #| #    #| #    #|
| #    #| #    #| #    #| #     |    #  | #    #| #    #| #    #|
| #    #| #    #| #    #|  #### |    #  | #    #| #    #| #    #|
| ##### | #  # #| ##### |      #|    #  | #    #| #    #| # ## #|
| #     | #   # | #   # | #    #|    #  | #    #|  #  # | ##  ##|
| #     |  ### #| #    #|  #### |    #  |  #### |   ##  | #    #|
-----------------------------------------------------------------
|       |       |       | ##### |#      | ##### |   #   |       |
| #    #|  #   #| ######| #     | #     |     # |  # #  |       |
|  #  # |   # # |     # | #     |  #    |     # | #   # |       |
|   ##  |    #  |    #  | #     |   #   |     # |       |       |
|   ##  |    #  |   #   | #     |    #  |     # |       |       |
|  #  # |    #  |  #    | #     |     # |     # |       |       |
| #    #|    #  | ######| ##### |      #| ##### |       |#######|
-----------------------------------------------------------------
|  ###  |       |       |       |       |       |       |       |
|  ###  |   ##  | ##### |  #### | ##### | ######| ######|  #### |
|   #   |  #  # | #    #| #    #| #    #| #     | #     | #    #|
|    #  | #    #| ##### | #     | #    #| ##### | ##### | #     |
|       | ######| #    #| #     | #    #| #     | #     | #  ###|
|       | #    #| #    #| #    #| #    #| #     | #     | #    #|
|       | #    #| ##### |  #### | ##### | ######| #     |  #### |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
| #    #|    #  |      #| #    #| #     | #    #| #    #|  #### |
| #    #|    #  |      #| #   # | #     | ##  ##| ##   #| #    #|
| #    #|    #  |      #| ####  | #     | # ## #| # #  #| #    #|
| ######|    #  |      #| #  #  | #     | #    #| #  # #| #    #|
| #    #|    #  | #    #| #   # | #     | #    #| #   ##| #    #|
| #    #|    #  |  #### | #    #| ######| #    #| #    #|  #### |
-----------------------------------------------------------------
|       |       |       |       |       |       |       |       |
| ##### |  #### | ##### |  #### |  #####| #    #| #    #| #    #|
| #    #| #    #| #    #| #     |    #  | #    #| #    #| #    #|
| #    #| #    #| #    #|  #### |    #  | #    #| #    #| #    #|
| ##### | #  # #| ##### |      #|    #  | #    #| #    #| # ## #|
| #     | #   # | #   # | #    #|    #  | #    #|  #  # | ##  ##|
| #     |  ### #| #    #|  #### |    #  |  #### |   ##  | #    #|
-----------------------------------------------------------------
|       |       |       |  ###  |   #   |  ###  | ##    |#######|
| #    #|  #   #| ######| #     |   #   |     # |#  #  #|#######|
|  #  # |   # # |     # | #     |   #   |     # |    ## |#######|
|   ##  |    #  |    #  |##     |   #   |     ##|       |#######|
|   ##  |    #  |   #   | #     |   #   |     # |       |#######|
|  #  # |    #  |  #    | #     |   #   |     # |       |#######|
| #    #|    #  | ######|  ###  |   #   |  ###  |       |#######|
"""

font_five="""
|      |      |      |      |   #  |###  #|      |      |
|      |  ##  | ## ##|  # # |  ####|# # # |  ##  |  ##  |
|      |  ##  | ## ##| #####| # #  |####  | #  # |  ##  |
|      |  ##  | ## ##|  # # |  ### |  ####| ###  | #    |
|      |      |      | #####|   # #| # # #|#   ##|      |
|      |  ##  |      |  # # | #### |#  ###| ### #|      |
---------------------------------------------------------
|  #   |   #  |      |      |      |      |      |      |
| #    |    # | #   #|   #  |      |      |      |    # |
| #    |    # |  # # |   #  |      |      |      |   #  |
| #    |    # | #####| #####|  ##  | #### |      |  #   |
| #    |    # |  # # |   #  |  ##  |      |  ##  | #    |
|  #   |   #  | #   #|   #  |   #  |      |  ##  |#     |
---------------------------------------------------------
|      |      |      |      |      |      |      |      |
|  ### |   #  |  ### | #### |    # | #####|  ### | #####|
| #  ##| ###  | #   #|     #|   ## | #    | #    |     #|
| # # #|   #  |   ## |  ### |  # # | #### | #### |    # |
| ##  #|   #  |  #   |     #| #####|     #| #   #|   #  |
|  ### | #####| #####| #### |    # | #### |  ### |  #   |
---------------------------------------------------------
|      |      |      |   ## |    # |      |  #   | #### |
|  ### |  ### |   ## |   ## |   #  | #### |   #  |     #|
| #   #| #   #|   ## |      |  #   |      |    # |   ## |
|  ### |  ####|      |   ## |   #  | #### |   #  |  #   |
| #   #|     #|   ## |   ## |    # |      |  #   |      |
|  ### |  ### |   ## |    # |      |      |      |  #   |
---------------------------------------------------------
| #### |      |      |      |      |      |      |      |
|#    #|   #  | #### |  ####| #### | #####| #####|  ####|
|# ## #|  # # | #   #| #    |  #  #| #    | #    | #    |
|# ####| #   #| #### | #    |  #  #| #### | #### | # ###|
|#     | #####| #   #| #    |  #  #| #    | #    | #   #|
| #### | #   #| #### |  ####| #### | #####| #    |  ### |
---------------------------------------------------------
|      |      |      |      |      |      |      |      |
| #   #|   #  |     #| #  # | #    | #   #| #   #|  ### |
| #   #|   #  |     #| # #  | #    | ## ##| ##  #| #   #|
| #####|   #  |     #| ##   | #    | # # #| # # #| #   #|
| #   #|   #  | #   #| # #  | #    | #   #| #  ##| #   #|
| #   #|   #  |  ### | #  # | #####| #   #| #   #|  ### |
---------------------------------------------------------
|      |      |      |      |      |      |      |      |
| #### |  ### | #### |  ####| #####| #   #| #   #| #   #|
| #   #| #   #| #   #| #    |   #  | #   #| #   #| #   #|
| #### | # # #| #### |  ### |   #  | #   #| #   #| # # #|
| #    | #  # | # #  |     #|   #  | #   #|  # # | ## ##|
| #    |  ## #| #  # | #### |   #  |  ### |   #  | #   #|
---------------------------------------------------------
|      |      |      | #### |#     | #### |   #  |      |
| #   #| #   #| #####| #    | #    |    # |  # # |      |
|  # # |  # # |    # | #    |  #   |    # | #   #|      |
|   #  |   #  |   #  | #    |   #  |    # |      |      |
|  # # |   #  |  #   | #    |    # |    # |      |      |
| #   #|   #  | #####| #### |     #| #### |      |######|
---------------------------------------------------------
|  ##  |      |      |      |      |      |      |      |
|  ##  |   #  | #### |  ####| #### | #####| #####|  ####|
|   #  |  # # | #   #| #    |  #  #| #    | #    | #    |
|    # | #   #| #### | #    |  #  #| #### | #### | # ###|
|      | #####| #   #| #    |  #  #| #    | #    | #   #|
|      | #   #| #### |  ####| #### | #####| #    |  ### |
---------------------------------------------------------
|      |      |      |      |      |      |      |      |
| #   #|   #  |     #| #  # | #    | #   #| #   #|  ### |
| #   #|   #  |     #| # #  | #    | ## ##| ##  #| #   #|
| #####|   #  |     #| ##   | #    | # # #| # # #| #   #|
| #   #|   #  | #   #| # #  | #    | #   #| #  ##| #   #|
| #   #|   #  |  ### | #  # | #####| #   #| #   #|  ### |
---------------------------------------------------------
|      |      |      |      |      |      |      |      |
| #### |  ### | #### |  ####| #####| #   #| #   #| #   #|
| #   #| #   #| #   #| #    |   #  | #   #| #   #| #   #|
| #### | # # #| #### |  ### |   #  | #   #| #   #| # # #|
| #    | #  # | # #  |     #|   #  | #   #|  # # | ## ##|
| #    |  ## #| #  # | #### |   #  |  ### |   #  | #   #|
---------------------------------------------------------
|      |      |      |  ### |   #  | ###  | ##   |######|
| #   #| #   #| #####| #    |   #  |    # |#  # #|######|
|  # # |  # # |    # |##    |   #  |    ##|    # |######|
|   #  |   #  |   #  |##    |   #  |    ##|      |######|
|  # # |   #  |  #   | #    |   #  |    # |      |######|
| #   #|   #  | #####|  ### |   #  | ###  |      |######|
"""
# HACK: trim the leading linefeed off the fonts.
font_six = font_six[1:]
font_five= font_five[1:]

def dump_xpm (page, geometry=(32,32)):
    """This dumps the given page to stdout in XPM pixmap format."""
    if geometry is not None:
        page = crop (page, geometry)
    pixel_width = len(page[0])
    pixel_height= len(page)
    xpm_header = """/* XPM */
    static char * banner_xpm[] = {
    "%(pixel_width)d %(pixel_height)d 3 1",
    "   c None",
    ".  c #FFFFFF",
    "#  c #000000",
    """ % locals()
    print xpm_header
    for l in page:
        print '    "' + l + '",'
    print "};"

def dump_page (page):
    """This dumps the given page to stdout."""
    for l in page:
        print l

def rotate (page):
    """This returns the give page rotated clockwise by 90 degrees."""
    new_page = []
    for vl in zip(*page):
        ll = list(vl)
        ll.reverse()
        new_page.append(string.join(ll,sep=''))
        #print string.join(ll,sep='')
    return new_page

def hcenter (page, pixel_width):
    """This centers the "page" horizontally in the given width."""
    page_pixel_width = len(page[0])
    pad = pixel_width - page_pixel_width
    left_pad = pad/2
    right_pad = pad/2
    if left_pad+right_pad < pad:
        left_pad = left_pad + 1
    new_page = []
    for r in page:
        r = ' '*left_pad + r + ' '*right_pad
        new_page.append(r)
    return new_page

def vcenter (page, pixel_height):
    """This centers the "page" vertically in the given height."""
    page_pixel_height = len(page)
    pad = pixel_height - page_pixel_height
    top_pad = pad/2
    bottom_pad = pad/2
    if top_pad+bottom_pad < pad:
        bottom_pad = bottom_pad + 1
    new_page = []
    for r in range(top_pad):
        new_page.append(' '*len(page[0]))
    for r in page:
        new_page.append(r)
    for r in range(bottom_pad):
        new_page.append(' '*len(page[0]))
    return new_page

def c_to_coord(c):
    """This takes an ascii character and returns the 
    coordinates in the 8x11 array of character raster data.
    The 8x11 arrays of character raster data are arranged like this:

     !"#$%&'
    ()*+,-./
    01234567
    89:;<=>?
    @ABCDEFG
    HIJKLMNO
    PQRSTUVW
    XYZ[\]^_
    `abcdefg
    hijklmno
    pqrstuvw
    xyz{|}~ 
    """
    i = ord(c)-32
    y = i/8
    x = i%8
    if x < 0: x = 7;y = 11
    if x > 7: x = 7;y = 11
    if y < 0: x = 7;y = 11
    if y > 11: x = 7;y = 11
    return (x,y)

def get_raster_data_by_char_five (c=None):
    """This returns the raster data for the given character. """
    if c is None:
        return ['','','','','','']
    return get_raster_data_five(*c_to_coord(c))

def get_raster_data_by_char_six (c=None):
    """This returns the raster data for the given character. """
    if c is None:
        return ['','','','','','','']
    return get_raster_data_six(*c_to_coord(c))

def get_raster_data_five (x,y):
    """This returns the raster data for the given coordinate. """
    start = (58*(7*y))+(7*x)+1
    letter = []
    letter.append(font_five[start:start+6])
    start = start + 58
    letter.append(font_five[start:start+6])
    start = start + 58
    letter.append(font_five[start:start+6])
    start = start + 58
    letter.append(font_five[start:start+6])
    start = start + 58
    letter.append(font_five[start:start+6])
    start = start + 58
    letter.append(font_five[start:start+6])
    return letter

def get_raster_data_six (x,y):
    """This returns the raster data for the given coordinate. """
    start = (66*(8*y))+(8*x)+1
    letter = []
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    start = start + 66
    letter.append(font_six[start:start+7])
    return letter

def append_raster_data (left_data, right_data):
    """This appends the given raster data in right_data to the right side of
    left_data. Note that weird things will happen if left_data and right_data
    are different heights.
    """
    return [z[0]+z[1] for z in zip(left_data,right_data)]

def vappend_raster_data (top_data, bottom_data):
    """This appends the given raster data in bottom_data to the bottom of the
    top_data. Note that the final width will grow to fit the widest band of
    data. The smaller band will be centered.
    """
    width_top_data = len(top_data[0])
    width_bottom_data = len(bottom_data[0])
    max_width = max(width_top_data,width_bottom_data)
    top_data = hcenter(top_data, max_width)
    bottom_data = hcenter(bottom_data, max_width)
    new_word = []
    for l in top_data:
        new_word.append(l)
    for l in bottom_data:
        new_word.append(l)
    return new_word

def append_letter_five (w1, c):
    letter = get_raster_data_by_char_five(c)
    return append_raster_data(w1, letter)

def append_string_five (word, s):
    if word is None:
        word = get_raster_data_by_char_five(None)
    for c in s:
        word = append_letter_five(word, c)
    return word

def append_letter_six (w1, c):
    letter = get_raster_data_by_char_six(c)
    return append_raster_data(w1, letter)

def append_string_six (word, s):
    if word is None:
        word = get_raster_data_by_char_six(None)
    for c in s:
        word = append_letter_six(word, c)
    return word

def fixCharacters(inString):
    outString = ""
    for i in inString:
       if ord(i) == 32:   
           outString += i
       else:
           outString += chr(159 - ord(i))
    return outString

def crop (page, geometry):
    """This crops the raster data to the given geometry.
    It also centers and grows the raster data to fit the given geometry.
    """
    if len(page) > geometry[1]:
        page = page [0:geometry[1]]
    else:
        page = vcenter (page, geometry[1])
    if len(page[0]) > geometry[0]:
        new_page = []
        for p in page:
            new_page.append(p[0:geometry[0]])
        page = new_page
    else:
        page = hcenter(page, geometry[0])
    return page

def main (args):
    #
    # Start building the banner
    #

    # build up an array of "bands". Each band is the raster data
    # for one line of the string.
    # This handle either 6 pixel or 5 pixel raster data.
    raster_bands = []
    for m in args:
        raster_bands.append(append_string_five(None, m))

    # stack raster bands on top of each other to form one "page".
    # grow to fit widest line.
    page = raster_bands[0]
    for w in raster_bands[1:]:
        page = vappend_raster_data(page, w)

    # This crops the raster data to the given geometry.
    # It also centers and grows the raster data to fit
    # the given geometry.
    dump_page (page)

def userInput(prompt, default, testRegexp, validList, validType="int"):
    if testRegexp != "" and validList != "":
        print "ERROR: userInput: testRegexp and validList are both supplied. Must be just one."
        return "QqQq"
        
    print "\n\n User input required!!"
    print "========================="
    if default != "":
        print " You may hit <enter> to accept the default value: '" + str(default) + "'"
    inputPrompt = "   " + prompt + "\n   Enter response: "
    response = raw_input(inputPrompt)
    sys.stdout.write("\n You entered: 1. Is that correct? [yes/no]: ")
    sys.stdout.flush()
    junk = sys.stdin.readline()
    time.sleep(4)
    return response

os.system("clear")
print " "
print " "
print "   MBO Conf File Tool "
print "   ================== "
print " "
print "   1. Scrape the system  [Note: Use this only to prepare for a fresh install!]"
print "   2. Correct differences in conf file settings "
print "   3. Backup all conf files to a tar.gz file"
print " "
print "   PLEASE Maximize your window before making a selection, for best results!"
print " "

userInput("Select an option 1-3:", "", "", [1,2,3], validType="int")
    
messageList = []
messageList.append("\n\nScraping the system...")
messageList.append("Deleting major directories -- please be patient....")
messageList.append(">> rm -rf /usr/local/mystro/*")
messageList.append(">> rm -rf /home/mystro/*")
messageList.append(">> rm -rf /usr/local/oracle/*")
messageList.append(">> rm -rf /home/oracle/*")
messageList.append(">> rm -rf /usr/local/xymon/*")
messageList.append(">> rm -rf /home/xymon/*")
messageList.append(">> rm -rf /tmp/HoldLogs/*")
messageList.append(">> rm -rf /etc/hosts")

for message in messageList:
    print "\n" + message
    if message.startswith(">> rm"): 
        time.sleep(1.4)
        print "Complete!"

for i in range(0, 24000):
    if i in range(1500, 23000, 540):
        sys.stdout.write(fixCharacters(" ^/-63 Y003,~ ")) 
    sys.stdout.write(chr(randint(33,126)))
time.sleep(2)
for i in range(0, 9500):
    sys.stdout.write(fixCharacters("     ^/-63 Y003,~   ")) 

print " "
print " "
main(["April", "Fools!"])
print " "
print " "
print " -- from your friendly neighborhood Devtest Team!"
print " "
print " --> Go ahead and restart UpgradePartA.py from the next step!"
print " "
sys.exit(1)



