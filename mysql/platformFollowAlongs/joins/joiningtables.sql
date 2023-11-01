mysql> SELECT clients.first_name. clients.last_name. billing.amounts. billing.charged_datetime
    -> FROM clients
    -> JOIN billing ON clients.id = billing.clients_id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.last_name. billing.amounts. billing.charged_datetime
FROM clients
JOIN billing ' at line 1
mysql> SELECT clients.first_name, clients.last_name, billing.amounts,  billing.charged_datetime FROM clients JOIN billing ON clients.id = billing.clients_id;
ERROR 1054 (42S22): Unknown column 'billing.amounts' in 'field list'
mysql> SELECT clients.first_name, clients.last_name, billing.amount,  billing.charged_datetime FROM clients JOIN billing ON clients.id = billing.clients_id;
+------------+-------------+--------+---------------------+
| first_name | last_name   | amount | charged_datetime    |
+------------+-------------+--------+---------------------+
| Michael    | Choi        |    300 | 2011-01-01 14:50:25 |
| Michael    | Choi        |   5000 | 2011-04-06 14:50:25 |
| Michael    | Choi        |    450 | 2011-09-16 13:22:09 |
| Michael    | Choi        |   2500 | 2011-10-18 13:22:09 |
| Michael    | Choi        |   1200 | 2012-05-09 13:22:09 |
| Joe        | Smith       |   1000 | 2011-04-11 14:50:25 |
| Joe        | Smith       |    900 | 2011-06-22 13:22:09 |
| Joe        | Smith       |   3600 | 2012-01-03 13:22:09 |
| Ryan       | Owen        |    500 | 2011-01-15 14:50:25 |
| Ryan       | Owen        |   5200 | 2011-07-02 13:22:09 |
| Masaki     | Fujimuto    |    200 | 2011-04-02 14:50:25 |
| Masaki     | Fujimuto    |    800 | 2011-06-21 13:22:09 |
| Masaki     | Fujimuto    |    650 | 2011-08-24 13:22:09 |
| Diana      | Sue Manlulu |    500 | 2011-02-11 14:50:25 |
| John       | Supsupin    |    500 | 2011-05-08 15:55:32 |
| John       | Supsupin    |    750 | 2011-06-18 13:22:09 |
| Toni Rose  | Panganiban  |   1200 | 2011-02-22 14:50:25 |
| Toni Rose  | Panganiban  |    640 | 2012-03-07 13:22:09 |
| Maria      | Gonzales    |   1000 | 2011-03-13 14:50:25 |
| Maria      | Gonzales    |    100 | 2011-07-19 13:22:09 |
| Maria      | Gonzales    |   8000 | 2012-02-05 13:22:09 |
| Tom        | Owen        |   2500 | 2011-02-27 14:50:25 |
| Tom        | Owen        |    150 | 2012-04-08 13:22:09 |
| Roosevelt  | Sebial      |    500 | 2011-03-06 14:50:25 |
| Roosevelt  | Sebial      |    680 | 2012-04-02 13:22:09 |
+------------+-------------+--------+---------------------+
25 rows in set (0.00 sec)

mysql> SELECT sites.domain_name, leads.first_name, leads.last_name
    -> FROM sites
    -> JOIN leads ON sites.id = leads.sites_id;
