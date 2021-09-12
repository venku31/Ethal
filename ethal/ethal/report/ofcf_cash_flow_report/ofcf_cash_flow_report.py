# Copyright (c) 2013, Atrina Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	data = get_data(filters)
	columns = ["Account::180"]+["Jan::120"]+["Feb::120"]+["Mar::120"]+["April::120"]+["May::120"]+["Jun::120"]+["July::120"]+["Aug::120"]+["Sept::120"]+["oct::120"]+["Nov::120"]+["Dec::120"]
	return columns, data

def add_one_by_one(l):
		new_l = []
		cumsum = 0
		for elt in l:
			cumsum -= elt
			new_l.append(cumsum)
		return new_l

def indirect_income(filters):
	lst_42000 = get_monthly_gl_credit_no_opening("42", filters)
	lst_42000.insert(0,"Indirect Income")
	fin = [lst_42000]
	return fin

def sales_net_of_taxes(filters):
	lst_41000 = get_monthly_gl_credit_no_opening("41", filters)
	lst_41000.insert(0,"Sales Net of Taxes")
	fin = [lst_41000]
	return fin

def stock_valuation_change_in_fg(filters):
	lst_11510_11 = get_monthly_gl_debit("11510-11", filters)
	lst_11520_02 = get_monthly_gl_debit("11520-02", filters)
	final = [a+b for a,b in zip(lst_11510_11, lst_11520_02)]
	final_1 = [x - y for x, y in zip(final[:-1],final[1:])]
	final_1.insert(0,final[0])
	final_1.insert(0,"Stock Valuation Change in FG")
	fin = [final_1]
	return fin

def total_sales_net_of_taxes(filters):
	l1 = indirect_income(filters)
	for i in l1:
		l11 = i
	l11.pop(0)
	l2 = sales_net_of_taxes(filters)
	for i in l2:
		l22 = i
	l22.pop(0)
	l3 = stock_valuation_change_in_fg(filters)
	for i in l3:
		l33 = i
	l33.pop(0)
	final = [a+b+c for a,b,c in zip(l11,l22,l33)]
	final.insert(0,"Total Sales Net of Taxes")
	final = [final]
	return final

def power_consumed(filters):
	lst_54400_01 = get_monthly_gl_debit_no_opening("54400-01", filters)
	lst_54400_01.insert(0,"Power-Consumed")
	fin = [lst_54400_01]
	return fin

def consumables(filters):
	lst_54200_06 = get_monthly_gl_debit_no_opening("54200-06", filters)
	lst_54200_06.insert(0,"Consumables")
	fin = [lst_54200_06]
	return fin

def out_sourcing_costs(filters):
	lst_51000_02 = get_monthly_gl_debit_no_opening("51000-02", filters)
	lst_52000_04 = get_monthly_gl_debit_no_opening("52000-04", filters)
	lst_53000_03 = get_monthly_gl_debit_no_opening("53000-03", filters)
	lst_55000_01 = get_monthly_gl_debit_no_opening("55000-01", filters)
	final = [a+b+c+d for a,b,c,d in zip(lst_51000_02,lst_52000_04,lst_53000_03,lst_55000_01)]
	final.insert(0,"Out Sourcing Cost")
	fin = [final]
	return fin

def packing_cost(filters):
	lst_52000_03 = get_monthly_gl_debit_no_opening("52000-03", filters)
	lst_52000_03.insert(0,"Packing Cost")
	fin = [lst_52000_03]
	return fin

def total_stores(filters):
	lst_54200 = get_monthly_gl_debit_no_opening("542", filters)
	lst_54200_06 = get_monthly_gl_debit_no_opening("54200-06", filters)
	final = [a-b for a,b in zip(lst_54200,lst_54200_06)]
	final.insert(0,"stores")
	fin = [final]
	return fin

def fuel_diesel(filters):
	lst_51000_03 = get_monthly_gl_debit_no_opening("51000-03", filters)
	lst_51000_03.insert(0,"Fuel - Diesel")
	fin = [lst_51000_03]
	return fin

