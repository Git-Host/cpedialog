## Preface ##

Before you start to install cpedialog, you need to know what appengine is and what appengine can do. If you still have some uncertainty, please refer to:
http://code.google.com/appengine/docs/whatisgoogleappengine.html

Make sure Google App Engine has been installed correctly.

And we also recommend you to read the article for "Uploading an App" to appengine:
http://code.google.com/appengine/docs/appcfgpy.html

## Details ##

1.Download cpedialog from googlecode site (http://code.google.com/p/cpedialog/downloads/list) and decompress it to a folder, for example, extract it to "D:\My projects\cpedialog", make sure file "app.yaml" is located in the folder of cpedialog.

> ![http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO0YDA&p.png](http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO0YDA&p.png)

2.Open the file app.yaml with some text editor (such as Microsoft Notpad). Change the applocation property in the first line to your own appengine app name.
For example:
application: pchen   change to:
application: your\_app\_id

> ![http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGLUaDA&p.png](http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGLUaDA&p.png)

3.Run the appcfg.py update command to upload cpedialog to your appengine app.
> ![http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO4YDA&p.png](http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO4YDA&p.png)

```
cd D:\My projects
appcfg.py update cpedialog
```
> ![http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO8YDA&p.png](http://blog.cpedia.com/rpc/img?img_id=agVwY2hlbnINCxIGSW1hZ2VzGO8YDA&p.png)

wait until the command execute finished.



Now you can access your app running on App Engine:
http://your_app_id.appspot.com

If you met the index not found error, please refer to:
http://code.google.com/p/cpedialog/wiki/How_to_fix_the_index_not_found_error_when_deploy_to_production