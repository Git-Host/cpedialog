YAHOO.namespace("cpedia.call");
YAHOO.util.Event.addListener(window, "load", function() {
    var call_voice = function() {
        var outgoingNumber = document.getElementById("outgoingNumber");
        var forwardingNumber = document.getElementById("forwardingNumber");
        var gv_call_send_button = document.getElementById("gv_call_send_button");
        gv_call_send_button.disabled = true;
        gv_call_send_button.value = 'Connecting...';
        if (outgoingNumber.value == "") {
            alert("Please input call number.");
            outgoingNumber.focus();
            return false;
        }
        var resetBtn = function() {
            gv_call_send_button.disabled = false;
            gv_call_send_button.value = 'Connect';
        };
        var formObject = document.getElementById('gv_form');
        YAHOO.util.Connect.setForm(formObject);
        YAHOO.util.Connect.asyncRequest(
                'POST',
                '/google_voice/call',
        {
            success: function (o) {
                window.alert(o.responseText);
                window.alert("You call has been connected successfully.");
                resetBtn();
            },
            failure: function(o) {
                window.alert("Unsuccessfully, please try again.");
                resetBtn();
            },
            scope: this
        }
                );
    };
    var get_account_info = function() {
        var gv_account_info_button = document.getElementById("gv_account_info_button");
        gv_account_info_button.disabled = true;
        gv_account_info_button.value = 'Connecting...';
        var resetBtn = function() {
            gv_account_info_button.disabled = false;
            gv_account_info_button.value = 'Account Info';
        };
        var formObject = document.getElementById('gv_form');
        YAHOO.util.Connect.setForm(formObject);
        YAHOO.util.Connect.asyncRequest(
                'POST',
                '/google_voice/account',
        {
            success: function (o) {
                window.alert(o.responseText);
                window.alert("You Account information has been fetched successfully.");
                resetBtn();
            },
            failure: function(o) {
                window.alert("Unsuccessfully, please try again.");
                resetBtn();
            },
            scope: this
        }
                );
    };
    YAHOO.util.Event.addListener("gv_call_send_button", "click", call_voice);
    YAHOO.util.Event.addListener("gv_account_info_button", "click", get_account_info);
});