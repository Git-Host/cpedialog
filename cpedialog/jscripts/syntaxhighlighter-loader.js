Array.prototype.contains = function (element) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] == element) {
            return true;
        }
    }
    return false;
};

if (!window.BrushUtils) var BrushUtils = (function() {
    var ut = {
        baseurl:"",
        resources:[],
        brushMap : {js:"JScript",jscript:"JScript",javascript:"JScript",
            bash:"Bash",shell:"Bash",css:"Css",actionscript3:"AS3",as3:"AS3",cpp:"Cpp",c:"Cpp",
            csharp:"CSharp",groovy:"Groovy",java:"Java",javafx:"JavaFX",jfx:"JavaFX",
            perl:"Perl",pl:"Perl",php:"Php",text:"Plain",plain:"Plain",py:"Python",python:"Python",
            ruby:"Ruby",ror:"Ruby",rails:"Ruby",scala:"Scala",sql:"Sql",xml:"Xml",html:"Xml",xhtml:"Xml",xslt:"Xml"
        },
        parseBrush :function() {
            var pres = document.getElementsByTagName("pre");
            var brushs = new Array();
            for (var i = 0; i < pres.length; i++) {
                var pre = pres[i];
                var className = pre.className;
                className = className.toLowerCase();
                var brush = null;
                if (className.indexOf('brush:') == 0) {
                    brush = className.substr(className.indexOf(':') + 1);
                } else if (pre.getAttribute('name') == 'code') {
                    brush = className;
                    pre.className = 'brush:' + className;
                }
                if (brush == null)
                    continue;
                if (!eval("ut.brushMap." + brush)) {
                    pre.className = 'brush:text';
                    brush = "text";
                }
                if (!brushs.contains(brush)) {
                    brushs.push(brush);
                }
            }
            return brushs;
        },
        loadLibs : function(_baseurl, _theme) {
            var theme = _theme || "Default";
            var baseurl = _baseurl;
            ut.baseurl = baseurl;
            var brushs = ut.parseBrush();
            if (brushs.length == 0)
                return;
            ut.loadStyle(baseurl + "styles/shCore.css");
            ut.loadStyle(baseurl + "styles/shTheme" + theme + ".css");
            ut.resources.push({url:baseurl + 'scripts/shCore.js',type:'js'});
            for (var i = 0; i < brushs.length; i++) {
                var lib = brushs[i];
                lib = eval("ut.brushMap." + lib);
                ut.resources.push({url:baseurl + "scripts/shBrush" + lib + ".js",type:'js'});
            }
            ut.loadNext();
        },
        loadNext : function() {
            if (ut.resources.length > 0) {
                var resource = ut.resources.shift();
                //var tempUt = ut;
                var callback = ut.resources.length > 0 ? function() {
                    ut.loadNext();
                } : function() {
                    SyntaxHighlighter.config.clipboardSwf = ut.baseurl + 'scripts/clipboard.swf';
                    SyntaxHighlighter.highlight();
                };
                if (resource.type == 'js') {
                    ut.loadJs(resource.url, callback);
                } else if (resource.type = 'css') {
                    ut.loadStyle(resource.url, callback);
                }
            }
        },
        loadJs : function(src, callback) {
            var oHead = document.getElementsByTagName('HEAD').item(0);
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = src;
            script.onreadystatechange = function () {
                if (this.readyState == 'loaded' || this.readyState == 'complete') {
                    callback();
                }
            };
            script.onload = callback;
            oHead.appendChild(script);
        },
        loadStyle : function(url) {
            var oHead = document.getElementsByTagName('HEAD').item(0);
            var style = document.createElement("link");
            style.type = "text/css";
            style.rel = "stylesheet";
            style.href = url;
            oHead.appendChild(style);
        }
    };
    return ut;
})();