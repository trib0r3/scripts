import sys
import os
import re

# m3u header file magic
M3U_MAGIC = "#EXTM3U"

# new track
# #EXTINF:[time], [track name]
M3U_TRACK_HEAD = "#EXTINF:0,"

# file extension
M3U_FILE_EXT = ".m3u"

# supported file extensions
FILE_EXTENSIONS = ['.mp3', '.ogg']

# creates file 
# IN
#   (string)     playlist_name     name of the playlist
#   (string[])   track_paths       list of track paths
def createplaylist(playlist_name, track_paths):
    if len(track_paths) < 1:
        print "[I] Skipping creating playlist. No supported files in: %s" % playlist_name
        return False

    fname = playlist_name + M3U_FILE_EXT
    print "[I] Creating playlist..."
    #print '[D] fname: %s' % fname
    with open(fname, 'w') as f:
        f.write(M3U_MAGIC + '\n')

        for track in track_paths:
            name = track
            if len(track) > 4:
                name = track[:-4]

            f.write(M3U_TRACK_HEAD + name + '\n')
            f.write(track + '\n\n')
            print "[I] Adding: %s" % track

    return True

def gettrackpaths(location):
    all_files = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
    #print all_files
    audio_files = []
    for f in all_files:

        # WARNING! 4 letters file extension!
        if f[-4:] in FILE_EXTENSIONS:
            audio_files.append(f)

    return audio_files


def main(argv):
    cwd = os.getcwd()
    #print '[D] CWD: %s' % cwd 
    tracks = gettrackpaths(cwd)

    playlist_name = os.path.basename(os.path.normpath(cwd))
    createplaylist(playlist_name, tracks)

    return 0

if __name__ == "__main__":
    main(sys.argv)
