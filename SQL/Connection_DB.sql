%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where 
	TABSCHEMA='YOUR-DB2-USERNAME'

## you can retrieve list of all tables where the schema name is not 
   one of the system created ones:

%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES \
      where TABSCHEMA not in ('SYSIBM', 'SYSCAT', 'SYSSTAT', 'SYSIBMADM', 'SYSTOOLS', 'SYSPUBLIC')
      
## or, just query for a specifc table that you want to verify exists 
   in the database

%sql select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'