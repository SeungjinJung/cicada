# import pythoncom
# import win32com.client
# from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

# from trader.hts.xing import XASessionEvents


class IndexView(View):
    def get(self, request):

        # inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        # inXASession.ConnectServer(settings.SERVER_ADDRESS, settings.SERVER_PORT)
        # inXASession.Login(settings.USER_ID, settings.USER_PWD, settings.USER_CERT, settings.SERVER_TYPE, 0)
        #
        # while XASessionEvents.logInState == 0:
        #     pythoncom.PumpWaitingMessages()
        #
        # nCount = inXASession.GetAccountListCount()
        # print("The number of account: ", nCount)
        #
        # for i in range(nCount):
        #     print("Account: %d - %s" % (i, inXASession.GetAccountList(i)))

        return render_to_response("index.html",
                                  context_instance=RequestContext(request))

    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

