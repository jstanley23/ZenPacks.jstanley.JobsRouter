New Jobs router that allows a user to get job details from Zenoss.

Examples:


```
ZenossAPI()._router_request('NewJobsRouter', 'getJobInfo', [{'jobid': 'b9d9de2a-4914-49f1-8abf-7f8b181ccae21'}])
{u'msg': u'Job not present: b9d9de2a-4914-49f1-8abf-7f8b181ccae21: b9d9de2a-4914-49f1-8abf-7f8b181ccae21', u'type': u'error', u'success': False}
```

```
ZenossAPI()._router_request('NewJobsRouter', 'getJobInfo', [{'jobid': 'b9d9de2a-4914-49f1-8abf-7f8b181ccae2'}])
{u'data': {u'scheduled': 1440879444.162728, u'status': u'SUCCESS', u'description': u'Add device mediapc', u'started': 1440880385.86784, u'completed': 1440880387.179378, u'finished': True, u'result': u'None', u'uid': u'b9d9de2a-4914-49f1-8abf-7f8b181ccae2'}, u'success': True}
```
