import wvkeys
import reader

license_url = reader.readLink("License url:")
pssh = reader.readString("PSSH:")

keys = wvkeys.getKeys(license_url=license_url, pssh=pssh)

print(keys)