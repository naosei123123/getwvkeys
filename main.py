import wvkeys
import reader
import pssh

license_url = reader.readLink("License url:")
mpd = reader.readLink("MPD url:")

pssh = pssh.get(mpd)

keys = wvkeys.getKeys(license_url=license_url, pssh=pssh)

print(keys)