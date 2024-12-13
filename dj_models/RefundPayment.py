class RefundPayment(models.Model):
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    id = models.ID()
    paymentType = models.RefundPaymentTypeEnum()
    refund = models.Refund()
    refundMethod = models.RefundMethod()

