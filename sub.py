import moviepy.editor as mp
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip

# Function to generate text clips for each subtitle with a background color
def subtitle_generator(txt):
    # Ensure font is specified, and create the text clip
    txt_clip = mp.TextClip(txt, font='Arial', fontsize=56, color='white')
    
    # Check if text clip creation was successful
    if txt_clip is None:
        raise ValueError("TextClip creation failed. Ensure the font is available.")
    
    # Add a background color box
    txt_background = txt_clip.on_color(size=(txt_clip.w + 20, txt_clip.h + 10),
                                       color=(0, 0, 0),  # Background color (black here)
                                       col_opacity=0.6)  # Background opacity (0.6 for semi-transparent)
    
    return txt_background

# Load the video
video = VideoFileClip("video.mp4")

# Load subtitles from SRT file
subs = SubtitlesClip("video.srt", subtitle_generator)

# Combine the video with the subtitles
video_with_subtitles = mp.CompositeVideoClip([video, subs.set_position(("center", video.h - 250))])


# Export the video with subtitles
video_with_subtitles.write_videofile("video_with_subtitles.mp4", fps=video.fps)
