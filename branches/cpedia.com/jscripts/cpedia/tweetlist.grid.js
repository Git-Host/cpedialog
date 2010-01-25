YAHOO.namespace("cpedia");
YAHOO.namespace("cpedia.twitter");
YAHOO.util.Event.addListener(window, "load", function() {
    YAHOO.cpedia.twitter.GetTweets = new function() {
        var DataTable  = YAHOO.widget.DataTable;
        var pageCount = 1;
        var pageSize=9;
        var myTableConfig = {
            initialRequest         : '&arg0='+pageCount+'&arg1='+pageSize+'&time='+ new Date().getTime()  //'startIndex=0&results=25'
        };
        var myColumnDefs = [
            {key:"text", label:"Tweet", sortable:true,formatter:function(elCell,oRecord) {
                var text = oRecord.getData("text")+"<br/><span class=tweet-meta>"+oRecord.getData("created_at")+" from "+oRecord.getData("source")+"</span>";
                elCell.innerHTML = text;}}
        ];

        this.myDataSource = new YAHOO.util.DataSource("/rpc?action=GetTweets");
        this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_JSON;
        this.myDataSource.responseSchema = {
            resultsList: "records",
            fields: ["text","id","source",{key:"created_at"}]
        };
        //this.myDataSource.subscribe("dataErrorEvent",this.myDataSource.sendRequest());        
        this.myDataTable = new YAHOO.widget.DataTable("tweetdiv", myColumnDefs,
                this.myDataSource, myTableConfig);
        //this.myDataTable.subscribe("rowMouseoverEvent", this.myDataTable.onEventHighlightRow);
        //this.myDataTable.subscribe("rowMouseoutEvent", this.myDataTable.onEventUnhighlightRow);
        var show_or_hide_link = function() {
            document.getElementById("paging").style.display = "";
            if (pageCount = 1) {
                document.getElementById("newer_tweets").style.display = "none";
            } else {
                document.getElementById("newer_tweets").style.display = "";
            }
        };

        // Set up polling
        var myCallback = {
            success: function() {
                this.myDataTable.onDataReturnInitializeTable;
                show_or_hide_link();
            },
            failure: function() {
                YAHOO.log("Polling tweets failure", "error");
            },
            scope: this.myDataTable
        };
        show_or_hide_link();
        var show_more_tweets = function(ev,linkId){
            alert("ttt");
            var target = YAHOO.util.Event.getTarget(ev);
            if(target.id="newer_tweets"){
                pageCount--;
            }else{
                pageCount++;
            }
            alert(target.id);
            this.myDataSource.sendRequest( '&arg0='+pageCount+'&arg1='+pageSize+'&time='+ new Date().getTime() ,
                    myCallback);                            
        };

        YAHOO.util.Event.addListener(["older_tweets","newer_tweets"],"click",show_more_tweets);
        //this.myDataSource.setInterval(30000, null, myCallback);
        
     };
});
