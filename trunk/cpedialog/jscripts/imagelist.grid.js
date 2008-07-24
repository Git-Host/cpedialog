YAHOO.util.Event.addListener(window, "load", function() {
    EnhanceFromMarkup = new function() {
        var myColumnDefs = [
            {key:"image",label:"Image",sortable:true},
            {key:"url",label:"URL"},
            {key:"date",label:"Date",sortable:true,formatter:YAHOO.widget.DataTable.formatDate},
            {key:"id",label:"Id",sortable:true,isPrimaryKey:true},
            {key:"delete",label:"",action:'delete',formatter:function(elCell) {
                elCell.innerHTML = '<img src="/img/delete.gif" title="delete row" />';
                elCell.style.cursor = 'pointer';}}
        ];

        this.myDataSource = new YAHOO.util.DataSource(YAHOO.util.Dom.get("albumtable"));
        this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_HTMLTABLE;
        this.myDataSource.responseSchema = {
            fields: [{key:"image"},{key:"url"},
                {key:"date"}, {key:"id"}, {key:"delete"}
            ]
        };
        this.myDataTable = new YAHOO.widget.DataTable("imagediv", myColumnDefs, this.myDataSource,
           { sortedBy:{key:"date",dir:"desc"}});

        // Set up editing flow
        this.highlightEditableCell = function(oArgs) {
            var elCell = oArgs.target;
            if (YAHOO.util.Dom.hasClass(elCell, "yui-dt-editable")) {
                this.highlightCell(elCell);
            }
        };
        this.myDataTable.subscribe("cellMouseoverEvent", this.highlightEditableCell);
        this.myDataTable.subscribe("cellMouseoutEvent", this.myDataTable.onEventUnhighlightCell);
        //this.myDataTable.subscribe("cellClickEvent", this.myDataTable.onEventShowCellEditor);

        var myBuildUrl = function(datatable,record) {
            var url = '';
            var cols = datatable.getColumnSet().keys;
            for (var i = 0; i < cols.length; i++) {
                if (cols[i].isPrimaryKey) {
                    url += '&' + cols[i].key + '=' + encodeURIComponent(record.getData(cols[i].key));
                }
            }
            return url;
        };

        this.myDataTable.subscribe('cellClickEvent', function(ev) {
            var target = YAHOO.util.Event.getTarget(ev);
            var column = this.getColumn(target);
            if (column.action == 'delete') {
                if (confirm('Are you sure to delete the image?')) {
                    var record = this.getRecord(target);
                    YAHOO.util.Connect.asyncRequest('POST','/rpc?action=DeleteImage' + myBuildUrl(this,record),
                    {
                        success: function (o) {
                            if (o.responseText == 'true') {
                                this.deleteRow(target);
                            } else {
                                alert(o.responseText);
                            }
                        },
                        failure: function (o) {
                            alert(o.statusText);
                        },
                        scope:this
                    }
                            );
                }
            } else {
                this.onEventShowCellEditor(ev);
            }
        });

        ;
    };
});
