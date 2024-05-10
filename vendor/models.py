from datetime import timedelta
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name
    


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()  # Details of items ordered
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    
    
@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    vendor = instance.vendor
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    
    if instance.status == 'completed':
        total_completed_orders = completed_orders.count()
        on_time_completed_orders = completed_orders.filter(delivery_date__lte=instance.delivery_date).count()
        if total_completed_orders > 0:
            vendor.on_time_delivery_rate = (on_time_completed_orders / total_completed_orders) * 100
        else:
            vendor.on_time_delivery_rate = 0
        vendor.save()

    if instance.status == 'completed' and instance.quality_rating is not None:
        completed_orders_with_rating = completed_orders.exclude(quality_rating=None)
        total_ratings = completed_orders_with_rating.aggregate(total_ratings=models.Avg('quality_rating'))['total_ratings']
        vendor.quality_rating_avg = total_ratings
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_average_response_time(sender, instance, created, **kwargs):
    vendor = instance.vendor
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', acknowledgment_date__isnull=False)
    total_time = timedelta(0)
    for order in completed_orders:
        total_time += order.acknowledgment_date - order.issue_date
    if completed_orders.count() > 0:
        vendor.average_response_time = total_time.total_seconds() / completed_orders.count()
    else:
        vendor.average_response_time = 0
    vendor.save()

@receiver(pre_delete, sender=PurchaseOrder)
def calculate_fulfillment_rate(sender, instance, **kwargs):
    vendor = instance.vendor
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    if total_orders > 0:
        vendor.fulfillment_rate = (fulfilled_orders / total_orders) * 100
    else:
        vendor.fulfillment_rate = 0
    vendor.save()