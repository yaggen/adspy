import os
from pyads import ADS
path = '/'

streams = []
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
	handler = ADS(f)
	if handler.containStreams():
		for stream in handler.getStreams()[:]:
	# Zone.Identifier is a common ADS, containing information from where a specific file is downloaded.
			if stream == "Zone.Identifier": 
				continue
			print("Found ADS stream in following file(s):")
			print(f)
			print("Containing following stream:")
			print(stream)
			streams.append(f)
			choice = input("Do you want to extract streams? Y/N: ")
			if choice.upper() == "Y":
				fh = open(stream,"wb")
				fh.write(handler.getStreamContent(stream))
				print("Wrote stream to file: "+stream)
				fh.close()
			else:
				continue
