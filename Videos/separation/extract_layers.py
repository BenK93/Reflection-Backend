from video_separation import video_separation as vs
import os


def get_all_layers(video_name):
    video = "uploads/"+str(video_name)
    full_path = os.path.abspath(video)
    separator = vs.VideoSeparation(full_path)
    return separator.reflection_video, separator.transmission_video, separator.stabilized_video


