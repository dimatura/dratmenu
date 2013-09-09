#!/usr/bin/env python

import subprocess

# this is the separator string. if one of your windows has this in its name
# things will break
sep = '^[^[^['
rp_cmd = ['ratpoison', '-c', "windows " + sep.join(['%n','%c','%t'])]
rp = subprocess.Popen(rp_cmd, stdout=subprocess.PIPE)
windows = [ln.split(sep) for ln in rp.stdout.read().strip().split('\n')]
rp.wait()
# change this for different menu strings
windows_txt = '\n'.join([ ' '.join([ln[0].rjust(3), ln[1].ljust(10)[:10], ln[2]])
    for ln in windows ])

# some font names candidates
#font = "-*-clean-*-r-*-*-*-*-*-*-*-*-*-*"
#font = '-*-clean-*-r-*-*-17-*-*-*-*-*-*-*'
#font = '-*-helvetica-*-r-*-*-17-*-*-*-*-*-*-*'

font = '-*-terminus-*-r-*-*-14-*-*-*-*-*-*-*'
normal_bg_color = '#002b36'
selected_bg_color = '#859900'
num_lines_vert = '20'

dmenu_cmd = ['dmenu', '-i',
            '-sb', selected_bg_color,
            '-nb', normal_bg_color,
            '-fn', font,
            '-l', num_lines_vert]
dmenu = subprocess.Popen(dmenu_cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
selection = dmenu.communicate(windows_txt)[0]
sel_number = selection[:3].strip()

rp_cmd = ['ratpoison', '-c', 'select '+sel_number]
subprocess.call(rp_cmd)
