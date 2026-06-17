# Business Report


## Dataset Overview

Dataset:
Olist Brazilian E-Commerce Dataset

Analysis Period:
2016 - 2018

Architecture:
Raw → Bronze → Silver → Gold → PostgreSQL Analytics Warehouse

Analytics Tables:

* customer_revenue
* product_revenue
* monthly_revenue
* state_revenue
* order_summary

## Dataset Summary

Dataset: Olist Brazilian E-Commerce Dataset

Period:
2016 - 2018

Orders:
99,441

Customers:
99,441

Products:
32,951

---

## KPI Summary

Total Revenue:
15397738.61

Average Order Value:
136.6865389258766

Total Customers:
99441

Total Products Sold:
134936

---

## Customer Analysis

### Top Customers By Revenue

SQL Used:

SELECT *
FROM customer_revenue
ORDER BY total_revenue DESC
LIMIT 10;

Key Findings:

* Top 10 customers generated the highest revenue in the platform.
* Revenue distribution can be used to identify high-value customers.
* Customer purchase frequency can be analyzed using total_orders.

"1617b1357756262bfa56ab541c47bc16"	1	13440
"ec5b2ba62e574342386871631fafd3fc"	1	7160
"c6e2731c5b391845f6800c97401a43a9"	1	6735
"f48d464a0baaea338cb25f816991ab1f"	1	6729
"3fd6777bbce08a352fddd04e4a7cc8f6"	1	6499
"05455dfa7cd02f13d132aa7a6a9729c6"	1	5934.6
"df55c14d1476a9a3467f131269c2477f"	1	4799
"24bbf5fd2f2e1b359ee7de94defc4a15"	1	4690
"e0a2412720e9ea4f26c1ac985f6a7358"	1	4599.9
"3d979689f636322c62418b6346b1c6d2"	1	4590

---

## Product Analysis

### Top Products By Revenue

SQL Used:

SELECT *
FROM product_revenue
ORDER BY total_revenue DESC
LIMIT 10;

Key Findings:

* Certain products contribute a disproportionately large share of revenue.
* Product categories help identify the strongest performing product segments.

"bb50f2e236e5eea0100680137654686c"	"beleza_saude"	195	63885
"6cdd53843498f92890544667809f1595"	"beleza_saude"	156	54730.2
"d6160fb7873f184099d9bc95e30376af"	"pcs"	35	48899.340000000004
"d1c427060a0f73f6b889a5c7c61f2ac4"	"informatica_acessorios"	343	47214.51
"99a4788cb24856965c36a24e339b6058"	"cama_mesa_banho"	488	43025.560000000005
"3dd2a17168ec895c781a9191c1e95ad7"	"informatica_acessorios"	274	41082.6
"25c38557cf793876c5abdd5931f922db"	"bebes"	38	38907.32
"5f504b3a1c75b73d6151be81eb05bdc9"	"cool_stuff"	63	37733.9
"53b36df67ebb7c41585e8d54d6772e08"	"relogios_presentes"	323	37683.42
"aca2eb7d00ea1a7b8ebd4e68314663af"	"moveis_decoracao"	527	37608.9

---

## State Analysis

### Revenue By State

SQL Used:

SELECT *
FROM state_revenue
ORDER BY total_revenue DESC;

Key Findings:

* Revenue is concentrated in a small number of states.
* High-performing regions can be targeted for future business growth.

"SP"	5202955.05
"RJ"	1824092.67
"MG"	1585308.03
"RS"	750304.02
"PR"	683083.76
"SC"	520553.34
"BA"	511349.99
"DF"	302603.94
"GO"	294591.95
"ES"	275037.31
"PE"	262788.03
"CE"	227254.71
"PA"	178947.81
"MT"	156453.53
"MA"	119648.22
"MS"	116812.64
"PB"	115268.08
"PI"	86914.08
"RN"	83034.98
"AL"	80314.81
"SE"	58920.85
"TO"	49621.74
"RO"	46140.64
"AM"	22356.84
"AC"	15982.95
"AP"	13474.3
"RR"	7829.43

---

## Revenue Trend Analysis

### Monthly Revenue Trend

SQL Used:

SELECT *
FROM monthly_revenue
ORDER BY month_year;

Key Findings:

* Revenue trends can be monitored over time.
* Monthly performance helps identify seasonality and growth patterns.

"2016-09"	267.36
"2016-10"	49507.66
"2016-12"	10.9
"2017-01"	120312.87
"2017-02"	247303.02
"2017-03"	374344.3
"2017-04"	359927.23
"2017-05"	506071.14
"2017-06"	433038.6
"2017-07"	498031.48
"2017-08"	573971.68
"2017-09"	624401.6900000001
"2017-10"	664219.43
"2017-11"	1010271.37
"2017-12"	743914.17
"2018-01"	950030.36
"2018-02"	844178.71
"2018-03"	983213.4400000001
"2018-04"	996647.75
"2018-05"	996517.68
"2018-06"	865124.31
"2018-07"	895507.22
"2018-08"	854686.33
"2018-09"	145

---

## Order Analysis

### Average Order Value

SQL Used:

SELECT
ROUND(AVG(total_order_value), 2)
FROM order_summary;

Result:

137.75

### Highest Value Orders

SQL Used:

SELECT *
FROM order_summary
ORDER BY total_order_value DESC
LIMIT 10;

Key Findings:

* High-value orders contribute significantly to overall revenue.
* Order-level analysis supports customer and product insights.

"03caa2c082116e1d31e67e9ae3700499"	"1617b1357756262bfa56ab541c47bc16"	"delivered"	"2017-09-29 15:24:52"	8	13440
"736e1922ae60d0d6a89247b851902527"	"ec5b2ba62e574342386871631fafd3fc"	"delivered"	"2018-07-15 14:49:44"	4	7160
"0812eb902a67711a1cb742b3cdaa65ae"	"c6e2731c5b391845f6800c97401a43a9"	"delivered"	"2017-02-12 20:37:36"	1	6735
"fefacc66af859508bf1a7934eab1e97f"	"f48d464a0baaea338cb25f816991ab1f"	"delivered"	"2018-07-25 18:10:17"	1	6729
"f5136e38d1a14a4dbd87dff67da82701"	"3fd6777bbce08a352fddd04e4a7cc8f6"	"delivered"	"2017-05-24 18:14:34"	1	6499
"2cc9089445046817a7539d90805e6e5a"	"05455dfa7cd02f13d132aa7a6a9729c6"	"delivered"	"2017-11-24 11:03:35"	6	5934.6
"a96610ab360d42a2e5335a3998b4718a"	"df55c14d1476a9a3467f131269c2477f"	"delivered"	"2017-04-01 15:58:40"	1	4799
"199af31afc78c699f0dbf71fb178d4d4"	"24bbf5fd2f2e1b359ee7de94defc4a15"	"delivered"	"2017-04-18 18:50:13"	1	4690
"b4c4b76c642808cbe472a32b86cddc95"	"e0a2412720e9ea4f26c1ac985f6a7358"	"canceled"	"2018-07-12 12:08:36"	2	4599.9
"8dbc85d1447242f3b127dda390d56e19"	"3d979689f636322c62418b6346b1c6d2"	"delivered"	"2018-06-22 12:23:19"	1	4590

---

## Conclusion

The Medallion Architecture successfully transformed raw e-commerce data into business-ready datasets.

The Gold layer enables customer analytics, product analytics, revenue analysis, and operational reporting.