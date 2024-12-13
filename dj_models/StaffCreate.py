class StaffCreate(models.Model):
    staffErrors = models.StaffError()
    user = models.User()

