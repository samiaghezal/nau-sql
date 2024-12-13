class UserCountableEdge(models.Model):
    node = models.User()
    cursor = models.String()

