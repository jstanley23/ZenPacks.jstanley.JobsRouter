from Products import Zuul
from Products.ZenUtils.Ext import DirectRouter, DirectResponse


class NewJobsRouter(DirectRouter):
    """
    Allows for requesting Zenoss job information
    """
    def __init__(self, context, request):
        self.facade = Zuul.getFacade('newjobs', context.dmd)
        self.context = context
        self.request = request
        super(DirectRouter, self).__init__(context, request)


    def getJobInfo(self, jobid):
        """
        Get information on job
        """
        success, data = self.facade.getJobInfo(jobid)
        if success:
            return DirectResponse.succeed(data=Zuul.marshal(data))
        else:
            return DirectResponse.fail(msg=data)

