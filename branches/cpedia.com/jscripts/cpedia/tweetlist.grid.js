YAHOO.namespace("cpedia");
YAHOO.namespace("cpedia.twitter");
YAHOO.util.Event.addListener(window, "load", function() {
    YAHOO.cpedia.twitter.GetTweets = new function() {
        var myColumnDefs = [
            {key:"text", label:"Tweet", sortable:true,formatter:function(elCell,oRecord) {
                var text = oRecord.getData("text")+"<br/>"+oRecord.getData("created_at")+" from "+oRecord.getData("source");
                elCell.innerHTML = text;}}
        ];

        this.myDataSource = new YAHOO.util.DataSource("/rpc?action=GetTweets");
        this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_JSON;
        this.myDataSource.responseSchema = {
            resultsList: "records",
            fields: ["text","id","source",{key:"created_at",parser:"date"}]
        };

        this.myDataTable = new YAHOO.widget.DataTable("tweetdiv", myColumnDefs,
                this.myDataSource, {initialRequest:"&date="+ new Date().getTime()});

        this.myDataTable.subscribe("rowMouseoverEvent", this.myDataTable.onEventHighlightRow);
        this.myDataTable.subscribe("rowMouseoutEvent", this.myDataTable.onEventUnhighlightRow);

        // Set up polling
        var myCallback = {
            success: this.myDataTable.onDataReturnInitializeTable,
            failure: function() {
                YAHOO.log("Polling tweets failure", "error");
            },
            scope: this.myDataTable
        };
        this.myDataSource.setInterval(30000, null, myCallback);
        
     };
});
