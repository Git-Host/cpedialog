var MUSIC = {version:"1.0",_QMFL:true,_debugMode:false};
MUSIC.userAgent = (function() {
    var vie,vff,vopera,vsf,vapple,wintype,mactype,vair,vchrome;
    var discerned = false;
    var agent = (/(?:MSIE.(\d+\.\d+))|(?:(?:Firefox|GranParadiso|Iceweasel|Minefield).(\d+\.\d+))|(?:Opera.(\d+\.\d+))|(?:AppleWebKit.(\d+(?:\.\d+)?))/).exec(navigator.userAgent);
    var os = (/(Windows.*?;)|(Mac OS X.*?;)/).exec(navigator.userAgent);
    if (agent) {
        vie = agent[1] ? parseFloat(agent[1]) : NaN;
        vff = agent[2] ? parseFloat(agent[2]) : NaN;
        vopera = agent[3] ? parseFloat(agent[3]) : NaN;
        vsf = agent[4] ? parseFloat(agent[4]) : NaN;
        if (!isNaN(vsf)) {
            var _ua = navigator.userAgent;
            if (/AdobeAIR/.test(_ua)) {
                vair = 1;
            } else if (/Chrome/.test(_ua)) {
                vchrome = 1;
            } else {
                vapple = parseFloat((/Version\/(\d+(?:\.\d+)?)/).exec(_ua)[1]);
            }
        }
    } else {
        vie = vff = vopera = vsf = vapple = vair = NaN;
    }
    if (os) {
        wintype = !!os[1];
        mactype = !!os[2];
    } else {
        wintype = mactype = false;
    }
    function adjustBehaviors() {
        if (ua.ie < 7) {
            try {
                document.execCommand('BackgroundImageCache', false, true);
            } catch(ignored) {
            }
        }
        adjusted = true;
    }

    return{firefox:vff,ie:window.XDomainRequest ? 8 : vie,opera:vopera,air:vair,safari:vsf,safariV:vapple,windows:wintype,macs:mactype,chrome:vchrome,adjustBehaviors:adjustBehaviors};
})();
MUSIC.namespace = {map:function(namespace) {
    if (MUSIC.lang.isHashMap(namespace)) {
        for (var k in namespace) {
            window[k] = namespace[k];
        }
    }
}};
MUSIC.emptyFn = function() {
};
MUSIC.widget = {};
var ua = MUSIC.userAgent;
var Browser = {isMozilla:!!ua.firefox,isIE:!!ua.ie,isIE7:ua.ie >= 7,isIE8:ua.ie > 7,isFirefox:!!ua.firefox,isSafari:!!ua.safari,isOpera:!!ua.opera};
MUSIC.console = {print:function(msg, type) {
    if (window.console) {
        console.log((type == 4 ? (new Date() + ":") : "") + msg);
    }
}}
MUSIC.report = {receive:MUSIC.emptyFn,addRule:MUSIC.emptyFn}
Object.extend = function(destination, source) {
    for (var property in source) {
        destination[property] = source[property];
    }
    return destination;
}
MUSIC.object = {map:function(object, scope, tf) {
    scope = scope || window;
    QZFL.object.each(object, function(value, key) {
        if (typeof(tf) == "string") {
            if (typeof(value == tf)) {
                scope[key] = value;
            }
        } else {
            scope[key] = value;
        }
    });
},extend:function(object, extendModule) {
    var _t = QZFL.object.getType(object);
    if (_t != "object" && _t != "function") {
        return;
    }
    QZFL.object.each(extendModule, function(value, key) {
        object[key] = value;
    });
},each:function(object, fn) {
    if (typeof object != "object" || typeof fn != "function") {
        return false;
    }
    var i = 0,k,_fn = fn;
    if (Object.prototype.toString.call(object) === "[object Array]") {
        if (!!object.forEach) {
            object.forEach(fn);
        } else {
            var len = object.length
            while (i < len) {
                _fn(object[i], i, object);
                ++i;
            }
        }
    } else {
        for (k in object) {
            _fn(object[k], k, object);
        }
    }
    return true;
},getType:function(object) {
    var _t;
    return((_t = typeof(object)) == "object" ? object == null && "null" || Object.prototype.toString.call(object).slice(8, -1) : _t).toLowerCase();
}};

MUSIC.config = {defaultDataCharacterSet:"GB2312",DCCookieDomain:"music.soso.com",domainPrefix:"soso.com",gbEncoderPath:"",FSHelperPage:"http://music.soso.com/portal/toolpage/fp_gbk.html",defaultShareObject:"http://cache.music.soso.com/sosocache/music/proxy/getset.swf"};
document.domain = MUSIC.config.domainPrefix;

