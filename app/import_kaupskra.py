import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brennisteinn_project.settings")



import csv
import requests
from app.models import Fasteignakaup



def import_kaupskra():
    url = 'https://frs3o1zldvgn.objectstorage.eu-frankfurt-1.oci.customer-oci.com/n/frs3o1zldvgn/b/public_data_for_download/o/kaupskra.csv'
    response = requests.get(url)
    response.raise_for_status()

    csv_data = response.text.splitlines()
    reader = csv.DictReader(csv_data, delimiter=";")
    for row in reader:
        Fasteignakaup.objects.update_or_create(
            FAERSLUNUMER = row['FAERSLUNUMER'],
            EMNR = row['EMNR'],
            SKJALANUMER = row['SKJALANUMER'],
            FASTNUM = row['FASTNUM'],
            HEIMILISFANG = row['HEIMILISFANG'],
            POSTNR = row['POSTNR'],
            HEINUM = row['HEINUM'],
            SVFN = row['SVFN'],
            SVEITARFELAG = row['SVEITARFELAG'].strip(),
            UTGDAG = row['UTGDAG'],
            THINGLYSTDAGS = row['THINGLYSTDAGS'],
            KAUPVERD = row['KAUPVERD'],
            FASTEIGNAMAT = row['FASTEIGNAMAT'],
            FASTEIGNAMAT_GILDANDI = row['FASTEIGNAMAT_GILDANDI'],
            BRUNABOTAMAT_GILDANDI = row['BRUNABOTAMAT_GILDANDI'],
            BYGGAR = row['BYGGAR'],
            FEPILOG = row['FEPILOG'],
            EINFLM = row['EINFLM'],
            LOD_FLM = row['LOD_FLM'],
            LOD_FLMEIN = row['LOD_FLMEIN'],
            FJHERB = row['FJHERB'],
            TEGUND = row['TEGUND'],
            FULLBUID = row['FULLBUID'],
            ONOTHAEFUR_SAMNINGUR = row['ONOTHAEFUR_SAMNINGUR']
        )
    ##dummy skrá með 1000 færslum
    # with open('c:/Users/gylfi/Downloads/kaupskra2.csv', 'r', encoding="utf-8") as file:
    #     reader = csv.DictReader(file, delimiter=';')
    #     for row in reader:
    #         Fasteignakaup.objects.update_or_create(
    #             FAERSLUNUMER = row['FAERSLUNUMER'],
    #             EMNR = row['EMNR'],
    #             SKJALANUMER = row['SKJALANUMER'],
    #             FASTNUM = row['FASTNUM'],
    #             HEIMILISFANG = row['HEIMILISFANG'],
    #             POSTNR = row['POSTNR'],
    #             HEINUM = row['HEINUM'],
    #             SVFN = row['SVFN'],
    #             SVEITARFELAG = row['SVEITARFELAG'].strip(),
    #             UTGDAG = row['UTGDAG'],
    #             THINGLYSTDAGS = row['THINGLYSTDAGS'],
    #             KAUPVERD = row['KAUPVERD'],
    #             FASTEIGNAMAT = row['FASTEIGNAMAT'],
    #             FASTEIGNAMAT_GILDANDI = row['FASTEIGNAMAT_GILDANDI'],
    #             BRUNABOTAMAT_GILDANDI = row['BRUNABOTAMAT_GILDANDI'],
    #             BYGGAR = row['BYGGAR'],
    #             FEPILOG = row['FEPILOG'],
    #             EINFLM = row['EINFLM'],
    #             LOD_FLM = row['LOD_FLM'],
    #             LOD_FLMEIN = row['LOD_FLMEIN'],
    #             FJHERB = row['FJHERB'],
    #             TEGUND = row['TEGUND'],
    #             FULLBUID = row['FULLBUID'],
    #             ONOTHAEFUR_SAMNINGUR = row['ONOTHAEFUR_SAMNINGUR']
    #         )

if __name__ == '__main__':
    import_kaupskra()
