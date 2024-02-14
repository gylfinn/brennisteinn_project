from django.db import models

# Create your models here.

#FAERSLUNUMER;EMNR;SKJALANUMER;FASTNUM;HEIMILISFANG;POSTNR;HEINUM;SVFN;SVEITARFELAG;UTGDAG;THINGLYSTDAGS;KAUPVERD;FASTEIGNAMAT;FASTEIGNAMAT_GILDANDI;BRUNABOTAMAT_GILDANDI;BYGGAR;FEPILOG;EINFLM;LOD_FLM;LOD_FLMEIN;FJHERB;TEGUND;FULLBUID;ONOTHAEFUR_SAMNINGUR
#500342;411;R-005069/2006;2067729;Melabraut 3;170;1024617;1100;Seltjarnarnesbær            ;2006-05-08 00:00:00.0;2006-05-10 09:22:39.0;25500;19610;90600;53650;1963;010101;102.3;;;3;Fjölbýli;1;1




class Fasteignakaup(models.Model):
    FAERSLUNUMER = models.IntegerField()
    EMNR = models.IntegerField()
    SKJALANUMER = models.CharField(max_length=100)
    FASTNUM = models.IntegerField()
    HEIMILISFANG = models.CharField(max_length=100)
    POSTNR = models.IntegerField()
    HEINUM = models.IntegerField()
    SVFN = models.IntegerField()
    SVEITARFELAG = models.CharField(max_length=100)
    UTGDAG = models.DateTimeField()
    THINGLYSTDAGS = models.DateTimeField()
    KAUPVERD = models.IntegerField()
    FASTEIGNAMAT = models.IntegerField()
    FASTEIGNAMAT_GILDANDI = models.CharField(max_length=100)
    BRUNABOTAMAT_GILDANDI = models.CharField(max_length=100)
    BYGGAR = models.CharField(max_length=100)
    FEPILOG = models.CharField(max_length=100)
    EINFLM = models.DecimalField(max_digits=10, decimal_places=2)
    LOD_FLM = models.CharField(max_length=100)
    LOD_FLMEIN = models.CharField(max_length=100)
    FJHERB = models.CharField(max_length=100)
    TEGUND = models.CharField(max_length=100)
    FULLBUID = models.IntegerField()
    ONOTHAEFUR_SAMNINGUR = models.IntegerField()

