from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from utility.mixin import MetaInformationMixin, SoftDeletionModelMixin
# Create your models here.




class AssesmentManager(models.Manager):
    def get_queryset(self):
        return super(AssesmentManager, self).get_queryset()\
                .filter(deleted='N')


class Assesment(MetaInformationMixin, SoftDeletionModelMixin):
    ASSESMENT_START_TYPE_CHOICES = (
        ('auto', 'Automatic'),
        ('manual', 'Manually'),
        )
    
    ASSESMENT_PRIVILEGE_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
        )
    
    #objects = models.Manager()  # The Default Manager
    #active = AssesmentManager()  # Our custom manager


    header = models.CharField(max_length=150)
    slug = models.SlugField(max_length=140,
                            unique=True,
                            blank=True)
    brief = models.TextField()
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(default=timezone.now())
    exam_start_type = models.CharField(max_length=14,
                                       choices=ASSESMENT_START_TYPE_CHOICES,
                                       default='auto')
    

    total_exam_duration = models.TimeField(null=True)
    
    privilege = models.CharField(max_length=14,
                                       choices=ASSESMENT_PRIVILEGE_CHOICES,
                                       default='private')
    
   
    is_exam_active = models.BooleanField(default=True)
    expired_on = models.DateTimeField()
    
    
    
    type = models.CharField(max_length=10, default="assessment", editable=False)
    #deleted = models.CharField(max_length=1, default="N")

    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return 'Assesment - {}'.format(self.header)
    
    def _get_unique_slug(self):
        slug = slugify(self.header)
        unique_slug = slug
        num = 1
        while Assesment.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        
        if self.pk is None and self.created_by is None:
            created_by = user
        elif self.updated_by is None:
            updated_by = user
        super().save()
