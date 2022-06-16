import speedtest
import time

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()







def CheckSpeed():
    fileName = "d:/speedtesterbot/" + str(time.localtime().tm_mday) + "." + str(time.localtime().tm_mon) + "." + str(time.localtime().tm_year) + ".txt"
    s.get_servers(servers)
    s.get_best_server()
    results_dict = s.results.dict()
    download = (int) (s.download(threads=threads)/1000000)
    upload = (int) (s.upload(threads=threads) / 1000000)
    picLink = s.results.share()
    with open(fileName, "a") as log:
        log.write("\nDate: " + time.asctime()
            + "\nDownload: " + str(download) + "Mb/s"
                + "\nUpload: " + str(upload) + "Mb/s"
                    + "\nPic: " + str(picLink) + "\n")
    return [download, upload, picLink]


def GetFileName():
    fileName = "d:/speedtesterbot/" + str(time.localtime().tm_mday) + "." + str(time.localtime().tm_mon) + "." + str(time.localtime().tm_year) + ".txt"
    print("Get FileName " + fileName)
    return fileName

    