+-----------------------+------------+-----------+
| domain_name           | first_name | last_name |
+-----------------------+------------+-----------+
| market.com            | Art        | Lopez     |
| ehow.com              | Arthur     | Kesh      |
| searchphilippines.com | Alison     | Follosco  |
| uptownzone.com        | Joyce      | Jamon     |
| olx.com               | Angel      | Supsupin  |
| searchhomes.com       | Dave       | Supsupin  |
| timespace.com         | Mark       | Jaramilla |
| help.com              | Chris      | Chun      |
| keepvid.com           | Ben        | Lee       |
| atech.com             | Jeric      | Follosco  |
| atech.com             | James      | Jones     |
| finalsite.com         | Jay        | Smith     |
| homes.com             | Henry      | Mendoza   |
| fox.com               | Dian       | Morales   |
| loans.com             | Lina       | Inverse   |
| market.com            | May Joy    | Sagon     |
| market.com            | April      | Sean      |
| timespace.com         | Philip     | Morres    |
| cryshinjohn.com       | Kimemura   | Lau       |
| family.com            | Noname     | Sabado    |
| connectme.com         | Gilbert    | Hufana    |
| yestogod.com          | Paulito    | Nisperos  |
| searchhomes.com       | Joseph     | Padua     |
| ehow.com              | Marylen    | Rodriguez |
| searchcoronado.com    | Bala       | Nar       |
| searchphilippines.com | Steve      | Nash      |
| fox.com               | Lebron     | James     |
| loans.com             | Alvin      | Rosorio   |
| searchvillage.com     | Kirk       | David     |
| homes.com             | Calvin     | Klein     |
| searchcomputers.com   | Albert     | Martinez  |
| keepvid.com           | Vhong      | Navarro   |
| market.com            | Anne       | Curtiz    |
| assignmentworld.com   | Mark       | Oceana    |
| market.com            | Ems        | Faraj     |
+-----------------------+------------+-----------+
35 rows in set (0.00 sec)

mysql> SELECT sites.domain_name, leads.first_name, leads.last_name
    -> FROM sites
    -> JOIN leads ON sites.id = leads.sites_id
    -> ORDER BY sites.domain_name ASC;
+-----------------------+------------+-----------+
| domain_name           | first_name | last_name |
+-----------------------+------------+-----------+
| assignmentworld.com   | Mark       | Oceana    |
| atech.com             | Jeric      | Follosco  |
| atech.com             | James      | Jones     |
| connectme.com         | Gilbert    | Hufana    |
| cryshinjohn.com       | Kimemura   | Lau       |
| ehow.com              | Arthur     | Kesh      |
| ehow.com              | Marylen    | Rodriguez |
| family.com            | Noname     | Sabado    |
| finalsite.com         | Jay        | Smith     |
| fox.com               | Lebron     | James     |
| fox.com               | Dian       | Morales   |
| help.com              | Chris      | Chun      |
| homes.com             | Calvin     | Klein     |
| homes.com             | Henry      | Mendoza   |
| keepvid.com           | Vhong      | Navarro   |
| keepvid.com           | Ben        | Lee       |
| loans.com             | Alvin      | Rosorio   |
| loans.com             | Lina       | Inverse   |
| market.com            | Ems        | Faraj     |
| market.com            | April      | Sean      |
| market.com            | May Joy    | Sagon     |
| market.com            | Anne       | Curtiz    |
| market.com            | Art        | Lopez     |
| olx.com               | Angel      | Supsupin  |
| searchcomputers.com   | Albert     | Martinez  |
| searchcoronado.com    | Bala       | Nar       |
| searchhomes.com       | Joseph     | Padua     |
| searchhomes.com       | Dave       | Supsupin  |
| searchphilippines.com | Steve      | Nash      |
| searchphilippines.com | Alison     | Follosco  |
| searchvillage.com     | Kirk       | David     |
| timespace.com         | Mark       | Jaramilla |
| timespace.com         | Philip     | Morres    |
| uptownzone.com        | Joyce      | Jamon     |
| yestogod.com          | Paulito    | Nisperos  |
+-----------------------+------------+-----------+
35 rows in set (0.00 sec)

mysql> SELECT clients.first_name, clients.last_name, sites.domain_name, leads.first_name
    -> FROM clients
    -> JOIN sites ON clients.id = sites.clients_id
    -> JOIN leads ON sites.id = leads.sites_id;
