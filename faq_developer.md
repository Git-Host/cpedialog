# Introduction #

Use this page to answer the frequently asked question.


# Why cpedialog is too slow when my laptop is behind a proxy #
  * **Reason**
    * it is because the urlfetch model provided by GAE can't use proxy
    * by default cpedialog will request http://feeds.delicious.com/v2/json/tags/%username for delicious tag when you starup, so the urlfetch will hang your request.
    * [urlfetch cannot be used behind a proxy](http://code.google.com/p/googleappengine/issues/detail?id=544)
  * **Solotion**
    * go to model.py
    * find variable delicious\_enable
    * change the default value to False
# How to use log message when I develop #
  * use util.getLogger(name).debug($msg)
# Internationalization #
  * **Preconditions**
    * Make sure you've installed Django. If not, go to _/google\_appengine/lib/django_ and run _python setup.py install_.
    * Add _Python25/Lib/site-packages/django/bin_ to you system variable **Path**.
  * **Wrap strings you want to i18n**
    * In .py file, you could use <sub>-</sub>(). For example, use `response.out.write(_('hello'))` to replace `response.out.write('hello')`.
    * In template file, you could use {% trans %}. For example, use `<span>{% trans "hello" %}</span>` to replace `<span>hello</span>`. Don't forget to add {% load i18n %} at the first line of the template file.
    * Further information visit [here](http://docs.djangoproject.com/en/dev/topics/i18n/).
  * **Create locale files**
    * Make sure there is a folder named **locale** under root folder of project. If not, create it.
    * Open command line prompt and change to your project folder. Run _make-messages.py -l language_, for example _make-messages.py -l zh\_CN_. This will create a file named _django.po_ under _proj/locale/zh\_CN/LC\_MESSAGES_. Make-messages.py will scan all source files and templates to gather strings which need to i18n.
    * There are two way to create .mo file.
      * Use [poEdit](http://www.poedit.net/). Open django.po and edit. Add your translation. Then save. poEdit will create django.mo automatically.
      * Use compile-messages.py. Change to project folder in command line prompt, run _compile-messages.py_. Django.mo will be created.
    * Once you update source code or template, you should run _make-messages.py -l language_ again to update django.po. Then run poEdit/compile-messages.py again to create django.mo.