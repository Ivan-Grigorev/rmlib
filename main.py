from myrm.rmlib import mkdir, mv, mvdir, rm, rmdir


def main():
    mv(
        "/Users/ivangrigorev/documents/src/traveler.txt",
        "/Users/ivangrigorev/documents/dst/traveler.txt",
    )
    mvdir("/Users/ivangrigorev/documents/src", "/Users/ivangrigorev/documents/dst")
    rm("/Users/ivangrigorev/documents/src/traveler.txt")
    rmdir("/Users/ivangrigorev/documents/src")
    mkdir("/Users/ivangrigorev/documents/new/")


if __name__ == "__main__":
    main()
