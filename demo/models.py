from django.db import models

# Create your models here.
import demo.models

class Location(models.Model):
    LEVERINGSSTEDER = (
        ('Alta', 'Alta'),
        ('Kristiansund', 'Kristiansund'),
    )
    EMP_STATUS = (
        ('OK','OK'),

    )
    EXTRA_SWITCHES = (
        ('JA','JA'),
        ('NEI','NEI'),
    )
    NETWORKS = (
        ('P1, P2, O, Kjernerutere','P1, P2, O, Kjernerutere'),
        ('P1, P2, O','P1, P2, O'),
    )
    class Meta:
        pass
        #verbose_name = 'Lokasjon'
        #verbose_name_plural =   'Lokasjoner'
    name = models.CharField(max_length=255, verbose_name='Navn')
    delivery_place = models.CharField(max_length=255, choices=LEVERINGSSTEDER, null=True, verbose_name='Leveringssted')
    technical_location = models.CharField(max_length=255, verbose_name='Teknisk lokasjonsnavn', null=True)
    emp = models.CharField(max_length=2, verbose_name='EMP', choices=EMP_STATUS, null=True)
    network = models.CharField(max_length=255, verbose_name='Nettverk', choices=NETWORKS, null=True)
    extra_switches = models.CharField(max_length=3, verbose_name='Lokasjon med ekstra svitsjer', choices=EXTRA_SWITCHES, null=True)
    circuit_info = models.CharField(max_length=255, verbose_name='Samband', null=True)
    other_info = models.TextField(verbose_name='Annen Info')

    def __str__(self):
        return self.name

class Serialnumber(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.serial_number

class Equipment(models.Model):
    class Meta:
        verbose_name_plural = 'Equipment'

    DEVICE_TYPES = (
        ('Router', 'Router'),
        ('Switch', 'Switch'),
    )
    NETWORKS = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('O', 'O'),
    )
    LOCATION_TYPES = (
        ('Knutepunkt','Knutepunkt'),
        ('Knutepunkt standard lokasjon', 'Knutepunkt standard lokasjon'),
        ('Alle', 'Alle'),
    )
    FUNCTIONS = (
        ('Kjerneruter P1', 'Kjerneruter P1'),
        ('Kjerneruter P2A', 'Kjerneruter P2A'),
        ('Kjerneruter P2B', 'Kjerneruter P2B'),
        ('Kjerneruter O', 'Kjerneruter O'),
    )
    MODELS = (
        ('N540','N540'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    location_type = models.CharField(max_length=255, choices=LOCATION_TYPES, verbose_name='Lokasjonstype', null=True)
    function = models.CharField(max_length=255, choices=FUNCTIONS, verbose_name='Funksjon', null=True)
    model = models.CharField(max_length=255, choices=MODELS, verbose_name='Modell', null=True)
    count = models.PositiveIntegerField(verbose_name='Antall', default=1)
    serial_number = models.OneToOneField(Serialnumber, on_delete=models.CASCADE, null=True)
    rack_location = models.CharField(max_length=255, null=True, verbose_name='Plasseres i skap')
    room = models.CharField(max_length=255, null=True, verbose_name='Plasseres i rom')


    def __str__(self):
        return self.function

class Link(models.Model):
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_location', null=True, default=None)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_location', null=True, default=None)
    sambandsnr = models.CharField(max_length=255,default='')

    def __str__(self):
        #link_id = ' <-> '.join(i.name for i in self.locations.all())
        #return link_id
        return f'{self.to_location} <-> {self.from_location}'
