from datetime import datetime
from zope.interface import implements

from Products.Zuul.facades import ZuulFacade
from Products.Zuul.interfaces import IFacade


class INewJobsFacade(IFacade):
    '''
    New JobsRouter API interface
    '''
    def getJobInfo(self, jobid):
        '''
        Get information on job
        '''


class NewJobsFacade(ZuulFacade):
    '''
    New JobsRouter API implementation
    '''
    implements(INewJobsFacade)

    def getJobInfo(self, jobid):
        epoch = datetime(1970, 1, 1)
        dateObjStr = "%Y-%m-%d %H:%M:%S"
        jm = self._dmd.JobManager
        try:
            result = jm.getJob(jobid)
        except Exception as e:
            return (False, e.message)

        data = dict(
            uid=result.id,
            status=result.status,
            result=str(result.result),
            finished=result.isFinished(),
            description=result.description,
            scheduled='',
            started='',
            completed='',
            )

        if result.date_scheduled:
            data['scheduled'] = (result.date_scheduled - epoch).total_seconds()
        if result.date_started:
            data['started'] = (result.date_started - epoch).total_seconds()
        if result.date_done:
            data['completed'] = (result.date_done - epoch).total_seconds()

        return (True, data)

