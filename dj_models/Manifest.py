class Manifest(models.Model):
    identifier = models.String()
    version = models.String()
    name = models.String()
    about = models.String()
    permissions = models.Permission()
    appUrl = models.String()
    configurationUrl = models.String()
    tokenTargetUrl = models.String()
    dataPrivacy = models.String()
    dataPrivacyUrl = models.String()
    homepageUrl = models.String()
    supportUrl = models.String()

