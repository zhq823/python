
# 供应商名称	供应商性质	服务次数	结算金额	服务公里数	单公里价格	均单价

SELECT 
r.SupplierId, # 供应商Id
r.SupplierName, # 供应商名称
r.OnCarTime, # 上车时间
r.OffCarTime, # 下车时间
r.Platform, # 供应商性质
count(*) AS Qty, # 服务次数
sum(r.SettleAmount) AS SettleAmount, # 结算金额
sum(r.Kilometre) AS Kilometre, # 服务公里数
CAST(sum(r.SettleAmount)/sum(r.Kilometre) AS  DECIMAL(12,2)) AS KPrice, # 单公里价格
CAST(sum(r.SettleAmount)/count(*) AS DECIMAL(12,2)) AS Price # 均单价

FROM (

SELECT 
s.SupplierId,
'平台车' AS Platform,
(CASE WHEN SourceCode='DIDI' THEN '滴滴' WHEN SourceCode='ShenZhou' THEN '神州' WHEN SourceCode='EHI' THEN '一嗨租车' END) SupplierName, 
IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.departure_time') WHEN SourceCode='ShenZhou' THEN FROM_UNIXTIME(json_value(ExtOrderData,'$.order.departureTime'),'%Y-%m-%d %H:%i:%S') ELSE DATE_FORMAT(json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.actualPickUpDateTime'),'%Y-%m-%d %H:%m:%s') END),'') AS OnCarTime,
 IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.finish_time') WHEN SourceCode='ShenZhou' THEN IF(json_value(ExtOrderData,'$.order.finishedTime')=0,'', FROM_UNIXTIME(json_value(ExtOrderData,'$.order.finishedTime'))) ELSE json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.actualDropUpDateTime') END),'') AS OffCarTime, 
 IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.normal_distance') WHEN SourceCode='ShenZhou' THEN json_value(ExtOrderData,'$.price.distance')/1000 ELSE json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.mileage') END),'') AS Kilometre, 
 IFNULL(c.Amount,0) SettleAmount
FROM smartx_engine.ttproposals a
INNER JOIN smartx_passport.fnusers d ON a.TuUserId=d.UserId
INNER JOIN smartx_engine.ttproposalxitems b ON a.ProposalId=b.ProposalId AND b.IsDeleted=0 
			AND b.ExtOrderId IS NOT NULL AND b.ItemType=8 AND b.IsExtra=1
LEFT JOIN smartx_engine.ttproposalxitemexpenses c ON b.ItemId=c.ItemId AND c.IsDeleted=0 AND pricetype=1
LEFT JOIN smartx_resource.suppliers AS s ON c.SupplierId=s.SupplierId
WHERE a.tenantid='9d5fb68a-3e33-11e9-ad25-0242ac142204'
 AND a.IsDeleted=0 
 AND (b.`Status`>0 OR (b.`Status`=-1 AND c.Amount IS NOT NULL)) AND NOT EXISTS (
SELECT 1
FROM smartx_administrator.cfg_testing_accounts
WHERE account=d.UserName)

 UNION ALL
 
 
SELECT 
x5.SupplierId,
'线下车' AS Platform,
x5.Name AS SupplierName, 
DATE_FORMAT(json_value(x6.ExpenseData,'$.sDateTime'),'%Y-%m-%d %H:%m:%s') AS OnCarTime,
json_value(x6.ExpenseData,'$.eDateTime') AS OffCarTime,
json_value(x6.ExpenseData,'$.kilometers') AS Kilometre, 
IFNULL(x6.Amount,0) SettleAmount
FROM smartx_engine.ttproposals a
INNER JOIN smartx_passport.fnusers d ON a.TuUserId=d.UserId
INNER JOIN smartx_eorder.orders x4 ON a.ProposalId=x4.EventId AND x4.Status>=40
INNER JOIN smartx_resource.suppliers x5 ON x4.SupplierId=x5.SupplierId
LEFT JOIN smartx_eorder.orderexpenses x6 ON x4.OrderId=x6.OrderId AND x6.PriceType=20 AND x6.IsDeleted=0
WHERE a.TenantId='9d5fb68a-3e33-11e9-ad25-0242ac142204' AND a.IsDeleted=0 AND NOT EXISTS (
SELECT 1
FROM smartx_administrator.cfg_testing_accounts
WHERE account=d.UserName)



) AS r
GROUP BY r.SupplierId