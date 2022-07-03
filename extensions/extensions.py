def main():
    error = 1
    mediatype ={
        ".gif":"image/gif",
        ".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",
        ".png":"image/png",
        ".pdf":"application/pdf",
        ".txt":"text/plain",
        ".zip":"application/zip"
    }

    filename = input("Filename: ").strip().lower()
    for extension in mediatype:
        if(extension in filename):
            print (mediatype[extension])
            error = 0
            break
    if (error == 1):
        print("application/octet-stream")
main()