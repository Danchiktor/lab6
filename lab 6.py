import math

# Базовый класс
class OpticalDisk:
    def __init__(self, capacity_gb, rpm, laser_thickness_nm):
        self.capacity_gb = capacity_gb
        self.rpm = rpm
        self.laser_thickness_nm = laser_thickness_nm

    def data_processed_in_20_seconds(self):

        disk_circumference = 2 * math.pi * (12 / 2)

        data_per_second = (self.rpm / 60) * disk_circumference * (self.capacity_gb * 1e9)
        return data_per_second * 20

    def __str__(self):
        return f"Оптический диск: емкость {self.capacity_gb} ГБ, обороты {self.rpm} об/мин, толщина лазера {self.laser_thickness_nm} нм"


class CD(OpticalDisk):
    def __init__(self, capacity_gb, rpm, laser_thickness_nm, audio_quality_kbps):
        super().__init__(capacity_gb, rpm, laser_thickness_nm)
        self.audio_quality_kbps = audio_quality_kbps

    def average_rotation_time(self):

        return 60 / self.rpm

    def __str__(self):
        return f"CD: {super().__str__()}, качество аудио {self.audio_quality_kbps} Кбит/с"


class DVD(OpticalDisk):
    def __init__(self, capacity_gb, rpm, laser_thickness_nm, video_quality_mbps):
        super().__init__(capacity_gb, rpm, laser_thickness_nm)
        self.video_quality_mbps = video_quality_mbps

    def average_rotation_time(self):

        return 60 / self.rpm

    def __str__(self):
        return f"DVD: {super().__str__()}, качество видео {self.video_quality_mbps} Мбит/с"



cd = CD(capacity_gb=0.7, rpm=200, laser_thickness_nm=780, audio_quality_kbps=320)
dvd = DVD(capacity_gb=4.7, rpm=570, laser_thickness_nm=650, video_quality_mbps=8)

print(cd)
print(f"CD: Количество данных за 20 секунд: {cd.data_processed_in_20_seconds()} байт")
print(f"CD: Среднее время одного оборота: {cd.average_rotation_time()} секунд\n")

print(dvd)
print(f"DVD: Количество данных за 20 секунд: {dvd.data_processed_in_20_seconds()} байт")
print(f"DVD: Среднее время одного оборота: {dvd.average_rotation_time()} секунд")