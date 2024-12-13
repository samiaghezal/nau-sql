class AvalaraRequestLog(models.Model):
    createdAt = models.DateTime()
    requestUrl = models.String()
    requestData = models.JSONString()
    responseData = models.JSONString()
    error = models.String()
    id = models.ID()

