#!/usr/bin/env python

import subprocess

sep = '^[^[^['
rp_cmd = ['ratpoison', '-c', "windows " + sep.join(['%n','%c','%t'])]
rp = subprocess.Popen(rp_cmd, stdout=subprocess.PIPE)
windows = [ln.split(sep) for ln in rp.stdout.read().strip().split('\n')]
rp.wait()
windows_txt = '\n'.join([ ' '.join([ln[0].rjust(3), ln[1].ljust(10)[:10], ln[2]]) for ln in windows ])

#font = "-*-clean-*-r-*-*-*-*-*-*-*-*-*-*"
#font = '-*-clean-*-r-*-*-17-*-*-*-*-*-*-*'
#font = '-*-helvetica-*-r-*-*-17-*-*-*-*-*-*-*'
font = '-*-terminus-*-r-*-*-14-*-*-*-*-*-*-*'
dmenu_cmd = ['dmenu', '-i', '-sb', '#859900', '-nb', '#002b36', '-fn', font, '-l', '20']
print dmenu_cmd
dmenu = subprocess.Popen(dmenu_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
selection = dmenu.communicate(windows_txt)[0]
sel_number = selection[:3].strip()

rp_cmd = ['ratpoison', '-c', 'select '+sel_number]
subprocess.call(rp_cmd)