function commonReplace(s, p, r) {
    return s.toString().replace(p, r);
}
function listRaplace(s, l) {
    if (isHashMap(l)) {
        for (var i in l) {
            s = (commonReplace(s, l[i], i) || s);
        }
        return s;
    } else {
        return s;
    }
}
function trim(str) {
    return commonReplace(str + "", /^\s*|\s*$/g, '');
}
function ltrim(str) {
    return commonReplace(str + "", /^\s*/g, '');
}
function rtrim(str) {
    return commonReplace(str + "", /\s*$/g, '');
}
function nl2br(str) {
    return commonReplace(str + "", /\n/g, '<br />');
}
function s2nb(str) {
    return commonReplace(str + "", /[ ]{2}/g, '&nbsp;&nbsp;');
}
function URIencode(str) {
    return(str + "").replace(/[\x09\x0A\x0D\x21-\x29\x2B\x2C\x2F\x3A-\x3F\x5B-\x5E\x60\x7B-\x7E]/g, function(a) {
        return"%"
                + ((a.charCodeAt(0) < 16) ? ("0" + a.charCodeAt(0).toString(16)) : (a.charCodeAt(0).toString(16)))
    }).replace(/[\x00-\x20]/g, "+");
}
function escHTML(str) {
    return listRaplace((str + ""), {'&amp;':/&/g,'&lt;':/</g,'&gt;':/>/g,'&#039;':/\x27/g,'&quot;':/\x22/g});
}
function restHTML(str) {
    var t = restHTML.__utilDiv;
    t.innerHTML = (str + "");
    if (typeof(t.innerText) != 'undefined') {
        return t.innerText;
    } else if (typeof(t.textContent) != 'undefined') {
        return t.textContent;
    } else if (typeof(t.text) != 'undefined') {
        return t.text;
    } else {
        return'';
    }
}
restHTML.__utilDiv = document.createElement("div");
var StringBuilder = function() {
    this._strList = arg2arr(arguments);
};
StringBuilder.prototype.append = function(str) {
    if (isString(str)) {
        this._strList.push(str.toString());
    }
};
StringBuilder.prototype.insertFirst = function(str) {
    if (isString(str)) {
        this._strList.unshift(str.toString());
    }
};
StringBuilder.prototype.appendArray = function(arr) {
    if (isArray(arr)) {
        this._strList = this._strList.concat(arr);
    }
};
StringBuilder.prototype.toString = function(spliter) {
    return this._strList.join(!spliter ? '' : spliter);
};
StringBuilder.prototype.clear = function() {
    this._strList.splice(0, this._strList.length);
};
function write(strFormat, someArgs) {
    if (arguments.length < 1 || !isString(strFormat)) {
        rt.warn('No patern to write()');
        return'';
    }
    var rArr = arg2arr(arguments);
    var result = rArr.shift();
    var tmp;
    return result.replace(/\{(\d{1,2})(?:\:([xodQqb]))?\}/g, function(a, b, c) {
        b = parseInt(b, 10);
        if (b < 0 || (typeof rArr[b] == 'undefined')) {
            rt.warn('write() wrong patern:{0:Q}', strFormat);
            return'(n/a)';
        } else {
            if (!c) {
                return rArr[b];
            } else {
                switch (c) {case'x':return'0x' + rArr[b].toString(16);case'o':return'o' + rArr[b].toString(8);case'd':return rArr[b].toString(10);case'Q':return'\x22' + rArr[b].toString(16) + '\x22';case'q':return'`' + rArr[b].toString(16) + '\x27';case'b':return'<' + !!rArr[b] + '>';
                }
            }
        }
    });
}
function isURL(s) {
    var p = /^(?:ht|f)tp(?:s)?\:\/\/(?:[\w\-\.]+)\.\w+/i;
    return p.test(s);
}
function customEncode(s, type) {
    var r;
    if (typeof type == 'undefined') {
        type = '';
    }
    switch (type.toUpperCase()) {case"URICPT":r = encodeURIComponent(s);break;default:r = encodeURIComponent(s);
    }
    return r;
}
function escapeURI(s) {
    if (!isString(s)) {
        return'';
    }
    if (window.encodeURIComponent) {
        return encodeURIComponent(s);
    }
    if (window.escape) {
        return escape(s);
    }
}
function parseXML(text) {
    if (window.ActiveXObject) {
        var doc = MUSIC.lang.tryThese(function() {
            return new ActiveXObject('MSXML2.DOMDocument.6.0');
        }, function() {
            return new ActiveXObject('MSXML2.DOMDocument.5.0');
        }, function() {
            return new ActiveXObject('MSXML2.DOMDocument.4.0');
        }, function() {
            return new ActiveXObject('MSXML2.DOMDocument.3.0');
        }, function() {
            return new ActiveXObject('MSXML2.DOMDocument');
        }, function() {
            return new ActiveXObject('Microsoft.XMLDOM');
        });
        doc.async = "false";
        doc.loadXML(text);
        if (doc.parseError.reason) {
            rt.error(doc.parseError.reason);
            return null;
        }
    } else {
        var parser = new DOMParser();
        var doc = parser.parseFromString(text, "text/xml");
        if (doc.documentElement.nodeName == 'parsererror') {
            rt.error(doc.documentElement.textContent);
            return null;
        }
    }
    var x = doc.documentElement;
    return x;
}
function fillLength(s, l, ss, isBack) {
    if (typeof(s) != 'string') {
        s = s.toString();
    }
    if (s.length < l) {
        var res = (1 << (l - s.length)).toString(2).substring(1);
        if (typeof(ss) != 'undefined' && !!ss) {
            res = res.replace("0", ss.toString()).substring(1);
        }
        return isBack ? (s + res) : (res + s);
    } else {
        return s;
    }
}
;
function timeFormatString(s, format) {
    var n;
    if (typeof(s) == 'number') {
        n = new Date();
        n.setTime(s);
        s = n;
    }
    if (typeof(s) == 'object') {
        try {
            s.getTime();
        } catch(err) {
            rt.error("????????");
            return"";
        }
        if (typeof(format) != 'string') {
            return s.toString();
        } else {
            return format.replace(/\{([yYMdhms])(\:[\d\w\s]|)\}/g, function(a, b, c) {
                var tmp;
                switch (b) {case'y':tmp = s.getYear().toString();return fillLength(tmp.substring(tmp.length - 2), 2);case'Y':return fillLength(s.getFullYear(), 2);case'M':return fillLength(s.getMonth() + 1, 2, c);case'd':return fillLength(s.getDate(), 2, c);case'h':return fillLength(s.getHours(), 2, c);case'm':return fillLength(s.getMinutes(), 2);case's':return fillLength(s.getSeconds(), 2);
                }
            });
        }
    }
}
function cut(s, bl, tails) {
    if (typeof(s) != 'string')
        return'';
    if (typeof(tails) == 'undefined')
        tails = "";
    if (getRealLen(s) <= bl) {
        return s;
    }
    var res = [];
    var tmp;
    var ascii_re = /[\x00-\xFF]/;
    for (var i = 0,cnt = 0,len = s.length; i < len && cnt < bl; ++i) {
        res.push(tmp = s.charAt(i));
        if (ascii_re.test(tmp)) {
            cnt++;
        } else {
            cnt += 2;
        }
    }
    return res.join("") + tails;
}
function getRealLen(s, isUTF8) {
    if (typeof(s) != 'string')
        return 0;
    var r = /[^\x00-\xFF]/g;
    if (!isUTF8) {
        return s.replace(r, "**").length;
    } else {
        r = /[\x00-\xFF]/g;
        var cc = s.replace(r, "");
        return(s.length - cc.length) + (encodeURI(cc).length / 3);
    }
}
function createURIVbScript() {
    if (document.getElementById("vbEscapeScriptNode"))
        return;
    var script = document.createElement("script")
    script.id = "vbEscapeScriptNode"
    script.type = "text/vbscript";
    script.text = "Function str2asc(strstr) \n"
            + "str2asc = hex(asc(strstr)) \n" + "End Function \n"
            + "Function asc2str(ascasc) \n" + "    asc2str = chr(ascasc) \n"
            + "End Function";
    document.getElementsByTagName("head")[0].appendChild(script);
}
function UrlEncode(str) {
    return URIencode(str)
}
function UrlDecode(str) {
    createURIVbScript();
    var ret = "";
    for (var i = 0; i < str.length; i++) {
        var chr = str.charAt(i);
        if (chr == "+") {
            ret += " ";
        } else if (chr == "%") {
            var asc = str.substring(i + 1, i + 3);
            if (parseInt("0x" + asc) > 0x7f) {
                ret += asc2str(parseInt("0x" + asc
                        + str.substring(i + 4, i + 6)));
                i += 5;
            } else {
                ret += asc2str(parseInt("0x" + asc));
                i += 2;
            }
        } else {
            ret += chr;
        }
    }
    return ret;
}
String.prototype.trim = function() {
    return this.replace(/^\s+|\s+$/, "");
}
String.prototype.entityReplace = function() {
    return this.replace(/&#38;?/g, "&amp;").replace(/&#(\d+);?/g, function(a, b) {
        return String.fromCharCode(b)
    }).replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, "\"").replace(/&nbsp;/g, " ").replace(/&#13;/g, "\n").replace(/(&#10;)|(&#x\w*;)/g, "").replace(/&amp;/g, "&");
}
String.prototype.toTextEncode = function() {
    if (this && this != "") {
        return this.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\'/g, "&#39;").replace(/\"/g, "&quot;").replace(/\\/, "&#92;").replace(/script/ig, "Script");
    } else {
        return"";
    }
}
String.prototype.toScriptEncode = function() {
    if (this && this != "") {
        return this.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\'/g, "&#39;").replace(/\\/, "&#92;").replace(/\(/g, "?").replace(/\)/g, "?");
    } else {
        return"";
    }
}
String.prototype.singleEncode = function() {
    return this.replace(/[\x00-\xff]/g, function(a) {
        return escape(a)
    });
}
String.prototype.myEncode = function() {
    return this.replace(/\'/g, "’").replace(/\"/g, "“").replace(/&#39;/g, "’").replace(/&quot;/g, "“").replace(/&acute;/g, "’").replace(/\%/g, "?");
}
var r = /[\x21-\x29\x2B\x2C\x2F\x3A-\x3F\x5B-\x5E\x60\x7B-\x7E]/g;
String.prototype.encode = function() {
    return this.replace(r, function(a) {
        return"%" + a.charCodeAt(0).toString(16)
    }).replace(/ /g, "+")
};
var StrBuf = StringBuilder;
StrBuf.prototype.a = StringBuilder.prototype.append;
StrBuf.prototype.c = StringBuilder.prototype.clear;
StrBuf.prototype.d = StringBuilder.prototype.clear;
StrBuf.prototype.toS = StringBuilder.prototype.toString;
function g_MyEncode(s) {
    return(s == null) ? "" : s.myEncode();
}
String.prototype.toHTML = function() {
    var div = document.createElement("div");
    div.innerHTML = this;
    return div.innerHTML;
}
function htmlReplace(srcString) {
    srcString = srcString.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    return srcString;
}
function getNode(objectDoc, strPath) {
    var returnValue = "";
    if (objectDoc && objectDoc.xml != null && objectDoc.xml != "") {
        var strValue = objectDoc.selectSingleNode(strPath);
        if (strValue)
            returnValue = strValue.text;
    }
    return returnValue;
}
function getNodeAttr(objectDoc, strPath, strAttr) {
    var returnValue = -1;
    if (objectDoc && objectDoc.xml != "") {
        var strValue = objectDoc.selectSingleNode(strPath);
        if (strValue)
            returnValue = strValue.getAttribute(strAttr);
    }
    return returnValue;
}
function getChildNodeValue(objectDoc, strTagName) {
    if (objectDoc.getElementsByTagName(strTagName).length > 0 && objectDoc.getElementsByTagName(strTagName)[0].firstChild) {
        return objectDoc.getElementsByTagName(strTagName)[0].firstChild.nodeValue;
    } else {
        return"&nbsp;";
    }
}
function compile_html(html) {
    if (!html)
        return null;
    html = html.trim().toLowerCase();
    var div = document.createElement('div');
    div.innerHTML = html;
    return div.childNodes;
}
function JS_TPL(tmpl, ns) {
    function fn(w, g) {
        g = g.split("|");
        var names = g[0].split(".");
        var cnt = ns;
        for (i in names) {
            cnt = cnt[names[i]];
        }
        for (var i = 1; i < g.length; i++)
            cnt = eval(g[i])(cnt);
        return cnt;
    }

    ;
    return tmpl.replace(/%\(([A-Za-z0-9_|.]+)\)/g, fn);
}
Object.extend(String.prototype, {to_html:function() {
    return compile_html(this);
},format:function(ns) {
    return JS_TPL(this, ns);
},jsformat:function(ns) {
    return JS_TPL(this, ns);
}});
function Hex(n) {
    c = n;
    execScript("c = Hex(c)", "vbscript");
    return c;
}
function Asc(s) {
    c = s;
    execScript("c = Asc(c)", "vbscript");
    return c;
}
function gb2312Encode(str) {
    var string = "";
    c = s = "";
    var high = "";
    var low = "";
    for (var i = 0; i < str.length; i++) {
        c = Asc(str.charAt(i));
        if (Math.abs(c) < 0xFF)
            string += str.charAt(i); else {
            if (c < 0)
                c += 0x10000;
            high = ((c & 0xFF00) >> 8) & 0x00FF;
            low = c & 0xFF;
            string += "%" + Hex(high) + "%" + Hex(low);
        }
    }
    return string;
}
var div_for_convert_html = document.createElement("DIV");
String.prototype.HTML2Text = function() {
    with (div_for_convert_html) {
        innerHTML = this.replace(/(?:&#13;)|(?:\n)/g, "<br>").replace(/(?:&#32;)|(?: )/g, "&nbsp;");
        return(Browser.isIE ? innerText : textContent).replace(/\xa0/g, " ");
    }
    ;
}
String.prototype.Text2HTML = function() {
    if (Browser.isIE) {
        div_for_convert_html.innerText = this;
        return div_for_convert_html.innerHTML
    }
    div_for_convert_html.textContent = this;
    return div_for_convert_html.innerHTML.replace(/\x0a/g, "<br>").replace(/ /g, "&nbsp;")
}
function avoidEscapeChar(varstr, charstr) {
    var invalid_str = "";
    for (i = 0; i < charstr.length; i++) {
        if (varstr.indexOf(charstr.charAt(i)) >= 0) {
            invalid_str += charstr.charAt(i) + " ";
        }
    }
    return invalid_str;
}
String.prototype.trim = function() {
    return this.replace(/^\s+|\s+$/, "");
}
String.prototype.getRealLength = function() {
    return this.replace(/[^\x00-\xff]/g, "aa").length;
}
function getStringLength(sValue) {
    return sValue.trim().getRealLength();
}

MUSIC.event = {KEYS:{BACKSPACE:8,TAB:9,RETURN:13,ESC:27,SPACE:32,LEFT:37,UP:38,RIGHT:39,DOWN:40,DELETE:46},extendType:/(click|mousedown|mouseover|mouseout|mouseup|mousemove|scroll|contextmenu|resize)/i,addEvent:function(obj, eventType, fn, argArray) {
    var cfn = fn;
    var res = false;
    if (!obj) {
        return res;
    }
    if (!obj.eventsList) {
        obj.eventsList = {};
    }
    if (!obj.eventsList[eventType]) {
        obj.eventsList[eventType] = {};
    }
    if (MUSIC.event.extendType.test(eventType)) {
        argArray = argArray || [];
        cfn = function(e) {
            return fn.apply(null, ([MUSIC.event.getEvent(e)]).concat(argArray));
        };
    }
    if (obj.addEventListener) {
        obj.addEventListener(eventType, cfn, false);
        res = true;
    } else if (obj.attachEvent) {
        res = obj.attachEvent("on" + eventType, cfn);
    } else {
        res = false;
    }
    if (res) {
        obj.eventsList[eventType][fn.toString()] = cfn;
    }
    return res;
},removeEvent:function(obj, eventType, fn) {
    var cfn = fn;
    var res = false;
    if (!obj) {
        return res;
    }
    if (!obj.eventsList) {
        obj.eventsList = {};
    }
    if (!obj.eventsList[eventType]) {
        obj.eventsList[eventType] = {};
    }
    if (!cfn) {
        res = MUSIC.event.purgeEvent(obj, eventType);
        return res;
    }
    if (MUSIC.event.extendType.test(eventType) && obj.eventsList[eventType] && obj.eventsList[eventType][fn.toString()]) {
        cfn = obj.eventsList[eventType][fn.toString()];
    }
    if (obj.removeEventListener) {
        obj.removeEventListener(eventType, cfn, false);
        res = true;
    } else if (obj.detachEvent) {
        res = obj.detachEvent("on" + eventType, cfn);
    } else {
        MUSIC.dialog.createInfoBox("??!", 1, 1);
    }
    if (res && obj.eventsList[eventType]) {
        delete obj.eventsList[eventType][fn.toString()];
    }
    return res;
},purgeEvent:function(obj, type) {
    if (obj.eventsList && obj.eventsList[type]) {
        for (var i in obj.eventsList[type]) {
            if (obj.removeEventListener) {
                obj.removeEventListener(type, obj.eventsList[type][i], false);
            } else if (obj.detachEvent) {
                obj.detachEvent('on' + type, obj.eventsList[type][i]);
            }
        }
    }
    if (obj['on' + type]) {
        obj['on' + type] = null;
    }
},getEvent:function(evt) {
    evt = evt || window.event;
    if (!evt && !MUSIC.userAgent.ie) {
        var c = this.getEvent.caller;
        while (c) {
            evt = c.arguments[0];
            if (evt && Event == evt.constructor) {
                break;
            }
            c = c.caller;
        }
    }
    return evt;
},getButton:function(evt) {
    var e = MUSIC.event.getEvent(evt);
    if (!e) {
        return-1
    }
    if (MUSIC.userAgent.ie) {
        return e.button - Math.ceil(e.button / 2);
    } else {
        return e.button;
    }
},getTarget:function(evt) {
    var e = MUSIC.event.getEvent(evt);
    if (e) {
        return e.target || e.srcElement;
    } else {
        return null;
    }
},getCurrentTarget:function(evt) {
    var e = MUSIC.event.getEvent(evt);
    if (e) {
        return e.currentTarget || document.activeElement;
    } else {
        return null;
    }
},cancelBubble:function(evt) {
    evt = MUSIC.event.getEvent();
    if (!evt) {
        return false
    }
    if (evt.stopPropagation) {
        evt.stopPropagation();
    } else {
        if (!evt.cancelBubble) {
            evt.cancelBubble = true;
        }
    }
},preventDefault:function(evt) {
    evt = MUSIC.event.getEvent();
    if (!evt) {
        return false
    }
    if (evt.preventDefault) {
        evt.preventDefault();
    } else {
        evt.returnValue = false;
    }
},mouseX:function(evt) {
    evt = MUSIC.event.getEvent();
    return evt.pageX || (evt.clientX + (document.documentElement.scrollLeft || document.body.scrollLeft));
},mouseY:function(evt) {
    evt = MUSIC.event.getEvent();
    return evt.pageY || (evt.clientY + (document.documentElement.scrollTop || document.body.scrollTop));
},getRelatedTarget:function(ev) {
    var t = ev.relatedTarget;
    if (!t) {
        if (ev.type == "mouseout") {
            t = ev.toElement;
        } else if (ev.type == "mouseover") {
            t = ev.fromElement;
        }
    }
    return t;
},bind:function(obj, method) {
    var args = Array.prototype.slice.call(arguments, 2);
    return function() {
        var _obj = obj || this;
        var _args = args.concat(Array.prototype.slice.call(arguments, 0));
        if (typeof(method) == "string") {
            if (_obj[method]) {
                return _obj[method].apply(_obj, _args);
            }
        } else {
            return method.apply(_obj, _args);
        }
    }
}};
MUSIC.event.on = MUSIC.event.addEvent;
window.addEvent = MUSIC.event.addEvent;
window.removeEvent = MUSIC.event.removeEvent;
window.getEvent = MUSIC.event.getEvent;
function EventUtil(oTarget, sEventType, fnHandler) {
    MUSIC.event.addEvent(oTarget, sEventType, fnHandler);
}
function EventUtilRemove(oTarget, sEventType, fnHandler) {
    MUSIC.event.removeEvent(oTarget, sEventType, fnHandler);
}

MUSIC.lang = {isString:function(o) {
    return(typeof(o) != 'undefined') && (o !== null) && (typeof(o) == 'string' || !!o.toString);
},isArray:function(o) {
    return(typeof(o) == 'object' && (o instanceof Array));
},isHashMap:function(o) {
    return((o !== null) && (typeof(o) == 'object'));
},isNode:function(o) {
    if (typeof(Node) == 'undefined') {
        Node = null;
    }
    try {
        if (!o || !((Node != undefined && o instanceof Node) || o.nodeName)) {
            return false;
        }
    } catch(ignored) {
        return false;
    }
    return true;
},isElement:function(o) {
    return o && o.nodeType == 1;
},isValidXMLdom:function(o) {
    if (!o) {
        return false;
    }
    if (!o.xml) {
        return false;
    }
    if (o.xml == "") {
        return false;
    }
    if (!(/^<\?xml/.test(o.xml))) {
        return false;
    }
    return true;
},arg2arr:function(refArgs, start) {
    if (typeof start == 'undefined') {
        start = 0;
    }
    return Array.prototype.slice.apply(refArgs, [start,refArgs.length]);
},getObjByNameSpace:function(ns) {
    if (typeof(ns) == 'undefined')
        return ns;
    var l = ns.split(".");
    var r = window;
    try {
        for (var i = 0,len = l.length; i < len; ++i) {
            r = r[l[i]];
            if (typeof(r) == 'undefined')
                return void(0);
        }
        return r;
    } catch(ignore) {
        return void(0);
    }
},objectClone:function(obj, preventName) {
    if ((typeof obj) == 'object') {
        var res = (MUSIC.lang.isArray(obj) || !!obj.sort) ? [] : {};
        for (var i in obj) {
            if (i != preventName)
                res[i] = objectClone(obj[i], preventName);
        }
        return res;
    } else if ((typeof obj) == 'function') {
        return(new obj()).constructor;
    }
    return obj;
},propertieCopy:function(s, b, propertiSet) {
    if (typeof propertiSet == 'undefined') {
        for (var p in b) {
            s[p] = b[p];
        }
    } else {
        for (var p in propertiSet) {
            s[p] = b[p];
        }
    }
    return s;
},tryThese:function() {
    var res;
    for (var ii = 0,len = arguments.length; ii < len; ii++) {
        try {
            res = arguments[ii]();
            return res;
        } catch(ignore) {
        }
    }
    return res;
},chain:function(u, v) {
    var calls = [];
    for (var ii = 0,len = arguments.length; ii < len; ii++) {
        calls.push(arguments[ii]);
    }
    return(function() {
        for (var ii = 0,len = calls.length; ii < len; ii++) {
            if (calls[ii] && calls[ii].apply(null, arguments) === false) {
                return false;
            }
        }
        return true;
    });
},uniqueArray:function(arr) {
    var flag = {};
    var index = 0;
    while (index < arr.length) {
        if (flag[arr[index]] == typeof(arr[index])) {
            arr.splice(index, 1);
            continue;
        }
        flag[arr[index].toString()] = typeof(arr[index]);
        ++index;
    }
    return arr;
}};
MUSIC.namespace.map(MUSIC.lang);
Function.prototype.bind = function() {
    var __method = this,args = MUSIC.lang.arg2arr(arguments),object = args.shift();
    return function() {
        return __method.apply(object, args.concat(MUSIC.lang.arg2arr(arguments)));
    }
}
Function.prototype.bindAsEventListener = function(object) {
    var __method = this,args = MUSIC.lang.arg2arr(arguments),object = args.shift();
    return function(event) {
        return __method.apply(object, [(event || window.event)].concat(args).concat(MUSIC.lang.arg2arr(arguments)));
    }
}

function HashTable() {
    this._hash = new Object();
    this.add = function(key, value) {
        if (typeof(key) != "undefined") {
            if (this.contains(key) == false) {
                this._hash[key] = typeof(value) == "undefined" ? null : value;
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
    this.remove = function(key) {
        delete this._hash[key];
    }
    this.count = function() {
        var i = 0;
        for (var k in this._hash) {
            i++;
        }
        return i;
    }
    this.items = function(key) {
        return this._hash[key];
    }
    this.contains = function(key) {
        return typeof(this._hash[key]) != "undefined";
    }
    this.clear = function() {
        for (var k in this._hash) {
            delete this._hash[k];
        }
    }
}

MUSIC.dom = {getById:function(id) {
    return document.getElementById(id);
},getByName:function(name, tagName) {
    if (!tagName)
        return document.getElementsByName(name);
    var arr = [];
    var e = document.getElementsByTagName(tagName);
    for (var i = 0; i < e.length; ++i) {
        if (!!e[i].getAttribute("name") && (e[i].getAttribute("name").toLowerCase() == name.toLowerCase())) {
            arr.push(e[i]);
        }
    }
    return arr;
},get:function(e) {
    if (e && (e.tagName || e.item)) {
        return e;
    }
    return this.getById(e);
},getNode:function(e) {
    if (e && (e.nodeType || e.item)) {
        return e;
    }
    if (typeof e === 'string') {
        return this.getById(e);
    }
    return null;
},getByTagName:function(e) {
    return document.getElementsByTagName(e);
},getInBody:function(id, tagName, insertFirst, parentNodeID, className, initCSSText) {
    var e = Element(id);
    if (!e) {
        tagName = (!tagName) ? "div" : tagName;
        e = document.createElement(tagName);
        e.id = id;
        var parentNode = (!parentNodeID) ? document.body : Element(parentNodeID);
        if (insertFirst)
            parentNode.insertBefore(e, parentNode.firstChild); else
            parentNode.appendChild(e);
        e.className = className ? className : "";
        e.style.cssText = initCSSText ? initCSSText : "";
    }
    parentNode = null;
    return e;
},removeElement:function(el) {
    if (!el) {
        return;
    }
    if (el.removeNode) {
        el.removeNode(true);
    } else {
        if (el.childNodes.length > 0) {
            for (var ii = el.childNodes.length - 1; ii >= 0; ii--) {
                MUSIC.dom.removeElement(el.childNodes[ii]);
            }
        }
        if (el.parentNode) {
            el.parentNode.removeChild(el);
        }
    }
    el = null;
    return null;
},searchElementByClassName:function(el, className) {
    el = this.get(el);
    if (!el) {
        return null
    }
    var re = MUSIC.css.getClassRegEx(className);
    while (el) {
        if (re.test(el.className)) {
            return el;
        }
        el = el.parentNode;
    }
    return null;
},getElementsByClassName:function(className, tag, root) {
    tag = tag || '*';
    root = (root) ? this.get(root) : null || document;
    if (!root) {
        return[];
    }
    var nodes = [],elements = root.getElementsByTagName(tag),re = MUSIC.css.getClassRegEx(className);
    for (var i = 0,len = elements.length; i < len; ++i) {
        if (re.test(elements[i].className)) {
            nodes[nodes.length] = elements[i];
        }
    }
    return nodes;
},isAncestor:function(node1, node2) {
    if (!node1 || !node2) {
        return false;
    }
    if (node1.contains && node2.nodeType && !MUSIC.userAgent.Safari) {
        return node1.contains(node2) && node1 != node2;
    }
    if (node1.compareDocumentPosition && node2.nodeType) {
        return!!(node1.compareDocumentPosition(node2) & 16);
    } else if (node2.nodeType) {
        return!!this.getAncestorBy(node2, function(el) {
            return el == node1;
        });
    }
    return false;
},getAncestorBy:function(node, method) {
    while (node = node.parentNode) {
        if (node && node.nodeType == 1 && (!method || method(node))) {
            return node;
        }
    }
    return null;
},getFirstChild:function(node) {
    node = this.getNode(node);
    if (!node) {
        return null;
    }
    var child = MUSIC.lang.isElement(node.firstChild) ? node.firstChild : null;
    return child || this.getNextSibling(node.firstChild);
},getNextSibling:function(node) {
    node = this.getNode(node);
    if (!node) {
        return null;
    }
    while (node) {
        node = node.nextSibling;
        if (MUSIC.lang.isElement(node)) {
            return node;
        }
    }
    return null;
},getPreviousSibling:function(node) {
    node = this.getNode(node);
    if (!node) {
        return null;
    }
    while (node) {
        node = node.previousSibling;
        if (MUSIC.lang.isElement(node)) {
            return node;
        }
    }
    return null;
},createElementIn:function(tagName, el, insertFirst, attributes) {
    tagName = tagName || "div";
    el = this.get(el) || document.body;
    var _doc = el.ownerDocument;
    var _e = _doc.createElement(tagName);
    if (attributes) {
        for (var k in attributes) {
            if (/class/.test(k)) {
                _e.className = attributes[k];
            } else if (/style/.test(k)) {
                _e.style.cssText = attributes[k];
            } else {
                _e[k] = attributes[k];
            }
        }
    }
    if (insertFirst) {
        el.insertBefore(_e, el.firstChild);
    } else {
        el.appendChild(_e);
    }
    return _e;
},getStyle:function(el, property) {
    el = this.get(el);
    var w3cMode = document.defaultView && document.defaultView.getComputedStyle;
    var computed = !w3cMode ? null : document.defaultView.getComputedStyle(el, '');
    var value = "";
    switch (property) {case"float":property = w3cMode ? "cssFloat" : "styleFloat";break;case"opacity":if (!w3cMode) {
        var val = 100;
        try {
            val = el.filters['DXImageTransform.Microsoft.Alpha'].opacity;
        } catch(e) {
            try {
                val = el.filters('alpha').opacity;
            } catch(e) {
            }
        }
        return val / 100;
    }
        break;case"backgroundPositionX":if (w3cMode) {
        property = "backgroundPosition";
        return((computed || el.style)[property]).split(" ")[0];
    }
        break;case"backgroundPositionY":if (w3cMode) {
        property = "backgroundPosition";
        return((computed || el.style)[property]).split(" ")[1];
    }
        break;
    }
    if (w3cMode) {
        return(computed || el.style)[property];
    } else {
        return(el.currentStyle[property] || el.style[property]);
    }
},setStyle:function(el, property, value) {
    el = this.get(el);
    if (!el) {
        return false;
    }
    var w3cMode = document.defaultView && document.defaultView.getComputedStyle;
    switch (property) {case"float":property = w3cMode ? "cssFloat" : "styleFloat";case"opacity":if (!w3cMode) {
        if (value >= 1) {
            el.style.filter = "";
            return;
        }
        el.style.filter = 'alpha(opacity=' + (value * 100) + ')';
        return true;
    } else {
        el.style[property] = value;
        return true;
    }
        break;case"backgroundPositionX":if (w3cMode) {
        var _y = MUSIC.dom.getStyle(el, "backgroundPositionY");
        el.style["backgroundPosition"] = value + " "
                + (_y || "top");
    } else {
        el.style[property] = value;
    }
        break;case"backgroundPositionY":if (w3cMode) {
        var _x = MUSIC.dom.getStyle(el, "backgroundPositionX");
        el.style["backgroundPosition"] = (_x || "left") + " "
                + value;
    } else {
        el.style[property] = value;
    }
        break;default:if (typeof el.style[property] == "undefined") {
        return false
    }
        el.style[property] = value;return true;
    }
},createNamedElement:function(type, name, doc) {
    doc = doc || document;
    var element;
    try {
        element = doc.createElement('<' + type + ' name="' + name + '">');
    } catch(ignore) {
    }
    if (!element || !element.name) {
        element = doc.createElement(type);
        element.name = name;
    }
    return element;
},getPosition:function(el) {
    var xy = MUSIC.dom.getXY(el);
    var size = MUSIC.dom.getSize(el);
    return{"top":xy[1],"left":xy[0],"width":size[0],"height":size[1]};
},setPosition:function(el, pos) {
    MUSIC.dom.setXY(el, pos['left'], pos['top']);
    MUSIC.dom.setSize(el, pos['width'], pos['height']);
},getXY:function(el, doc) {
    var _t = 0,_l = 0,_doc = doc || document;
    if (el) {
        if (_doc.documentElement.getBoundingClientRect && el.getBoundingClientRect) {
            var box = el.getBoundingClientRect(),oDoc = el.ownerDocument,_fix = QZFL.userAgent.ie ? 2 : 0;
            _t = box.top - _fix + QZFL.dom.getScrollTop(oDoc);
            _l = box.left - _fix + QZFL.dom.getScrollLeft(oDoc);
        } else {
            while (el.offsetParent) {
                _t += el.offsetTop;
                _l += el.offsetLeft;
                el = el.offsetParent;
            }
        }
    }
    return[_l,_t];
},getSize:function(el) {
    var _w = el.offsetWidth;
    var _h = el.offsetHeight;
    return[_w,_h];
},setXY:function(el, x, y) {
    el = this.get(el);
    var _ml = parseInt(this.getStyle(el, "marginLeft")) || 0;
    var _mt = parseInt(this.getStyle(el, "marginTop")) || 0;
    this.setStyle(el, "left", parseInt(x) - _ml + "px");
    this.setStyle(el, "top", parseInt(y) - _mt + "px");
},getScrollLeft:function(doc) {
    doc = doc || document;
    return Math.max(doc.documentElement.scrollLeft, doc.body.scrollLeft);
},getScrollTop:function(doc) {
    doc = doc || document;
    return Math.max(doc.documentElement.scrollTop, doc.body.scrollTop);
},getScrollHeight:function(doc) {
    doc = doc || document;
    return Math.max(doc.documentElement.scrollHeight, doc.body.scrollHeight);
},getScrollWidth:function(doc) {
    doc = doc || document;
    return Math.max(doc.documentElement.scrollWidth, doc.body.scrollWidth);
},setScrollLeft:function(value, doc) {
    doc = doc || document;
    doc[doc.compatMode == "CSS1Compat" && !MUSIC.userAgent.safari ? "documentElement" : "body"].scrollLeft = value;
},setScrollTop:function(value, doc) {
    doc = doc || document;
    doc[doc.compatMode == "CSS1Compat" && !MUSIC.userAgent.safari ? "documentElement" : "body"].scrollTop = value;
},getClientHeight:function(doc) {
    doc = doc || document;
    var height = doc.innerHeight;
    var mode = doc.compatMode;
    if ((mode || ua.ie) && !ua.opera) {
        height = (mode == 'CSS1Compat') ? doc.documentElement.clientHeight : doc.body.clientHeight;
    }
    return height;
},getClientWidth:function(doc) {
    doc = doc || document;
    var width = doc.innerWidth;
    var mode = doc.compatMode;
    if (mode || ua.ie) {
        width = (mode == 'CSS1Compat') ? doc.documentElement.clientWidth : doc.body.clientWidth;
    }
    return width;
},setSize:function(el, width, height) {
    el = this.get(el);
    var _wFix = /\d+([a-z%]+)/i.exec(width);
    _wFix = _wFix ? _wFix[1] : "";
    var _hFix = /\d+([a-z%]+)/i.exec(height);
    _hFix = _hFix ? _hFix[1] : "";
    this.setStyle(el, "width", (!width || width < 0 || /auto/i.test(width)) ? "auto" : (parseInt(width) + (_wFix || "px")));
    this.setStyle(el, "height", (!height || height < 0 || /auto/i.test(height)) ? "auto" : (parseInt(height) + (_hFix || "px")));
},getDocumentWindow:function(doc) {
    _doc = doc || document;
    return _doc.parentWindow || _doc.defaultView;
},getElementsByTagNameNS:function(node, ns, tgn) {
    var res = [];
    if (node) {
        if (node.getElementsByTagNameNS) {
            return node.getElementsByTagName(ns + ":" + tgn);
        } else if (node.getElementsByTagName) {
            var n = document.namespaces;
            if (n.length > 0) {
                var l = node.getElementsByTagName(tgn);
                for (var i = 0,len = l.length; i < len; ++i) {
                    if (l[i].scopeName == ns) {
                        res.push(l[i]);
                    }
                }
            }
        }
    }
    return res;
},hideElement:function(e) {
    var obj;
    try {
        if (typeof(e) == "string") {
            obj = Element(e);
        } else {
            obj = e;
        }
        obj.style.display = "none";
    } catch(Ignore) {
    }
},showElement:function(e) {
    try {
        if (typeof(e) == "string") {
            Element(e).style.display = "";
        } else {
            e.style.display = "";
        }
    } catch(e) {
    }
}};
var _CN = MUSIC.dom.createNamedElement;
var Element = $ = MUSIC.dom.getById;
var removeNode = MUSIC.dom.removeElement;
var showElement = MUSIC.dom.showElement;
var hideElement = MUSIC.dom.hideElement;
var getElementInBody = MUSIC.dom.getInBody;
var getScrollTop = MUSIC.dom.getScrollTop;
var getScrollLeft = MUSIC.dom.getScrollLeft;

function utilGetCookie(name) {
    var r = new RegExp("(?:^|;+|\\s+)" + name + "=([^;]*)");
    var m = document.cookie.match(r);
    return(!m ? "" : m[1]);
}
function utilSetCookie(name, value, domain, path, hour) {
    if (hour) {
        var today = new Date();
        var expire = new Date();
        expire.setTime(today.getTime() + 3600000 * hour);
    }
    document.cookie = name
            + "="
            + value
            + "; "
            + (hour ? ("expires=" + expire.toGMTString() + "; ") : "")
            + (path ? ("path=" + path + "; ") : "path=/; ")
            + (domain ? ("domain=" + domain + ";") : ("domain="
            + MUSIC.config.DCCookieDomain + ";"));
    return true;
}
function copyToClip(text) {
    if (ua.ie) {
        return clipboardData.setData("Text", text);
    } else {
        var o = MUSIC.shareObject.getValidSO();
        return o ? o.setClipboard(text) : false;
    }
}
function _showHashmap(object) {
    var descString = [];
    var n = 20;
    for (var value in object) {
        try {
            descString.push(value + " ==> " + object[value]);
        } catch(exception) {
            descString.push(value + " =!> " + exception.message);
        }
        if (!n--) {
            MUSIC.dialog.createInfoBox(descString.join("\n"), 1, 1);
            descString = [];
            n = 20;
        }
    }
    if (descString.length > 0) {
        MUSIC.dialog.createInfoBox(descString.join("\n"), 1, 1);
    } else {
        alert(object);
    }
}
function evalGlobal(js) {
    var obj = document.createElement('script');
    obj.type = 'text/javascript';
    obj.id = "__evalGlobal_" + evalGlobal._counter;
    try {
        obj.innerHTML = js;
    } catch(e) {
        obj.text = js;
    }
    document.body.appendChild(obj);
    evalGlobal._counter++;
    setTimeout('removeNode($("' + obj.id + '"));', 50);
}
evalGlobal._counter = 0;
function runStyleGlobal(st) {
    if (ua.safari) {
        var obj = document.createElement('style');
        obj.type = 'text/css';
        obj.id = "__runStyle_" + runStyleGlobal._counter;
        try {
            obj.textContent = st;
        } catch(e) {
            MUSIC.dialog.createInfoBox(e.message, 1, 1);
        }
        var h = document.getElementsByTagName("head")[0];
        if (h) {
            h.appendChild(obj);
            runStyleGlobal._counter++;
        }
    } else {
        rt.warn("plz use runStyleGlobal() in Safari!");
    }
}
runStyleGlobal._counter = 0;
function URI(s) {
    if (!isString(s)) {
        return null;
    }
    var depart = s.split("://");
    if (isArray(depart) && depart.length > 1 && (/^[a-zA-Z]+$/).test(depart[0])) {
        this.protocol = depart[0].toLowerCase();
        var h = depart[1].split("/");
        if (isArray(h) && h[0].length > 0) {
            this.host = h[0];
            this.pathname = "/"
                    + h.slice(1).join("/").replace(/(\?|\#).+/i, "");
            this.href = s;
            var se = depart[1].lastIndexOf("?");
            var ha = depart[1].lastIndexOf("#");
            this.search = (se >= 0) ? depart[1].substring(se) : "";
            this.hash = (ha >= 0) ? depart[1].substring(ha) : "";
            if (this.search.length > 0 && this.hash.length > 0) {
                if (ha < se) {
                    this.search = "";
                } else {
                    this.search = depart[1].substring(se, ha);
                }
            }
            return this;
        } else {
            return null;
        }
    } else {
        return null;
    }
}
function genHttpParamString(o) {
    if (MUSIC.lang.isHashMap(o)) {
        var r = new StringBuilder();
        try {
            for (var i in o) {
                r.append(i + "=" + customEncode(o[i], "URICPT"));
            }
        } catch(ignore) {
            return'';
        }
        return r.toString("&");
    } else if (typeof(o) == 'string') {
        return o;
    } else {
        return'';
    }
}
function splitHttpParamString(s) {
    return commonDictionarySplit(s, "&");
}
function commonDictionarySplit(s, esp, vq) {
    if (typeof(esp) == 'undefined') {
        esp = "&";
    }
    if (typeof(vq) == 'undefined') {
        vq = "";
    }
    var re_vq = new RegExp("^" + vq + "|" + vq + "$", "g");
    if (isString(s)) {
        var l = s.split(vq + esp);
        var tmp;
        var res = {};
        for (var i = 0,len = l.length; i < len; i++) {
            tmp = l[i].split("=");
            if (tmp.length > 1) {
                res[tmp[0]] = (tmp.slice(1).join("=")).replace(re_vq, "");
            } else {
                res[l[i]] = true;
            }
        }
        return res;
    } else {
        return{};
    }
}
var MUSIC = MUSIC || {};
function getParameter(name, cancelBubble) {
    var r = new RegExp("(\\?|#|&)" + name + "=([^&#]*)(&|#|$)");
    var m = location.href.match(r);
    if ((!m || m == "") && !cancelBubble) {
        if (1)
            m = window.location.href.match(r); else
            m = top.location.href.match(r);
    }
    return(!m ? "" : m[2]);
}
function getPosition(obj) {
    var top = 0;
    var left = 0;
    var width = obj.offsetWidth;
    var height = obj.offsetHeight;
    while (obj.offsetParent) {
        top += obj.offsetTop;
        left += obj.offsetLeft;
        obj = obj.offsetParent;
    }
    return{"top":top,"left":left,"width":width,"height":height};
}
function loadJs(sSrc, charset) {
    var head = document.getElementsByTagName("head")[0] || document.documentElement;
    var oScriptTag = document.createElement("script");
    oScriptTag.type = "text/javascript";
    oScriptTag.src = sSrc;
    if (charset)
        oScriptTag.charset = charset;
    head.appendChild(oScriptTag);
}
function openPostWindow(sUrl, sWindowName, oPostData, feature) {
    if (typeof sWindowName !== "string") {
        sWindowName = "";
    }
    var win;
    if (1)
    {
        win = window.open("http://cache.music.soso.com/sosocache/music/predata_loading.html", sWindowName, feature);
    } else
        win = top.window.open("http://cache.music.soso.com/sosocache/music/predata_loading.html", sWindowName, feature);
    if (!win) {
        MUSIC.dialog.createInfoBox("???????,?????!", 1, 1);
    } else
        win.focus();
    var sFormId = "post_window_form";
    var oForm = document.getElementById(sFormId);
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
    var oForm = document.createElement("form");
    oForm.id = sFormId;
    oForm.action = sUrl;
    oForm.method = "POST";
    oForm.target = sWindowName;
    for (key in oPostData) {
        var oInput = document.createElement("input");
        oInput.type = "hidden";
        oInput.name = key;
        oInput.value = oPostData[key];
        oForm.appendChild(oInput);
    }
    document.body.appendChild(oForm);
    oForm.submit();
}
(function doFireForxInnerText() {
    if (!ua.ie) {
        HTMLElement.prototype.__defineGetter__("innerText", function() {
            var anyString = "";
            var childS = this.childNodes;
            for (var i = 0; i < childS.length; i++) {
                if (childS[i].nodeType == 1) {
                    anyString += childS[i].tagName == "BR" ? '\n' : childS[i].innerText;
                } else if (childS[i].nodeType == 3) {
                    anyString += childS[i].nodeValue;
                }
            }
            return anyString;
        });
        HTMLElement.prototype.__defineSetter__("innerText", function(sText) {
            this.textContent = sText;
        });
    }
})();
function isMouseLeaveOrEnter(e, handler) {
    if (e.type != 'mouseout' && e.type != 'mouseover')
        return false;
    var reltg = e.relatedTarget ? e.relatedTarget : e.type == 'mouseout' ? e.toElement : e.fromElement;
    while (reltg && reltg != handler)
        reltg = reltg.parentNode;
    return(reltg != handler);
}
var utils = new Object();
utils.each = function(func, list) {
    for (var i = 0; i < list.length; i++) {
        if (func.call(this, list[i], i) == false)
            break;
    }
}

MUSIC.css = {getClassRegEx:function(className) {
    var re = MUSIC.css.classNameCache[className];
    if (!re) {
        re = new RegExp('(?:^|\\s+)' + className + '(?:\\s+|$)');
        MUSIC.css.classNameCache[className] = re;
    }
    return re;
},convertHexColor:function(color) {
    color = /^#/.test(color) ? color.substr(1) : color;
    var reColor = new RegExp("\\w{2}", "ig");
    color = color.match(reColor);
    if (!color || color.length < 3) {
        return[0,0,0]
    }
    var r = parseInt(color[0], 16);
    var g = parseInt(color[1], 16);
    var b = parseInt(color[2], 16);
    return[r,g,b];
},styleSheets:{},getStyleSheetById:function(id) {
    try {
        return MUSIC.dom.get(id).sheet || document.styleSheets[id];
    } catch(e) {
        return null
    }
},getRulesBySheet:function(sheetId) {
    var ss = MUSIC.css.getStyleSheetById(sheetId);
    if (ss) {
        try {
            return ss.cssRules || ss.rules;
        } catch(e) {
            return null
        }
    } else {
        return null
    }
},getRuleBySelector:function(sheetId, selector) {
    var _ss = this.getStyleSheetById(sheetId);
    if (!_ss.cacheSelector) {
        _ss.cacheSelector = {}
    }
    ;
    if (_ss) {
        var _rs = _ss.cssRules || _ss.rules;
        var re = new RegExp('^' + selector + '$', "i");
        var _cs = _ss.cacheSelector[selector];
        if (_cs && re.test(_rs[_cs].selectorText)) {
            return _rs[_cs];
        } else {
            for (var i = 0; i < _rs.length; i++) {
                if (re.test(_rs[i].selectorText)) {
                    _ss.cacheSelector[selector] = i;
                    return _rs[i];
                }
            }
            return null;
        }
    } else {
        return null;
    }
},insertCSSLink:function(url, id, sco) {
    var dom = document;
    if (sco != null) {
        var dom = sco.document;
    }
    if (id != null && dom.getElementById(id) != null) {
        return;
    }
    var cssLink = dom.createElement("link");
    if (id) {
        cssLink.id = id;
    }
    cssLink.rel = "stylesheet";
    cssLink.rev = "stylesheet";
    cssLink.type = "text/css";
    cssLink.media = "screen";
    cssLink.href = url;
    dom.getElementsByTagName("head")[0].appendChild(cssLink);
    return cssLink.sheet || cssLink;
},insertStyleSheet:function(sheetId) {
    var ss = document.createElement("style");
    ss.id = sheetId;
    document.getElementsByTagName("head")[0].appendChild(ss);
    return ss.sheet || ss;
},removeStyleSheet:function(id) {
    var _ss = this.getStyleSheetById(id);
    if (_ss) {
        var own = _ss.owningElement || _ss.ownerNode;
        MUSIC.dom.removeElement(own);
    }
},hasClassName:function(elem, cname) {
    return(elem && cname) ? new RegExp('\\b' + trim(cname) + '\\b').test(elem.className) : false;
},swapClassName:function(elements, class1, class2) {
    function _swap(el, c1, c2) {
        if (MUSIC.css.hasClassName(el, c1)) {
            el.className = el.className.replace(c1, c2);
        } else if (MUSIC.css.hasClassName(el, c2)) {
            el.className = el.className.replace(c2, c1);
        }
    }

    if (elements.constructor != Array) {
        elements = [elements];
    }
    for (var i = 0,len = elements.length; i < len; i++) {
        _swap(elements[i], class1, class2);
    }
},replaceClassName:function(elements, sourceClass, targetClass) {
    function _replace(el, c1, c2) {
        if (MUSIC.css.hasClassName(el, c1)) {
            el.className = el.className.replace(c1, c2);
        }
    }

    if (elements.constructor != Array) {
        elements = [elements];
    }
    for (var i = 0,len = elements.length; i < len; i++) {
        _replace(elements[i], sourceClass, targetClass);
    }
},addClassName:function(elem, cname) {
    if (elem && cname) {
        if (elem.className) {
            if (MUSIC.css.hasClassName(elem, cname)) {
                return false;
            } else {
                elem.className += ' ' + trim(cname);
                return true;
            }
        } else {
            elem.className = cname;
            return true;
        }
    } else {
        return false;
    }
},removeClassName:function(elem, cname) {
    if (elem && cname && elem.className) {
        var old = elem.className;
        elem.className = trim(elem.className.replace(new RegExp('\\b' + trim(cname) + '\\b'), ''));
        return elem.className != old;
    } else {
        return false;
    }
},toggleClassName:function(elem, cname) {
    var r = MUSIC.css;
    if (r.hasClassName(elem, cname)) {
        r.removeClassName(elem, cname);
    } else {
        r.addClassName(elem, cname);
    }
}}
MUSIC.css.classNameCache = {};

MUSIC.XHR = function(actionURL, cname, method, data, isAsync, nocache) {
    if (!isURL(actionURL)) {
        rt.error("error actionURL -> {0:Q} in MUSIC.XHR construct!", actionURL);
        return null;
    }
    if (!cname) {
        cname = "_xhrInstence_" + (MUSIC.XHR.counter + 1);
    }
    var prot;
    if (MUSIC.XHR.instance[cname]instanceof MUSIC.XHR) {
        prot = MUSIC.XHR.instance[cname];
    } else {
        prot = (MUSIC.XHR.instance[cname] = this);
        MUSIC.XHR.counter++;
    }
    prot._name = cname;
    prot._nc = !!nocache;
    prot._method = (!isString(method) || method.toUpperCase() != "GET") ? "POST" : (method = "GET");
    prot._isAsync = (!(isAsync === false)) ? true : isAsync;
    prot._uri = actionURL;
    prot._data = (isHashMap(data) || typeof(data) == 'string') ? data : null;
    prot._sender = null;
    prot._isHeaderSetted = false;
    this.onSuccess = MUSIC.emptyFn;
    this.onError = MUSIC.emptyFn;
    this.charset = "gb2312";
    this.proxyPath = "";
    return prot;
}
MUSIC.XHR.instance = {};
MUSIC.XHR.counter = 0;
MUSIC.XHR._errCodeMap = {400:{msg:'Bad Request'},401:{msg:'Unauthorized'},403:{msg:'Forbidden'},404:{msg:'Not Found'},999:{msg:'Proxy page error'},1000:{msg:'Bad Response'},1001:{msg:'No Network'},1002:{msg:'No Data'},1003:{msg:'Eval Error'}};
MUSIC.XHR.xsend = function(o, uri) {
    if (!(o instanceof MUSIC.XHR)) {
        return false;
    }
    if (ua.firefox && ua.firefox < 3) {
        rt.error("can't surport xsite in firefox!");
        return false;
    }
    function clear(obj) {
        try {
            obj._sender = obj._sender.callback = obj._sender.errorCallback = obj._sender.onreadystatechange = null;
        } catch(ignore) {
        }
        if (ua.safari || ua.opera) {
            setTimeout('removeNode($("_xsend_frm_' + obj._name + '"))', 50);
        } else {
            removeNode($("_xsend_frm_" + obj._name));
        }
    }

    if (o._sender === null || o._sender === void(0)) {
        var sender = document.createElement("iframe");
        sender.id = "_xsend_frm_" + o._name;
        sender.style.width = sender.style.height = sender.style.borderWidth = "0";
        document.body.appendChild(sender);
        sender.callback = MUSIC.event.bind(o, function(data) {
            o.onSuccess(data);
            clear(o);
        });
        sender.errorCallback = MUSIC.event.bind(o, function(num) {
            o.onError(MUSIC.XHR._errCodeMap[num]);
            clear(o);
        });
        o._sender = sender;
    }
    var tmp = MUSIC.config.gbEncoderPath;
    o.GBEncoderPath = tmp ? tmp : "";
    o._sender.src = uri.protocol + "://" + uri.host + (this.proxyPath ? this.proxyPath : "/xhr_proxy_gbk.html");
    return true;
}
MUSIC.XHR.prototype.send = function() {
    if (this._method == 'POST' && this._data == null) {
        rt.warn("MUSIC.XHR -> {0:q}, can't send data 'null'!", this._name);
        return false;
    }
    var u = new URI(this._uri);
    if (u == null) {
        rt.warn("MUSIC.XHR -> {0:q}, bad url", this._name);
        return false;
    }
    if (u.host != location.host) {
        return MUSIC.XHR.xsend(this, u);
    }
    if (this._sender === null || this._sender === void(0)) {
        var sender = tryThese(function() {
            return new XMLHttpRequest();
        }, function() {
            return new ActiveXObject("Msxml2.XMLHTTP");
        }, function() {
            return new ActiveXObject("Microsoft.XMLHTTP");
        }) || null;
        if (!sender) {
            rt.error("MUSIC.XHR -> {0:q}, create xhr object faild!", this._name);
            return false;
        }
        this._sender = sender;
    }
    try {
        this._sender.open(this._method, this._uri, this._isAsync);
    } catch(err) {
        rt.error("exception when opening connection to {0:q}:{1}", this._uri, err);
        return false;
    }
    if (this._method == 'POST' && !this._isHeaderSetted) {
        this._sender.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        this._isHeaderSetted = true;
    }
    if (this._nc) {
        this._sender.setRequestHeader('If-Modified-Since', 'Thu, 1 Jan 1970 00:00:00 GMT');
        this._sender.setRequestHeader('Cache-Control', 'no-cache');
    }
    var d = genHttpParamString(this._data);
    this._sender.onreadystatechange = MUSIC.event.bind(this, function() {
        try {
            if (this._sender.readyState == 4) {
                if (this._sender.status >= 200 && this._sender.status < 300) {
                    this.onSuccess({text:this._sender.responseText,xmlDom:this._sender.responseXML});
                } else {
                    if (ua.safari && (typeof(this._sender.status) == 'undefined')) {
                        this.onError(MUSIC.XHR._errCodeMap[1002]);
                    } else {
                        this.onError(MUSIC.XHR._errCodeMap[this._sender.status]);
                    }
                }
                delete this._sender;
                this._sender = null;
            }
        } catch(err) {
            rt.error("unknow exception in MUSIC.XHR.prototype.send()");
        }
    });
    this._sender.send(d);
    return true;
};
MUSIC.XHR.prototype.destroy = function() {
    var n = this._name;
    delete MUSIC.XHR.instance[n]._sender;
    MUSIC.XHR.instance[n]._sender = null;
    delete MUSIC.XHR.instance[n];
    MUSIC.XHR.counter--;
    return null;
};

MUSIC.console = {_inited:false,_html:'<h5 id="log_head" class="QMFL_log_head"><input type=button id="log_close" value="xconsole"/></h5><ul id="log_list"></ul><div class="QMFL_log_foot"><div class="log_console">&gt;<input id="log_console"/></div></div>',_opened:false,TYPE:{DEBUG:0,ERROR:1,WARNING:2,INFO:3,PROFILE:4},_typeInfo:[
    ["QMFL_log_debug","?"],
    ["QMFL_log_error","!"],
    ["QMFL_log_warning","-"],
    ["QMFL_log_info","i"],
    ["QMFL_log_profile","?"]
],show:function() {
    if (!this._inited) {
        this._init();
    }
    showElement(this._main);
    this._opened = true;
},hide:function() {
    hideElement(MUSIC.console._main);
    MUSIC.console._opened = false;
},_init:function() {
    this._main = MUSIC.dom.createElementIn("div", document.body);
    this._main.className = "QMFL_log";
    this._main.innerHTML = this._html;
    this._input = MUSIC.dom.get("log_console");
    this._button = MUSIC.dom.get("log_close");
    this._list = MUSIC.dom.get("log_list");
    MUSIC.css.insertCSSLink("http://imgcache.qq.com/music/QMFL/example/css/console.css");
    if (MUSIC.dragdrop) {
        MUSIC.dragdrop.registerDragdropHandler(MUSIC.dom.get("log_head"), this._main);
    }
    MUSIC.event.addEvent(this._input, "keypress", this._execScript);
    MUSIC.event.addEvent(this._button, "click", this.hide);
    this._inited = true;
},print:function(msg, type) {
    if (!this._opened) {
        this.show();
    }
    var _item = MUSIC.dom.createElementIn("li", MUSIC.console._list);
    var _ti = MUSIC.console._typeInfo[type] || MUSIC.console._typeInfo[0];
    _item.className = _ti[0];
    _item.innerHTML = '<span class="log_icon">' + _ti[1] + '</span>' + msg;
    this._list.scrollTop = this._list.scrollHeight;
},clear:function() {
    MUSIC.console._list.innerHTML = "";
},_execScript:function(e) {
    e = MUSIC.event.getEvent(e);
    if (e.keyCode != "13") {
        return;
    }
    switch (MUSIC.console._input.value) {case"help":var _rv = "Console Help<br/>help - console help<br/>clear - clear console list.<br/>hide - hide console"
        MUSIC.console.print(_rv, 3);break;case"clear":MUSIC.console.clear();break;case"hide":MUSIC.console.hide();break;default:var _rv = '<span style="color:#CCFF00">' + MUSIC.console._input.value + '</span><br/>';try {
        _rv += (eval(MUSIC.console._input.value) || "").toString().replace(/</g, "&lt;").replace(/>/g, "&gt;")
        MUSIC.console.print(_rv, 0);
    } catch(ex) {
        _rv += ex.description;
        MUSIC.console.print(_rv, 1);
    }
    }
    MUSIC.console._input.value = "";
}}

MUSIC.cookie = {set:function(name, value, domain, path, hour) {
    if (hour) {
        var today = new Date();
        var expire = new Date();
        expire.setTime(today.getTime() + 3600000 * hour);
    }
    document.cookie = name
            + "="
            + value
            + "; "
            + (hour ? ("expires=" + expire.toGMTString() + "; ") : "")
            + (path ? ("path=" + path + "; ") : "path=/; ")
            + (domain ? ("domain=" + domain + ";") : ("domain="
            + MUSIC.config.DCCookieDomain + ";"));
    return true;
},get:function(name) {
    var r = new RegExp("(?:^|;+|\\s+)" + name + "=([^;]*)");
    var m = document.cookie.match(r);
    return(!m ? "" : m[1]);
},del:function(name, domain, path) {
    document.cookie = name
            + "=; expires=Mon, 26 Jul 1997 05:00:00 GMT; "
            + (path ? ("path=" + path + "; ") : "path=/; ")
            + (domain ? ("domain=" + domain + ";") : ("domain="
            + MUSIC.config.DCCookieDomain + ";"));
}};
window.Cookie = MUSIC.cookie;

MUSIC.dataCenter = (function() {
    var keyPool = {};
    var dataPool = [];

    function _mSave(k, v) {
        dataPool[k] = v;
        return true;
    }

    function _sSave(k, v) {
        var o = MUSIC.shareObject.getValidSO();
        if (o) {
            return o.set("_dc_so_" + k, v);
        } else {
            rt.error("DataCenter.save: Can't find usable shareObject!");
            return false;
        }
    }

    function _cSave(k, v) {
        var d = MUSIC.config.DCCookieDomain;
        if (d) {
            return o.set("_dc_co_" + k, v, d, "/", 120);
        } else {
            rt.error("DataCenter.save: Can't find cookie domain!");
            return false;
        }
    }

    function getData(key, level) {
        var res,tmp;
        switch (level) {case"memory":res = dataPool[key];break;case"soflash":{
            tmp = MUSIC.shareObject.getValidSO();
            if (tmp) {
                res = tmp.get("_dc_so_" + key);
            } else
                tmp = null;
            break;
        }
            case"cookie":{
                tmp = MUSIC.cookie;
                if (tmp) {
                    res = tmp.get("_dc_co_" + key);
                } else
                    tmp = null;
                break;
            }
            default:tmp = MUSIC.shareObject.getValidSO();if (tmp) {
                res = tmp.get("_dc_so_" + key);
            } else
                tmp = null;break;
        }
        return res;
    }

    function deleteData(key, level) {
        switch (level) {case"memory":delete dataPool[key];break;case"soflash":{
            tmp = MUSIC.shareObject.getValidSO();
            if (tmp) {
                res = tmp.del("_dc_so_" + key);
            }
            break;
        }
            case"cookie":{
                tmp = MUSIC.cookie;
                if (tmp) {
                    res = tmp.del("_dc_co_" + key, MUSIC.config.DCCookieDomain, "/");
                }
                break;
            }
            default:tmp = MUSIC.shareObject.getValidSO();if (tmp) {
                res = tmp.del("_dc_so_" + key);
            }
                break;
        }
        return true;
    }

    ;
    function saveData(key, value, level) {
        level = level || "soflash";
        if (arguments.length < 2 || typeof(arguments[0]) != 'string') {
            throw(new Error("???????:\nkeyName{String}:value{String/Object}"));
            return false;
        }
        switch (level) {case"memory":return _mSave(key, value);case"soflash":return _sSave(key, value);case"cookie":return _cSave(key, value);default:return _sSave(key, value);
        }
        return false;
    }

    function getDataSize(key, level) {
        var res,tmp;
        switch (level) {case"memory":break;case"soflash":{
            tmp = MUSIC.shareObject.getValidSO();
            if (tmp) {
                res = MUSIC.shareObject.getSize("_dc_so_" + key);
            } else
                tmp = -1;
            break;
        }
            case"cookie":{
                break;
            }
            default:tmp = MUSIC.shareObject.getValidSO();if (tmp) {
                res = MUSIC.shareObject.getSize("_dc_so_" + key);
            } else
                tmp = -1;break;
        }
        return res;
    }

    return{save:saveData,get:getData,del:deleteData,getSize:getDataSize};
})();

MUSIC.debug = {errorLogs:[],startDebug:function() {
    window.onerror = function(msg, url, line) {
        var urls = (url || "").replace(/\\/g, "/").split("/");
        MUSIC.console.print(msg + "<br/>" + urls[urls.length - 1]
                + " (line:" + line + ")", 1);
        MUSIC.debug.errorLogs.push(msg);
        return false;
    }
    return true;
},stopDebug:function() {
    window.onerror = null;
},clearErrorLog:function() {
    this.errorLogs = [];
},showLog:function() {
    var o = ENV.get("debug_out");
    if (!!o) {
        o.innerHTML = nl2br(escHTML(this.errorLogs.join("\n")));
    }
},getLogString:function() {
    return(this.errorLogs.join("\n"));
},init:function() {
    return MUSIC._debugMode ? this.startDebug() : false;
}};
MUSIC.runTime = (function() {
    function isDebugMode() {
        return MUSIC.enviroment.get("debug");
    }

    function log(msg, type) {
        var info;
        if (isDebugMode()) {
            info = msg + '\n=STACK=\n' + stack();
        } else {
            if (type == 'error') {
                info = msg;
            } else if (type == 'warn') {
            }
        }
        MUSIC.debug.errorLogs.push(info);
    }

    function warn(sf, args) {
        log(write.apply(null, arguments), 'warn');
    }

    function error(sf, args) {
        log(write.apply(null, arguments), 'error');
    }

    function stack(e, a) {
        function genTrace(ee, aa) {
            if (ee.stack) {
                return ee.stack;
            } else if (ee.message.indexOf("\nBacktrace:\n") >= 0) {
                var cnt = 0;
                return ee.message.split("\nBacktrace:\n")[1].replace(/\s*\n\s*/g, function() {
                    cnt++;
                    return(cnt % 2 == 0) ? "\n" : " @ ";
                });
            } else {
                var entry = (aa.callee == stack) ? aa.callee.caller : aa.callee;
                var eas = entry.arguments;
                var r = [];
                for (var i = 0,len = eas.length; i < len; i++) {
                    r.push((typeof eas[i] == 'undefined') ? ("<u>") : ((eas[i] === null) ? ("<n>") : (eas[i])));
                }
                var fnp = /function\s+([^\s\(]+)\(/;
                var fname = fnp.test(entry.toString()) ? (fnp.exec(entry.toString())[1]) : ("<ANON>");
                return(fname + "(" + r.join() + ");").replace(/\n/g, "");
            }
        }

        var res;
        if ((e instanceof Error) && (typeof arguments == 'object') && (!!arguments.callee)) {
            res = genTrace(e, a);
        } else {
            try {
                ({}).sds();
            } catch(err) {
                res = genTrace(err, arguments);
            }
        }
        return res.replace(/\n/g, " <= ");
    }

    return{stack:stack,warn:warn,error:error};
})();
var rt = MUSIC.runTime;
MUSIC.debug.init();

MUSIC.report = {_queue:[],_timer:null,_poster:[],_rules:{},time:10000,receive:function(source, status, url, time) {
    if (!status) {
        MUSIC.console.print("receive data error.");
        return;
    }
    var uri = new URI(url);
    var path = "http://" + uri.host + uri.pathname;
    if (this._rules[path]) {
        MUSIC.console.print("[" + source + "] report data receive!" + " status:" + status, 3);
        this._queue.push({source:source,status:status,fullurl:url,url:path,time:(time || 0)});
        this._postDelay();
    }
},addRule:function(url, reportUrl) {
    this._rules[url] = {reportUrl:reportUrl};
},_postDelay:function() {
    clearTimeout(this._timer);
    this._timer = setTimeout(function() {
        MUSIC.report.post.call(MUSIC.report)
    }, this.time);
},post:function() {
    var _request;
    while (_request = this._queue.shift()) {
        MUSIC.console.print(this._queue.length, 3);
        var _u = this._rules[_request.url] ? this._rules[_request.url].reportUrl : "";
        if (!_u) {
            continue;
        }
        ;
        var percent = _request.status > 1 ? 100 : 0.01;
        if (percent / 100 >= Math.random()) {
            _u = _u.replace(/%status%/g, _request.status).replace(/%scale%/g, (100 / percent)).replace(/%percent%/g, percent).replace(/%url%/g, _request.url).replace(/%time%/g, _request.time).replace(/%fullUrl%/g, _request.fullurl).replace(/%source%/g, _request.source);
            MUSIC.console.print(_u);
            var i = new Image();
            i.src = _u;
            this._poster.push(i);
        }
    }
}}

MUSIC.dialog = {items:[],lastFocus:null,tween:false,_infoid:-1,_timeoutInfoBox:[],createInfoBox:function(content, timeout, st, top, left) {
    var node;
    st = st || 1;
    if (st == 1) {
        var env = MUSIC.event.getEvent();
        var _t = 200;
        var _l = 300;
        try {
            _t = env.clientY - 60 + MUSIC.dom.getScrollTop();
            _l = (env.clientX - 80);
        } catch(e) {
        }
        node = MUSIC.dom.getInBody("tips_em" + (++this._infoid), "div", null, null, "tips_em", "top:" + (top || _t) + "px;left:"
                + (left || _l)
                + "px;z-index:9999;position:absolute");
        node.innerHTML = content;
    } else if (st == 2) {
        var _t = 45;
        var _l = MUSIC.dom.getClientWidth() / 2 - 200;
        node = MUSIC.dom.getInBody("tips_em" + (++this._infoid), "div", null, null, "tips_str", "top:" + (top || _t) + "px;left:"
                + (left || _l)
                + "px;z-index:9999;position:absolute");
        node.innerHTML = '<div class="tips_str_con"><div class="tips_text">'
                + content + "</div></div>";
    } else
        return;
    timeout = timeout || 0.5;
    this._timeoutInfoBox.push(setTimeout("MUSIC.dialog.removeInfoBox("
            + this._infoid + ")", timeout * 1000));
    return this._infoid;
},removeInfoBox:function(id) {
    $("tips_em" + id) && removeNode($("tips_em" + id));
    this._timeoutInfoBox[id] && clearTimeout(this._timeoutInfoBox[id]);
},create:function(title, content, width, height, info) {
    var _i = this.items;
    _i.push(new MUSIC.DialogHandler(_i.length, false));
    var dialog = _i[_i.length - 1];
    dialog.init(width || 300, height || 200);
    dialog.fillTitle(title || "???");
    dialog.fillImg(info || 1);
    dialog.fillContent(content || "");
    return dialog;
},createBorderNone:function(content, width, height, timeout) {
    var _i = this.items;
    var dialog;
    _i.push(dialog = (new MUSIC.DialogHandler(_i.length, true)));
    dialog.init(width || 300, height || 200, true, timeout);
    dialog.fillContent(content || "");
    return dialog;
}};
MUSIC.DialogHandler = function(id, isNoBorder) {
    this._id = id;
    this._isIE6 = (MUSIC.userAgent.ie && MUSIC.userAgent.ie < 7);
    this.id = "dialog_" + id;
    this.mainId = "dialog_main_" + id;
    this.headId = "dialog_head_" + id;
    this.titleId = "dialog_title_" + id;
    this.imgId = "dialog_img_" + id;
    this.closeId = "dialog_button_" + id;
    this.contentId = "dialog_content_" + id;
    this.frameId = "dialog_frame_" + id;
    this.btnOk = "btnok_" + id;
    this.btnCancle = "btncancle_" + id;
    this.useTween = MUSIC.dialog.tween,this.zIndex = 6000 + this._id;
    this.iconClass = "none";
    this.onBeforeUnload = function() {
        return true;
    };
    this.onOkBtn = function() {
        return true;
    };
    this.onCancleBtn = function() {
        return true;
    };
    this.onUnload = MUSIC.emptyFn;
    this.isFocus = false;
    var _t = ['<div id="',this.mainId,'" class="',(isNoBorder ? "" : "tips_content"),'">','<h3 id="',this.headId,'" class="',(isNoBorder ? "none" : "tips_title"),'">SOSO?????','</h3>','<a id="',this.closeId,'" title="??" class="bt_tipsclose" href="javascript:;">??</a>','<div class="tips_con"><span class="warn_obj" id="',this.imgId,'"></span>','<h3 class="title" id="',this.titleId,'"></h3>','<div class="info" id="' + this.contentId
            + '" style="display:none;"></div></div>','<div class="bt_con">','<a class="bt_obj" href="javascript:;"><button type="button" id="',this.btnCancle,'" title="??">??</button></a>','<a class="bt_em" href="javascript:;"><button type="button" id="',this.btnOk,'" title="??">??</button></a>','</div>','</div>'];
    this.temlate = _t.join("");
};
MUSIC.DialogHandler.prototype.init = function(width, height, isNoneBerder, iCloseAutoTime) {
    this.dialog = document.createElement("div");
    this.dialog.id = this.id;
    var _l = (MUSIC.dom.getClientWidth() - width) / 2
            + MUSIC.dom.getScrollLeft();
    var _t = Math.max((MUSIC.dom.getClientHeight() - height) / 2
            + MUSIC.dom.getScrollTop(), 0);
    with (this.dialog) {
        className = "tipbox";
        style.zIndex = this.zIndex;
        innerHTML = this.temlate;
    }
    document.body.appendChild(this.dialog);
    this.dialogClose = MUSIC.dom.get(this.closeId);
    var o = this;
    MUSIC.event.addEvent(this.dialog, "mousedown", MUSIC.event.bind(o, o.focus));
    MUSIC.event.addEvent(this.dialogClose, "click", function() {
        MUSIC.dialog.items[o._id].unload();
    })
    if (!!iCloseAutoTime) {
        setTimeout("for(var it in MUSIC.dialog.items)MUSIC.dialog.items[it].unload()", iCloseAutoTime);
    }
    this.btnOkObj = MUSIC.dom.get(this.btnOk);
    MUSIC.event.addEvent(this.btnOkObj, "click", function() {
        return o.onOkBtn();
    });
    this.btnCancleObj = MUSIC.dom.get(this.btnCancle);
    MUSIC.event.addEvent(this.btnCancleObj, "click", function() {
        return o.onCancleBtn();
    });
    if (MUSIC.dragdrop) {
        MUSIC.dragdrop.registerDragdropHandler(MUSIC.dom.get(this.headId), MUSIC.dom.get(this.id), {range:[0,null,null,null],ghost:0});
    }
    this.focus();
    this.setSize(width, height);
    if (this.useTween && MUSIC.Tween) {
        MUSIC.dom.setStyle(this.dialog, "opacity", 0);
        var tween1 = new MUSIC.Tween(this.dialog, "top", MUSIC.transitions.regularEaseIn, _t - 30 + "px", _t + "px", 0.3);
        tween1.onMotionChange = function() {
            MUSIC.dom.setStyle(o.dialog, "opacity", this.getPercent() / 100);
        }
        tween1.onMotionStop = function() {
            MUSIC.dom.setStyle(o.dialog, "opacity", 1);
            tween1 = null;
        }
        tween1.start();
    } else {
    }
};
MUSIC.DialogHandler.prototype.focus = function(title) {
    if (this.isFocus) {
        return;
    }
    this.dialog.style.zIndex = this.zIndex + 3000;
    if (MUSIC.dialog.lastFocus) {
        MUSIC.dialog.lastFocus.blur();
    }
    ;
    this.isFocus = true;
    MUSIC.dialog.lastFocus = this;
};
MUSIC.DialogHandler.prototype.blur = function(title) {
    this.isFocus = false;
    this.dialog.style.zIndex = this.zIndex;
};
MUSIC.DialogHandler.prototype.getZIndex = function() {
    return this.dialog.style.zIndex;
};
MUSIC.DialogHandler.prototype.fillTitle = function(title) {
    var _t = MUSIC.dom.get(this.titleId);
    _t.innerHTML = title;
};
MUSIC.DialogHandler.prototype.fillImg = function(info) {
    var _t = MUSIC.dom.get(this.imgId);
    var infoType = "";
    switch (info) {case 1:infoType = "warn_obj";break;case 2:infoType = "succ_obj";break;case 3:infoType = "error_obj";break;default:;break;
    }
    _t.className = infoType;
};
MUSIC.DialogHandler.prototype.fillContent = function(html, info) {
    if (!html)
        return;
    var _c = MUSIC.dom.get(this.contentId);
    _c.innerHTML = "<p>" + html + "</p>";
    showElement(_c);
};
MUSIC.DialogHandler.prototype.setSize = function(width, height) {
    var _m = MUSIC.dom.get(this.id);
    var _c = MUSIC.dom.get(this.contentId);
    height = height - 28 < 0 ? 50 : height - 28;
    _m.style.width = width + "px";
    _c.style[MUSIC.userAgent.ie < 7 ? "height" : "minHeight"] = height + "px";
    if (this._isIE6) {
        var _s = MUSIC.dom.getSize(MUSIC.dom.get(this.mainId));
        var _f = MUSIC.dom.get(this.frameId);
        MUSIC.dom.setSize(_f, _s[0], _s[1]);
    }
};
MUSIC.DialogHandler.prototype.unload = function() {
    if (!this.onBeforeUnload()) {
        return;
    }
    ;
    var o = this;
    if (this.useTween && MUSIC.Tween) {
        var tween1 = new MUSIC.Tween(this.dialog, "opacity", MUSIC.transitions.regularEaseIn, 1, 0, 0.2);
        tween1.onMotionStop = function() {
            o._unload();
            tween1 = null;
        };
        tween1.start();
    } else {
        this._unload();
    }
    ;
};
MUSIC.DialogHandler.prototype._unload = function() {
    this.onUnload();
    if (MUSIC.dragdrop) {
        MUSIC.dragdrop.unRegisterDragdropHandler(MUSIC.dom.get(this.headId));
    }
    MUSIC.dom.removeElement(this.dialog);
    delete MUSIC.dialog.items[this._id];
};

MUSIC.enviroment = (function() {
    var _p = {};
    var hookPool = {};

    function envGet(kname) {
        return _p[kname];
    }

    function envDel(kname) {
        delete _p[kname];
        return true;
    }

    function envSet(kname, value) {
        if (typeof value == 'undefined') {
            if (typeof kname == 'undefined') {
                return false;
            } else if (!(_p[kname] === undefined)) {
                MUSIC.runTime.warn("Do you want to set env var {0:q} to 'undefined'", kname);
                return false;
            }
        } else {
            _p[kname] = value;
            return true;
        }
    }

    return{get:envGet,set:envSet,del:envDel,hookPool:hookPool};
})();
var ENV = MUSIC.enviroment;
MUSIC.pageEvents = (function() {
    function _ihp() {
        var qs = location.search.substring(1);
        var qh = location.hash.substring(1);
        ENV.set("_queryString", qs);
        ENV.set("_queryHash", qh);
        ENV.set("queryString", splitHttpParamString(qs));
        ENV.set("queryHash", splitHttpParamString(qh));
    }

    function _bootStrap() {
        if (document.addEventListener) {
            if (ua.safari) {
                var interval = setInterval(function() {
                    if ((/loaded|complete/).test(document.readyState)) {
                        _onloadHook();
                        clearInterval(interval);
                    }
                }, 50);
            } else {
                document.addEventListener("DOMContentLoaded", _onloadHook, true);
            }
        } else {
            var src = 'javascript:void(0)';
            if (window.location.protocol == 'https:') {
                src = '//:';
            }
            document.write('<script onreadystatechange="if(this.readyState==\'complete\'){this.parentNode.removeChild(this);MUSIC.pageEvents._onloadHook();}" defer="defer" src="' + src + '"><\/script\>');
        }
        window.onload = MUSIC.lang.chain(window.onload, function() {
            _onloadHook();
            _runHooks('onafterloadhooks');
        });
        window.onbeforeunload = function() {
            return _runHooks('onbeforeunloadhooks');
        };
        window.onunload = MUSIC.lang.chain(window.onunload, function() {
            _runHooks('onunloadhooks');
        });
    }

    function _onloadHook() {
        _runHooks('onloadhooks');
        window.loaded = true;
    }

    function _runHook(handler) {
        try {
            handler();
        } catch(ex) {
            rt.error('Uncaught exception in hook (run after page load): {0}', ex);
        }
    }

    function _runHooks(hooks) {
        var isbeforeunload = (hooks == 'onbeforeunloadhooks');
        var warn = null;
        var hc = window.ENV.hookPool;
        do{
            var h = hc[hooks];
            if (!isbeforeunload) {
                hc[hooks] = null;
            }
            if (!h) {
                break;
            }
            for (var ii = 0; ii < h.length; ii++) {
                if (isbeforeunload) {
                    warn = warn || h[ii]();
                } else {
                    h[ii]();
                }
            }
            if (isbeforeunload) {
                break;
            }
        } while (hc[hooks]);
        if (isbeforeunload) {
            if (warn) {
                return warn;
            } else {
                window.loaded = false;
            }
        }
    }

    function _addHook(hooks, handler) {
        var c = window.ENV.hookPool;
        (c[hooks] ? c[hooks] : (c[hooks] = [])).push(handler);
    }

    function _insertHook(hooks, handler, position) {
        var c = window.ENV.hookPool;
        if (typeof(position) == 'number' && position >= 0 && c[hooks]) {
            c[hooks].splice(position, 0, handler);
        } else {
            return false;
        }
    }

    function _lr(handler) {
        window.loaded ? _runHook(handler) : _addHook('onloadhooks', handler);
    }

    function _bulr(handler) {
        _addHook('onbeforeunloadhooks', handler);
    }

    function _ulr(handler) {
        _addHook('onunloadhooks', handler);
    }

    function pinit() {
        _bootStrap();
        _ihp();
        ua.adjustBehaviors();
        var _dt = $("__DEBUG_out");
        if (_dt) {
            ENV.set("dout", _dt);
        }
        var __dalert;
        if (!ENV.get("alertConverted")) {
            __dalert = alert;
            eval('var alert=function(msg){if(msg!=undefined){__dalert(msg);return msg;}}');
            ENV.set("alertConverted", true);
        }
    }

    return{onloadRegister:_lr,onbeforeunloadRegister:_bulr,onunloadRegister:_ulr,initHttpParams:_ihp,bootstrapEventHandlers:_bootStrap,_onloadHook:_onloadHook,insertHooktoHooksQueue:_insertHook,pageBaseInit:pinit};
})();

MUSIC.JsLoader = function() {
    this.loaded = false;
    this.debug = true;
    this.onload = MUSIC.emptyFn;
    this.onerror = MUSIC.emptyFn;
}
MUSIC.JsLoader.scriptId = 1;
MUSIC.JsLoader.prototype.load = function(src, doc, charset) {
    var sId = MUSIC.JsLoader.scriptId;
    MUSIC.JsLoader.scriptId++;
    var o = this;
    setTimeout(function() {
        o._load2.apply(o, [sId,src,doc,charset]);
        o = null;
    }, 0);
}
MUSIC.JsLoader.prototype._load2 = function(sId, src, doc, charset) {
    _doc = doc || document;
    charset = charset || "gb2312";
    var _ie = MUSIC.userAgent.ie;
    var _js = _doc.createElement("script");
    MUSIC.event.addEvent(_js, (_ie ? "readystatechange" : "load"), (function(o) {
        if (_ie) {
            return(function() {
                if (/(complete|loaded)/.test(_js.readyState)) {
                    o.onload();
                    if (!o.debug) {
                        MUSIC.dom.removeElement(_js);
                    }
                    _js = null;
                }
            });
        } else {
            return(function() {
                o.onload();
                if (!o.debug) {
                    MUSIC.dom.removeElement(_js);
                }
                _js = null;
            });
        }
    })(this));
    if (!_ie) {
        MUSIC.event.addEvent(_js, (_ie ? "readystatechange" : "load"), (function(o) {
            return(function() {
                o.onerror();
                if (!o.debug) {
                    MUSIC.dom.removeElement(_js);
                }
                _js = null;
            });
        })(this));
    }
    _js.id = "js_" + sId;
    _js.defer = true;
    _js.charset = charset;
    _js.src = src;
    _doc.getElementsByTagName("head")[0].appendChild(_js);
}
MUSIC["js" + "Loader"] = MUSIC.JsLoader;

MUSIC.FormSender = function(actionURL, method, data, charset) {
    if (!isURL(actionURL)) {
        rt.error("error actionURL -> {0:Q} in MUSIC.FormSender construct!", actionURL);
        return null;
    }
    this.name = "_fpInstence_" + MUSIC.FormSender.counter;
    MUSIC.FormSender.instance[this.name] = this;
    MUSIC.FormSender.counter++;
    this.method = method || "POST";
    this.uri = actionURL;
    this.data = (isHashMap(data) || typeof(data) == 'string') ? data : null;
    this.proxyURL = (typeof(charset) == 'string' && charset.toUpperCase() == "UTF-8") ? MUSIC.config.FSHelperPage.replace(/_gbk/, "_utf8") : MUSIC.config.FSHelperPage;
    this._sender = null;
    this.onSuccess = MUSIC.emptyFn;
    this.onError = MUSIC.emptyFn;
};
MUSIC.FormSender.instance = {};
MUSIC.FormSender.counter = 0;
MUSIC.FormSender._errCodeMap = {999:{msg:'Connection or Server error'}};
MUSIC.FormSender.prototype.send = function() {
    if (this.method == 'POST' && this.data == null) {
        rt.warn("MUSIC.FormSender -> {0:q}, can't send data 'null'!", this.name);
        return false;
    }
    function clear(o) {
        o._sender = o._sender.callback = o._sender.errorCallback = o._sender.onreadystatechange = null;
        if (ua.safari || ua.opera) {
            setTimeout('removeNode($("_fp_frm_' + o.name + '"))', 50);
        } else {
            removeNode($("_fp_frm_" + o.name));
        }
    }

    if (this._sender === null || this._sender === void(0)) {
        var sender = document.createElement("iframe");
        sender.id = "_fp_frm_" + this.name;
        sender.style.width = sender.style.height = sender.style.borderWidth = "0";
        document.body.appendChild(sender);
        sender.callback = MUSIC.event.bind(this, function(o) {
            clearInterval(interval);
            clear(this);
            this.onSuccess(o);
        });
        sender.errorCallback = MUSIC.event.bind(this, function(o) {
            clearInterval(interval);
            clear(this);
            this.onError(o);
        });
        if (typeof sender.onreadystatechange != 'undefined') {
            sender.onreadystatechange = MUSIC.event.bind(this, function() {
                if (this._sender.readyState == 'complete' && this._sender.submited) {
                    clear(this);
                    this.onError(MUSIC.FormSender._errCodeMap[999]);
                }
            });
        }
        else {
            var interval = setInterval(MUSIC.event.bind(this, function() {
                try {
                    var _t = this._sender.contentWindow.location.href;
                    if (_t.indexOf(this.uri) == 0) {
                        clear(this);
                        this.onError(MUSIC.FormSender._errCodeMap[999]);
                        clearInterval(interval);
                    }
                } catch(err) {
                    clear(this);
                    this.onError(MUSIC.FormSender._errCodeMap[999]);
                    clearInterval(interval);
                }
            }), 100);
        }
        this._sender = sender;
    }
    this._sender.src = this.proxyURL;
    return true;
};
MUSIC.FormSender.prototype.destroy = function() {
    var n = this.name;
    delete MUSIC.FormSender.instance[n]._sender;
    MUSIC.FormSender.instance[n]._sender = null;
    delete MUSIC.FormSender.instance[n];
    MUSIC.FormSender.counter--;
    return null;
};

MUSIC.JSONGetter = function(actionURL, cname, data, charset, junctionMode) {
    if (!isString(cname)) {
        cname = "_jsonInstence_" + (MUSIC.JSONGetter.counter + 1);
    }
    var prot;
    if (MUSIC.JSONGetter.instance[cname]instanceof MUSIC.JSONGetter) {
        prot = MUSIC.JSONGetter.instance[cname];
    } else {
        prot = (MUSIC.JSONGetter.instance[cname] = this);
        MUSIC.JSONGetter.counter++;
    }
    prot._name = cname;
    prot._uri = actionURL;
    prot._data = (isHashMap(data) || typeof(data) == 'string') ? data : null;
    prot._sender = null;
    prot._charset = (typeof charset != 'string') ? MUSIC.config.defaultDataCharacterSet : charset;
    prot._jMode = !!junctionMode;
    prot._timer = null;
    this.onSuccess = MUSIC.emptyFn;
    this.onError = MUSIC.emptyFn;
    this.onTimeout = MUSIC.emptyFn;
    this.timeout = 5000;
    return prot;
};
MUSIC.JSONGetter.instance = {};
MUSIC.JSONGetter.counter = 0;
MUSIC.JSONGetter._errCodeMap = {999:{msg:'Connection or Server error.'},998:{msg:'Connection to Server timeout.'}};
MUSIC.JSONGetter.prototype.send = function(callbackFnName) {
    var cfn = (typeof callbackFnName != 'string') ? "MusicJsonCallback" : callbackFnName;
    var clear;
    var da = this._uri
            + (this._data ? ("?" + genHttpParamString(this._data)) : "");
    var _s = new Date();
    if (this._jMode) {
        window[cfn] = this.onSuccess;
        var _sd = new MUSIC.JsLoader();
        _sd.onerror = this.onError;
        _sd.load(da, void(0), this._charset);
        return;
    }
    this._timer = setTimeout(MUSIC.event.bind(this, function() {
        MUSIC.console.print("jsonGetter timeout", 3);
        MUSIC.report.receive("MUSIC.JSONGetter", 4, this._uri, (new Date()) - _s);
    }), this.timeout);
    if (ua.ie && ua.ie < 8) {
        var df = document.createDocumentFragment();
        var sender = df.createElement("script");
        sender.charset = this._charset;
        this._senderDoc = df;
        this._sender = sender;
        clear = function(o) {
            clearTimeout(o._timer);
            if (o._sender) {
                o._sender.onreadystatechange = null;
            }
            o._senderDoc = o._sender = null;
        };
        df[cfn] = MUSIC.event.bind(this, function(o) {
            this.onSuccess(o);
            MUSIC.report.receive("MUSIC.JSONGetter", 1, this._uri, (new Date()) - _s);
            clear(this);
        });
        sender.onreadystatechange = MUSIC.event.bind(this, function() {
            if (this._sender && this._sender.readyState == "loaded") {
                try {
                    this.onError(MUSIC.JSONGetter._errCodeMap[999]);
                    MUSIC.report.receive("MUSIC.JSONGetter", 2, this._uri, (new Date()) - _s);
                    clear(this);
                } catch(ignore) {
                }
            }
        });
        this._sender.src = da;
        df.appendChild(sender);
    } else {
        clear = function(o) {
            clearTimeout(o._timer);
            if (!ua.ie) {
                o._sender.src = "about:blank";
                o._sender = o._sender.callback = o._sender.errorCallback = null;
                if (ua.safari || ua.opera) {
                    setTimeout('removeNode($("_JSON_frm_' + o._name + '"))', 50);
                } else {
                    removeNode($("_JSON_frm_" + o._name));
                }
            } else {
                _hf.parentWindow["errorCallback"] = MUSIC.emptyFn;
                _hf = null;
            }
        };
        var _cb = MUSIC.event.bind(this, function(o) {
            this.onSuccess(o);
            MUSIC.report.receive("MUSIC.JSONGetter", 1, this._uri, (new Date()) - _s);
            clear(this);
        });
        var _ecb = MUSIC.event.bind(this, function() {
            this.onError(MUSIC.JSONGetter._errCodeMap[999]);
            MUSIC.report.receive("MUSIC.JSONGetter", 2, this._uri, (new Date()) - _s);
            clear(this);
        });
        if (ua.ie) {
            var _hf = new ActiveXObject("htmlfile");
            _hf.open();
            _hf.parentWindow[cfn] = function(o) {
                _cb(objectClone(o));
            };
            _hf.parentWindow["errorCallback"] = _ecb;
            _hf.write("<script src=\""
                    + da
                    + "\" charset=\""
                    + this._charset
                    + "\"><\/script><script defer>setTimeout(\"errorCallback()\",0)<\/script>");
            if (_hf) {
                _hf.close();
            }
        } else {
            var frm = document.createElement("iframe");
            frm.id = "_JSON_frm_" + this._name;
            frm.style.width = frm.style.height = frm.style.borderWidth = "0";
            this._sender = frm;
            var dout = '<html><head><meta http-equiv="Content-type" content="text/html; charset='
                    + this._charset
                    + '" /></head><body><script>document.domain="'
                    + document.domain
                    + '";function '
                    + cfn
                    + '(o){frameElement.callback(o);}<\/script><script src="'
                    + da
                    + '" charset="'
                    + this._charset
                    + '"><\/script><script>setTimeout(frameElement.errorCallback,50);<\/script></body></html>';
            frm.callback = _cb;
            frm.errorCallback = _ecb;
            if (ua.opera) {
                frm.src = "javascript:'" + dout + "'";
                document.body.appendChild(frm);
            } else {
                document.body.appendChild(frm);
                frm.contentWindow.document.open('text/html');
                frm.contentWindow.document.write(dout);
                frm.contentWindow.document.close();
            }
        }
    }
};
MUSIC.JSONGetter.prototype.destroy = function() {
    var n = this._name;
    delete MUSIC.JSONGetter.instance[n]._sender;
    MUSIC.JSONGetter.instance[n]._sender = null;
    delete MUSIC.JSONGetter.instance[n];
    MUSIC.JSONGetter.counter--;
    return null;
};
function JsonLoadData(url, callback, errcallback, callbackFunctionName, charset, callBackParameters) {
    var j = new MUSIC.JSONGetter(url, callbackFunctionName, null, charset, true);
    j.onSuccess = callback;
    j.send(callbackFunctionName);
}

MUSIC.maskLayout = {count:0,items:{},create:function(zindex, _doc) {
    this.count++;
    zindex = zindex || 5000;
    _doc = _doc || document;
    var _m = MUSIC.dom.createElementIn("div", _doc.body, false, {className:"tipsout"});
    var _h = Math.max(_doc.documentElement.scrollHeight, _doc.body.scrollHeight);
    _m.style.zIndex = zindex;
    _m.style.height = _h + "px";
    this.items[this.count] = _m;
    return this.count;
},remove:function(countId) {
    MUSIC.dom.removeElement(this.items[countId]);
    delete this.items[countId];
}};

MUSIC.shareObject = {};
MUSIC.shareObject.create = function(path) {
    if (typeof(path) == 'undefined') {
        path = MUSIC.config.defaultShareObject;
    }
    var t = new MUSIC.shareObject.DataBase(path);
};
MUSIC.shareObject.instance = {};
MUSIC.shareObject.refCount = 0;
MUSIC.shareObject.getValidSO = function() {
    var cnt = MUSIC.shareObject.refCount + 1;
    for (var i = 1; i < cnt; ++i) {
        if (MUSIC.shareObject.instance["so_" + i] && MUSIC.shareObject.instance["so_" + i]._ready) {
            return MUSIC.shareObject.instance["so_" + i];
        }
    }
    return null;
};
MUSIC.shareObject.getSize = function(s) {
    var o = MUSIC.shareObject.getValidSO();
    if (o)return o.getDataSize(s); else return-1;
};
MUSIC.shareObject.get = function(s) {
    var o = MUSIC.shareObject.getValidSO();
    if (o)return o.get(s); else return void(0);
};
MUSIC.shareObject.set = function(k, v) {
    var o = MUSIC.shareObject.getValidSO();
    if (o)return o.set(k, v); else return false;
};
MUSIC.shareObject.DataBase = function(soUrl) {
    if (MUSIC.shareObject.refCount > 0) {
        return MUSIC.shareObject.instance["so_1"];
    }
    var fv = MUSIC.media.getFlashVersion();
    if (fv.toNumber() < 8) {
        rt.error("flash player version is too low to build a shareObject!");
        return null;
    }
    this._ready = false;
    MUSIC.shareObject.refCount++;
    var c = document.createElement("div");
    c.style.marginTop = "-1px";
    document.body.appendChild(c);
    c.innerHTML = insertFlash({src:soUrl,id:"__so" + MUSIC.shareObject.refCount,width:0,height:0,allowscriptaccess:"always"});
    this.ele = $("__so" + MUSIC.shareObject.refCount);
    MUSIC.shareObject.instance["so_" + MUSIC.shareObject.refCount] = this;
};
MUSIC.shareObject.DataBase.prototype.set = function(key, value) {
    if (this._ready) {
        this.ele.set("seed", Math.random());
        this.ele.set(key, value);
        this.ele.flush();
        return true;
    } else {
        return false;
    }
};
MUSIC.shareObject.DataBase.prototype.del = function(key) {
    if (this._ready) {
        this.ele.set("seed", Math.random());
        this.ele.set(key, void(0));
        this.ele.flush();
        return true;
    } else {
        return false;
    }
};
MUSIC.shareObject.DataBase.prototype.get = function(key) {
    return(this._ready) ? (this.ele.get(key)) : null;
};
MUSIC.shareObject.DataBase.prototype.clear = function() {
    if (this._ready) {
        this.ele.clear();
        return true;
    } else {
        return false;
    }
};
MUSIC.shareObject.DataBase.prototype.getDataSize = function() {
    if (this._ready) {
        return this.ele.getSize();
    } else {
        return-1;
    }
};
MUSIC.shareObject.DataBase.prototype.load = function(url, succFnName, errFnName, data) {
    if (this._ready) {
        this.ele.load(url, succFnName, errFnName, data);
        return true;
    } else {
        return false;
    }
};
MUSIC.shareObject.DataBase.prototype.setReady = function() {
    this._ready = true;
};
function getShareObjectPrefix() {
    MUSIC.shareObject.instance["so_" + MUSIC.shareObject.refCount].setReady();
    return"sosomusic";
}
MUSIC.shareObject.DataBase.prototype.setClipboard = function(value) {
    if (this._ready && isString(value)) {
        this.ele.setClipboard(value);
        return true;
    } else {
        return false;
    }
};

MUSIC.media = {_flashVersion:null,adjustImageSize:function(w, h, trueSrc, callback) {
    var ele = MUSIC.event.getTarget();
    if (ua.firefox < 3 && ele === document) {
        ele = MUSIC.event.getEvent().currentTarget;
    }
    ele.onload = null;
    var timg = new Image();
    timg.onload = (function(mainImg, tempImg, ew, eh) {
        return function() {
            tempImg.onload = null;
            var ow = tempImg.width;
            var oh = tempImg.height;
            if (ow / oh > ew / eh) {
                if (ow > ew) {
                    mainImg.width = ew;
                }
            } else {
                if (oh > eh) {
                    mainImg.height = eh;
                }
            }
            mainImg.src = tempImg.src;
            if (typeof(callback) == 'function') {
                callback(mainImg, w, h, tempImg, ow, oh);
            }
        };
    })(ele, timg, w, h)
    timg.src = trueSrc;
},getFlashHtml:function(flashArguments, requiredVersion, flashPlayerCID) {
    var _attrs = new StringBuilder();
    var _params = new StringBuilder();
    if (typeof(flashPlayerCID) == 'undefined') {
        flashPlayerCID = 'D27CDB6E-AE6D-11cf-96B8-444553540000';
    }
    for (var k in flashArguments) {
        switch (k) {case"movie":continue;break;case"id":case"name":case"width":case"height":case"style":_attrs.append(k + "='" + flashArguments[k] + "' ");break;default:_params.append("<param name='"
                + ((k == "src") ? "movie" : k) + "' value='"
                + flashArguments[k] + "' />");_attrs.append(k + "='" + flashArguments[k] + "' ");
        }
    }
    if (requiredVersion && (requiredVersion instanceof MUSIC.media.SWFVersion)) {
        if (requiredVersion.major == 9 && requiredVersion.rev == 16) {
            (function() {
                __flash_unloadHandler = MUSIC.emptyFn;
                __flash_savedUnloadHandler = MUSIC.emptyFn;
            })();
        }
    } else {
        requiredVersion = new MUSIC.media.SWFVersion(8, 0);
    }
    _attrs.append("codeBase='http://fpdownload.macromedia.com/get/flashplayer/current/swflash.cab#version="
            + requiredVersion + "' ");
    if (ua.ie) {
        return"<object classid='clsid:" + flashPlayerCID + "' " + _attrs
                + ">" + _params + "</object>";
    } else {
        return"<embed "
                + _attrs
                + " pluginspage='http://www.macromedia.com/go/getflashplayer' type='application/x-shockwave-flash'></embed>";
    }
},getWMMHtml:function(wmpArguments, cid) {
    var params = new StringBuilder();
    var objArgm = new StringBuilder();
    if (typeof(cid) == 'undefined') {
        cid = "clsid:6BF52A52-394A-11D3-B153-00C04F79FAA6";
    }
    for (var k in wmpArguments) {
        switch (k) {case"id":case"width":case"height":case"style":objArgm.append(k + '="' + wmpArguments[k] + '" ');break;case"src":objArgm.append(k + '="' + wmpArguments[k] + '" ');break;default:objArgm.append(k + '="' + wmpArguments[k] + '" ');params.append('<param name="' + k + '" value="'
                + wmpArguments[k] + '" />');
        }
    }
    if (wmpArguments["src"]) {
        params.append('<param name="URL" value="' + wmpArguments["src"]
                + '" />');
    }
    if (ua.ie) {
        return'<object classid="' + cid + '" ' + objArgm + '>' + params
                + '</object>';
    } else {
        return'<object  type="application/x-ms-wmp" ' + objArgm + '></object>';
    }
}}
MUSIC.media.SWFVersion = function() {
    var a;
    if (arguments.length > 1) {
        a = arg2arr(arguments);
    } else if (arguments.length == 1) {
        if (typeof(arguments[0]) == "object") {
            a = arguments[0];
        } else if (typeof arguments[0] == 'number') {
            a = [arguments[0]];
        } else {
            a = [];
        }
    } else {
        a = [];
    }
    this.major = parseInt(a[0], 10) || 0;
    this.minor = parseInt(a[1], 10) || 0;
    this.rev = parseInt(a[2], 10) || 0;
    this.add = parseInt(a[3], 10) || 0;
}
MUSIC.media.SWFVersion.prototype.toString = function(spliter) {
    return([this.major,this.minor,this.rev,this.add]).join((typeof spliter == 'undefined') ? "," : spliter);
};
MUSIC.media.SWFVersion.prototype.toNumber = function() {
    var se = 0.001;
    return this.major + this.minor * se + this.rev * se * se + this.add * se * se * se;
};
MUSIC.media.getFlashVersion = function() {
    if (!MUSIC.media._flashVersion) {
        var resv = 0;
        if (navigator.plugins && navigator.mimeTypes.length) {
            var x = navigator.plugins['Shockwave Flash'];
            if (x && x.description) {
                resv = x.description.replace(/(?:[a-z]|[A-Z]|\s)+/, "").replace(/(?:\s+r|\s+b[0-9]+)/, ".").split(".");
            }
        } else {
            try {
                for (var i = (resv = 6),axo = new Object(); axo != null; ++i) {
                    axo = new ActiveXObject("ShockwaveFlash.ShockwaveFlash."
                            + i);
                    resv = i;
                }
            } catch(e) {
                resv = Math.max(resv - 1, 0);
            }
            try {
                resv = new MUSIC.media.SWFVersion(axo.GetVariable("$version").split(" ")[1].split(","));
            } catch(ignore) {
            }
        }
        if (!(resv instanceof MUSIC.media.SWFVersion)) {
            resv = new MUSIC.media.SWFVersion(resv);
        }
        if (resv.major < 3) {
            resv.major = 0;
        }
        MUSIC.media._flashVersion = resv;
    }
    return MUSIC.media._flashVersion;
};
var insertFlash = MUSIC.media.getFlashHtml;
var insertMediaPlayer = MUSIC.media.getWMMHtml;

MUSIC.widget.watch = {set:function(_pageid, _webid, _busineseid) {
    this._pageid = !_pageid ? this._pageid : _pageid;
    this._webid = !_webid ? this._webid : _webid;
    this._busineseid = !_busineseid ? this._busineseid : _busineseid;
},_busineseid:170,_webid:105,_pageid:0,_rnd:11,watchData:{totalTime:0,connectTime:0,cssLoad:0,jsLoad:0,pageLoad:0},getWaitTime:function() {
    var t = Cookie.get("TRANS_TIME_POINT");
    if (!!t) {
        t = parseInt(t);
    } else {
        return g_cssBegin;
    }
    return t;
},getTime:function() {
    var lastPageDate = this.getWaitTime();
    this.watchData["connectTime"] = g_cssBegin - lastPageDate;
    this.watchData["totalTime"] = g_watchStop - g_cssBegin;
    this.watchData["cssLoad"] = g_jsBegin - g_cssBegin;
    this.watchData["jsLoad"] = g_pageBegin - g_jsBegin;
    this.watchData["pageLoad"] = g_watchStop - g_pageBegin;
},send:function(_id, _rnd) {
    this.getTime();
    var url = "http://isdspeed.qq.com/cgi-bin/r.cgi?flag1=170&flag2="
            + this._webid;
    url += "&flag3=" + _id;
    url += "&flag4=" + this._rnd;
    url += "&1=" + this.watchData["totalTime"];
    url += "&2=" + this.watchData["connectTime"];
    url += "&3=" + this.watchData["cssLoad"];
    url += "&4=" + this.watchData["jsLoad"];
    url += "&5=" + this.watchData["pageLoad"];
    var img = new Image();
    img.src = url;
    img.onerror = img.onload = null;
}}
var watch = MUSIC.widget.watch;
function watchSearchCommit() {
    var _url = window.location.toString();
    var _id = 0;
    var s1 = window.location.href;
    var s2 = window.location.host;
    var index = s1.lastIndexOf(s2) + s2.length;
    var s3 = s1.substring(index);
    if (s3 == "/" || s3 == "/index.html") {
        _id = 1;
    } else {
        var _page = [/hit\/index\.html/,/hit/,/singer\/index\.html/,/singer\/hot\//,/singer\/\d{1,2}\/singer_/,/singer\/\d{1,2}\/singerAlbumn_/,/singer\/\d{1,2}\/singerSong_/,/albumn\/hot\//,/albumn\/new\//,/albumn\/language\//,/albumn\/type\//,/albumn\/genre\//,/albumn\/\d{1,2}\//,/cgi.music.soso.com\/fcgi-bin\/m.q\?w=.*t=0/,/cgi.music.soso.com\/fcgi-bin\/m.q\?w=.*t=8/,/cgi.music.soso.com\/fcgi-bin\/m.q\?w=.*t=7/,/cgi.music.soso.com\/fcgi-bin\/fcg_music_play.q/,/taoge\/index\.html/,/taoge\/tag\//,/taoge\/album\//,/taoge\/taoge_personal.html/,/taoge\/taoge_cddetail.html/,/topic\/index\.html/,/topic\/content\//,/shoufa\/index\.html/,/shoufa\/content\//];
        for (var i = 0,_length = _page.length; i < _length; i++) {
            if (_url.search(_page[i]) > 0) {
                _id = i + 2;
                break;
            }
        }
    }
    if (typeof watch != "undefined" && _id > 0)
        watch.send(_id, 11);
}

var MUSIC = MUSIC || {};
if ((typeof(yueFlag) != "undefined" && yueFlag == 1) || (typeof(playerSource) != "undefined" && (playerSource == 2 || playerSource == 3)))
    var xSosoFlag = 0; else
    var xSosoFlag = (parent.location.href).indexOf("x.soso.com");
MUSIC.lazyLoad = (function() {
    var timer = 0,elems = [],hide_elems = [],count = 0,defaultImg = "http://cache.music.soso.com/sosocache/sosomusic_v1/pic/default.gif",$ = MUSIC,$C = $.css,$E = $.event;

    function _onChange()
    {
        if (timer != 0) {
            return;
        }
        timer = setTimeout(load, 30);
    }

    function _isVisible(e)
    {
        var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        var bottom = scrollTop + document.documentElement.clientHeight;
        var eOffsetTop = e.offsetTop;
        while (e = e.offsetParent) {
            eOffsetTop += e.offsetTop;
        }
        return eOffsetTop <= bottom;
    }

    function load()
    {
        if (count < 1) {
            $E.removeEvent(window, "scroll", _onChange);
            $E.removeEvent(window, "resize", _onChange);
            return;
        }
        for (var i = 0,j = elems.length; i < j; i++) {
            if (!elems[i]) {
                continue;
            }
            if (_isVisible(elems[i]) || xSosoFlag > 0) {
                elems[i].src = elems[i].getAttribute("init_src");
                delete elems[i];
                count--;
            }
        }
        timer = 0;
    }

    function init(tagNames)
    {
        if (!tagNames)
            tagNames = ['img','iframe'];
        for (var i = 0,j = tagNames.length; i < j; i++) {
            var es = document.getElementsByTagName(tagNames[i]);
            for (var n = 0,m = es.length; n < m; n++) {
                if (typeof es[n] == 'object' && es[n].getAttribute('init_src')) {
                    elems.push(es[n]);
                    count++;
                } else if (typeof es[n] == 'object' && es[n].getAttribute('hide_init_src')) {
                    hide_elems.push(es[n]);
                }
                $E.on(es[n], "load", (function(el) {
                    return function() {
                        if (el.src && el.src != $.lazyLoad.defaultImg) {
                            $C.removeClassName(el, "loading_82_21");
                            $C.removeClassName(el, "loading_36_35");
                            $C.removeClassName(el, "loading_58_58");
                        }
                    }
                })(es[n]))
            }
        }
        var defaultImg = new Image();
        var els = elems.concat(hide_elems);
        $E.on(defaultImg, "load", (function(els) {
            return function() {
                for (var i = 0,len = els.length; i < len; i++) {
                    if (!els[i].src) {
                        els[i].src = $.lazyLoad.defaultImg;
                    }
                }
            }
        })(els));
        defaultImg.src = $.lazyLoad.defaultImg;
        $E.on(window, "scroll", _onChange);
        $E.on(window, "resize", _onChange);
        load();
    }

    function loadHideImg(con) {
        var imgs = (typeof con == "string") ? $.element.get("#" + con + " img").elements : con;
        $.object.each(imgs, function(el) {
            if (el.getAttribute("hide_init_src")) {
                el.src = el.getAttribute("hide_init_src");
                el.setAttribute("hide_init_src", "");
            }
        })
    }

    return{init:init,loadHideImg:loadHideImg,defaultImg:defaultImg}
})();

var Class = {create:function() {
    return function() {
        this.initialize.apply(this, arguments);
    }
}}
var PeriodicalExecuter = Class.create();
PeriodicalExecuter.prototype = {initialize:function(callback, frequency) {
    if (!!callback) {
        this.set(callback, frequency);
    }
},set:function(callback, frequency) {
    this.stop();
    this.callback = callback;
    this.frequency = frequency;
    this.currentlyExecuting = false;
    this.registerCallback();
},registerCallback:function() {
    this.timer = setInterval(this.onTimerEvent.bind(this), this.frequency * 1000);
},stop:function() {
    if (!this.timer)
        return;
    clearInterval(this.timer);
    this.timer = null;
},onTimerEvent:function() {
    if (!this.currentlyExecuting) {
        try {
            this.currentlyExecuting = true;
            this.callback(this);
        } catch(e) {
        } finally {
            this.currentlyExecuting = false;
        }
    }
}}
var timerExecuter = new PeriodicalExecuter();
MUSIC.widget.timer = {frequency:0.5,updateTimer:function(timerSpan, time, tipsCallback, actionCallback) {
    MUSIC.widget.timer.frequency = 1;
    this._timer = time;
    this.apply(this._updateTime.bind(this), timerSpan, tipsCallback, actionCallback);
},_timer:0,_updateTime:function(timerSpan, tipsCallback, actionCallback) {
    if (this._timer > 0) {
        if (!!timerSpan) {
            timerSpan.innerHTML = --this._timer;
            if (this._timer == 0 && tipsCallback)
                tipsCallback();
        } else {
            MUSIC.dialog.createInfoBox("??????????DIV?????!", 1, 1);
        }
    } else {
        timerExecuter.stop();
        if (actionCallback)
            actionCallback();
        MUSIC.widget.timer.frequency = 0.5;
    }
}}
MUSIC.widget.timer.apply = function() {
    if (arguments.length < 2)
        return;
    var args = MUSIC.lang.arg2arr(arguments),pFun = args.shift();
    var fun = function() {
        return pFun.apply(null, args);
    }
    timerExecuter.set(fun, this.frequency);
}
var timerCallBack = MUSIC.widget.timer.apply;

MUSIC.widget.smartbox = {_const:{maxListNum:10,maxTryTime:2,dataUrl:"http://cgi.music.soso.com/fcgi-bin/fcg_smartbox.q?utf8=1&w=",_inputN:"search_input",_listN:"keywords_list"},keyword:"",hashkey:"",data:null,cache:new HashTable(),useCache:false,timer:0,_callBack:null,getKeyword:function(keyword) {
    return this.deleteDirtyWord(this.keyword).replace(/</g, "").replace(/>/g, "").replace(/%20/g, " ").replace(/&/g, " ").replace(/#/g, " ").replace(/;/g, " ").replace(/\\/, " ").replace(/\,/, " ").replace(/\//, " ").replace(/'/, " ").replace(/\"/, " ").replace(/\{/, " ").replace(/\}/, " ").replace(/\[/, " ").replace(/\?/, " ").replace(/\|/, " ").replace(/\]/, " ");
},deleteDirtyWord:function(_str) {
    return _str.replace(/???/g, "").replace(/cocaine/g, "").replace(/cocain/g, "").replace(/???/g, "")
},load:function(callback, keyword) {
    if (keyword)
        this.keyword = keyword;
    if (callback)
        this._callBack = callback;
    this.hashkey = this.getKeyword().replace(/(^\s*)|(\s*$)/g, "_");
    if (this.useCache && this.cache.contains(this.hashkey)) {
        try {
            this.data = this.cache.items(this.hashkey);
            this.show();
        } catch(e) {
            var url = this._const.dataUrl + this.getKeyword();
            JsonLoadData(url, this.setData.bind(this), this.loadFail.bind(this));
        }
    } else {
        var url = this._const.dataUrl + this.getKeyword();
        JsonLoadData(url, this.setData.bind(this), this.loadFail.bind(this), null, "gb2312");
    }
},setData:function(data) {
    this.timer = 0;
    this.data = data;
    if (this._callBack) {
        this._callBack();
    }
    this.timer = 0;
    if (this.useCache)
        this.cache.add(this.hashkey, this.data);
},loadFail:function() {
    if (this.timer++ < this._const.maxTryTime) {
        this.load();
    } else {
    }
},set:function(keyword) {
    if (keyword)
        this.keyword = keyword;
    this.bindEvent();
    if (trim(keyword) == "") {
        return;
    }
    this.load(this.show.bind(this));
},doIntervalEvent:function() {
    var curInputVal = Element(this._const._inputN).value;
    if (trim(curInputVal) == "") {
        hideElement(this._const._listN);
        MUSIC.widget.smartbox._hasResult = false;
        return;
    }
    if (trim(curInputVal) != "" && curInputVal != this.keyword) {
        this.set(curInputVal);
    }
},_hasResult:false,show:function() {
    if (!this.data || !this.data.head) {
        return;
    }
    var _obj = Element(this._const._listN);
    if (!_obj.getElementsByTagName("ul"))
        return;
    _obj.style.zIndex = 99999;
    var ul = _obj.getElementsByTagName("ul")[0];
    if (this.data.head.error != 0) {
        hideElement(this._const._listN);
        this._hasResult = false;
        return;
    } else {
        var html = [];
        if (!this.data.item || this.data.item.length == 0) {
            hideElement(this._const._listN);
            this._hasResult = false;
            return;
        } else {
            for (var i = 0; i < this.data.item.length && i < this._const.maxListNum; i++) {
                html.push("<li style='z-index:99999'><a href='#' onclick='MUSIC.widget.smartbox.search(this)'"
                        + " onmouseover='MUSIC.widget.smartbox._onmouseEvent(this);' index="
                        + i
                        + " onmouseout='this.className=\"\"'>"
                        + this.data.item[i].w + "</a></li>");
            }
            ul.innerHTML = html.join("");
            this._hasResult = true;
        }
    }
    showElement(this._const._listN);
},_onmouseEvent:function(obj, index) {
    var _obj = Element(this._const._listN);
    if (!_obj)
        return;
    var ul = _obj.getElementsByTagName("ul")[0];
    var lis = ul.getElementsByTagName("li");
    for (var i = 0; i < lis.length; i++) {
        lis[i].childNodes[0].className = "";
        lis[i].childNodes[0].style.backgroundColor = "";
    }
    this.curIndex = obj.index;
    obj.className = "on";
},search:function(obj) {
    this.clear();
    hideElement(this._const._listN);
    Element(this._const._inputN).value = obj.innerHTML;
    if (gcomm.checkForm())
        Element("search_form").submit();
},_event:null,clear:function() {
    if (this._event)
        clearInterval(this._event);
    this._event = null;
    document.onkeydown = null;
},curIndex:-1,bindEvent:function() {
    this.clear();
    this.curIndex = -1;
    document.onkeydown = this._keydown;
    this._event = setInterval(this.doIntervalEvent.bind(this), 300);
    var _obj = Element(this._const._listN);
    if (!_obj)
        return;
    addEvent(_obj, "mouseover", function() {
        MUSIC.event.cancelBubble(window.event);
        MUSIC.widget.smartbox._mlf = false;
        if (MUSIC.widget.smartbox._hasResult && trim(Element(MUSIC.widget.smartbox._const._inputN).value) != "")
            showElement('keywords_list');
    });
    addEvent(_obj, "mouseout", function() {
        MUSIC.event.cancelBubble(window.event);
        MUSIC.widget.smartbox._mlf = true;
        setTimeout("if(MUSIC.widget.smartbox._mlf)hideElement('keywords_list');", 100);
    });
    addEvent(Element(this._const._inputN), "mouseout", function() {
        MUSIC.event.cancelBubble(window.event);
        setTimeout("if(MUSIC.widget.smartbox._mlf)hideElement('keywords_list');", 100);
    });
    addEvent(Element(this._const._inputN), "mouseover", function() {
        MUSIC.event.cancelBubble(window.event);
        MUSIC.widget.smartbox._mlf = false;
        if (MUSIC.widget.smartbox._hasResult && trim(Element(MUSIC.widget.smartbox._const._inputN).value) != "")
            showElement('keywords_list');
    });
    addEvent(document, "click", function() {
        var ev = MUSIC.event.getEvent()
        if (!ev || !ev.srcElement)
            return;
        var _ev = ev.srcElement;
        var _edit = false;
        if (_ev.tagName && _ev.tagName == "INPUT") {
            _edit = true;
        }
        if (!_edit) {
            hideElement('keywords_list');
        }
    });
},_mlf:false,_keydown:function() {
    var _obj = Element(MUSIC.widget.smartbox._const._listN);
    if (!_obj)
        return;
    var ul = _obj.getElementsByTagName("ul")[0];
    var lis = ul.getElementsByTagName("li");
    for (var i = 0; i < lis.length; i++) {
        lis[i].childNodes[0].className = "";
        lis[i].childNodes[0].style.backgroundColor = "";
    }
    var index = 0;
    var ev = MUSIC.event.getEvent()
    switch (ev.keyCode) {case 38:{
        if (MUSIC.widget.smartbox.curIndex > 0) {
            MUSIC.widget.smartbox.curIndex--;
        } else {
            MUSIC.widget.smartbox.curIndex = lis.length - 1;
        }
    }
        break;case 40:{
        if (MUSIC.widget.smartbox.curIndex < lis.length - 1) {
            MUSIC.widget.smartbox.curIndex++;
        } else {
            MUSIC.widget.smartbox.curIndex = 0;
        }
    }
        break;default:{
        if (!MUSIC.widget.smartbox._event)
            MUSIC.widget.smartbox._event = setInterval(MUSIC.widget.smartbox.doIntervalEvent.bind(MUSIC.widget.smartbox), 300);
        return;
    }
        break;
    }
    index = MUSIC.widget.smartbox.curIndex;
    try {
        lis[index].childNodes[0].className = "on";
        Element(MUSIC.widget.smartbox._const._inputN).value = lis[index].innerText;
        if (MUSIC.widget.smartbox._event) {
            clearInterval(MUSIC.widget.smartbox._event);
            MUSIC.widget.smartbox._event = null;
        }
    } catch(i) {
    }
}}
var g_smartbox = MUSIC.widget.smartbox;

MUSIC.widget.imgPlayer = {_timer:null,_items:[],_container:null,_index:0,_imgs:[],intervalTime:5000,linkStyle:"display: block;",init:function(objID, w, h, time) {
    this.intervalTime = time || this.intervalTime;
    this._container = document.getElementById(objID);
    var html = "<a href=\""
            + this._items[this._index].link
            + "\" class=\"shoufa_pic\"><img src=\""
            + this._items[this._index].img
            + "\" alt=\""
            + this._items[this._index].title
            + "\" target=\""
            + this._items[this._index].target
            + "\" style=\""
            + this.linkStyle
            + "\"/><em  class=\"pic_title\">"
            + this._items[this._index].title
            + "</em><span class=\"pic_title_bg\"></span></a>"
            + "<div>"
            + this.getPage() + "</div>";
    this._container.innerHTML = html;
    this._timer = setInterval("imgPlayer.play()", this.intervalTime);
},addItem:function(_title, _link, _imgURL, _target, _desc) {
    this._items.push({title:_title,link:_link,img:_imgURL,target:_target,descrip:_desc});
    var img = new Image();
    img.src = restHTML(_imgURL);
    this._imgs.push(img);
},play:function(index) {
    if (index != null) {
        this._index = index;
        clearInterval(this._timer);
        this._timer = setInterval("imgPlayer.play()", this.intervalTime);
    } else {
        this._index = this._index < this._items.length - 1 ? this._index
                + 1 : 0;
    }
    var html = "<a href=\""
            + this._items[this._index].link
            + "\" target=\""
            + this._items[this._index].target
            + "\" class=\"shoufa_pic\"><img src=\""
            + this._items[this._index].img
            + "\" alt=\""
            + this._items[this._index].title
            + "\"/><em  class=\"pic_title\">"
            + this._items[this._index].title
            + "</em><span class=\"pic_title_bg\"></span></a>"
            + this.getPage();
    this._container.innerHTML = html;
},getPage:function() {
    var ulHTML = "";
    var preIndex = this._index > 0 ? this._index - 1 : this._items.length - 1;
    var nextIndex = this._index < this._items.length - 1 ? this._index + 1 : 0;
    ulHTML = "<a href=\"#\" onclick=\"imgPlayer.play(" + preIndex + ");pgv();return false;\" class=\"bt_pre\"> < </a><a href=\"#\" onclick=\"imgPlayer.play(" + nextIndex + ");pgv();return false;\" class=\"bt_next\"> > </a>"
    return ulHTML;
}}
var imgPlayer = MUSIC.widget.imgPlayer;
if (document.implementation.hasFeature("XPath", "3.0")) {
    XMLDocument.prototype.selectNodes = function(cXPathString, xNode) {
        if (!xNode) {
            xNode = this;
        }
        var oNSResolver = this.createNSResolver(this.documentElement)
        var aItems = this.evaluate(cXPathString, xNode, oNSResolver, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null)
        var aResult = [];
        for (var i = 0; i < aItems.snapshotLength; i++) {
            aResult[i] = aItems.snapshotItem(i);
        }
        return aResult;
    }
    Element.prototype.selectNodes = function(cXPathString) {
        if (this.ownerDocument.selectNodes) {
            return this.ownerDocument.selectNodes(cXPathString, this);
        } else {
            throw"For XML Elements Only";
        }
    }
}
window.imgPlayer = MUSIC.widget.imgPlayer;

MUSIC.widget.player = {version:"1.0"}
MUSIC.widget.player.webPlayer = {getPostData:function(aList) {
    if (!aList) {
        return;
    }
    var iLen = aList.length;
    if (iLen === 0) {
        return"[];";
    }
    var sJson = "[";
    for (var i = 0; i < iLen; i++) {
        if (i > 0) {
            sJson += ',';
        }
        var iLen2 = aList[i].length;
        if (iLen2 == 0) {
            sJson += '[]';
            continue;
        }
        sJson += '[';
        for (var j = 0; j < iLen2; j++) {
            if (j > 0) {
                sJson += ',';
            }
            sJson += '"' + (aList[i][j]).toString().replace(/"/g, '\\"')
                    + '"';
        }
        sJson += ']';
    }
    sJson += "]";
    return sJson;
},OpenPostWindow:function(sUrl, sWindowName, oPostData) {
    this._openPlayer("http://cache.music.soso.com/sosocache/music/playerdata_loading.html");
    if (typeof sWindowName !== "string") {
        sWindowName = "";
    }
    var sFormId = "post_window_form";
    var oForm = document.getElementById(sFormId);
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
    var oForm = document.createElement("form");
    oForm.id = sFormId;
    oForm.action = sUrl;
    oForm.method = "POST";
    oForm.target = sWindowName;
    for (key in oPostData) {
        var oInput = document.createElement("input");
        oInput.type = "hidden";
        oInput.name = key;
        oInput.value = oPostData[key];
        oForm.appendChild(oInput);
    }
    document.body.appendChild(oForm);
    oForm.submit();
},listen_feature:'toolbar=no,location=no,menubar=no,resizable=yes,status=yes,scrollbars=no,width=750,height=520,left=100,top=10',_playerWin:null,playerCapacity:1000,openWebMusicPlayer:function(aList, oPostData, top, left) {
    var param = '',sUrl = "",o = null;
    var playUrl = "http://cgi.music.soso.com/fcgi-bin/fcg_music_play_mid.q";
    if (typeof oPostData != "object" || null == oPostData) {
        oPostData = {};
    }
    if (oPostData.url) {
        sUrl = oPostData.url;
    } else {
        sUrl = playUrl;
    }
    oPostData.songList = this.getPostData(aList);
    for (key in oPostData) {
        param += (key + "=");
        param += (escape(oPostData[key]) + "&");
    }
    this.OpenPostWindow(sUrl, "_webSosoMusicPlayer", oPostData);
    window.postSongNum = aList.length;
    if (Cookie.get("playerSongListLen") != "")
    {
        var len = parseInt(Cookie.get("playerSongListLen"));
        if ((len + aList.length) > 1000)
        {
            MUSIC.dialog.createInfoBox("?????????1000?????????????????", 2, 1, top, left);
            return;
        }
        if (oPostData.userName != '')
        {
        } else
            MUSIC.dialog.createInfoBox("????????????", 1, 1, top, left);
    } else {
        window.getPlayerSongTimeout = setTimeout("if (Cookie.get(\"playerSongListLen\")!=\"\"){var len = parseInt(Cookie.get(\"playerSongListLen\"));if ((len + window.postSongNum)>1000)alert(\"????\");}clearTimeout(getPlayerSongTimeout);", 1000)
    }
},openEmptyPlayer:function(cb) {
    this._openPlayer("http://cache.music.soso.com/sosocache/music/playerdata_loading.html?player=load", cb);
    this._playerWin && this._playerWin.focus();
},_openPlayer:function(url, cb) {
    this._playerWin = top.window.open(url, "_webSosoMusicPlayer", this.listen_feature);
    if (this._playerWin) {
        cb && cb();
    } else {
        MUSIC.dialog.createInfoBox("???????,?????!", 1, 1);
    }
}}
MUSIC.widget.player.webPlayerPlay = function(play_type, song_type, song_url, song_id, song_name, singer_id, singer_name, albumid, album_name, minteral, urls) {
    var aList = [
        [song_id,song_type,song_url.trim().myEncode(),(song_name.trim().myEncode()),singer_id,(singer_name.trim().myEncode()),albumid,(album_name.trim().myEncode()),minteral,(urls)]
    ];
    if (typeof(isXsoso) == 'undefined')
    {
        if (typeof(xsosoFlag) == 'undefined')
        {
            isXsoso = 0;
        } else isXsoso = xsosoFlag;
    }
    var playXsosoFlag = isXsoso ? '1' : '0';
    MUSIC.widget.player.webPlayer.openWebMusicPlayer(aList, {songList:'',type:play_type,vip:-1,userName:'',playXsosoFlag:playXsosoFlag});
};
MUSIC.widget.player.play = function(obj) {
    var music = new FormatSosoMusic(obj);
    var urls = music.mapSongUrlStr ? music.mapSongUrlStr.join(";") : "";
    var url = (music.mapSongUrlStr && music.mapSongUrlStr.length) ? music.mapSongUrlStr[0] : ((music.msongurl && music.msongurl != "") ? music.msongurl : "");
    this.webPlayerPlay(1, music.mdownload, url, music.mid, music.msong, music.msingerid, music.msinger, music.malbumid, music.malbum, music.iInteral, urls);
}
MUSIC.widget.player.add = function(obj) {
    var music = new FormatSosoMusic(obj);
    var urls = music.mapSongUrlStr ? music.mapSongUrlStr.join(";") : "";
    var url = (music.mapSongUrlStr && music.mapSongUrlStr.length) ? music.mapSongUrlStr[0] : ((music.msongurl && music.msongurl != "") ? music.msongurl : "");
    this.webPlayerPlay(0, music.mdownload, url, music.mid, music.msong, music.msingerid, music.msinger, music.malbumid, music.malbum, music.iInteral, urls)
}
MUSIC.widget.player.updateNickName = function() {
    var nickName = user.getNick();
    var aList = [];
    if (typeof(isXsoso) == 'undefined')
    {
        if (typeof(xsosoFlag) == 'undefined')
        {
            isXsoso = 0;
        } else isXsoso = xsosoFlag;
    }
    var playXsosoFlag = isXsoso ? '1' : '0';
    MUSIC.widget.player.webPlayer.openWebMusicPlayer(aList, {songList:'',type:0,vip:-1,userName:nickName,playXsosoFlag:playXsosoFlag});
}
MUSIC.widget.player.list = {music:null,setMusic:function() {
    try {
        this.music = null;
        this.music = new FormatSosoMusic(arguments[0]);
    } catch(e) {
        throw"set xml error";
    }
},_getList:function(args) {
    var eleTmp;
    var arraySelect = [];
    var _this = this;
    var index = 0;
    utils.each(function(lstMusic) {
        var _lstMusic = lstMusic.firstChild;
        if (lstMusic && lstMusic.nodeName == "TABLE") {
            while (_lstMusic && _lstMusic.nodeName != "TBODY") {
                _lstMusic = _lstMusic.nextSibling;
            }
            if (_lstMusic && _lstMusic.nodeName == "TBODY") {
                lstMusic = _lstMusic;
            }
        }
        lstMusic = lstMusic.childNodes;
        for (var j = 0; j < lstMusic.length && index < 50; j++,index++) {
            if (lstMusic[j].nodeType != 1 || lstMusic[j].firstChild.nodeName == "TH") {
                continue;
            }
            var input = lstMusic[j].getElementsByTagName("input");
            if (input.length > 0 && input[0].checked == false) {
                continue;
            }
            _this.setMusic(lstMusic[j]);
            arraySelect.push(_this.music);
        }
    }, args);
    var noSong = 1;
    var sid = -1,stype = 0,sname = "",ssinger = "",sduration = 0,ssingerid = -1,salbumid = -1,surl = "",salbum = "";
    var aList = [],ls = [],a = null;
    for (var i = 0,len = arraySelect.length; i < len; i++) {
        a = arraySelect[i];
        sname = a.msong.toString().myEncode();
        if (!sname)
            continue;
        stype = 1;
        surl = a.msongurl.toString();
        sid = a.mid
        surl += "";
        ssinger = (a.msinger.toString().myEncode());
        salbumid = (a.malbumid);
        salbum = (a.malbum);
        ssingerid = (a.msingerid);
        ls = [sid,stype,surl,sname,ssingerid,ssinger,salbumid,salbum,sduration];
        aList.push(ls);
        noSong = 0;
    }
    if (!noSong) {
    } else {
        MUSIC.dialog.createInfoBox("???????????", 1, 1);
        return;
    }
    return aList;
},play:function() {
    var args = MUSIC.lang.arg2arr(arguments);
    var aList = this._getList(args);
    if (typeof(isXsoso) == 'undefined')
    {
        if (typeof(xsosoFlag) == 'undefined')
        {
            isXsoso = 0;
        } else isXsoso = xsosoFlag;
    }
    var playXsosoFlag = isXsoso ? '1' : '0';
    MUSIC.widget.player.webPlayer.openWebMusicPlayer(aList, {songList:'',type:1,vip:-1,userName:'',playXsosoFlag:playXsosoFlag});
},add:function() {
    var args = MUSIC.lang.arg2arr(arguments);
    var aList = this._getList(args);
    if (typeof(isXsoso) == 'undefined')
    {
        if (typeof(xsosoFlag) == 'undefined')
        {
            isXsoso = 0;
        } else isXsoso = xsosoFlag;
    }
    var playXsosoFlag = isXsoso ? '1' : '0';
    MUSIC.widget.player.webPlayer.openWebMusicPlayer(aList, {songList:'',type:0,vip:-1,userName:'',playXsosoFlag:playXsosoFlag});
},playRank:function(rankId, startIndex) {
    if (typeof(isXsoso) == 'undefined')
    {
        if (typeof(xsosoFlag) == 'undefined')
        {
            isXsoso = 0;
        } else isXsoso = xsosoFlag;
    }
    var playXsosoFlag = isXsoso ? '1' : '0';
    MUSIC.widget.player.webPlayer.openWebMusicPlayer([
        [rankId,startIndex]
    ], {songList:'',type:2,vip:-1,userName:'',playXsosoFlag:playXsosoFlag});
}}
MUSIC.widget.player.util = {select:function() {
    try {
        for (var i = 0; i < arguments.length; i++) {
            var lstMusic = arguments[i].getElementsByTagName("input");
            for (var j = 0,length = lstMusic.length; j < length; j++) {
                if (!lstMusic[j].disabled) {
                    lstMusic[j].checked = true;
                }
            }
        }
    } catch(e) {
    }
},select2:function(objTable, bStatus) {
    try {
        var lstMusic = objTable.getElementsByTagName("input");
        for (var j = 0,length = lstMusic.length; j < length; j++) {
            if (!lstMusic[j].disabled) {
                lstMusic[j].checked = bStatus;
            }
        }
    } catch(e) {
        ;
    }
},cancel:function() {
    try {
        for (var i = 0; i < arguments.length; i++) {
            var lstMusic = arguments[i].getElementsByTagName("input");
            for (var j = 0,length = lstMusic.length; j < length; j++) {
                if (!lstMusic[j].disabled) {
                    lstMusic[j].checked = false;
                }
            }
        }
    } catch(e) {
    }
}}
var player = MUSIC.widget.player;
var openWebMusicPlayer = MUSIC.widget.player.webPlayer.openWebMusicPlayer.bind(MUSIC.widget.player.webPlayer);
var openEmptyPlayer = MUSIC.widget.player.webPlayer.openEmptyPlayer.bind(MUSIC.widget.player.webPlayer);
;
window.g_JData = {};

MUSIC.widget.gcomm = {getMusicUrlStream:function(songid, songLoc) {
    var str = "http://stream" + songLoc + ".music.soso.com/"
            + (parseInt(songid) + 12000000) + ".wma";
    return str;
},getMusicUrlIp:function(url) {
    var disp = "";
    var StreamIP = ["116.28.66.253","116.28.63.250","116.28.63.250","116.28.66.253","121.9.210.27","121.9.210.27","121.9.210.102","121.9.210.102","121.9.210.27","121.9.210.102","121.9.210.102"];
    var type = getParameter("t");
    var useWma = (type == "2");
    if (url.indexOf("music.soso.com") != -1 || url.indexOf("qqmusic.qq.com") != -1) {
        var result = url.match(/(\d)+/gi);
        if (!result || result.length < 2) {
            disp = url;
        } else {
            var steam = parseInt(result[0]);
            var songid = parseInt(result[1]);
            if (useWma || /^?12?/.test(result[1])) {
                disp = "http://" + StreamIP[steam - 1] + "/" + songid
                        + ".wma";
            } else if (steam > 10) {
                disp = "http://" + StreamIP[steam - 11] + "/" + songid
                        + ".mp3";
            } else {
                songid = parseInt(result[1]) - 12000000 + 30000000;
                disp = "http://" + StreamIP[steam - 1] + "/" + songid
                        + ".mp3";
            }
        }
    } else
        disp = url;
    return disp;
},getStreamFromUrl:function(url) {
    var songStream = {stream:0,songID:0};
    if (url.indexOf("music.soso.com") != -1) {
        var result = url.match(/(\d)+/gi);
        if (!result || result.length < 2) {
        } else {
            var steam = parseInt(result[0]);
            var songid = parseInt(result[1]);
            songStream.stream = steam;
            songStream.songID = songid;
        }
    }
    return songStream;
},_sosoMusic:null,downLoadSong:function(obj) {
    var isXsosoFlag = 0;
    if (typeof(isXsoso) != "undefined")
    {
        isXsosoFlag = isXsoso ? "1" : "0";
    } else if (typeof(lyricXsosoFlag) != "undefined")
    {
        isXsosoFlag = lyricXsosoFlag ? "1" : "0";
    }
    this._sosoMusic = new FormatSosoMusic(obj);
    var musicdata = this._sosoMusic.mid + "@@" + this._sosoMusic.msong
            + "@@" + this._sosoMusic.msingerid + "@@"
            + this._sosoMusic.msinger + "@@" + this._sosoMusic.malbumid
            + "@@" + this._sosoMusic.malbum + "@@" + isXsosoFlag + "@@";
    gcomm.submitForm(musicdata);
},submitForm:function(musicData) {
    openPostWindow("http://cgi.music.soso.com/fcgi-bin/fcg_download_song.q", "sosoSongTips", {f:musicData,t:1}, "top=0,left=0,height=385,width=562,toolbar=no,menubar=no,status=no,resizable=yes,scrollbars=yes");
},viewLyric:function(obj) {
    var isXsosoFlag = 0;
    if (typeof(isXsoso) != "undefined")
    {
        isXsosoFlag = isXsoso ? "1" : "0";
    }
    this._sosoMusic = new FormatSosoMusic(obj);
    var song = this._sosoMusic.msong;
    var singer = this._sosoMusic.msinger;
    openPostWindow("http://cgi.music.soso.com/fcgi-bin/m.q", "sosoLyricTips", {w:song + " " + singer,singer:singer,song:song,source:1,p:1,t:10,isXsoso:isXsosoFlag}, "top=0,left=0,height=550,width=550,toolbar=no,menubar=no,status=no,resizable=no,scrollbars=yes");
},navi:{flag:null,"??":"http://www.soso.com/q?sc=web&pid=n.soso&uin=&w={value}","??":"http://image.soso.com/q?sc=img&pid=n.soso&uin=&w={value}","??":"http://video.soso.com/search/?sc=vid&w={value}","??":"http://cgi.music.soso.com/m.q?ty=1&sc=mus&pid=n.soso&uin=&t=1&w={value}","??":"http://post.soso.com/sobar.q?op=entry&pid=b.idx&w={value}","??":"http://wenwen.soso.com/z/SearchSolved.e?sp=S","??":"http://news.soso.com/n.q?sc=news&ty=c&w={value}","??":"http://blog.soso.com/qz.q?sc=qz&op=blog.blog&ty=blog&w={value}","??»":"http://www.soso.com/more.shtml?w={value}","??":"http://zh.soso.com/int.cgi?sc=int&pid=n.soso&w={value}","??":"http://dict.soso.com/d.q?sc=dict&w={value}","??":"http://life.soso.com/","??":"http://baike.soso.com/Search.e?sp=S","????":"http://www.soso.com/more.shtml?w={value}",go:function(obj) {
    var name = trim(obj.innerHTML);
    var url = this[name] || "";
    if (!url) {
        MUSIC.dialog.createInfoBox(name + ":?????????", 1, 1);
        return false;
    }
    var value = Element("search_input") && Element("search_input").value;
    url = url.replace(/\{value}/gi, value || "");
    window.location.href = url;
},show:function() {
    showElement("more_list_con");
    this.flag = 1;
},set:function(flag) {
    this.flag = flag;
    if (!flag)
        this.hide();
},hide:function() {
    setTimeout('if(!navi.flag)hideElement("more_list_con");', 200);
}},openMusPlayer:function() {
},checkForm:function(flag) {
    var suffix = flag || "";
    var env = MUSIC.event.getEvent();
    var _t = env.clientY - 15 + MUSIC.dom.getScrollTop();
    var _l = MUSIC.dom.getClientWidth() / 2 - 150;
    if ((trim(Element("search_form" + suffix).w.value) == "") && (trim(Element("search_form_foot" + suffix).w.value) == "")) {
        MUSIC.dialog.createInfoBox("?????????", 1.5, 2, _t, _l);
        return false;
    }
    return true;
},_pClassName:"",ie6hover:function(obj, type) {
    if (ua.ie != 6)
        return;
    if (type == 1) {
        this._pClassName = obj.className;
        obj.className = this._pClassName + " on";
    } else
        obj.className = this._pClassName;
},ie6btnhover:function(obj, type) {
    if (ua.ie != 6 || /_n/.test(obj.className))
        return;
    if (type == 1)
        obj.className = obj.className + "_h"; else
        obj.className = obj.className.replace("_h", "");
},ie6Tophover:function(obj, type) {
    if (ua.ie != 6)
        return;
    if (type == 1) {
        this._pClassName = obj.className;
        obj.className = this._pClassName + " hover";
    } else
        obj.className = this._pClassName;
},getQQMusDownUrl:function(url) {
    var res = "";
    var result = url.match(/(\d)+/gi);
    var type = getParameter("t");
    var useWma = (type == "2");
    if (!result || result.length != 2) {
        res = url;
    } else if (useWma) {
        res = url;
    } else {
        var steam = parseInt(result[0]);
        var songid = parseInt(result[1]) - 12000000 + 30000000;
        res = "http://stream" + (steam + 10) + ".music.soso.com/" + songid
                + ".mp3";
    }
    return res;
},srhKeyWord:function(value, flag) {
    value = value || "";
    if (typeof(value) == "object") {
        value = value.title;
    }
    if (!flag) {
        window.open("http://cgi.music.soso.com/fcgi-bin/m.q?source=1&w="
                + UrlEncode(value), "_self");
    } else
        window.open("http://cgi.music.soso.com/fcgi-bin/m.q?source=1&w="
                + UrlEncode(value), "_blank");
}}
function addBookMark() {
    var url = "http://music.soso.com";
    var title = document.title;
    if (window.sidebar) {
        window.sidebar.addPanel(title, url, "");
    } else if (document.all) {
        window.external.AddFavorite(url, title);
    } else if (window.opera && window.print) {
        return true;
    }
}
window.gcomm = MUSIC.widget.gcomm;
window.navi = MUSIC.widget.gcomm.navi;
function FormatSosoMusic(obj) {
    var re = new RegExp("<\\w[^>]+class=([\"|\'])?data([\"|\'])?[^>]*>(.*?)<\\/\\w[^>]*>", "mi");
    var arrTmp = ["mid","msong","malbum","msinger","msize","mformat","mconn","iInteral","msongurl","msingerid","malbumid","mdownload"];
    var length = arrTmp.length;
    var arrMusic = [];
    var i = 0;
    if ((arrMusic = re.exec(obj.innerHTML.replace(/&amp;/mgi, "&"))) != null) {
        arrMusic = arrMusic[3].split("@@");
        if (arrMusic.length < 8) {
            for (i = 0; i < length; i++)
                this[arrTmp[i]] = "";
            if (arrMusic.length < 6)
                this["error"] = 1; else {
                this.mid = arrMusic[0];
                this.msong = arrMusic[1];
                this.msingerid = arrMusic[2];
                this.msinger = arrMusic[3];
                this.malbumid = arrMusic[4];
                this.malbum = arrMusic[5];
                if (arrMusic.length > 6) {
                    this.msongurl = arrMusic[6];
                    var songurl = this.msongurl;
                    var formator = new FormateSongUrl(songurl);
                    this.mapSongUrl = formator.mapSongUrl || [];
                    this.mapSongUrlStr = formator.mapSongUrlStr || [];
                    this.urls = formator.urls || {};
                }
            }
            return;
        }
    } else {
        this["error"] = 1;
        for (i = 0; i < length; i++) {
            this[arrTmp[i]] = "";
        }
        return;
    }
    if (arrMusic.length < 2) {
        this["error"] = 1;
    }
    _length = Math.min(length, arrMusic.length);
    for (i = 0; i < _length; i++) {
        this[arrTmp[i]] = arrMusic[i];
    }
    for (i = _length; i < length; i++) {
        this[arrTmp[i]] = "";
    }
    var songurl = this["msongurl"];
    var formator = new FormateSongUrl(songurl);
    this.mapSongUrl = formator.mapSongUrl || [];
    this.mapSongUrlStr = formator.mapSongUrlStr || [];
    this.urls = formator.urls || {};
}
function getUserIsp()
{
    var ispFlag = Cookie.get("isp_flag");
    var ispName;
    switch (parseInt(ispFlag))
    {case 1:ispName = "??";break;case 2:ispName = "??";break;case 3:ispName = "???";break;case 4:ispName = "??";break;case 5:ispName = "??";break;case 6:ispName = "????";break;default:ispName = "??";break;
    }
    return ispName;
}
function FormateSongUrl(songurl) {
    this.urls = {};
    this.mapSongUrl = [];
    this.mapSongUrlStr = [];
    var urls = songurl.split("|");
    var CLS = function() {
        this.url = "",this.source = "",this.init = function() {
            this.url = "";
            this.source = "";
        }
    }
    this.urls.QQ = this.urls.QQ || [];
    this.urls.QQ128 = this.urls.QQ128 || [];
    this.urls.FI = this.urls.FI || [];
    this.urls.SI = this.urls.SI || [];
    this.urls.AN = this.urls.AN || [];
    var userIsp = getUserIsp();
    var reshuffleFlag = 0;
    if (urls && urls.length > 0) {
        reshuffleFlag = 0;
        for (var i = urls.length - 1; i >= 0; i--) {
            var tmp = urls[i].split(";")
            if (!tmp || !tmp[0])
                continue;
            if (/^(FI)/.test(tmp[0])) {
                for (var j = 0; j < tmp.length; j = j + 2) {
                    var _cls = new CLS();
                    if (!tmp[j])
                        break;
                    _cls.url = tmp[j].replace(/^(FI)/, "");
                    _cls.source = tmp[j + 1] || "??";
                    if (_cls.url.indexOf("qqmusic.qq.com") == -1 && _cls.url.indexOf("music.soso.com") == -1)
                        this.urls.FI.push(_cls); else if (1) {
                        var _cls1 = new CLS();
                        if (_cls.source == "??")
                            _cls.source = userIsp;
                        _cls1.source = _cls.source;
                        this.urls.QQ.push(_cls);
                        _cls1.url = gcomm.getQQMusDownUrl(_cls.url);
                        this.urls.QQ128.push(_cls1);
                    }
                    if (reshuffleFlag == 1 && j == 0)
                    {
                        this.urls.FI.push(this.urls.QQ128[0]);
                        for (var k = 0; k < this.urls.AN.length; k++)
                            this.urls.FI.push(this.urls.AN[k]);
                    }
                }
            } else if (/^(SI)/.test(tmp[0])) {
                for (var j = 0; j < tmp.length; j = j + 2) {
                    var _cls = new CLS();
                    if (!tmp[j])
                        break;
                    _cls.url = tmp[j].replace(/^(SI)/, "");
                    _cls.source = tmp[j + 1] || "??";
                    this.urls.SI.push(_cls);
                }
            } else if (/^(AN)/.test(tmp[0])) {
                var _cls = new CLS();
                _cls.url = tmp[0].replace(/^(AN)/, "");
                _cls.source = tmp[1] || "??";
                this.urls.AN.push(_cls);
            } else if (1 && /^(QQ)/.test(tmp[0])) {
                var _cls = new CLS();
                _cls.url = tmp[0].replace(/^(QQ)/, "");
                _cls.source = tmp[1] || "??";
                if (_cls.source == "??")
                    _cls.source = userIsp;
                if (1 || (_cls.url.indexOf("qqmusic.qq.com") == -1 && _cls.url.indexOf("music.soso.com") == -1))
                    this.urls.QQ.push(_cls);
                var _cls1 = new CLS();
                _cls1.source = _cls.source;
                if ((_cls.url.indexOf("qqmusic.qq.com") != -1 || _cls.url.indexOf("music.soso.com") != -1) && 1) {
                    _cls1.url = gcomm.getQQMusDownUrl(_cls.url);
                    this.urls.QQ128.push(_cls1);
                    reshuffleFlag = 1;
                }
            }
        }
        if (reshuffleFlag == 0)
        {
            this.mapSongUrl = this.urls.QQ128.concat(this.urls.AN.concat(this.urls.FI.concat(this.urls.SI)));
            var mapSongUrlStrTemp = this.urls.QQ.concat(this.urls.AN.concat(this.urls.FI.concat(this.urls.SI)));
        }
        else
        {
            this.mapSongUrl = this.urls.FI.concat(this.urls.SI);
            var mapSongUrlStrTemp = this.urls.FI.concat(this.urls.SI);
        }
        for (var i = 0; i < mapSongUrlStrTemp.length; i++) {
            this.mapSongUrlStr.push(mapSongUrlStrTemp[i].url);
        }
        if (this.urls.QQ128.length < 1)
            this.urls.QQ128 = null;
        if (this.urls.QQ.length < 1)
            this.urls.QQ = null;
        if (this.urls.AN.length < 1)
            this.urls.AN = null;
        if (this.urls.SI.length < 1)
            this.urls.SI = null;
        if (this.urls.FI.length < 1)
            this.urls.FI = null;
    }
}
function generQMusicKey(flag) {
    var loaded = Cookie.get("qqmusic_fromtag");
    if (!loaded || !!flag) {
        Cookie.set("qqmusic_fromtag", 10, "soso.com");
        Cookie.set("qqmusic_sosokey", "4D96476733A6D833E90FEA9E590408D171B92452775E15FB", "soso.com");
    }
}
function initXSOSO() {
    var _url = window.location.toString();
    var _id = 0;
    var s1 = window.location.href;
    var s2 = window.location.host;
    var index = s1.lastIndexOf(s2) + s2.length;
    var s3 = s1.substring(index);
    if (s3 == "/" || s3 == "/index.html") {
        _id = 1;
    } else {
        var _page = [/\/portal\/hit/,/\/portal\/singer/,/\/portal\/albumn/,/\/portal\/taoge/,/\/portal\/topic/,/\/portal\/shoufa/];
        for (var i = 0,_length = _page.length; i < _length; i++) {
            if (_url.search(_page[i]) > 0) {
                _id = i + 2;
                break;
            }
        }
    }
    if ((_id == 1) || (_url.search(/\/index.html/) > 0) || (_url.search(/\/portal\/albumn\/hot\/albumn_hot_/) > 0))
    {
        (Element('xmusic_top') && (Element('xmusic_top').className = 'xsoso_nav'));
    } else(Element('xmusic_top') && (Element('xmusic_top').className = 'xsoso_nav xnav_2'));
    (Element('xsoso_top_' + _id) && (Element('xsoso_top_' + _id).className = 'on'));
}
function main() {
    document.getElementsByTagName("body")[0].onbeforeunload = function() {
        var d = new Date();
        Cookie.set("TRANS_TIME_POINT", d.getTime());
    }
    try {
        watchSearchCommit();
    } catch(e) {
    }
    user.loginer().checkLogin();
    generQMusicKey();
    initXSOSO();
    try {
        document.execCommand("BackgroundImageCache", false, true);
    } catch(e) {
    }
}
addEvent(window, "load", main);
window.onerror = function() {
    return true;
}

MUSIC.widget.user = {reportCount:0,uin:-1,getUin:function() {
    var _t = MUSIC.cookie.get("uin").match(/[123456789]{1}(\d)+/g);
    this.uin = !_t ? 0 : _t[0];
    if (this.uin > 0) {
    } else
        this.uin = 0;
    return this.uin;
},getKey:function() {
    return(MUSIC.cookie.get("verifysession"));
},getSKey:function() {
    return(MUSIC.cookie.get("skey"));
},getNick:function() {
    var nickname = unescape(MUSIC.cookie.get("nickname"));
    return nickname;
},isLogin:function() {
    return!!this.getUin();
},getGUin:function() {
    var guid = MUSIC.cookie.get("g_newuid");
    if (!guid) {
        var curDate = new Date();
        var curMs = curDate.getUTCMilliseconds();
        guid = (Math.round(Math.random() * 2147483647) * curMs) % 1000000000 + 10000;
        Cookie.set("g_newuid", guid, "soso.com");
    }
    if (!guid)
        return user.getUin();
    return guid;
},clear:function(force) {
    MUSIC.config.DCCookieDomain = "soso.com";
    MUSIC.cookie.del("sopass");
    MUSIC.cookie.del("uin");
    MUSIC.cookie.del("skey");
    MUSIC.config.DCCookieDomain = "music.soso.com";
    MUSIC.cookie.del("nickname");
    MUSIC.cookie.del("player_login");
    MUSIC.cookie.del("run_count");
    MUSIC.cookie.del("reportFlag");
    MUSIC.cookie.del("city_music_flag");
    user.reportCount = 0;
},loginer:function() {
    var appid = 6000501;
    var config = {target:"parent",f_url:"loginerroralert",width:373,height:280,cb_simple:null,cb_info:null,cb_simple_url:"http://cache.music.soso.com/sosocache/music/loginsuccess.html",logout_callback:function() {
        top.location.reload();
    },mask:true,auto_login:{url:"http://i.soso.com/music/loginfo"}};
    var localVars = ";width;height;left;top;mask;cb_simple;cb_info;cb_simple_url;cb_info_url;logout_callback;auto_login;uin;";
    return{setConfig:function(oConfig) {
        for (var prop in oConfig) {
            if (typeof oConfig[prop] == "undefined") {
                config[prop] = "";
            } else {
                config[prop] = oConfig[prop];
            }
        }
        return this;
    },doLogin:function() {
        if ($("musicFlash"))
            inserSosoWebPlayer(1);
        var oLoginDiv = $("login_div");
        if (null !== oLoginDiv) {
            oLoginDiv.parentNode.removeChild(oLoginDiv);
        }
        if (config.mask) {
            window._LoginMaskId = MUSIC.maskLayout.create();
        }
        oLoginDiv = document.createElement("div");
        oLoginDiv.id = "login_div";
        oLoginDiv.style.zIndex = 9999;
        oLoginDiv.style.display = "none";
        oLoginDiv.style.position = "absolute";
        oLoginDiv.style.width = config.width + 'px';
        oLoginDiv.style.height = config.height + 'px';
        oLoginDiv.style.padding = '0px';
        oLoginDiv.style.margin = '0px';
        oLoginDiv.align = "center";
        document.body.appendChild(oLoginDiv);
        oLoginDiv.innerHTML = '<iframe id="login_frame" frameborder="0" scrolling="no" width="100%" height="100%" src="" onload="changeJumpTarget();"></iframe>';
        function ietruebody() {
            return(document.compatMode && document.compatMode != "BackCompat") ? document.documentElement : document.body;
        }

        var iDocumentWidth,iDocumentHeight,iLeft,iTop;
        if (document.all) {
            iDocumentWidth = ietruebody().offsetWidth / 2
                    + ietruebody().scrollLeft - 20;
            iDocumentHeight = ietruebody().offsetHeight / 2
                    + ietruebody().scrollTop - 20;
        } else if (document.layers) {
            iDocumentWidth = window.innerWidth / 2 + window.pageXOffset
                    - 20;
            iDocumentHeight = window.innerHeight / 2
                    + window.pageYOffset - 20;
        } else if ($ && !document.all) {
            iDocumentWidth = self.innerWidth / 2 + window.pageXOffset
                    - 20;
            iDocumentHeight = self.innerHeight / 2 + window.pageYOffset
                    - 20;
        }
        var iLeft = iDocumentWidth - 150;
        var iTop = iDocumentHeight - 250;
        iTop = iTop < 100 ? 100 : iTop;
        oLoginDiv.style.left = (config.left ? config.left : iLeft)
                + "px";
        oLoginDiv.style.top = (config.top ? config.top : iTop) + "px";
        oLoginDiv.style.display = "block";
        if (!config.s_url) {
            config.s_url = /#$/.test(window.location.href) ? window.location.href.substr(0, window.location.href.length - 1) : window.location.href;
        }
        if (config.uin) {
            user.uin = config.uin;
        }
        var sSrc = "http://ui.ptlogin2.soso.com/cgi-bin/login?appid="
                + appid;
        for (var prop in config) {
            var sType = typeof config[prop];
            var regExp = new RegExp(";" + prop + ";");
            if ((sType == "string" || sType == "number") && !regExp.test(localVars)) {
                sSrc += "&" + encodeURIComponent(prop) + "="
                        + encodeURIComponent(config[prop]);
            }
        }
        $("login_frame").src = sSrc;
        return this;
    },checkLogin:function() {
        user.uin = user.getUin();
        var nickname = user.getNick();
        if (!!user.uin && !!nickname) {
            this.show({uin:user.uin,nick:nickname,flag:true});
        } else if (!!user.uin) {
            var js = new MUSIC.JsLoader();
            js.load("http://i.soso.com/music/loginfo");
        } else
            this.show({uin:0,nick:"",flag:true});
        return this;
    },doLogout:function() {
        user.clear();
        config.logout_callback();
        return this;
    },show:function(data) {
        if ($("auto_check_login") != null && user.reportCount < 1)
        {
            MUSIC.cookie.set("reportFlag", 0);
        }
        if (typeof(MUSIC.cookie.get("reportFlag")) == "undefined" || MUSIC.cookie.get("reportFlag") == "" || MUSIC.cookie.get("reportFlag") == "0")
        {
            !data.flag && g_stat.sosoData(1, "", "", "", "");
            MUSIC.cookie.set("reportFlag", 1);
            user.reportCount++;
        }
        var oAuto = $("auto_check_login");
        if (null === oAuto) {
            if (user.reportCount < 1)
            {
                MUSIC.cookie.set("reportFlag", 0);
            }
            return false;
        }
        var aTpls = oAuto.innerHTML.match(/<!--(.*?)-->/g);
        for (var i = 0; i < aTpls.length; i++) {
            aTpls[i] = aTpls[i].substring(4, aTpls[i].length - 3);
        }
        if (data.uin) {
            Cookie.set("nickname", escape(data.nick), "music.soso.com");
            oAuto.innerHTML = aTpls[0].replace(/\__uin__/gi, data.uin).replace(/__nick__/gi, data.nick.Text2HTML().replace(/\$/gi, ""));
            var oLogout = $("logout");
            if (!oLogout.onclick) {
                oLogout.onclick = function() {
                    user.loginer().doLogout();
                    return false;
                };
            }
        } else {
            oAuto.innerHTML = aTpls[1];
            var oLogin = $("login");
            if (!oLogin.onclick) {
                $("login").onclick = function() {
                    user.loginer().doLogin();
                    return false;
                };
            }
        }
        showElement(oAuto);
        oAuto.style.zIndex = 10000;
        try {
            oAuto.getElementsByTagName("a")[3].href = "http://i.music.soso.com/music/albums";
        } catch(e) {
        }
    }};
}}
var user = MUSIC.widget.user;
function changeJumpTarget()
{
    var iframeNode = $("login_frame").contentWindow.document;
    if (iframeNode.getElementById("label_newreg"))
        iframeNode.getElementById("label_newreg").target = "_blank";
    if (iframeNode.getElementById("label_forget_pwd"))
        iframeNode.getElementById("label_forget_pwd").target = "_blank";
}
window.ptlogin2_onClose = function() {
    if ($("musicFlash"))
        inserSosoWebPlayer(0);
    $("login_div").style.display = "none";
    (window._LoginMaskId > -1) && MUSIC.maskLayout.remove(window._LoginMaskId);
    clearTimeout(checkLoginForPlayerID);
    if ($("musicFlash") && !user.isLogin())
    {
        location.reload();
    }
};
window.com = window.com || {};
window.com.soso = window.com.soso || {};
window.com.soso.libbetter = window.com.soso.libbetter || {};
window.com.soso.libbetter.login = window.com.soso.libbetter.login || {};
window.com.soso.libbetter.login.loginCb = user.loginer().show;

MUSIC.widget.statistics = {checkUrl:function(songUrl) {
    if (!songUrl.localeCompare(''))
    {
        return 0;
    }
    var strEnd = songUrl.indexOf("/", 7);
    var _url = songUrl.substring(7, strEnd);
    var qqUrl = /.music.soso.com/;
    var ret = 0;
    if (_url.search(qqUrl) > 0) {
        ret = 1;
        return ret;
    } else {
        var animUrl = /^([1-9]|[1-9]\d|1\d{2}|2[0-1]\d|22[0-3])(\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])){3}$/;
        if (animUrl.test(_url))
        {
            ret = 2;
            return ret;
        } else {
            ret = 3;
            return ret;
        }
    }
},sosoData:function(type, songName, singerName, albumName, songUrl, xSoso) {
    var urlSource = "";
    if ((type == 7) || (type == 6))
    {
    } else urlSource = this.checkUrl(songUrl);
    var uin = user.getGUin();
    var uinLogin = user.getUin();
    var base_url = "http://cgi.music.soso.com/fcgi-bin/fcg_tj2.q?msgid=2080000061&num=10&uin=";
    var url = "";
    if ((type == 7) || (type == 6))
    {
        var hostUrl = "";
        var host = "";
        var index = 0;
        hostUrl = document.referrer;
        index = hostUrl.indexOf("/", 7);
        host = hostUrl.substring(0, index);
        if (type == 7)
        {
            url = base_url + uinLogin + "&type=7&searchKeyword=&searchType=0&songName=&singerName=&albumName=&bak1=" + uin + "&bak2=" + host + "&bak3=";
        } else if (type == 6)
        {
            url = base_url + uinLogin + "&type=6&searchKeyword=&searchType=" + songName + "&songName=&singerName=&albumName=&bak1=" + uin + "&bak2=" + host + "&bak3=";
        }
    } else {
        if ((typeof(xSoso) == 'undefined') && (typeof(xsosoFlag) == 'undefined'))
        {
            xsosoFlag = '0';
        } else if (typeof(xsosoFlag) == 'undefined')
        {
            xsosoFlag = xSoso;
        }
        if (type == 2 || type == 4)
        {
            if (type == 2)
            {
                if (xSoso)
                {
                    xsosoFlag = '1';
                } else
                    xsosoFlag = '0';
            }
            url = base_url + uin + "&type=" + type + "&searchKeyword=" + "" + "&searchType=" + 0 + "&songName=" + UrlEncode(songName)
                    + "&singerName=" + UrlEncode(singerName) + "&albumName=" + UrlEncode(albumName) + "&bak1=" + urlSource + "&bak2=" + xsosoFlag + "&bak3=" + " ";
        } else if (type == 1)
        {
            url = base_url + uinLogin + "&type=" + type + "&searchKeyword=" + "" + "&searchType=" + 0 + "&songName=" + UrlEncode(songName)
                    + "&singerName=" + UrlEncode(singerName) + "&albumName=" + UrlEncode(albumName) + "&bak1=" + uin + "&bak2=" + " " + "&bak3=" + " ";
        } else
            url = base_url + uin + "&type=" + type + "&searchKeyword=" + "" + "&searchType=" + 0 + "&songName=" + UrlEncode(songName)
                    + "&singerName=" + UrlEncode(singerName) + "&albumName=" + UrlEncode(albumName) + "&bak1=" + urlSource + "&bak2=" + " " + "&bak3=" + " ";
    }
    var sImag = new Image();
    sImag.src = url + "&p=" + Math.random();
    sImag.style.width = 0;
    sImag.style.height = 0;
},submitPlayForEng:function(singer, song, album, url) {
    this.sosoDataForEng(2, "", "", singer, song, album, url, "", 0, "", 0, 0, "", "");
},submitDownloadForEng:function(singer, song, album, url) {
    this.sosoDataForEng(3, "", "", singer, song, album, url, "", 0, "", 0, 0, "", "");
},submitCerrectForEng:function(obj) {
    var keyword = document.getElementsByName("w")[0].value;
    var cerrectKey = obj.title;
    this.sosoDataForEng(4, keyword, "", "", "", "", "", "", 0, "", 0, 0, "", cerrectKey);
},submitSearchResultForEng:function(obj) {
    var objParentNode = obj.parentNode.parentNode;
    var clientY = objParentNode.index;
    var clientX = document.getElementsByName("p")[0].value;
    var musicData = MUSIC.dom.getFirstChild(objParentNode).innerHTML;
    var startIndex = musicData.indexOf("@@");
    var endIndex = musicData.indexOf("@@", startIndex + 2);
    var song = musicData.substring(startIndex + 2, endIndex);
    startIndex = endIndex + 2;
    endIndex = musicData.indexOf("@@", startIndex);
    var album = musicData.substring(startIndex, endIndex);
    startIndex = endIndex + 2;
    endIndex = musicData.indexOf("@@", startIndex);
    var singer = musicData.substring(startIndex, endIndex);
    this.sosoDataForEng(6, "", "", singer, song, album, "", musicData, 0, "", clientX, clientY, "", "");
},sosoDataForEng:function(type, keyword, encodeKeyword, singer, song, album, url, musicData, resultNum, ip, clientX, clientY, referencePage, cerrectKey) {
    var uin = user.getGUin();
    var base_url = "http://cgi.music.soso.com/fcgi-bin/fcg_tj2.q?msgid=2080000062&num=18&uin=";
    var url = base_url + uin + "&type=" + type + "&keyword=" + UrlEncode(keyword) + "&encodeKeyword=" + UrlEncode(encodeKeyword) + "&singer=" + UrlEncode(singer)
            + "&song=" + UrlEncode(song) + "&album=" + UrlEncode(album) + "&url=" + UrlEncode(url) + "&musicData=" + UrlEncode(musicData) + "&resultNum=" + resultNum + "&ip=" + ip
            + "&clientX=" + clientX + "&clientY=" + clientY + "&referencePage=" + referencePage + "&cerrectKey=" + UrlEncode(cerrectKey) + "&bak1=" + 0 + "&bak2=" + " " + "&bak3=" + " ";
    var sImag = new Image();
    sImag.src = url + "&p=" + Math.random();
    sImag.style.width = 0;
    sImag.style.height = 0;
}}
var g_stat = MUSIC.widget.statistics;

MUSIC.widget.collect = {version:"1.0.0",webqqFlag:(typeof(playerSource) != "undefined") ? playerSource : 0,webqqUin:(typeof(postUin) != "undefined") ? postUin.match(/[123456789]{1}(\d)+/g) : 0,webqqKey:(typeof(postKey) != "undefined") ? postKey : "",m_dirNum:0,addFailFlag:0,emptyList:false,commonList:[],dirList:[],music:null,_t:0,_l:0,_fromPortalFlagDivFlag:false,_evn:null,_fromPortalFlag:0,_defaultDirId:1,getDirList:function(flag, fromPortal, obj, event) {
    function err_cb()
    {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("????????");
        } else MUSIC.dialog.createInfoBox("????????", 1, 1, this._t - 80, this._l - 40);
    }

    if (fromPortal)
    {
        if (!flag)
        {
            this.music = new FormatSosoMusic(obj);
            this._t = event.clientY + getScrollTop();
            this._l = event.clientX + getScrollLeft();
            this._evn = event;
        }
    }
    if (user.isLogin())
    {
        var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=1&dirid=200&uin=" + user.getUin() + "&p=" + Math.random();
        JsonLoadData(url, this.handleGetDirList.bind(this, flag, fromPortal), err_cb, "jsonCallback");
    }
    else if (MUSIC.widget.collect.webqqFlag == 2)
    {
        if (parseInt(MUSIC.widget.collect.webqqUin) > 0)
        {
            var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=1&dirid=200&uin=" + MUSIC.widget.collect.webqqUin + "&p=" + Math.random();
            JsonLoadData(url, this.handleGetDirList.bind(this, flag, fromPortal), err_cb, "jsonCallback");
        }
    }
    else
    {
        user.loginer().doLogin();
        if (!fromPortal)
        {
            checkLoginForPlayer();
        }
    }
},handleGetDirList:function(flag, fromPortal, data) {
    this.initDirArray(data);
    this.setQQCookie();
    if (fromPortal)
    {
        if (!flag)
        {
            var arrHTML = new Array();
            var oDiv = getElementInBody("sosoCollectTips", "div", null, null, "collect_tips");
            if (!oDiv)return;
            if (this.commonList.length > 4)
            {
                arrHTML.push("<div class=\"collect_list max\"><ul>");
            } else arrHTML.push("<div class=\"collect_list\"><ul>");
            for (var i = 0; i < this.commonList.length; i++)
            {
                arrHTML.push("<li><a href=\"#\" onclick=\"collect.addSongToCollectFromPortal(" + i + ");hideElement('sosoCollectTips');return false;\" title='" + this.commonList[i].name + "'>" + this.commonList[i].name + "</a></li>");
            }
            arrHTML.push("</ul></div><div class=\"line\"></div><p><a href=\"#\" onclick=\"collect.addSongToCollectFromPortal(-1);collect._fromPortalFlag=1;hideElement('sosoCollectTips');return false;\" title='??????'>??????</a></p>");
            oDiv.innerHTML = arrHTML.join("");
            if (oDiv.style.display == "block")
            {
                oDiv.style.display = "none";
                this._fromPortalFlagDivFlag = false;
            } else {
                oDiv.style.display = "block";
                this._fromPortalFlagDivFlag = true;
            }
            if (ua.ie)
            {
                oDiv.style.pixelTop = this._t + 5;
                oDiv.style.pixelLeft = this._l;
            } else {
                oDiv.style.top = this._t + 5 + "px";
                oDiv.style.left = this._l + "px";
            }
        }
    } else {
        var oFlash = $(flashId);
        if (oFlash)
        {
            oFlash.setSwfRankList(1, this.commonList);
            if (curTabIndex == curListIndex)
            {
                if (curPlayCollectId >= 0)
                    oFlash.setSwfListPlayIcon(curTabIndex, curPlayCollectId);
            }
        }
        else
            showInfoBox("???????????????????");
    }
    if (flag == 1)
    {
        if (addToNewList != "")
        {
            if (movesongFlag == 1)
            {
                if (collect.webqqFlag == 2)
                    var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_movesong_v2.q"; else
                    var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_movesong.q";
                var data = {formsender:2,dirfrom:g_dirFrom,dirto:g_dirTo,ids:addToNewList,types:dirTypeList,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin()};
                var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
                fs.onSuccess = function(o) {
                    collect.moveSongCallback(o);
                };
                fs.onError = collect.moveSongFailInfo;
                fs.send();
            }
            else
            {
                if (collect.webqqFlag == 2)
                    var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav_v2.q"; else
                    var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav.q";
                var data = {dirid:(collect.dirList[collect.dirList.length - 1]) ? collect.dirList[collect.dirList.length - 1].dirid : 0,formsender:2,idlist:addToNewList,source:142,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin()};
                var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
                fs.onSuccess = function(o) {
                    collect.addSong2FavCallback(o);
                };
                fs.onError = collect.addSongFailInfo;
                fs.send();
            }
        }
        if (addToNewListForUrl != "")
        {
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav_url.q";
            var data = {uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),songtitle:addToNewListForUrlSongList,singer:addToNewListForUrlSingerList,url:addToNewListForUrl,dirid:(collect.dirList[collect.dirList.length - 1]) ? collect.dirList[collect.dirList.length - 1].dirid : 0};
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.addSong2FavForUrlCallback(o);
            };
            fs.onError = collect.addSongForUrlFailInfo;
            fs.send();
        }
    }
    return;
},initDirArray:function(data) {
    this.commonList = [];
    this.dirList = [];
    var musicJson = data;
    if (!musicJson || typeof(musicJson) != "object")
    {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("???????????????????");
        } else MUSIC.dialog.createInfoBox("???????????????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
    if (musicJson.code == 0)
    {
        var dirnum = musicJson.DirList.length;
        if (dirnum == 0)
        {
            this.m_dirNum = 0;
            return;
        }
        var dirNodes = musicJson.DirList;
        var dirInfo = null;
        var dirInfoMore = null;
        for (var i = 0,l = dirNodes.length; i < l && i < dirnum; i++)
        {
            dirInfo = {id:parseInt(i),name:(dirNodes[i].DirName != null) ? dirNodes[i].DirName.entityReplace() : "no info"}
            dirInfoMore = {id:parseInt(i),dirid:(dirNodes[i].DirID != null) ? dirNodes[i].DirID : 0,name:(dirNodes[i].DirName != null) ? dirNodes[i].DirName : "no info"}
            g_dirTo = dirInfoMore.dirid;
            if (i == 0)
            {
                this._defaultDirId = dirInfo.id;
            }
            this.commonList.push(dirInfo);
            this.dirList.push(dirInfoMore);
        }
        Cookie.set("dirlistnum", this.dirList.length);
        if (this.commonList.length == 0)
        {
            this.m_dirNum = 0;
            return;
        }
        this.m_dirNum = this.commonList.length;
    }
    else
    {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("???????????????");
        } else MUSIC.dialog.createInfoBox("???????????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
},getSongList:function(dirid) {
    function err_cb()
    {
        showInfoBox("?????????????!");
    }

    $(flashId).setSwfSongNum(curTabIndex, dirid, 0);
    if (user.isLogin())
    {
        if (this.dirList[dirid])
            var realDirId = this.dirList[dirid].dirid; else
            var realDirId = 0;
        var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=0&dirid=" + realDirId + "&uin=" + user.getUin() + "&p=" + Math.random();
        JsonLoadData(url, this.handleGetSongList.bind(this, dirid), err_cb, "jsonCallback");
    }
    else if (MUSIC.widget.collect.webqqFlag == 2)
    {
        if (parseInt(MUSIC.widget.collect.webqqUin) > 0)
        {
            if (this.dirList[dirid])
                var realDirId = this.dirList[dirid].dirid; else
                var realDirId = 0;
            var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=0&dirid=" + realDirId + "&uin=" + MUSIC.widget.collect.webqqUin + "&p=" + Math.random();
            JsonLoadData(url, this.handleGetSongList.bind(this, dirid), err_cb, "jsonCallback");
        }
    }
    else
    {
        user.loginer().doLogin();
        checkLoginForPlayer();
    }
},handleGetSongList:function(dirid, data) {
    this.initSongArray(dirid, data);
    var oFlash = $(flashId);
    if (oFlash)
    {
        oFlash.setSwfSongList(g_songList[1][dirid]);
        if (g_songList[1][dirid].length == 0) {
            $(flashId).setSwfNoSongTips(true);
        } else {
            $(flashId).setSwfNoSongTips(false);
        }
        if (curTabIndex == curListIndex)
        {
            oFlash.setSwfScroll(curSongIndex);
            if (g_subTab == curPlayCollectId)
                oFlash.setSwfHighLight(curSongIndex, 0);
            if (g_songList[1][dirid].length == 0) {
                $(flashId).setSwfListPlayIcon(-1, -1);
                $(flashId).clearSwfHighLight();
            }
        }
    }
    else
    {
        showInfoBox("???????????????????");
    }
},handleGetSongNum:function(dirid, data) {
    var musicJson = data;
    if (!musicJson || typeof(musicJson) != "object")
    {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("???????????????????");
        } else MUSIC.dialog.createInfoBox("???????????????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
    if (musicJson.code == 0)
    {
        var songList = addToNewList.split(",");
        if (musicJson.CurNum >= 1000 || (musicJson.CurNum + songList.length) > 1000)
        {
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox("???????????????");
            } else MUSIC.dialog.createInfoBox("???????????????", 1, 1, this._t - 80, this._l - 40);
            return;
        }
        if (addToNewList != "")
        {
            if (collect.webqqFlag == 2)
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav_v2.q"; else
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav.q";
            var data = {dirid:dirid,formsender:2,idlist:addToNewList,source:142,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin()};
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.addSong2FavCallback(o);
            };
            fs.onError = collect.addSongFailInfo;
            fs.send();
        }
        if (addToNewListForUrl != "")
        {
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_add2fav_url.q";
            var data = {uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),songtitle:addToNewListForUrlSongList,singer:addToNewListForUrlSingerList,url:addToNewListForUrl,dirid:dirid};
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.addSong2FavForUrlCallback(o);
            };
            fs.onError = collect.addSongForUrlFailInfo;
            fs.send();
        }
        if (addFailFlag == 1) {
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox("????????????");
            } else MUSIC.dialog.createInfoBox("??????????", 1, 1, this._t - 80, this._l - 40);
        }
        return;
    }
},initSongArray:function(dirid, data) {
    g_songList[1] = g_songList[1] || {};
    g_songList[1][dirid] = [];
    var musicJson = data;
    if (!musicJson || typeof(musicJson) != "object")
    {
        showInfoBox("???????????????????");
        return false;
    }
    if (musicJson.code == 0)
    {
        var musicnum = (musicJson.SongNum) ? parseInt(musicJson.SongNum) : 0;
        var oFlash = $(flashId);
        if (musicnum == 0)
        {
            return;
        }
        var songNodes = (musicJson.SongList) ? musicJson.SongList : [];
        if (songNodes.length == 0)
        {
            if (oFlash)
                oFlash.setSwfNoSongTips(true);
            return;
        }
        oFlash.setSwfNoSongTips(false);
        var songInfo = null;
        for (var i = songNodes.length - 1; i >= 0; i--)
        {
            songInfo = {id:(songNodes[i].id != null) ? songNodes[i].id : 0,type:parseInt((songNodes[i].type != null ? songNodes[i].type : 3), 10),url:(songNodes[i].url != "") ? ((songNodes[i].url.indexOf("qqmusic.qq.com") == -1) ? songNodes[i].url : songNodes[i].url.replace("qqmusic.qq.com", "music.soso.com")) : "",songName:(songNodes[i].songname != null) ? songNodes[i].songname : "no info",singerId:(songNodes[i].singerid != null) ? songNodes[i].singerid : 0,singerName:(songNodes[i].singername != null) ? songNodes[i].singername : "no info",albumId:(songNodes[i].diskid != null) ? songNodes[i].diskid : 0,albumName:(songNodes[i].diskname != null) ? songNodes[i].diskname.toString().substr(0, 30) : "",albumLink:"",playtime:0,urls:""}
            g_songList[1][dirid].push(songInfo);
        }
    }
    else
    {
        if (musicJson.code == 1)
        {
            user.loginer().doLogin();
            checkLoginForPlayer();
            return false;
        }
        showInfoBox("?????????????");
        return false;
    }
    $(flashId).setSwfSongNum(curTabIndex, dirid, getCurTabSongNum() || 0);
},setQQCookie:function() {
    var oForm = document.getElementById("setCookie");
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
    MUSIC.dom.createElementIn("form", document.body, false, {id:"setCookie",onsubmit:"return;",action:"http://qzone-music.qq.com/fcg-bin/fcg_set_qqcookie.fcg",method:"get",innerHTML:"<input name=\"u\" maxlength=\"256\" /><input name=\"k\" maxlength=\"256\" />",target:"setCookieTarget"});
    Element("setCookie").u.value = (collect.webqqFlag == 2) ? collect.webqqUin : Cookie.get("uin");
    Element("setCookie").k.value = (collect.webqqFlag == 2) ? collect.webqqKey : Cookie.get("skey");
    Element("setCookie").submit();
    var oForm = document.getElementById("setCookie");
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
},setSOSOCookie:function() {
    var oForm = document.getElementById("setCookie");
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
    MUSIC.dom.createElementIn("form", document.body, false, {id:"setCookie",onsubmit:"return;",action:"http://cgi.music.soso.com/fcgi-bin/fcg_set_sosologininfo_player.q",method:"get",innerHTML:"<input name=\"u\" maxlength=\"256\" /><input name=\"k\" maxlength=\"256\" />",target:"setCookieTarget"});
    Element("setCookie").u.value = (collect.webqqFlag == 2) ? collect.webqqUin : Cookie.get("uin");
    Element("setCookie").k.value = (collect.webqqFlag == 2) ? collect.webqqKey : Cookie.get("skey");
    Element("setCookie").submit();
    var oForm = document.getElementById("setCookie");
    if (oForm != null) {
        document.body.removeChild(oForm);
    }
},dirAdd:function(addData) {
    if (addData.length == 0)
    {
        return false;
    }
    else
    {
        var dirNameList = "";
        var showList = "";
        for (var i = 0; i < addData.length; i++)
        {
            if (i == 0)
            {
                dirNameList = dirNameList + addData[i];
                showList = showList + "1";
            }
            else
            {
                dirNameList = dirNameList + "," + addData[i];
                showList = showList + ",1";
            }
        }
        if (collect.webqqFlag == 2)
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir_v2.q"; else
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir.q";
        var data = {formsender:2,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),name:dirNameList.trim(),show:showList,p:Math.random()};
        var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
        fs.onSuccess = function(o) {
            collect.addDirCallback(o);
        };
        fs.onError = collect.addFailInfo;
        fs.send();
        return false;
    }
},addFailInfo:function() {
    showInfoBox("????????");
    return;
},addDirCallback:function(o) {
    if (!o || typeof(o) != "object") {
        showInfoBox("?????????????");
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        showInfoBox("??????????");
        break;
    }
        case 1:{
            showInfoBox("?????????????");
            break;
        }
        default:{
            showInfoBox(o.msg);
            break;
        }
    }
    var oFlash = $(flashId);
    if (oFlash)
    {
        collect.getDirList();
    }
},dirMod:function(modData, delData) {
    if (modData[0] == "" && delData[0] == "")
    {
        return false;
    }
    else
    {
        var delDirs = "";
        var realDirId;
        if (delData[0].length > 0)
        {
            for (var i = 0; i < delData[0].length; i++)
            {
                realDirId = (this.dirList[delData[0][i]]) ? this.dirList[delData[0][i]].dirid : 0;
                if (i == 0)
                {
                    delDirs = delDirs + realDirId;
                }
                else
                {
                    delDirs = delDirs + "," + realDirId;
                }
            }
        }
        var modDirs = "";
        var modDirNames = "";
        var modShowList = "";
        if (modData[0].length > 0)
        {
            for (var i = 0; i < modData[0].length; i++)
            {
                realDirId = (this.dirList[modData[0][i]]) ? this.dirList[modData[0][i]].dirid : 0;
                if (i == 0)
                {
                    modDirs = modDirs + realDirId;
                    modShowList = modShowList + "1";
                    modDirNames = modDirNames + modData[1][i];
                }
                else
                {
                    modDirs = modDirs + "," + realDirId;
                    modShowList = modShowList + ",1";
                    modDirNames = modDirNames + "," + modData[1][i];
                }
            }
        }
        if (collect.webqqFlag == 2)
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_moddir_v2.q"; else
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_moddir.q";
        var data = {formsender:2,deldirids:delDirs,delnum:delData[0].length,moddirids:modDirs,moddirnames:modDirNames,moddirshows:modShowList,modnum:modData[0].length,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),p:Math.random()};
        var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
        fs.onSuccess = function(o) {
            collect.modDirCallback(o);
        };
        fs.onError = collect.modFailInfo;
        fs.send();
        return false;
    }
},modDirCallback:function(o) {
    if (!o || typeof(o) != "object") {
        showInfoBox("?????????????");
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        showInfoBox("?????????");
        break;
    }
        case 1:{
            showInfoBox("?????????????");
            break;
        }
        default:{
            showInfoBox(o.msg);
            break;
        }
    }
    var oFlash = $(flashId);
    if (oFlash)
    {
        collect.getDirList();
    }
    return;
},modFailInfo:function() {
    showInfoBox("????????");
    return;
},addToNewDir:function(o) {
    if (!o || typeof(o) != "object") {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("??????????????");
        } else MUSIC.dialog.createInfoBox("??????????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        if (typeof(flashId) != "undefined")
        {
            var oFlash = $(flashId);
            if (oFlash)
            {
                collect.getDirList(1);
            }
        }
        else if (collect._fromPortalFlag == 1)
        {
            collect.getDirList(1, 1);
            collect._fromPortalFlag = 0;
        }
        break;
    }
        case 1:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox("?????????????");
            } else MUSIC.dialog.createInfoBox("?????????????", 1, 1, this._t - 80, this._l - 40);
            break;
        }
        default:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox(o.msg);
            } else MUSIC.dialog.createInfoBox(o.msg, 1, 1, this._t - 80, this._l - 40);
            break;
        }
    }
    return;
},addToNewDirFailInfo:function() {
    if (typeof(showInfoBox) != "undefined")
    {
        showInfoBox("???????????");
    } else MUSIC.dialog.createInfoBox("???????????", 1, 1, this._t - 80, this._l - 40);
    return;
},addSongToCollect:function(dirId, songList, flag) {
    function err_cb()
    {
        showInfoBox("????????");
    }

    if ((!user.isLogin() || songList.length == 0) && !(MUSIC.widget.collect.webqqFlag == 2))
    {
        return false;
    }
    var tabId;
    if (flag == 1)
    {
        var tabTemp = getCurTab();
        tabId = tabTemp.tab;
    }
    else
    {
        tabId = (sourceTabForCollect == 1) ? curTabIndex : sourceTabForCollect;
    }
    var curSongListTmp;
    if (tabId == 5) {
        curSongListTmp = (g_songList[tabId][curTopicId]);
    } else if (tabId == 4) {
        curSongListTmp = (g_songList[tabId][curTaogeId]);
    } else if (tabId == 3) {
        curSongListTmp = (g_songList[tabId][curRankId]);
    } else if (tabId == 2) {
        curSongListTmp = (g_songList[tabId][curFreeClass]);
    } else if (tabId == 1) {
        curSongListTmp = (g_songList[tabId][(curCollectDirId == -1) ? g_collectTab : curCollectDirId]);
    } else {
        curSongListTmp = (g_songList[tabId]);
    }
    if (typeof(curSongListTmp) == "undefined")
    {
        return false;
    }
    var songIndexTemp;
    var songIdList = "";
    var songUrlList = "";
    var songTypeList = "";
    var songNameList = "";
    var singerList = "";
    addFailFlag = 0;
    if (tabId != 1)
    {
        for (var i = 0; i < songList.length; i++)
        {
            songIndexTemp = songList[i];
            if (songIndexTemp >= curSongListTmp.length)
            {
                continue;
            }
            var songObj = curSongListTmp[songIndexTemp];
            if (songObj.url == "")
            {
                addFailFlag = 1;
                continue;
            }
            if (songObj.url.indexOf("music.soso.com") != -1 || songObj.url.indexOf("qqmusic.qq.com") != -1)
            {
                var tempList = songObj.url.split("/");
                var musicID = parseInt(tempList[3]) - 12000000;
                if (i == 0)
                {
                    songIdList = songIdList + musicID;
                    songTypeList = songTypeList + songObj.type;
                }
                else
                {
                    songIdList = songIdList + "," + musicID;
                    songTypeList = songTypeList + "," + songObj.type;
                }
            }
            else
            {
                if (i == 0)
                {
                    songUrlList = songUrlList + songObj.url;
                    songTypeList = songTypeList + songObj.type;
                    songNameList = songNameList + songObj.songName;
                    singerList = singerList + songObj.singerName;
                }
                else
                {
                    songUrlList = songUrlList + ";" + songObj.url;
                    songTypeList = songTypeList + "," + songObj.type;
                    songNameList = songNameList + "," + songObj.songName;
                    singerList = singerList + "," + songObj.singerName;
                }
            }
        }
        if (dirId == -1)
        {
            var nameTemp = "";
            var searchFlag;
            for (var i = 1; ; i++)
            {
                nameTemp = "??????" + i;
                searchFlag = 0;
                for (var j = 0; j < collect.dirList.length; j++)
                    if (nameTemp == collect.dirList[j].name)
                    {
                        searchFlag = 1;
                        break;
                    }
                if (searchFlag == 0)
                    break;
            }
            if (collect.webqqFlag == 2)
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir_v2.q"; else
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir.q";
            var data = {formsender:2,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),name:nameTemp,show:"1",p:Math.random()};
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.addToNewDir(o);
            };
            fs.onError = collect.addToNewDirFailInfo;
            fs.send();
            addToNewList = songIdList;
            addToNewListForUrl = songUrlList;
            addToNewListForUrlSongList = songNameList;
            addToNewListForUrlSingerList = singerList;
            return;
        }
        else
        {
            var dirID = (collect.dirList[dirId]) ? collect.dirList[dirId].dirid : 0;
            var uinTemp = (collect.webqqFlag == 2) ? collect.webqqUin : user.getUin();
            var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=0&dirid=" + dirID + "&uin=" + uinTemp + "&p=" + Math.random();
            JsonLoadData(url, this.handleGetSongNum.bind(this, dirID), err_cb, "jsonCallback");
            addToNewList = songIdList;
            addToNewListForUrl = songUrlList;
            addToNewListForUrlSongList = songNameList;
            addToNewListForUrlSingerList = singerList;
            return;
        }
    }
    else
    {
        for (var i = 0; i < songList.length; i++)
        {
            songIndexTemp = songList[i];
            if (songIndexTemp >= curSongListTmp.length)
            {
                continue;
            }
            var songObj = curSongListTmp[songIndexTemp];
            if (songObj.id > 0)
            {
                if (i == 0)
                {
                    songIdList = songIdList + songObj.id;
                    songTypeList = songTypeList + songObj.type;
                }
                else
                {
                    songIdList = songIdList + "," + songObj.id;
                    songTypeList = songTypeList + "," + songObj.type;
                }
            }
        }
        if (collect.webqqFlag == 2)
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_movesong_v2.q"; else
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_movesong.q";
        var data = {formsender:2,dirfrom:(collect.dirList[(curCollectDirId == -1) ? g_collectTab : curCollectDirId]) ? collect.dirList[(curCollectDirId == -1) ? g_collectTab : curCollectDirId].dirid : 0,dirto:(collect.dirList[dirId]) ? collect.dirList[dirId].dirid : 0,ids:songIdList,types:songTypeList,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin()};
        if (data.dirto == 0)
        {
            movesongFlag = 1;
            var nameTemp = "";
            var searchFlag;
            for (var i = 1; ; i++)
            {
                nameTemp = "??????" + i;
                searchFlag = 0;
                for (var j = 0; j < collect.dirList.length; j++)
                    if (nameTemp == collect.dirList[j].name)
                    {
                        searchFlag = 1;
                        break;
                    }
                if (searchFlag == 0)
                    break;
            }
            if (collect.webqqFlag == 2)
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir_v2.q"; else
                var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir.q";
            var data = {formsender:2,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),name:nameTemp,show:"1",p:Math.random()};
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.addToNewDir(o);
            };
            fs.onError = collect.addToNewDirFailInfo;
            fs.send();
            addToNewList = songIdList;
            addToNewListForUrl = songUrlList;
            addToNewListForUrlSongList = songNameList;
            addToNewListForUrlSingerList = singerList;
            dirTypeList = songTypeList;
            g_dirFrom = data.dirfrom;
        }
        else
        {
            var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
            fs.onSuccess = function(o) {
                collect.moveSongCallback(o);
            };
            fs.onError = collect.moveSongFailInfo;
            fs.send();
        }
    }
    if (addFailFlag == 1)
        showInfoBox("????????????");
    return;
},addSongToCollectFromPortal:function(dirId) {
    function err_cb()
    {
        MUSIC.dialog.createInfoBox("????????", 1, 1, this._t - 80, this._l - 40);
    }

    if (!user.isLogin())
    {
        return false;
    }
    var songIndexTemp;
    var songIdList = "";
    var songUrlList = "";
    var songTypeList = "";
    var songNameList = "";
    var singerList = "";
    addFailFlag = 0;
    var url = ((this.music).mapSongUrlStr && (this.music).mapSongUrlStr.length) ? (this.music).mapSongUrlStr[0] : (((this.music).msongurl && (this.music).msongurl != "") ? (this.music).msongurl : "");
    if (url == "")
    {
        addFailFlag = 1;
        MUSIC.dialog.createInfoBox("??????????", 1, 1, this._t - 80, this._l - 40);
        return;
    }
    if (url.indexOf("music.soso.com") != -1 || url.indexOf("qqmusic.qq.com") != -1)
    {
        var tempList = url.split("/");
        var musicID = parseInt(tempList[3]) - 12000000;
        songIdList = songIdList + musicID;
        songTypeList = songTypeList + 1;
    }
    else
    {
        songUrlList = songUrlList + url;
        songTypeList = songTypeList + 1;
        songNameList = songNameList + (this.music).msong;
        singerList = singerList + (this.music).msinger;
    }
    if (dirId == -1)
    {
        var nameTemp = "";
        var searchFlag;
        for (var i = 1; ; i++)
        {
            nameTemp = "??????" + i;
            searchFlag = 0;
            for (var j = 0; j < collect.dirList.length; j++)
                if (nameTemp == collect.dirList[j].name)
                {
                    searchFlag = 1;
                    break;
                }
            if (searchFlag == 0)break;
        }
        if (collect.webqqFlag == 2)
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir_v2.q"; else
            var url = "http://cgi.music.soso.com/fcgi-bin/fcg_fav_adddir.q";
        var data = {formsender:2,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin(),name:nameTemp,show:"1",p:Math.random()};
        var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
        fs.onSuccess = function(o) {
            collect.addToNewDir(o);
        };
        fs.onError = collect.addToNewDirFailInfo;
        fs.send();
        addToNewList = songIdList;
        addToNewListForUrl = songUrlList;
        addToNewListForUrlSongList = songNameList;
        addToNewListForUrlSingerList = singerList;
        return;
    }
    else
    {
        var dirID = (collect.dirList[dirId]) ? collect.dirList[dirId].dirid : 0;
        var t_uin = (collect.webqqFlag == 2) ? collect.webqqUin : user.getUin();
        var url = "http://qzone-music.qq.com/fcg-bin/fcg_music_fav_getinfo.fcg?dirinfo=0&dirid=" + dirID + "&uin=" + t_uin + "&p=" + Math.random();
        JsonLoadData(url, this.handleGetSongNum.bind(this, dirID), err_cb, "jsonCallback");
        addToNewList = songIdList;
        addToNewListForUrl = songUrlList;
        addToNewListForUrlSongList = songNameList;
        addToNewListForUrlSingerList = singerList;
        return;
    }
    if (addFailFlag == 1)MUSIC.dialog.createInfoBox("??????????", 1, 1, this._t - 80, this._l - 40);
    return;
},moveSongCallback:function(o) {
    if (!o || typeof(o) != "object") {
        showInfoBox("?????????????");
        return false;
    }
    movesongFlag = 0;
    switch (parseInt(o.code))
    {case 0:{
        showInfoBox("???????????");
        break;
    }
        case 1:{
            showInfoBox("?????????????");
            break;
        }
        default:{
            showInfoBox(o.msg);
            break;
        }
    }
    var oFlash = $(flashId);
    if (oFlash)
    {
        collect.getDirList();
    }
    return;
},moveSongFailInfo:function() {
    showInfoBox("???????????");
    return;
},addSong2FavCallback:function(o) {
    if (!o || typeof(o) != "object") {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("?????????");
        } else MUSIC.dialog.createInfoBox("?????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("???????");
        }
        else
        {
            player.updateNickName();
            MUSIC.dialog.createInfoBox("???????", 1, 1, this._t - 80, this._l - 40);
        }
        break;
    }
        case 1:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox("?????????????");
            } else MUSIC.dialog.createInfoBox("?????????????", 1, 1, this._t - 80, this._l - 40);
            break;
        }
        default:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox(o.msg);
            } else MUSIC.dialog.createInfoBox(o.msg, 1, 1, this._t - 80, this._l - 40);
            break;
        }
    }
    if (typeof(flashId) != "undefined") {
        var oFlash = $(flashId);
        if (oFlash)
        {
            collect.getDirList();
        }
    }
    return;
},addSong2FavForUrlCallback:function(o) {
    if (!o || typeof(o) != "object") {
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("?????????");
        } else MUSIC.dialog.createInfoBox("?????????", 1, 1, this._t - 80, this._l - 40);
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        if (typeof(showInfoBox) != "undefined")
        {
            showInfoBox("???????");
        } else {
            player.updateNickName();
            MUSIC.dialog.createInfoBox("???????", 1, 1, this._t - 80, this._l - 40);
        }
        break;
    }
        case 1:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox(o.msg);
            } else MUSIC.dialog.createInfoBox(o.msg, 1, 1, this._t - 80, this._l - 40);
            break;
        }
        default:{
            if (typeof(showInfoBox) != "undefined")
            {
                showInfoBox(o.msg);
            } else MUSIC.dialog.createInfoBox(o.msg, 1, 1, this._t - 80, this._l - 40);
            break;
        }
    }
    if (typeof(flashId) != "undefined") {
        var oFlash = $(flashId);
        if (oFlash)
        {
            collect.getDirList();
        }
    }
    return;
},addSongFailInfo:function() {
    if (typeof(showInfoBox) != "undefined")
    {
        showInfoBox("?????????????");
    } else MUSIC.dialog.createInfoBox("?????????????", 1, 1, this._t - 80, this._l - 40);
    return;
},addSongForUrlFailInfo:function() {
    if (typeof(showInfoBox) != "undefined")
    {
        showInfoBox("?????????");
    } else MUSIC.dialog.createInfoBox("?????????", 1, 1, this._t - 80, this._l - 40);
    var oFlash = $(flashId);
    if (oFlash)
    {
        collect.getDirList();
    }
    return;
},deleteSong:function(songIndex) {
    if ((!user.isLogin() || songIndex.length == 0 || curTabIndex != 1) && !(collect.webqqFlag == 2))
    {
        return false;
    }
    var curSongListTmp = g_songList[curTabIndex][curCollectDirId];
    if (typeof(curSongListTmp) == "undefined")
    {
        return false;
    }
    var songIndexTemp;
    var songIdList = "";
    var songTypeList = "";
    for (var i = 0; i < songIndex.length; i++)
    {
        songIndexTemp = songIndex[i];
        if (songIndexTemp >= curSongListTmp.length)
        {
            continue;
        }
        var songObj = curSongListTmp[songIndexTemp];
        if (songObj.id > 0)
        {
            if (i == 0)
            {
                songIdList = songIdList + songObj.id;
                songTypeList = songTypeList + songObj.type;
            }
            else
            {
                songIdList = songIdList + "," + songObj.id;
                songTypeList = songTypeList + "," + songObj.type;
            }
        }
    }
    if (songIdList == "")
    {
        showInfoBox("????????");
        return false;
    }
    if (collect.webqqFlag == 2)
        var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_delbatchsong_v2.q"; else
        var url = "http://cgi.music.soso.com/fcgi-bin/fcg_music_delbatchsong.q";
    var data = {formsender:2,dirid:(collect.dirList[curCollectDirId]) ? collect.dirList[curCollectDirId].dirid : 0,flag:2,ids:songIdList,source:142,types:songTypeList,uin:(collect.webqqFlag == 2) ? collect.webqqUin : user.getUin()};
    var fs = new MUSIC.FormSender(url, "post", data, "GB2312");
    fs.onSuccess = function(o) {
        collect.delSongCallback(o);
    };
    fs.onError = collect.delSongFailInfo;
    fs.send();
    return false;
},delSongCallback:function(o) {
    if (!o || typeof(o) != "object") {
        showInfoBox("???????????");
        return false;
    }
    switch (parseInt(o.code))
    {case 0:{
        showInfoBox("?????????");
        break;
    }
        case 1:{
            showInfoBox("?????????????");
            break;
        }
        default:{
            showInfoBox(o.msg);
            break;
        }
    }
    var oFlash = $(flashId);
    if (oFlash)
    {
        collect.getSongList(curCollectDirId);
    }
    return;
},delSongFailInfo:function() {
    showInfoBox("????????");
    return;
}}
var collect = MUSIC.widget.collect;
var addToNewList;
var addToNewListForUrl;
var addToNewListForUrlSongList;
var addToNewListForUrlSingerList;
var dirTypeList;
var checkLoginForPlayerID;
var movesongFlag;
var g_dirFrom;
var g_dirTo;
function checkLoginForPlayer()
{
    var curPlayIndex = 0;
    if (curListIndex == 5) {
        curPlayIndex = curPlayTopicId;
    } else if (curListIndex == 4) {
        curPlayIndex = curPlayTaogeId;
    } else if (curListIndex == 3) {
        curPlayIndex = curPlayRankId;
    } else if (curListIndex == 2) {
        curPlayIndex = curPlayFreeClass;
    }
    else if (curListIndex == 1) {
        curPlayIndex = (curCollectDirId == -1) ? g_collectTab : curCollectDirId;
    } else {
        curPlayIndex = 0;
    }
    Cookie.set("player_login_curTab", curTabIndex);
    Cookie.set("player_login_subCurTab", g_subTab);
    Cookie.set("player_login_curplayTab", curListIndex);
    Cookie.set("player_login_subCurPlayTab", curPlayIndex);
    Cookie.set("player_login_curSongIndex", curSongIndex);
    if (user.isLogin())
    {
        Cookie.set("player_login", 1);
        window.location.replace("http://music.soso.com/player");
        if (top.window.opener)
            top.window.opener.location.reload();
        return;
    }
    else
        checkLoginForPlayerID = setTimeout(checkLoginForPlayer, 500);
}
function logOutForPlayer()
{
    user.clear();
    window.location.replace("http://music.soso.com/player");
    if (top.window.opener)
        top.window.opener.location.reload();
    return;
}
function loginForPlayer()
{
    user.loginer().doLogin();
    checkLoginForPlayer();
}
window.onresize = function() {
    if (collect._fromPortalFlagDivFlag)
    {
        hideElement("sosoCollectTips");
        collect._fromPortalFlagDivFlag = false;
    }
}
/*  |xGv00|4827459eb9c6a1534a3e460ef7868fb3 */