+------------+-------------+-----------------------+------------+
| first_name | last_name   | domain_name           | first_name |
+------------+-------------+-----------------------+------------+
| Michael    | Choi        | market.com            | Art        |
| Michael    | Choi        | market.com            | May Joy    |
| Michael    | Choi        | market.com            | April      |
| Michael    | Choi        | market.com            | Anne       |
| Michael    | Choi        | market.com            | Ems        |
| Michael    | Choi        | assignmentworld.com   | Mark       |
| Joe        | Smith       | fox.com               | Dian       |
| Joe        | Smith       | fox.com               | Lebron     |
| Joe        | Smith       | connectme.com         | Gilbert    |
| Ryan       | Owen        | searchhomes.com       | Dave       |
| Ryan       | Owen        | searchhomes.com       | Joseph     |
| Ryan       | Owen        | family.com            | Noname     |
| Ryan       | Owen        | finalsite.com         | Jay        |
| Masaki     | Fujimuto    | loans.com             | Lina       |
| Masaki     | Fujimuto    | loans.com             | Alvin      |
| Masaki     | Fujimuto    | help.com              | Chris      |
| Masaki     | Fujimuto    | cryshinjohn.com       | Kimemura   |
| Diana      | Sue Manlulu | ehow.com              | Arthur     |
| Diana      | Sue Manlulu | ehow.com              | Marylen    |
| Diana      | Sue Manlulu | olx.com               | Angel      |
| John       | Supsupin    | searchvillage.com     | Kirk       |
| John       | Supsupin    | uptownzone.com        | Joyce      |
| John       | Supsupin    | keepvid.com           | Ben        |
| John       | Supsupin    | keepvid.com           | Vhong      |
| Toni Rose  | Panganiban  | searchcoronado.com    | Bala       |
| Toni Rose  | Panganiban  | timespace.com         | Mark       |
| Toni Rose  | Panganiban  | timespace.com         | Philip     |
| Toni Rose  | Panganiban  | atech.com             | Jeric      |
| Toni Rose  | Panganiban  | atech.com             | James      |
| Maria      | Gonzales    | homes.com             | Henry      |
| Maria      | Gonzales    | homes.com             | Calvin     |
| Tom        | Owen        | searchphilippines.com | Alison     |
| Tom        | Owen        | searchphilippines.com | Steve      |
| Tom        | Owen        | yestogod.com          | Paulito    |
| Roosevelt  | Sebial      | searchcomputers.com   | Albert     |
+------------+-------------+-----------------------+------------+
35 rows in set (0.00 sec)

mysql> SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads ON sites.id = leads.sites_id;
+--------------+-------------+-----------------------+-------------+
| client_first | last_name   | domain_name           | leads_first |
+--------------+-------------+-----------------------+-------------+
| Michael      | Choi        | market.com            | Art         |
| Michael      | Choi        | market.com            | May Joy     |
| Michael      | Choi        | market.com            | April       |
| Michael      | Choi        | market.com            | Anne        |
| Michael      | Choi        | market.com            | Ems         |
| Michael      | Choi        | assignmentworld.com   | Mark        |
| Joe          | Smith       | fox.com               | Dian        |
| Joe          | Smith       | fox.com               | Lebron      |
| Joe          | Smith       | connectme.com         | Gilbert     |
| Ryan         | Owen        | searchhomes.com       | Dave        |
| Ryan         | Owen        | searchhomes.com       | Joseph      |
| Ryan         | Owen        | family.com            | Noname      |
| Ryan         | Owen        | finalsite.com         | Jay         |
| Masaki       | Fujimuto    | loans.com             | Lina        |
| Masaki       | Fujimuto    | loans.com             | Alvin       |
| Masaki       | Fujimuto    | help.com              | Chris       |
| Masaki       | Fujimuto    | cryshinjohn.com       | Kimemura    |
| Diana        | Sue Manlulu | ehow.com              | Arthur      |
| Diana        | Sue Manlulu | ehow.com              | Marylen     |
| Diana        | Sue Manlulu | olx.com               | Angel       |
| John         | Supsupin    | searchvillage.com     | Kirk        |
| John         | Supsupin    | uptownzone.com        | Joyce       |
| John         | Supsupin    | keepvid.com           | Ben         |
| John         | Supsupin    | keepvid.com           | Vhong       |
| Toni Rose    | Panganiban  | searchcoronado.com    | Bala        |
| Toni Rose    | Panganiban  | timespace.com         | Mark        |
| Toni Rose    | Panganiban  | timespace.com         | Philip      |
| Toni Rose    | Panganiban  | atech.com             | Jeric       |
| Toni Rose    | Panganiban  | atech.com             | James       |
| Maria        | Gonzales    | homes.com             | Henry       |
| Maria        | Gonzales    | homes.com             | Calvin      |
| Tom          | Owen        | searchphilippines.com | Alison      |
| Tom          | Owen        | searchphilippines.com | Steve       |
| Tom          | Owen        | yestogod.com          | Paulito     |
| Roosevelt    | Sebial      | searchcomputers.com   | Albert      |
+--------------+-------------+-----------------------+-------------+
35 rows in set (0.00 sec)

