class StaffUpdate(models.Model):
    staffErrors = models.StaffError()
    user = models.User()

