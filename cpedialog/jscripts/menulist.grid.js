//YAHOO.util.Event.onContentReady('menudiv', function() {
    var renderMenuTable = function() {
        var myColumnDefs = [
            {key:"title",label:"Title",sortable:true,editor:"textbox"},
            {key:"permalink",label:"Permalink",sortable:true,editor:"textbox"},
            {key:"target",label:"Target",sortable:true,editor:"dropdown",editorOptions:{dropdownOptions:["_self","_blank","_parent","_top"]}},
            {key:"order",label:"Order",formatter:YAHOO.widget.DataTable.formatNumber,sortable:true,editor:"textbox",editorOptions:{validator:YAHOO.widget.DataTable.validateNumber}},
            {key:"valid",label:"Valid",sortable:true,editor:"radio",editorOptions:{radioOptions:[true,false],disableBtns:true}},
            {key:"id",label:"Id",sortable:true,isPrimaryKey:true,hidden:true},
            {key:"delete",label:"Delete",action:'delete',formatter:function(elCell) {
                elCell.innerHTML = '<img src="/img/delete.gif" title="delete row" />';
                elCell.style.cursor = 'pointer';
            }},
            {key:"insert",label:"Add",action:'insert',formatter:function(elCell) {
                elCell.innerHTML = '<img src="/img/insert.png" title="insert new row" />';
                elCell.style.cursor = 'pointer';
            }}
        ];

        this.myDataSource = new YAHOO.util.DataSource(YAHOO.util.Dom.get("menutable"));
        this.myDataSource.responseType = YAHOO.util.DataSource.TYPE_HTMLTABLE;
        this.myDataSource.responseSchema = {
            fields: [{key:"title"},{key:"permalink"},{key:"target"},
                {key:"order", parser:YAHOO.util.DataSource.parseNumber},
                {key:"valid"}, {key:"id"}, {key:"delete"}, {key:"insert"}
            ]
        };
        this.myDataTable = new YAHOO.widget.DataTable("menudiv", myColumnDefs, this.myDataSource,
        { sortedBy:{key:"order",dir:"asc"}});

        this.myDataTable.updateMethod = "UpdateMenu";

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

        // Hook into custom event to customize save-flow of "radio" editor
        this.myDataTable.subscribe("editorUpdateEvent", function(oArgs) {
            if (oArgs.editor.column.key === "valid") {
                this.saveCellEditor();
            }
        });
        this.myDataTable.subscribe("editorBlurEvent", function(oArgs) {
            this.cancelCellEditor();
        });

        var myBuildUrl = function(datatable, record) {
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
            if (column.action == 'insert') {
                if (confirm('Are you sure to add a new menu?')) {
                    YAHOO.util.Connect.asyncRequest('POST', '/rpc?action=AddMenu',
                    {
                        success: function (o) {
                            var record = YAHOO.lang.JSON.parse(o.responseText);
                            this.addRow(record, this.getRecordIndex(target));
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

        this.myDataTable.subscribe('theadLabelDblclickEvent', function(ev) {
            var target = YAHOO.util.Event.getTarget(ev);
            //var column = this.getTheadEl(target);
            //if (column.label == 'insert') {
            if (confirm('Are you sure to add a new menu?')) {
                YAHOO.util.Connect.asyncRequest('POST', '/rpc?action=AddMenu',
                {
                    success: function (o) {
                        var record = YAHOO.lang.JSON.parse(o.responseText);
                        this.addRow(record, this.getRecordIndex(target));
                    },
                    failure: function (o) {
                        alert(o.statusText);
                    },
                    scope:this
                }
                );
            }
            //} else {
            //    this.onEventShowCellEditor(ev);
            //}
        });

        this.myDataTable.subscribe('cellClickEvent', function(ev) {
            var target = YAHOO.util.Event.getTarget(ev);
            var column = this.getColumn(target);
            if (column.action == 'delete') {
                if (confirm('Are you sure to delete the menu?')) {
                    var record = this.getRecord(target);
                    YAHOO.util.Connect.asyncRequest('POST', '/rpc?action=DeleteMenu' + myBuildUrl(this, record),
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
//});