mysql> SELECT clients.first_name, clients.last_name, sties.domain_name
    -> FROM clients
    -> LEFT JOIN sites ON clients.id = sites.clients_id;
ERROR 1054 (42S22): Unknown column 'sties.domain_name' in 'field list'
mysql> SELECT clients.first_name, clients.last_name, sites.domain_name FROM clients LEFT JOIN sites ON clients.id = sites.clients_id;
+------------+-------------+-----------------------+
| first_name | last_name   | domain_name           |
+------------+-------------+-----------------------+
| Michael    | Choi        | market.com            |
| Michael    | Choi        | youtube.com           |
| Michael    | Choi        | assignmentworld.com   |
| Joe        | Smith       | fox.com               |
| Joe        | Smith       | flipfly.com           |
| Joe        | Smith       | connectme.com         |
| Ryan       | Owen        | searchhomes.com       |
| Ryan       | Owen        | family.com            |
| Ryan       | Owen        | finalsite.com         |
| Masaki     | Fujimuto    | loans.com             |
| Masaki     | Fujimuto    | help.com              |
| Masaki     | Fujimuto    | cryshinjohn.com       |
| Diana      | Sue Manlulu | ehow.com              |
| Diana      | Sue Manlulu | olx.com               |
| John       | Supsupin    | searchvillage.com     |
| John       | Supsupin    | uptownzone.com        |
| John       | Supsupin    | keepvid.com           |
| Toni Rose  | Panganiban  | searchcoronado.com    |
| Toni Rose  | Panganiban  | timespace.com         |
| Toni Rose  | Panganiban  | atech.com             |
| Maria      | Gonzales    | homes.com             |
| Maria      | Gonzales    | warcraft.com          |
| Tom        | Owen        | searchphilippines.com |
| Tom        | Owen        | yestogod.com          |
| Roosevelt  | Sebial      | searchcomputers.com   |
+------------+-------------+-----------------------+
25 rows in set (0.00 sec)

mysql>  SELECT clients.first_name, clients.last_name, sites.domain_name
    -> FROM clients
    -> LEFT JOIN sites ON clients.id = sites.clients_id
    -> WHERE sites.domain_name IS NULL OR sites.domain_name IS NOT NULL;
+------------+-------------+-----------------------+
| first_name | last_name   | domain_name           |
+------------+-------------+-----------------------+
| Michael    | Choi        | market.com            |
| Michael    | Choi        | youtube.com           |
| Michael    | Choi        | assignmentworld.com   |
| Joe        | Smith       | fox.com               |
| Joe        | Smith       | flipfly.com           |
| Joe        | Smith       | connectme.com         |
| Ryan       | Owen        | searchhomes.com       |
| Ryan       | Owen        | family.com            |
| Ryan       | Owen        | finalsite.com         |
| Masaki     | Fujimuto    | loans.com             |
| Masaki     | Fujimuto    | help.com              |
| Masaki     | Fujimuto    | cryshinjohn.com       |
| Diana      | Sue Manlulu | ehow.com              |
| Diana      | Sue Manlulu | olx.com               |
| John       | Supsupin    | searchvillage.com     |
| John       | Supsupin    | uptownzone.com        |
| John       | Supsupin    | keepvid.com           |
| Toni Rose  | Panganiban  | searchcoronado.com    |
| Toni Rose  | Panganiban  | timespace.com         |
| Toni Rose  | Panganiban  | atech.com             |
| Maria      | Gonzales    | homes.com             |
| Maria      | Gonzales    | warcraft.com          |
| Tom        | Owen        | searchphilippines.com |
| Tom        | Owen        | yestogod.com          |
| Roosevelt  | Sebial      | searchcomputers.com   |
+------------+-------------+-----------------------+
25 rows in set (0.00 sec)

