CREATE PROCEDURE sp_ticketInBuild_list(ticketid int)
LANGUAGE SQL
as $$

	select 
		"TicketID",
		"Priority",
		"Status",
		"DueDate",
		(select CONCAT ("Responsibility",' - ', "FirstName") from shared_usersticket us where "UserID"="AssignedTo") as "AssignedTo",
		"Title",
		"Description",
		"created_date",
		"modified_date",
		"created_by",
		"modified_by",
		"Category",
		"MODULE",
		(select CONCAT ("Responsibility",' - ', "FirstName") from shared_usersticket us where "UserID"="PrimaryDEV") as "PrimaryDEV",
		(select CONCAT ("Responsibility",' - ', "FirstName") from shared_usersticket us where "UserID"="PrimaryQC") as "PrimaryQC",
		(select CONCAT ("Responsibility",' - ', "FirstName") from shared_usersticket us where "UserID"="PrimaryBA") as "PrimaryBA",
		(select CONCAT ("Responsibility",' - ', "FirstName") from shared_usersticket us where "UserID"="TicketOwner") as "TicketOwner"
	from taskmanagement_ticket tk
	where "TicketID"=111829

$$