def raw_materials_consumed(filters):
	lst_50000 = get_monthly_gl_debit_no_opening("5", filters)
	lst_51000_02 = get_monthly_gl_debit_no_opening("51000-02", filters)
	lst_52000_03 = get_monthly_gl_debit_no_opening("52000-03", filters)
	lst_51000_03 = get_monthly_gl_debit_no_opening("51000-03", filters)


	fin = [a-b-c-d for a,b,c,d in zip(lst_50000,lst_51000_02,lst_52000_03,lst_51000_03)]
	fin.insert(0,"Raw materials - Consumed")
	final = [fin]
	return final

def total_variable_cost(filters):
	rmc = raw_materials_consumed(filters)
	for i in rmc:
		rmc_1 = i
	rmc_1.pop(0)

	pc = power_consumed(filters)
	for i in pc:
		pc_1 = i
	pc_1.pop(0)

	con = consumables(filters)
	for i in con:
		con_1 = i
	con_1.pop(0)

	osc = out_sourcing_costs(filters)
	for i in osc:
		osc_1 = i
	osc_1.pop(0)

	pac_cos = packing_cost(filters)
	for i in pac_cos:
		pac_cos_1 = i
	pac_cos_1.pop(0)

	fd = fuel_diesel(filters)
	for i in fd:
		fd_1 = i
	fd_1.pop(0)

	stores = total_stores(filters)
	for i in stores:
		stores_1 = i
	stores_1.pop(0)

	fin = [a+b+c+d+e+f+j for a,b,c,d,e,f,j in zip(rmc_1,pc_1,con_1,osc_1,pac_cos_1,fd_1,stores_1)]
	fin.insert(0,"Total Variable Cost")
	final = [fin]
	return final

def throughput(filters):
	tot1 = total_sales_net_of_taxes(filters)
	for i in tot1:
		tot_1 = i
	tot_1.pop(0)

	tot2 = total_variable_cost(filters)
	for i in tot2:
		tot_2 = i
	tot_2.pop(0)

	final = [a-b for a,b in zip(tot_1,tot_2)]
	final.insert(0,"Throughput")
	fin = [final]
	return fin

def operating_expenses(filters):
	lst_54000 = get_monthly_gl_debit_no_opening("54", filters)
	lst_60000 = get_monthly_gl_debit_no_opening("6", filters)
	lst_62000 = get_monthly_gl_debit_no_opening("62", filters)
	lst_54200 = get_monthly_gl_debit_no_opening("542", filters)
	lst_54400_01 = get_monthly_gl_debit_no_opening("54400-01", filters)
	lst_62000_03 = get_monthly_gl_debit_no_opening("62000-03", filters)
	lst_62000_04 = get_monthly_gl_debit_no_opening("62000-04", filters)
	lst_62000_05 = get_monthly_gl_debit_no_opening("62000-05", filters)
	final = [(a+b)-c-d-e-f-g-h for a,b,c,d,e,f,g,h in zip(lst_54000,lst_60000,lst_62000,lst_54200,lst_54400_01,lst_62000_03,lst_62000_04,lst_62000_05)]
	final.insert(0,"Operating Expenses")
	fin = [final]
	return fin

def interest_count(filters):
	lst_62000_03 = get_monthly_gl_debit_no_opening("62000-03", filters)
	lst_62000_04 = get_monthly_gl_debit_no_opening("62000-04", filters)
	lst_62000_05 = get_monthly_gl_debit_no_opening("62000-05", filters)
	final = [a+b+c for a,b,c in zip(lst_62000_03,lst_62000_04,lst_62000_05)]
	final.insert(0,"Interest")
	fin = [final]
	return fin

def profit_before_taxes(filters):
	tp = throughput(filters)
	for i in tp:
		tp_1 = i
	tp_1.pop(0)

	oe = operating_expenses(filters)
	for i in oe:
		oe_1 = i
	oe_1.pop(0)

	ic = interest_count(filters)
	for i in ic:
		ic_1 = i
	ic_1.pop(0)

	final = [a-b-c for a,b,c in zip(tp_1,oe_1,ic_1)]
	final.insert(0,"Profit Before Taxes")
	fin = [final]
	return fin 

