#!/usr/bin/env python3

import os
import sys
import shutil
import hashlib
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from platform import python_version

################################################################
#
# Generated by: NCAR Climate Data Gateway
# Created: 2023-12-06T09:51:11-07:00
#
# Your download selection includes data that might be secured using API Token based
# authentication. Therefore, this script can have your api-token. If you
# re-generate your API Token after you download this script, the download will
# fail. If that happens, you can either re-download the script or you can edit
# this script replacing the old API Token with the new one. View your API token
# by going to "Account Home":
#
# https://www.earthsystemgrid.org/account/user/account-home.html
#
# and clicking on the "API Token" link under "Personal Account". You will be asked
# to log into the application before you can view your API Token.
#
# Usage: python3 python-ucar.cgd.cesm2le.atm.proc.daily_ave.TREFHTMN-20231206T0951.py
# Version: 0.1.1-alpha
#
# Dataset
# ucar.cgd.cesm2le.atm.proc.daily_ave.TREFHTMN
# d4dd89b1-32a3-4a50-9d89-b132a31a50bb
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.daily_ave.TREFHTMN.html
# https://www.earthsystemgrid.org/dataset/id/d4dd89b1-32a3-4a50-9d89-b132a31a50bb.html
#
# Dataset Version
# 1
# ec73aceb-582d-4761-b3ac-eb582de76108
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.daily_ave.TREFHTMN/version/1.html
# https://www.earthsystemgrid.org/dataset/version/id/ec73aceb-582d-4761-b3ac-eb582de76108.html
#
################################################################

print('This Python 3 download script is experimental.  Please email feedback to esg-support@earthsystemgrid.org.\n')

args = {}
args.update({'apiToken': 'get-your-own'})
args.update({'userAgent': 'python/{}/gateway/{}'.format(python_version(), '4.3.17-20231128-210705')})

data = [
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18500101-18591231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18500101-18591231.nc','bytes':'467381866'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18600101-18691231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18600101-18691231.nc','bytes':'467352763'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18700101-18791231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18700101-18791231.nc','bytes':'467341442'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18800101-18891231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18800101-18891231.nc','bytes':'467444412'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18900101-18991231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.18900101-18991231.nc','bytes':'467396044'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19000101-19091231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19000101-19091231.nc','bytes':'467281028'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19100101-19191231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19100101-19191231.nc','bytes':'467349310'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19200101-19291231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19200101-19291231.nc','bytes':'467373587'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19300101-19391231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19300101-19391231.nc','bytes':'467377682'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19400101-19491231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19400101-19491231.nc','bytes':'467267369'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19500101-19591231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19500101-19591231.nc','bytes':'467141860'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19600101-19691231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19600101-19691231.nc','bytes':'467352220'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19700101-19791231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19700101-19791231.nc','bytes':'467247274'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19800101-19891231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19800101-19891231.nc','bytes':'467011846'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19900101-19991231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.19900101-19991231.nc','bytes':'466818911'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20000101-20091231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20000101-20091231.nc','bytes':'466362503'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20100101-20141231.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20100101-20141231.nc','bytes':'233149052'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20150101-20241231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20150101-20241231.nc','bytes':'466037192'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20250101-20341231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20250101-20341231.nc','bytes':'465755820'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20350101-20441231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20350101-20441231.nc','bytes':'465484811'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20450101-20541231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20450101-20541231.nc','bytes':'465213792'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20550101-20641231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20550101-20641231.nc','bytes':'464840621'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20650101-20741231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20650101-20741231.nc','bytes':'464285236'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20750101-20841231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20750101-20841231.nc','bytes':'463877351'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20850101-20941231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20850101-20941231.nc','bytes':'463654326'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/day_1/TREFHTMN/b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20950101-21001231.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1011.001.cam.h1.TREFHTMN.20950101-21001231.nc','bytes':'278067279'},]

def main(args, data):

    for download in createDownloads(args, data):

        if isCompleteDownload(download):
            completeDownload(download)
        elif isPartialDownload(download):
            resumeDownload(download)
        else:
            startDownload(download)

def createDownloads(args, data):

    downloads = []

    for d in data:
        download = Download(d)
        download.setApiToken(args.get('apiToken'))
        download.setUserAgent(args.get('userAgent'))
        downloads.append(download)

    return downloads

def isCompleteDownload(download):

    return os.path.isfile(download.getFilename())

def isPartialDownload(download):

    return os.path.isfile(download.getPart())

def completeDownload(download):

    print('complete:', download.getFilename())

def resumeDownload(download):

    print('resuming:', download.getFilename())

    headers = createHeaders(download)
    headers.append(createRangeHeader(download))

    opener = urllib.request.build_opener()
    opener.addheaders = headers

    tryDownloadFile(download, opener)

def startDownload(download):

    print('downloading:', download.getFilename())

    headers = createHeaders(download)

    opener = urllib.request.build_opener()
    opener.addheaders = headers

    tryDownloadFile(download, opener)

def createHeaders(download):

    headers = []

    headers.append(('User-agent', download.getUserAgent()))

    if download.getApiToken():
        headers.append(('Authorization', 'api-token {}'.format(download.getApiToken())))

    return headers

def createRangeHeader(download):

    start = os.path.getsize(download.getPart())
    header = ('Range', 'bytes={}-'.format(start))

    return header

def tryDownloadFile(download, opener):

    try:
        downloadFile(download, opener)
    except HTTPError as error:
        print('Download of {} failed! Reason: code {}, {}'.format(download.getFilename(), error.status, error.reason))
    except URLError as error:
        print('Download of {} failed! Reason: {}'.format(download.getFilename(), error.reason))
    except TimeoutError:
        print('Download of {} failed! Reason: request timed out'.format(download.getFilename()))

def downloadFile(download, opener):

    with opener.open(download.getUrl()) as response, open(download.getPart(), 'ab') as fh:
        shutil.copyfileobj(response, fh)

    os.rename(download.getPart(), download.getFilename())

    print('complete:', download.getFilename())

class Download():

    def __init__(self, datum):

        self.url = datum.get('url')
        self.filename = datum.get('filename')
        self.bytes = datum.get('bytes')
        self.part = self.filename + '.part'
        self.apiToken = None
        self.userAgent = 'python'

    def getUrl(self):

        return self.url

    def getFilename(self):

        return self.filename

    def getBytes(self):

        return self.bytes

    def getPart(self):

        return self.part

    def setApiToken(self, apiToken):

        self.apiToken = apiToken

    def getApiToken(self):

        return self.apiToken

    def setUserAgent(self, userAgent):

        self.userAgent = userAgent

    def getUserAgent(self):

        return self.userAgent

    def __str__(self):

        return ', '.join([
            'url: ' + self.url,
            'filename: ' + self.filename,
            'bytes: ' + str(self.bytes),
        ])

main(args, data)
