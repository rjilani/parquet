
CREATE TABLE consumercomplains (
    datereceived              date,
    subproduct                TEXT,
    issue                     TEXT,
    subissue                  TEXT,
    consumercomplnarrative    TEXT,
    Companypublicresponse     TEXT,
	company                   varchar(100),
	state                     char(2),
	zip                       varchar(12),
	Tags                      Text,
	consumerconsentprovided   Text,
	submittedvia              varchar(50),
	datesenttocompany         date, 
	companyresponsetoconsumer TEXT, 
	timelyresponse            VARRCHAR (5),
    consumerdisputed          VARRCHAR(5), 
	complaintid               integer
	
);