def formatTime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return "%d:%02d:%02d" % (h, m, s)


if __name__ == "__main__":
    print(formatTime(35400))  # 9:50:00
