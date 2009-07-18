//to generate the collapsible button
YAHOO.util.Event.onDOMReady(function() {
    var Dom = YAHOO.util.Dom;
    var Event = YAHOO.util.Event;
    var grid_blog = Dom.get("grid_blog");
    var grid_menu_right = Dom.get("grid_menu_right");
    var blogcontainer = Dom.get("blogcontainer");
    //collapse bar
    var collapse = document.createElement("div");
    grid_blog.appendChild(collapse);
    collapse.innerHTML = " ";
    collapse.className = "gc-collapsible";
    Dom.setX(collapse, Dom.getX(grid_blog) + grid_blog.offsetWidth);
    Dom.setY(collapse, Dom.getY(grid_blog));
    Dom.setStyle(collapse, "height", Dom.getStyle(grid_blog, "height"));

    //arrow todo:
    var arrow = document.createElement("div");
    grid_blog.appendChild(arrow);
    arrow.innerHTML = " ";
    arrow.className = "gc-collapsible-arrow";
    Dom.setX(arrow, Dom.getX(grid_blog) + grid_blog.offsetWidth);
    Dom.setY(arrow, Dom.getY(grid_blog));

    //binding the action to hide/show grid_menu_right.
    var hoverCollapse = function(e) {
        Dom.setStyle(collapse, "border", "0 1px 0 1px solid #D3D9E5");
        Dom.setStyle(collapse, "width", "6px");
        //show arrow.
        if (Dom.getStyle(grid_menu_right, "display") != "none") {

        } else {

        }

    };
    var mouseoutCollapse = function(e) {
        Dom.setStyle(collapse, "border", "none");
        Dom.setStyle(collapse, "width", "4px");
    };
    var doCollapse = function(e) {
        if (Dom.getStyle(grid_menu_right, "display") != "none") {
            blogcontainer.className = 'yui-g';
            grid_blog.className = "";
            grid_menu_right.className = "";
            grid_menu_right.style.display = "none";
            Dom.setX(collapse, Dom.getX(grid_blog) + grid_blog.offsetWidth);
            Dom.setY(collapse, Dom.getY(grid_blog));
        } else {
            blogcontainer.className = "yui-gc";
            grid_blog.className = "yui-u first";
            grid_menu_right.className = "yui-u";
            grid_menu_right.style.display = "";
            Dom.setX(collapse, Dom.getX(grid_blog) + grid_blog.offsetWidth);
            Dom.setY(collapse, Dom.getY(grid_blog));
        }
    };
    Event.addListener(collapse, "mousemove", hoverCollapse);
    Event.addListener(collapse, "mouseout", mouseoutCollapse);
    Event.addListener(collapse, "click", doCollapse);
});