class PaymentGateway(models.Model):
    name = models.String()
    id = models.ID()
    config = models.GatewayConfigLine()
    currencies = models.String()

