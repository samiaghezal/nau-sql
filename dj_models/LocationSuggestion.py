class LocationSuggestion(models.Model):
    label = models.String()
    address = models.Address()