def profit_before_taxes_percentage(filters):
	pbt = profit_before_taxes(filters)
	for i in pbt:
		pbt_1 = i
	pbt_1.pop(0)

	snt = sales_net_of_taxes(filters)
	for i in snt:
		snt_1 = i
	snt_1.pop(0)

	final = [(a/b)*100 if a!=0 and b!=0 else 0 for a,b in zip(pbt_1,snt_1)]
	final.insert(0,"Profit before taxes Percentage")
	fin = [final]
	return fin

def receivables_count(filters):
	lst_11200 = get_monthly_gl_debit("112", filters)
	# final_1 = [x - y for x, y in zip(lst_11200,lst_11200[1:])]
	# final_1.append(lst_11200[0])
	lst_11200.insert(0,"Receivables")
	fin = [lst_11200]
	return fin

def advance_to_supplier(filters):
	lst_21000_01 = get_monthly_gl_credit("21000-01", filters)
	# final_1 = [x - y for x, y in zip(lst_21000_01,lst_21000_01[1:])]
	# final_1.append(lst_21000_01[0])
	lst_21000_01.insert(0,"Advance to Supplier")
	fin = [lst_21000_01]
	return fin

def rm_count(filters):
	lst_11510_01 = get_monthly_gl_debit("11510-01", filters)
	lst_11510_05 = get_monthly_gl_debit("11510-05", filters)
	lst_11510_06 = get_monthly_gl_debit("11510-06", filters)
	final = [a+b+c for a,b,c in zip(lst_11510_01,lst_11510_05,lst_11510_06)]
	# final_1 = [x - y for x, y in zip(final,final[1:])]
	# final_1.append(final[0])
	final.insert(0,"RM")
	fin = [final]
	return fin

def wip_count(filters):
	lst_11510_02 = get_monthly_gl_debit("11510-02", filters)
	lst_11510_03 = get_monthly_gl_debit("11510-03", filters)
	lst_11510_07 = get_monthly_gl_debit("11510-07", filters)
	lst_11510_08 = get_monthly_gl_debit("11510-08", filters)
	lst_11510_09 = get_monthly_gl_debit("11510-09", filters)
	lst_11510_10 = get_monthly_gl_debit("11510-10", filters)
	lst_11520_01 = get_monthly_gl_debit("11520-01", filters)
	final = [a+b+c+d+e+f+g for a,b,c,d,e,f,g in zip(lst_11510_02,lst_11510_03,lst_11510_07,lst_11510_08,lst_11510_09,lst_11510_10,lst_11520_01)]
	# final_1 = [x - y for x, y in zip(final,final[1:])]
	# final_1.append(final[0])
	final.insert(0,"WIP")
	fin = [final]
	return fin

def fg_count(filters):
	lst_11510_11 = get_monthly_gl_debit("11510-11", filters)
	lst_11520_02 = get_monthly_gl_debit("11520-02", filters)
	final = [a+b for a,b in zip(lst_11510_11,lst_11520_02)]
	# final_1 = [x - y for x, y in zip(final,final[1:])]
	# final_1.append(final[0])
	final.insert(0,"FG")
	fin = [final]
	return fin

def overdue_receivables(filters):
	lst_11200 = get_monthly_gl_debit("112", filters)
	lst = []
	for i in range(len(lst_11200)):
		if i == 0:
			lst.append(lst_11200[i])
		else:
			nb = sum(lst_11200[0:i+1]) - lst_11200[i]
			lst.append(nb)
	lst.insert(0,"Overdue Receivables")
	fin = [lst]
	return fin

