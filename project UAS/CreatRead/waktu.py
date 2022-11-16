import datetime

def jam_kerja():
    now = datetime.datetime.now()
    jam_buka = now.replace(hour=10, minute=0, second=0, microsecond=0)
    jam_tutup = now.replace(hour=17, minute=0, second=0, microsecond=0)

    if now > jam_buka and now < jam_tutup :
        return True

    else :
        return False

def time_header():
    jam = datetime.datetime.now()
    return f"{jam.hour} : {jam.minute} WIB"