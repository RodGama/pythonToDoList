def tracklist(**Bands):
    for band in Bands.items():
        print(band[0])
        albuns = dict(band[1])
        for album, music in albuns.items():
            print("ALBUM: " + album + " TRACK: " + music)
