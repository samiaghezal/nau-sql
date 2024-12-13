class Group(models.Model):
    id = models.ID()
    name = models.String()
    permissions = models.Permission()
    users = models.User()
    userCanManage = models.Boolean()

