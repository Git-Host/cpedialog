YAHOO.util.Event.addListener(window, "load", function() {
    YAHOO.example.GetTweets = new function() {
        this.formatUrl = function(elCell, oRecord, oColumn, sData) {
            elCell.innerHTML = "<a href='" + oRecord.getData("ClickUrl") + "' target='_blank'>" + sData + "</a>";
        };

        var myColumnDefs = [
            {key:"text", label:"Tweet", sortable:true },
            {key:"created_at", label:"Created At", formatter:YAHOO.widget.DataTable.formatDate, sortable:true},
            {key:"id"}
        ];

        this.myDataSource = new YAHOO.util.DataSource("rpc?action=GetTweets");
        this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_JSON;
        //this.myDataSource.connXhrMode = "queueRequests";
        this.myDataSource.responseSchema = {
            resultsList: "records",
            fields: ["text","id",{key:"created_at",parser:"date"}]
        };

        this.myDataTable = new YAHOO.widget.DataTable("tweetdiv", myColumnDefs,
                this.myDataSource, {initialRequest:"&date="+ new Date().getTime()});

        var myCallback = function() {
            this.set("sortedBy", null);
            this.onDataReturnAppendRows.apply(this,arguments);
        };
        var callback1 = {
            success : myCallback,
            failure : myCallback,
            scope : this.myDataTable
        };
        this.myDataSource.sendRequest("&date="+ new Date().getTime(),
                callback1);
    };
});
