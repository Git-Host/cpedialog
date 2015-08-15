**Want to join this project? [Just send email to me.](mailto:cpedia@gmail.com) or [twitter me](http://twitter.com/cpedia)**

blog implemented by python and can be hosted on google appengine
Now you can access the Demo at: http://blog.cpedia.net

You can try all the features at: http://cpedialog.cpedia.net (just login with your google account, then you can try all the features including the background functions.)

| [![](https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=1593159) | &lt;wiki:gadget url="http://hosting.gmodules.com/ig/gadgets/file/108082365880109588508/google\_code\_cpedialog.xml" height="60" width="468" border="0" /&gt; |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|

Updates:

Google change the translate site, [please upgrade to RC2 2.0 to fix the permlink generator error.](http://cpedialog.googlecode.com/files/cpedialog_20091203_2.0_RC2.tar.gz).

Wiki Updates:
[What's new in coming version 2.0](http://code.google.com/p/cpedialog/wiki/What_is_new_in_version_2_0)

[How to install cpedialog on appengine](http://code.google.com/p/cpedialog/wiki/How_To_Install_cpedialog)

[How to integrate picasaweb album with cpedialog](http://code.google.com/p/cpedialog/wiki/How_to_integrate_picasaweb_album_with_cpedialog)

## Screenshots ##
> ### Main Page ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/main_img.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Login with OpenID/Google Account ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/login.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Google profiles integration ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/profile.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Google Books integration ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/books.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Access picasaweb albums ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/albums.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### View albums with cooliris ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/albums_cooliris.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Add/Edit Blog ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/edit_blog.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Insert/Upload Images ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/upload_images.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### System configuraion ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/system_conf.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/system_conf2.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Page/Menu Admin ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/v2/page_menu.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Picasaweb Albums Admin ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/picasa_albums.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Feeds Management ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/feeds.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Uploaded Images Admin ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/upload_images.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

> ### Cache Management ###
> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/cache.gif?nonsense=something_that_ends_with.png)](http://blog.cpedia.net)

## Features: ##
### blog ###
  * All the configurations can be set in the background.

  * User-defined menus and pages.

  * Blog comment anti-spam support through reCAPTCHA.

  * using yui grid, so it's very easy to change or extend the page layout.

  * auto-generate permalink url through translating the blog title by google.

  * tags for the blog entry and del.icio.us tags support.

  * rich content editor by yui rich editor.

  * Ajax implemented by simplejson & yui Connection Manager. (Such as inline editable table.)

> [![](http://cpedialog.googlecode.com/svn/branches/wiki_images/editable_table.jpeg?p.jpg)](http://blog.cpedia.net/2008/07/yui-in-the-application-of-cpedialog)

  * Upload images file to bigTable in yui rich editor.

  * Uploaded images, tags, archives, albums management.

  * Menu & pages management.

  * AuthSub Session Token and System cache management.

  * Feeds management and can be shown on the right side of page.

### What's new in this version? ###

**1. OpenID integration, now user can register in the site, also can login with Google account and OpenID.**

**2. Google analytics**

**3. Google profile**

**4. Google books library**

**5. Upgrade YUI to latest version and fix some bug especially in the system configuration.**

**6. YUI Grid refactor.**

**7. Image auto resize**

**8. Google search upgrade**

**9. Integrate cooliris with the albums**

**10. Css refactor**

**11. Menu style refactor**

**12. Will roll out layout management feature soon.**

### albums ###
  * access the picasaweb albums through gdata API.

  * authSub implemented by decorating the python method.