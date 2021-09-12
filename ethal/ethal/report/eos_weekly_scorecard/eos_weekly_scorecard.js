// Copyright (c) 2016, Atrina Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["EOS Weekly Scorecard"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __('From Date'),
			"fieldtype": "Date",
			"default": frappe.datetime.month_start(),
		},
		{
			"fieldname":"to_date",
			"label": __('To Date'),
			"fieldtype": "Date",
			"default": frappe.datetime.month_end(),
		}
	]
};
