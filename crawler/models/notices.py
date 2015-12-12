from django.db import models


class Notices(models.Model):

    CMP_MARKET_KOSPI = 0
    CMP_MARKET_KOSDAQ = 1

    CMP_MARKET = (
        (CMP_MARKET_KOSPI, 'KOSPI'),
        (CMP_MARKET_KOSDAQ, 'KOSDAQ'),
    )

    NOTICE_TYPE_UNKNOWN = 0
    NOTICE_TYPE_CAPITAL_INCREASE_FREE = 1
    NOTICE_TYPE_CAPITAL_INCREASE_PAYING = 2
    NOTICE_TYPE_TREASURY_STOCK_RETIREMENT = 3

    NOTICE_TYPE = (
        (NOTICE_TYPE_CAPITAL_INCREASE_FREE, 'CAPITAL_INCREASE_FREE'),
        (NOTICE_TYPE_CAPITAL_INCREASE_PAYING, 'CAPITAL_INCREASE_PAYING'),
        (NOTICE_TYPE_TREASURY_STOCK_RETIREMENT, 'TREASURY_STOCK_RETIREMENT'),
    )

    NOTICE_MAIL_STATUS_REGISTERED = 0
    NOTICE_MAIL_STATUS_MAILED = 1

    NOTICE_MAIL_STATUS = (
        (NOTICE_MAIL_STATUS_REGISTERED, 'REGISTERED'),
        (NOTICE_MAIL_STATUS_MAILED, 'MAILED'),
    )

    rcp_no = models.IntegerField()

    cmp_code = models.CharField(max_length=6)
    cmp_name = models.CharField(max_length=10)
    cmp_market = models.IntegerField(choices=CMP_MARKET)

    notice_type = models.IntegerField(choices=NOTICE_TYPE, default=NOTICE_TYPE_UNKNOWN)
    notice_mail_status = models.IntegerField(choices=NOTICE_MAIL_STATUS, default=NOTICE_MAIL_STATUS_REGISTERED)

    url_outer = models.URLField()
    url_inner = models.URLField()

    html = models.TextField()

    registered = models.DateTimeField(auto_now_add=True, blank=True)
    delivered = models.DateTimeField(blank=True)

    class Meta:
        app_label = 'trader'
