import pyvolume


def volume_api(per):
    per_int=int(per)
    pyvolume.custom(percent=per_int)


# volume_api("10