# Index not found error #

If you download cpedialog, and then deploy it to the appengine server directly for the first time, you may meet the index not found error as below.

![http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/index_not_found.jpg?nonsense=something_that_ends_with.png](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/index_not_found.jpg?nonsense=something_that_ends_with.png)


# How to resolve? #

Replace index.yaml with the fixed index file:
http://code.google.com/p/cpedialog/downloads/detail?name=index.yaml&can=2&q=#makechanges




  * Then deploy it to appengine server.
![http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/deploy_to_appengine.jpg?nonsense=something_that_ends_with.png](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/deploy_to_appengine.jpg?nonsense=something_that_ends_with.png)