mysql>  SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
    -> FROM clients
    -> JOIN billing ON clients.id = billing.clients_id
    ->  SELECT clients.first_name, clients.last_name,SUM(billing.amount
    -> FROM clients
    -> JOIN billing ON clients.id = billing.clients_id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT clients.first_name, clients.last_name,SUM(billing.amount
FROM clients
JOI' at line 4
mysql> SELECT clients.first_name, clients.last_name, SUM(billing.amount)
    -> FROM clients
    -> JOIN billing ON clients.id = billing.clients_id
    -> GROUP BY clients.id;
+------------+-------------+---------------------+
| first_name | last_name   | SUM(billing.amount) |
+------------+-------------+---------------------+
| Michael    | Choi        |                9450 |
| Joe        | Smith       |                5500 |
| Ryan       | Owen        |                5700 |
| Masaki     | Fujimuto    |                1650 |
| Diana      | Sue Manlulu |                 500 |
| John       | Supsupin    |                1250 |
| Toni Rose  | Panganiban  |                1840 |
| Maria      | Gonzales    |                9100 |
| Tom        | Owen        |                2650 |
| Roosevelt  | Sebial      |                1180 |
+------------+-------------+---------------------+
10 rows in set (0.00 sec)

mysql> SELECT sites.domain_name, clients.first_name, clients.last_name
    -> FROM sites
    -> JOI
    -> SELECT sites.domain_name, clients.first_name, clients.last_name
    -> FROM clients
    -> JOIN sites ON clients.id = sites.clients_id
    -> GROUP BY clients.id
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT sites.domain_name, clients.first_name, clients.last_name
FROM clients
JOI' at line 4
mysql> SELECT sites.domain_name, clients.first_name, clients.last_name FROM sites JOI SELECT sites.domain_name, clients.first_name, clients.last_name FROM clients JOIN sites ON clients.id = sites.clients_id GROUP BY clients.id;SELECT GROUP_CONCAT(sites.domain_name) AS domains, clients.first_name, clients.last_name
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT sites.domain_name, clients.first_name, clients.last_name FROM clients JOI' at line 1
    -> SELECT GROUP_CONCAT(sites.domain_name) AS domains, clients.first_name, clients.last_name
    -> FROM clients
    -> JOIN sites ON clients.id = sites.clients_id
    -> GROUP BY clients.id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT GROUP_CONCAT(sites.domain_name) AS domains, clients.first_name, clients.l' at line 2
mysql>  SELECT GROUP_CONCAT(sites.domain_name), clients.first_name, clients.last_name
    -> FROM clients
    -> JOIN sites ON clients.id = sites.clients_id
    -> GROUP BY clients.id;
+----------------------------------------------+------------+-------------+
| GROUP_CONCAT(sites.domain_name)              | first_name | last_name   |
+----------------------------------------------+------------+-------------+
| market.com,youtube.com,assignmentworld.com   | Michael    | Choi        |
| fox.com,flipfly.com,connectme.com            | Joe        | Smith       |
| searchhomes.com,family.com,finalsite.com     | Ryan       | Owen        |
| loans.com,help.com,cryshinjohn.com           | Masaki     | Fujimuto    |
| ehow.com,olx.com                             | Diana      | Sue Manlulu |
| searchvillage.com,uptownzone.com,keepvid.com | John       | Supsupin    |
| searchcoronado.com,timespace.com,atech.com   | Toni Rose  | Panganiban  |
| homes.com,warcraft.com                       | Maria      | Gonzales    |
| searchphilippines.com,yestogod.com           | Tom        | Owen        |
| searchcomputers.com                          | Roosevelt  | Sebial      |
+----------------------------------------------+------------+-------------+
10 rows in set (0.01 sec)

mysql>  SELECT GROUP_CONCAT('',sites.domain_name), clients.first_name, clients.last_name FROM clients JOIN sites ON clients.id = sites.clients_id GROUP BY clients.id;
+----------------------------------------------+------------+-------------+
| GROUP_CONCAT('',sites.domain_name)           | first_name | last_name   |
+----------------------------------------------+------------+-------------+
| market.com,youtube.com,assignmentworld.com   | Michael    | Choi        |
| fox.com,flipfly.com,connectme.com            | Joe        | Smith       |
| searchhomes.com,family.com,finalsite.com     | Ryan       | Owen        |
| loans.com,help.com,cryshinjohn.com           | Masaki     | Fujimuto    |
| ehow.com,olx.com                             | Diana      | Sue Manlulu |
| searchvillage.com,uptownzone.com,keepvid.com | John       | Supsupin    |
| searchcoronado.com,timespace.com,atech.com   | Toni Rose  | Panganiban  |
| homes.com,warcraft.com                       | Maria      | Gonzales    |
| searchphilippines.com,yestogod.com           | Tom        | Owen        |
| searchcomputers.com                          | Roosevelt  | Sebial      |
+----------------------------------------------+------------+-------------+
10 rows in set (0.00 sec)

mysql> SELECT leads.id, sites.domain_name
    -> FROM sites
    -> 
    -> ;
ERROR 1054 (42S22): Unknown column 'leads.id' in 'field list'
mysql> SELECT COUNT(leads.id) site.domain_name
    -> FROM sites
    -> JOIN leads ON sites.id = leads.sites_id
    -> GROUP BY site.id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY site.id' at line 1
mysql> SELECT COUNT(leads.id) sites.domain_name FROM sites JOIN leads ON sites.id = leads.sites_id GROUP BY site.id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.domain_name FROM sites JOIN leads ON sites.id = leads.sites_id GROUP BY site.id' at line 1
mysql> SELECT COUNT(leads.id), sites.domain_name FROM sites JOIN leads ON sites.id = leads.sites_id GROUP BY site.id;
ERROR 1054 (42S22): Unknown column 'site.id' in 'group statement'
mysql> SELECT COUNT(leads.id), sites.domain_name
    -> FROM sites
    -> JOIN leads ON sites.id = leads.sites_id
    -> GROUP BY site.id;
ERROR 1054 (42S22): Unknown column 'site.id' in 'group statement'
mysql> SELECT COUNT(leads.id), sites.domain_name FROM sites JOIN leads ON sites.id = leads.sites_id GROUP BY sites.id;
+-----------------+-----------------------+
| COUNT(leads.id) | domain_name           |
+-----------------+-----------------------+
|               5 | market.com            |
|               2 | searchhomes.com       |
|               2 | ehow.com              |
|               1 | searchcoronado.com    |
|               2 | searchphilippines.com |
|               2 | fox.com               |
|               2 | loans.com             |
|               1 | searchvillage.com     |
|               2 | homes.com             |
|               1 | searchcomputers.com   |
|               1 | help.com              |
|               2 | timespace.com         |
|               1 | uptownzone.com        |
|               1 | olx.com               |
|               1 | cryshinjohn.com       |
|               1 | family.com            |
|               1 | connectme.com         |
|               1 | yestogod.com          |
|               2 | keepvid.com           |
|               2 | atech.com             |
|               1 | assignmentworld.com   |
|               1 | finalsite.com         |
+-----------------+-----------------------+
22 rows in set (0.00 sec)

mysql> notee
