from django.db import models

# Create your models here.

class TableA(models.Model):
    a_str = models.CharField(max_length=512, null = True, blank=True)
    a_bool = models.BooleanField(default=False)
    a_int = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'TableA'
        verbose_name_plural = "Tables of A"

    def __str__(self) -> str:
        return self.a_str 


class TableB(models.Model):
    b_str  = models.CharField(max_length=512, null = True, blank=True)
    b_bool  = models.BooleanField(default=False)
    b_int  = models.IntegerField(default = 0)
    table_a = models.ForeignKey(TableA, on_delete=models.CASCADE, related_name='table_b_to_a')

    class Meta:
        verbose_name = 'TableB'
        verbose_name_plural = "Tables ot B"

    def __str__(self) -> str:
        return self.b_str 


class TableC(models.Model):
    c_str  = models.CharField(max_length=512, null = True, blank=True)
    c_bool  = models.BooleanField(default=False)
    c_int  = models.IntegerField(default = 0)
    table_b = models.ForeignKey(TableB, on_delete=models.CASCADE, related_name='table_c_to_b')

    class Meta:
        verbose_name = 'TableC'
        verbose_name_plural = "Table of C"

    def __str__(self) -> str:
        return self.c_str 


class TableD(models.Model):
    d_str  = models.CharField(max_length=512, null = True, blank=True)
    d_bool  = models.BooleanField(default=False)
    d_int  = models.IntegerField(default = 0)
    table_c = models.ForeignKey(TableC, on_delete=models.CASCADE, related_name='table_d_to_c')
    
    class Meta:
        verbose_name = 'TableD'
        verbose_name_plural = "Table of D"

    def __str__(self) -> str:
        return self.d_str 


class TableE(models.Model):
    e_str  = models.CharField(max_length=512, null = True, blank=True)
    e_bool  = models.BooleanField(default=False)
    e_int  = models.IntegerField(default = 0)
    table_d = models.ForeignKey(TableD, on_delete=models.CASCADE, related_name='table_e_to_d')

    class Meta:
        verbose_name = 'TableE'
        verbose_name_plural = "Table of E"

    def __str__(self) -> str:
        return self.e_str