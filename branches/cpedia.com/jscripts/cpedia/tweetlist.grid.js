YAHOO.namespace("cpedia");
YAHOO.namespace("cpedia.twitter");
YAHOO.util.Event.addListener(window, "load", function() {
    YAHOO.cpedia.twitter.GetTweets = new function() {
        var pageCount = 1;
        var pageSize = 8;

        var bookmarkedTweetViewState = YAHOO.util.History.getBookmarkedState("tweet");
        var initialTweetViewState = bookmarkedTweetViewState || "page1";

        YAHOO.util.History.register("tweet", initialTweetViewState, function (state) {
            // "state" can be "page1", "page2" or "page3".
            pageCount = state.substr(4);
            //show_tweet_page(pageCount);
        });

        function handleTweetViewActivePageChange () {
            var newState, currentState;
            newState = "page" + pageCount;
            try {
                currentState = YAHOO.util.History.getCurrentState("tweet");
                if (newState != currentState) {
                    YAHOO.util.History.navigate("tweet", newState);
                }
            } catch (e) {
            }
        }

        // Use the Browser History Manager onReady method to instantiate the TabView widget.
        YAHOO.util.History.onReady(function () {
            var currentState;
            currentState = YAHOO.util.History.getCurrentState("tweet");
            pageCount = currentState.substr(4);
            //show_tweet_page(pageCount);
            initTableView();
        });

        // Initialize the browser history management library.
        try {
            YAHOO.util.History.initialize("yui-history-field", "yui-history-iframe");
        } catch (e) {
        }

        var initTableView = function() {
            var myTableConfig = {
                initialRequest: '&arg0=' + pageCount + '&arg1=' + pageSize   //'startIndex=0&results=25'
            };
            var myColumnDefs = [
                {
                    key:"text",
                    label:"Tweet",
                    sortable:true,
                    formatter:function(elCell, oRecord) {
                        var text = oRecord.getData("text") + "<br/><span class=tweet-meta>" + oRecord.getData("created_at") + " from " + oRecord.getData("source") + "</span>";
                        elCell.innerHTML = text;
                    }
                }
            ];

            this.myDataSource = new YAHOO.util.DataSource("/rpc?action=GetTweets");
            this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_JSON;
            this.myDataSource.responseSchema = {
                resultsList: "records",
                fields: ["text","id","source",{
                    key:"created_at"
                }]
            };
            //this.myDataSource.subscribe("dataErrorEvent",this.myDataSource.sendRequest());
            this.myDataTable = new YAHOO.widget.DataTable("tweetdiv", myColumnDefs,
                    this.myDataSource, myTableConfig);
            //this.myDataTable.subscribe("rowMouseoverEvent", this.myDataTable.onEventHighlightRow);
            //this.myDataTable.subscribe("rowMouseoutEvent", this.myDataTable.onEventUnhighlightRow);
            var show_or_hide_link = function() {
                document.getElementById("paging").style.display = "";
                if (pageCount == 1) {
                    document.getElementById("newer_tweets").style.display = "none";
                } else {
                    document.getElementById("newer_tweets").style.display = "";
                }
            };

            var mySuccessHandler = function() {
                this.onDataReturnInitializeTable.apply(this, arguments);
                if (this.target_ID) {
                    if (this.target_ID == "newer_tweets") {
                        pageCount--;
                    } else if (this.target_ID == "older_tweets") {
                        pageCount++;
                    }
                }
                handleTweetViewActivePageChange();
                show_or_hide_link();
                document.getElementById("ajax_icon").src = "/img/ajax-none.gif";
            };

            var myFailureHandler = function() {
                document.getElementById("ajax_icon").src = "/img/ajax-none.gif";
                this.showTableMessage(YAHOO.widget.DataTable.MSG_ERROR, YAHOO.widget.DataTable.CLASS_ERROR);
                this.onDataReturnAppendRows.apply(this, arguments);
                YAHOO.log("Polling tweets failure", "error");
            };

            // Set up polling
            var myCallback = {
                success: mySuccessHandler,
                failure: myFailureHandler,
                scope: this.myDataTable
            };

            show_or_hide_link();

            var show_more_tweets = function(e) {
                document.getElementById("ajax_icon").src = "/img/ajax.gif";
                var target = YAHOO.util.Event.getTarget(e);
                var pageCount_ = pageCount;
                if (target.id == "newer_tweets") {
                    pageCount_ = pageCount - 1;
                } else if (target.id == "older_tweets") {
                    pageCount_ = pageCount + 1;
                }
                this.myDataTable.target_ID = target.id;
                this.myDataSource.sendRequest('&arg0=' + pageCount_ + '&arg1=' + pageSize,
                        myCallback);
            };

            var show_tweet_page = function(page_number) {
                alert(page_number);
                this.myDataSource.sendRequest('&arg0=' + page_number + '&arg1=' + pageSize,
                        myCallback);
            };

            YAHOO.util.Event.addListener(["older_tweets","newer_tweets"], "click", show_more_tweets, this, this);
            //this.myDataSource.setInterval(30000, null, myCallback);

            return {
                oDS: this.myDataSource,
                oDT: this.myDataTable
            };
        };
    };
});
