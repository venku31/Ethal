// Copyright (c) 2021, Atrina Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weighbridge Sync', {
	refresh: function(frm) {
		if (frm.doc.file_path.trim() && frm.doc.file_name.trim()) {
			frm.add_custom_button(__('Sync weighbridge Data'), function(){
				return frappe.call({				
				method: 'ethal.weighbridge.set_values_for_weighbridge',
				freeze: true,
				freeze_message: "Syncing weighbridge data",
					callback: function(r) {
						frm.refresh();					
					}
				});
		  	});
		}  
	}
});
