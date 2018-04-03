#!/usr/bin/env python

import os
os.system("raspivid -o - -t 0 -n -w 800 -h 600 -fps 15 | cvlc -vvv stream:///dev/stdin --sout '#rtp"
          "{sdp=rtsp://:8554/}' :demux=h264")