def get_monthly_gl_credit(account, filters):
		a = frappe.db.sql("""select MONTH(posting_date) as month, sum(credit) 
		from `tabGL Entry` where account like "{0}%" 
		and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
		lst=[]
		for i in a:
			lst.append(i[0])
		
		for j in range(1,13):
			if j not in lst:
				a.append([j,0])
		a.sort()
		lst_a= []
		for i in a:
			lst_a.append(i[1])

		b = frappe.db.sql("""select MONTH(posting_date) as month, sum(debit) 
		from `tabGL Entry` where account like "{0}%" 
		and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
		lst_1=[]
		for i in b:
			lst_1.append(i[0])
		
		for j in range(1,13):
			if j not in lst_1:
				b.append([j,0])
		b.sort()
		lst_b= []
		for i in b:
			lst_b.append(i[1])

		res_a = [a-b for a,b in zip(lst_a,lst_b)]
		# print("get_monthly_gl_credit ======> ",res_a)

		def add_one_by_one(l):
			new_l = []
			cumsum = 0
			for elt in l:
				cumsum += elt
				new_l.append(cumsum)
			return new_l

		fin = add_one_by_one(res_a)
		# print("opening and total added is =====> ", fin)

		fin_abs= []
		for i in fin:
			abs_val = abs(i)
			fin_abs.append(abs_val)

		return fin_abs

def get_monthly_gl_debit(account, filters):
	a = frappe.db.sql("""select MONTH(posting_date) as month, sum(debit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst=[]
	for i in a:
		lst.append(i[0])
	
	for j in range(1,13):
		if j not in lst:
			a.append([j,0])
	a.sort()
	lst_a= []
	for i in a:
		lst_a.append(i[1])


	b = frappe.db.sql("""select MONTH(posting_date) as month, sum(credit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst_1=[]
	for i in b:
		lst_1.append(i[0])
	
	for j in range(1,13):
		if j not in lst_1:
			b.append([j,0])
	b.sort()
	lst_b= []
	for i in b:
		lst_b.append(i[1])

	res_a = [a-b for a,b in zip(lst_a,lst_b)]

	# print("get_monthly_gl_debit ======> ",res_a)

	def add_one_by_one(l):
		new_l = []
		cumsum = 0
		for elt in l:
			cumsum += elt
			new_l.append(cumsum)
		return new_l

	fin = add_one_by_one(res_a)
	# print("opening and total added is =====> ", fin)

	fin_abs= []
	for i in fin:
		abs_val = abs(i)
		fin_abs.append(abs_val)

	return fin_abs

def get_monthly_gl_credit_no_opening(account, filters):
	
	a = frappe.db.sql("""select MONTH(posting_date) as month, sum(credit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst=[]
	for i in a:
		lst.append(i[0])
	
	for j in range(1,13):
		if j not in lst:
			a.append([j,0])
	a.sort()
	lst_a= []
	for i in a:
		lst_a.append(i[1])

	b = frappe.db.sql("""select MONTH(posting_date) as month, sum(debit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst_1=[]
	for i in b:
		lst_1.append(i[0])
	
	for j in range(1,13):
		if j not in lst_1:
			b.append([j,0])
	b.sort()
	lst_b= []
	for i in b:
		lst_b.append(i[1])

	res_a = [a-b for a,b in zip(lst_a,lst_b)]
	# print("get_monthly_gl_credit ======> ",res_a)

	fin = res_a
	# print("opening and total added is =====> ", fin)

	fin_abs= []
	for i in fin:
		abs_val = abs(i)
		fin_abs.append(abs_val)

	return fin_abs

def get_monthly_gl_debit(account, filters):
	a = frappe.db.sql("""select MONTH(posting_date) as month, sum(debit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst=[]
	for i in a:
		lst.append(i[0])
	
	for j in range(1,13):
		if j not in lst:
			a.append([j,0])
	a.sort()
	lst_a= []
	for i in a:
		lst_a.append(i[1])


	b = frappe.db.sql("""select MONTH(posting_date) as month, sum(credit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst_1=[]
	for i in b:
		lst_1.append(i[0])
	
	for j in range(1,13):
		if j not in lst_1:
			b.append([j,0])
	b.sort()
	lst_b= []
	for i in b:
		lst_b.append(i[1])

	res_a = [a-b for a,b in zip(lst_a,lst_b)]

	# print("get_monthly_gl_debit ======> ",res_a)

	def add_one_by_one(l):
		new_l = []
		cumsum = 0
		for elt in l:
			cumsum += elt
			new_l.append(cumsum)
		return new_l

	fin = add_one_by_one(res_a)
	# print("opening and total added is =====> ", fin)

	fin_abs= []
	for i in fin:
		abs_val = abs(i)
		fin_abs.append(abs_val)

	return fin_abs

def get_monthly_gl_debit_no_opening(account,filters):
	a = frappe.db.sql("""select MONTH(posting_date) as month, sum(debit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst=[]
	for i in a:
		lst.append(i[0])
	
	for j in range(1,13):
		if j not in lst:
			a.append([j,0])
	a.sort()
	lst_a= []
	for i in a:
		lst_a.append(i[1])


	b = frappe.db.sql("""select MONTH(posting_date) as month, sum(credit) 
	from `tabGL Entry` where account like "{0}%" 
	and YEAR(posting_date) = {1} GROUP BY MONTH(posting_date) ORDER BY month;""".format(account, filters['year']), as_list=True)
	lst_1=[]
	for i in b:
		lst_1.append(i[0])
	
	for j in range(1,13):
		if j not in lst_1:
			b.append([j,0])
	b.sort()
	lst_b= []
	for i in b:
		lst_b.append(i[1])

	res_a = [a-b for a,b in zip(lst_a,lst_b)]

	# print("get_monthly_gl_debit ======> ",res_a)

	fin = res_a
	# print("opening and total added is =====> ", fin)

	fin_abs= []
	for i in fin:
		abs_val = abs(i)
		fin_abs.append(abs_val)

	return fin_abs

def gross_working_capital(filters):
	rc = receivables_count(filters)
	for i in rc:
		rc_1 = i
	rc_1.pop(0)

	ats = advance_to_supplier(filters)
	for i in ats:
		ats_1 = i
	ats_1.pop(0)

	rmc = rm_count(filters)
	for i in rmc:
		rmc_1 = i
	rmc_1.pop(0)

	wipc = wip_count(filters)
	for i in wipc:
		wipc_1 = i
	wipc_1.pop(0)

	fgc = fg_count(filters)
	for i in fgc:
		fgc_1 = i
	fgc_1.pop(0)

	ovr = overdue_receivables(filters)
	for i in ovr:
		ovr_1 = i
	ovr_1.pop(0)

	final = [(a+b+c+d+e+f) for a,b,c,d,e,f in zip(rc_1,ats_1,rmc_1,wipc_1,fgc_1,ovr_1)]
	final.insert(0,"Gross Working Capital")
	fin = [final]
	return fin

def total_payable(filters):
	lst_21000_01 = get_monthly_gl_credit("21000-01", filters)
	lst_21100 = get_monthly_gl_credit("211", filters)
	lst_21300 = get_monthly_gl_credit("213", filters)
	lst_21400 = get_monthly_gl_credit("214", filters)

	final = [(a+b+c+d) for a,b,c,d in zip(lst_21000_01,lst_21100,lst_21300,lst_21400)]
	final.insert(0,"Total Payable (other than bank and cash)")
	fin = [final]
	return fin

def overdue_payable(filters):
	tp = total_payable(filters)
	for i in tp:
		tp_1 = i
	tp_1.pop(0)
	lst = []
	for i in range(len(tp_1)):
		if i == 0:
			lst.append(tp_1[i])
		else:
			nb = sum(tp_1[0:i+1]) - tp_1[i]
			lst.append(nb)
	lst.insert(0,"Overdue Payable")
	fin = [lst]
	return fin

def net_working_capital(filters):
	gwc = gross_working_capital(filters)
	for i in gwc:
		gwc_1 = i
	gwc_1.pop(0)

	tp = total_payable(filters)
	for i in tp:
		tp_1 = i
	tp_1.pop(0)

	op = overdue_payable(filters)
	for i in op:
		op_1 = i
	op_1.pop(0)
	
	final = [a-b-c for a,b,c in zip(gwc_1, tp_1, op_1)]
	final.insert(0,"Net Working Capital")
	fin = [final]
	return fin

def operational_free_cash_flow(filters):
	pbt = profit_before_taxes(filters)
	for i in pbt:
		pbt_1 = i
	pbt_1.pop(0)

	nwc = net_working_capital(filters)
	for i in nwc:
		nwc_1 = i
	nwc_1.pop(0)

	final = [a+b for a,b in zip(pbt_1,nwc_1)]
	final.insert(0,"Operational Free Cash Flow (OFCF)")
	fin = [final]
	return fin

def operational_free_cash_score(filters):
	ofcf = operational_free_cash_flow(filters)
	for i in ofcf:
		ofcf_1 = i
	ofcf_1.pop(0)

	op = overdue_payable(filters)
	for i in op:
		op_1 = i
	op_1.pop(0)

	final = [a-b for a,b in zip(ofcf_1, op_1)]
	final.insert(0,"Operational Free Cash Score")
	fin = [final]
	return fin

def capital_expenditure(filters):
	lst_12000 = get_monthly_gl_debit_no_opening("12", filters)
	lst_11700 = get_monthly_gl_debit_no_opening("117", filters)
	lst_11410_01 = get_monthly_gl_debit_no_opening("11410-01", filters)

	final = [a+b+c for a,b,c in zip(lst_12000,lst_11700,lst_11410_01)]
	final.insert(0,"Capital Expenditure")
	fin = [final]
	return fin

def working_capital_term_loan(filters):
	lst_21200_02 = get_monthly_gl_credit_no_opening("21200-02",filters)
	lst_21200_01 = get_monthly_gl_credit_no_opening("21200-01",filters)
	lst_22100 = get_monthly_gl_credit_no_opening("221",filters)

	final = [a+b+c for a,b,c in zip(lst_21200_02,lst_21200_01,lst_22100)]
	final.insert(0,"Working Capital Term Loan")
	fin = [final]
	return fin

def balance_in_bank_and_cash(filters):
	lst_11100 = get_monthly_gl_debit_no_opening("111", filters)
	lst_11100.insert(0,"Balance in Bank and Cash")
	fin = [lst_11100]
	return fin

def get_data(filters):
	ii = indirect_income(filters)
	snt = sales_net_of_taxes(filters)
	svcf = stock_valuation_change_in_fg(filters)
	tsnt = total_sales_net_of_taxes(filters)
	pc = power_consumed(filters)
	con = consumables(filters)
	osc = out_sourcing_costs(filters)
	pac_cos = packing_cost(filters)
	strs = total_stores(filters)
	fd = fuel_diesel(filters)
	rmco = raw_materials_consumed(filters)
	tvc = total_variable_cost(filters)
	thp = throughput(filters)
	oe = operating_expenses(filters)
	ic = interest_count(filters)
	pbt = profit_before_taxes(filters)
	pbtp = profit_before_taxes_percentage(filters)
	rc = receivables_count(filters)
	ats = advance_to_supplier(filters)
	rmc = rm_count(filters)
	wipc = wip_count(filters)
	fgc = fg_count(filters)
	ovr = overdue_receivables(filters)
	gwc = gross_working_capital(filters)
	tp = total_payable(filters)
	op = overdue_payable(filters)
	nwc = net_working_capital(filters)
	ofcf = operational_free_cash_flow(filters)
	ofcr = operational_free_cash_score(filters)
	ce = capital_expenditure(filters)
	wctl = working_capital_term_loan(filters)
	bibc = balance_in_bank_and_cash(filters)

	return ii+snt+svcf+tsnt+pc+con+osc+pac_cos+strs+fd+rmco+tvc+thp+oe+ic+pbt+pbtp+gwc+rc+ats+rmc+wipc+fgc+ovr+tp+op+nwc+ofcf+ofcr+ce+wctl+bibc


	