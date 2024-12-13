class EmailEventCountableEdge(models.Model):
    node = models.EmailEvent()
    cursor = models.String()

