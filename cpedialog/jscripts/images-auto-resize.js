YAHOO.util.Event.onDOMReady(function() {
    //get all the images in blogcontent div.
    var img_div = YAHOO.util.Dom.get("blogcontent");
    var blog_div = YAHOO.util.Dom.get("bd");
    var images = blog_div.getElementsByTagName("img");
    var width_ = YAHOO.util.Dom.getStyle(img_div, 'width');
    var div_width = width_.substring(0,width_.length-2);
    for (var i = 0,len = images.length; i < len; i++) {
        var img = images[i];
        if (img.width > div_width) {
            debugger;
            img.width = div_width;
            //add url for the resized image.
            var a_ = document.createElement("a");
            a_.href = img.src;
            a_.target = "_blank";
            a_.appendChild(img.cloneNode(false));
            img.parentNode.appendChild(a_);
            a_.parentNode.removeChild(img);

        }
    }
});