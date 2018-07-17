import numpy as np
import gpxpy

def plot_activity(activity):
    fn = activity
    with open(fn,'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        pos = []
        speed = []
        segment = gpx.tracks[0].segments[0]
        for point_no, pt in enumerate(segment.points):
            cur_pt = segment.points[point_no]
            try:
                prev_pt = segment.points[point_no-1]
            except:
                prev_pt = cur_pt
            pos.append([cur_pt.latitude,cur_pt.longitude])
            speed.append(cur_pt.speed_between(prev_pt))
    return pos,speed

pos,speed = plot_activity('Data/activities/GPX/11823912.gpx')
