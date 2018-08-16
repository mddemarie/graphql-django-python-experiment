# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=13, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13, help_text="Enter Product Barcode (ISBN, UPC ...)")

    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Desctiption")

    unit_cost = models.FloatField(help_text="Enter Product Unit Cost")
    unit = models.CharField(max_length=10, help_text="Enter Product Unit")

    quantity = models.FloatField(help_text="Enter Product Quantity")
    minQuantity = models.FloatField(help_text="Enter Product Min Quontity")

    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Family(models.Model):
    reference = models.CharField(max_length=13, help_text="Enter Family Reference")
    title = models.CharField(max_length=200, help_text="Enter Family Title")
    description = models.TextField(help_text="Enter Family Description")

    unit = models.CharField(max_length=13, help_text="Enter Family Unit")

    minQuantity = models.FloatField(help_text="Enter Family Min Quantity")

    def __str__(self):
        return self.title

class Location(models.Model):
    reference = models.CharField(max_length=20, help_text="Enter Location reference")
    title = models.CharField(max_length=200, help_text="Enter Location Title")
    description = models.TextField(help_text="Enter Location Description")

    def __str__(self):
        return self.title

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=13, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(max_length=13, help_text="Enter Product Barcode (ISBN, UPC...")

    comment = models.TextField(help_text="Enter Product Comment")
    unit_cost = models.FloatField(help_text="Enter Product Unit Cost")
    quantity = models.FloatField(help_text="Enter Product Quantity")

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    REASONS = (
        ('ns', 'New Stock'),
        ('ur', 'Usable Return'),
        ('nr', 'Unusable Return')
    )

    reason = models.CharField(max_length=2, choices=REASONS, blank=True, default='ns', help_text='Reason for transaction')

    def __str__(self):
        return 'Transaction : %d' % (self.id)
