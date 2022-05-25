bgfile = open("background", 'r')
bgcolor = bgfile.readlines()
bgfile.close()

fgfile = open("foreground", 'r')
fgcolor = fgfile.readlines()
fgfile.close()

bgcolor = '"' + bgcolor[0].strip() + '"'
fgcolor = '"' + fgcolor[0].strip() + '"'

reading_file = open("xmobarrc_default", "r")

new_file_content = ""
for line in reading_file:
    stripped_line = line.strip()
    new_line = stripped_line.replace("xmobar_bg", fgcolor)
    new_file_content += new_line+"\n"
reading_file.close()

writing_file = open("half_way", "w")
writing_file.write(new_file_content)
writing_file.close()



reading_file = open("half_way", "r")

new_file_content = ""
for line in reading_file:
    stripped_line = line.strip()
    new_line = stripped_line.replace("xmobar_fg", bgcolor)
    new_file_content += new_line +"\n"
reading_file.close()

writing_file = open("xmobarrc", "w")
writing_file.write(new_file_content)
writing_file.close()

