# 叫车人姓名	使用次数	用车花费	服务公里数	均单价

SELECT 
T.proposalId, # 会议id
T.UserId, # 叫车人id
T.DspName, # 叫车人姓名
count(*) AS Qty, # 使用次数
sum(T.SettleAmount) AS SettleAmount, # 用车花费
sum(T.Kilometre) as Kilometre, # 服务公里数
CAST(sum(T.SettleAmount)/count(*) AS DECIMAL(12,2)) AS Price # 均单价


FROM  (
	SELECT 
	a.proposalId, # 会议id
	u.UserId, # 叫车人id
   u.DspName, # 叫车人姓名
	IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.departure_time') WHEN SourceCode='ShenZhou' THEN FROM_UNIXTIME(json_value(ExtOrderData,'$.order.departureTime'),'%Y-%m-%d %H:%i:%S') ELSE DATE_FORMAT(json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.actualPickUpDateTime'),'%Y-%m-%d %H:%m:%s') END),'') AS OnCarTime, # 上车时间
	IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.finish_time') WHEN SourceCode='ShenZhou' THEN IF(json_value(ExtOrderData,'$.order.finishedTime')=0,'', FROM_UNIXTIME(json_value(ExtOrderData,'$.order.finishedTime'))) ELSE json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.actualDropUpDateTime') END),'') AS OffCarTime, # 下车时间
	IFNULL((CASE WHEN SourceCode='DiDi' THEN json_value(ExtOrderData,'$.order.normal_distance') WHEN SourceCode='ShenZhou' THEN json_value(ExtOrderData,'$.price.distance')/1000 ELSE json_value(json_query(json_query(extorderdata,'$.detailRes'),'$.orderData'),'$.mileage') END),'') AS Kilometre, # 公里数
	IFNULL(c.Amount,0) AS SettleAmount # 结算金额
	FROM smartx_engine.ttproposals a
	INNER JOIN smartx_passport.fnusers d ON a.TuUserId=d.UserId
	INNER JOIN smartx_engine.ttproposalxitems b ON a.ProposalId=b.ProposalId AND b.IsDeleted=0 AND b.ExtOrderId IS NOT NULL AND b.ItemType=8 AND b.IsExtra=1
	LEFT JOIN smartx_engine.ttproposalxitemexpenses c ON b.ItemId=c.ItemId AND c.IsDeleted=0 AND pricetype=1
	LEFT JOIN smartx_passport.fnusers u on u.UserName=b.CreatedBy
	WHERE a.tenantid='9d5fb68a-3e33-11e9-ad25-0242ac142204' AND a.IsDeleted=0 AND (b.`Status`>0 OR (b.`Status`=-1 AND c.Amount IS NOT NULL)) AND NOT EXISTS (
	SELECT 1
	FROM smartx_administrator.cfg_testing_accounts
	WHERE account=d.UserName) 
	
	UNION ALL
	
	SELECT 
	a.proposalId, # 会议id
	u.UserId, # 叫车人id
	u.DspName, # 叫车人姓名
	DATE_FORMAT(json_value(x6.ExpenseData,'$.sDateTime'),'%Y-%m-%d %H:%m:%s') AS OnCarTime, # 上车时间
	json_value(x6.ExpenseData,'$.eDateTime') AS OffCarTime, # 下车时间
	json_value(x6.ExpenseData,'$.kilometers') AS Kilometre, # 公里数
	IFNULL(x6.Amount,0) AS SettleAmount # 结算金额
	FROM smartx_engine.ttproposals a
	INNER JOIN smartx_passport.fnusers d ON a.TuUserId=d.UserId
	INNER JOIN smartx_eorder.orders x4 ON a.ProposalId=x4.EventId AND x4.Status>=40
	INNER JOIN smartx_resource.suppliers x5 ON x4.SupplierId=x5.SupplierId
	LEFT JOIN smartx_eorder.orderexpenses x6 ON x4.OrderId=x6.OrderId AND x6.PriceType=20 AND x6.IsDeleted=0
	LEFT JOIN smartx_passport.fnusers u on u.UserName=x4.CreatedBy
	WHERE a.TenantId='9d5fb68a-3e33-11e9-ad25-0242ac142204' AND a.IsDeleted=0 AND NOT EXISTS (
	SELECT 1
	FROM smartx_administrator.cfg_testing_accounts
	WHERE account=d.UserName)
) AS T
GROUP BY T.UserId
