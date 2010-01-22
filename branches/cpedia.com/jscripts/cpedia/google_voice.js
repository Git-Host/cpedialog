YAHOO.util.Event.addListener(window, "load", function() {
   var send_sms = function(){
       var gv_message = document.getElementById("gv_message");
       var gv_message_send_button = document.getElementById("gv_message_send_button");
       gv_message_send_button.disabled = true;
       gv_message_send_button.value = 'Sending...';
       if(gv_message.value==""){
           alert("Please input SMS message.");
           gv_message.focus();
           return false;
       }
       var resetBtn = function(){
           gv_message_send_button.disabled = false;
           gv_message_send_button.value = 'Send SMS to me';
       };
       var formObject = document.getElementById('gv_form');
       YAHOO.util.Connect.setForm(formObject);
       YAHOO.util.Connect.asyncRequest(
               'POST',
               '/rpc?action=SendGoogleVoiceSMS',
       {
           success: function (o) {
               window.alert("You SMS message has been send successfully.");
               gv_message.value = "";
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
   YAHOO.util.Event.addListener("gv_message_send_button","click",send_sms);
});