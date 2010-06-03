YAHOO.util.Event.addListener(window, "load", function() {
    var search_mp3 = function() {
        var search_key = document.getElementById("key");
        var search_page = document.getElementById("page");
        var search_mp3_btn = document.getElementById("search_mp3_btn");
        search_mp3_btn.disabled = true;
        search_mp3_btn.value = 'Searching...';
        if (search_key.value == "") {
            alert("Please input search key.");
            search_key.focus();
            return false;
        }
        if (search_page.value == "") {
            alert("Please input result page.");
            search_page.focus();
            return false;
        }
        var resetBtn = function() {
            search_mp3_btn.disabled = false;
            search_mp3_btn.value = 'Search';
        };
        var formObject = document.getElementById('mp3_form');
        YAHOO.util.Connect.setForm(formObject);
        YAHOO.util.Connect.asyncRequest(
                'POST',
                '/baidump3/search',
        {
            success: function (o) {
                var search_result = document.getElementById("search_result");
                search_result.innerHTML = o.responseText;
                resetBtn();
            },
            failure: function(o) {
                window.alert("Error, please check or try again.");
                resetBtn();
            },
            scope: this
        }
                );
    };
    YAHOO.util.Event.addListener("search_mp3_btn", "click", search_mp3);
});