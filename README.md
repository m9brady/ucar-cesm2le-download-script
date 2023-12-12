# Feedback for UCAR CESM2-LE Python download scripts

I was recently encountering partial downloads where only ~10% of a file would download, rerunning the script wouldn't detect this which caused me to have to manually comment-out the "good" files out of the `data` dictionary and manually delete/redownload the problematic files.

The modifications in this repo attempt to detect cases where a file is incomplete by checking a local file's bytes against the expected bytes in the `data` dictionary, triggering a redownload if there is a mismatch. 

Other modifications:
- Remove `getAttr()` functions as class attributes can be accessed directly
- Add optional initiatilization arguments `token` and `agent` to `Download` class
- Simplify the `createDownloads()` function by passing the `UserToken` and `UserAgent` directly to `Download` class instantiation
- add the `if __name__ == '__main__'` block just in case anyone wants to import the `Download` class in a separate script without wanting to run the contents of this script