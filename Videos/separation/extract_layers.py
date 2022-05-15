from video_separation import video_separation as vs
import os


def get_layer(video_name, layer_name):
    full_path = os.path.abspath(video_name)
    path1 = '/'.join(full_path.split('/')[:-2])
    path2 = video_name.split('/')[0]+"/"+layer_name + \
        "/"+video_name.split('/')[1]
    layer_path = path1 + "/" + path2
    """
    checking wether tranmitted videos already exists
    """
    if os.path.exists(layer_path):
        return layer_path
    separator = vs.VideoSeparation(full_path)
    if layer_name is "transmissions":
        layer = separator.get_transmission()
    else:
        layer = separator.get_reflection()
    separator.save_video(layer, layer_path)
    return layer_path
