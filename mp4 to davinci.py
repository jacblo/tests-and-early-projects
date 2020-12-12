import os
cmd = "ffmpeg -i \"{}\" -vcodec dnxhd -acodec pcm_s16le -b:v 36M -pix_fmt yuv422p -f mov \"{}\""
cmd = 'ffmpeg -i "{}" -vcodec mpeg4 -b:v 1500k "{}"'
def get_filepaths(directory):
    files_and_directories = os.listdir(directory)
    return files_and_directories

def fillInput(text):
    currentStr = ""
    while True:
        x = currentStr + input(text+currentStr)
        posSlash = -x[::-1].find("/")-1
        if posSlash == -1:
            break
        wordToFill = x[posSlash+1:]
        directoryToFind = x[:posSlash+1]
        files = get_filepaths(directoryToFind)
        for w in files:
            if not(os.path.isdir(directoryToFind+w)):
                continue
            if wordToFill == w[:len(wordToFill)]:
                currentStr = directoryToFind+w+"/"
                break
    return x
    
    
directory = fillInput("folder: ")

for x in get_filepaths(directory):
	if x[-4:].lower() == ".mp4":
		os.system(cmd.format(directory+x,directory+x[:-4]+"2.mp4"))

input()